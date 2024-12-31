from django.core.management.base import BaseCommand
from analytical.models import ViewModel
from django.db import transaction
import json
import time


class Command(BaseCommand):
    help = 'Yedek dosyasından verileri geri yükler'

    def add_arguments(self, parser):
        parser.add_argument('backup_file', type=str, help='Yedek dosyasının yolu')

    def handle(self, *args, **kwargs):
        backup_file = kwargs['backup_file']
        batch_size = 1000
        restored = 0
        errors = []

        try:
            # Yedek dosyasını oku
            with open(backup_file, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)

            total = len(backup_data)
            self.stdout.write(f"Toplam {total} kayıt geri yüklenecek...")

            # Batch işleme
            for i in range(0, total, batch_size):
                batch = backup_data[i:i + batch_size]

                with transaction.atomic():
                    for record in batch:
                        try:
                            # Kaydı bul veya oluştur
                            view_model, created = ViewModel.objects.get_or_create(
                                id=record['id']
                            )

                            # Tüm alanları güncelle
                            view_model.visit_time = record['visit_time']
                            view_model.reload_count_in_a_clock = record['reload_count_in_a_clock']
                            view_model.ip_address = record['ip_address']
                            view_model.ip_data = record['ip_data']
                            view_model.is_i_am = record['is_i_am']
                            view_model.user_agent = record['user_agent']
                            view_model.query_string = record['query_string']
                            view_model.request_type = record['request_type']
                            view_model.http_sec_ch_ua = record['http_sec_ch_ua']
                            view_model.request_data = record['request_data']
                            view_model.time_tick_count = record['time_tick_count']

                            view_model.save()
                            restored += 1

                            if restored % 100 == 0:
                                self.stdout.write(f"Geri yüklenen: {restored}/{total}")

                        except Exception as record_error:
                            error_msg = f"ID {record['id']}: {str(record_error)}"
                            errors.append(error_msg)
                            self.stdout.write(
                                self.style.WARNING(f"Hata: {error_msg}")
                            )
                            continue

                time.sleep(0.1)  # Sunucu yükünü azalt

            # Sonuç raporu
            self.stdout.write(
                self.style.SUCCESS(
                    f'\nGeri yükleme tamamlandı:\n'
                    f'Toplam kayıt: {total}\n'
                    f'Başarıyla geri yüklenen: {restored}\n'
                    f'Hata sayısı: {len(errors)}'
                )
            )

            # Hataları göster
            if errors:
                self.stdout.write("\nHata Detayları:")
                for error in errors:
                    self.stdout.write(self.style.ERROR(error))

        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'Yedek dosyası bulunamadı: {backup_file}')
            )
        except json.JSONDecodeError:
            self.stdout.write(
                self.style.ERROR('Yedek dosyası geçerli bir JSON formatında değil')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Kritik hata oluştu: {str(e)}')
            )