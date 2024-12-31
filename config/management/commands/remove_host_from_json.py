from django.core.management.base import BaseCommand
from analytical.models import ViewModel
from django.db import transaction
import time
import json


class Command(BaseCommand):
    help = 'ip_data JSON alanından host anahtarını siler'

    def handle(self, *args, **kwargs):
        batch_size = 1000
        processed = 0
        errors = []

        try:
            total = ViewModel.objects.count()
            self.stdout.write(f"Toplam {total} kayıt işlenecek...")

            for offset in range(0, total, batch_size):
                with transaction.atomic():
                    records = ViewModel.objects.all()[offset:offset + batch_size]

                    for record in records:
                        try:
                            if record.ip_data and isinstance(record.ip_data, dict):
                                # 'host' anahtarı varsa sil
                                if 'host' in record.ip_data:
                                    original_data = record.ip_data.copy()  # Yedek al
                                    del record.ip_data['host']
                                    record.save()

                                    # Debug bilgisi
                                    self.stdout.write(
                                        f"ID {record.id}: host anahtarı silindi\n"
                                        f"Önceki: {original_data}\n"
                                        f"Sonraki: {record.ip_data}"
                                    )
                                    processed += 1

                        except Exception as record_error:
                            errors.append(f"ID {record.id}: {str(record_error)}")
                            self.stdout.write(
                                self.style.WARNING(f"Kayıt işlenirken hata: {str(record_error)}")
                            )
                            continue

                    current_count = min(offset + batch_size, total)
                    self.stdout.write(
                        f"İşlenen kayıt: {current_count}/{total} "
                        f"(Değiştirilen: {processed})"
                    )
                    time.sleep(0.1)  # Sunucu yükünü azaltmak için

            # Sonuç raporu
            self.stdout.write(
                self.style.SUCCESS(
                    f'\nİşlem tamamlandı:\n'
                    f'Toplam kayıt: {total}\n'
                    f'Host anahtarı silinen: {processed}\n'
                    f'Hata sayısı: {len(errors)}'
                )
            )

            # Hataları göster
            if errors:
                self.stdout.write("\nHata Detayları:")
                for error in errors:
                    self.stdout.write(self.style.ERROR(error))

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Kritik hata oluştu: {str(e)}')
            )