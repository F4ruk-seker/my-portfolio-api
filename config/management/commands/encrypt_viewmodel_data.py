from django.core.management.base import BaseCommand
from analytical.models import ViewModel
from config.utils import EncryptionService
from django.db import transaction
import time
import traceback


class Command(BaseCommand):
    help = 'ViewModel verilerini şifreler'

    def handle(self, *args, **kwargs):
        encryption_service = EncryptionService()
        batch_size = 1000

        try:
            total = ViewModel.objects.count()
            self.stdout.write(f"Toplam {total} kayıt işlenecek...")

            processed = 0
            errors = []

            for offset in range(0, total, batch_size):
                with transaction.atomic():
                    records = ViewModel.objects.all()[offset:offset + batch_size]

                    for record in records:
                        try:
                            if record.request_data:
                                # Debug bilgisi
                                self.stdout.write(f"İşleniyor ID: {record.id}")
                                self.stdout.write(f"Orijinal veri: {record.request_data[:100]}...")  # İlk 100 karakter

                                encrypted = encryption_service.encrypt_data(record.request_data)

                                # Şifreleme sonucunu kontrol et
                                if encrypted is None:
                                    raise ValueError(f"ID {record.id}: Şifreleme başarısız oldu")

                                record.request_data = encrypted
                                record.save()

                                processed += 1

                        except Exception as record_error:
                            errors.append(f"ID {record.id}: {str(record_error)}")
                            self.stdout.write(
                                self.style.WARNING(f"Kayıt işlenirken hata: {str(record_error)}")
                            )
                            continue

                    self.stdout.write(f"İşlenen kayıt: {min(offset + batch_size, total)}/{total}")
                    time.sleep(0.1)

            # Sonuç raporu
            self.stdout.write(
                self.style.SUCCESS(f'İşlem tamamlandı:\n'
                                   f'Toplam kayıt: {total}\n'
                                   f'Başarıyla işlenen: {processed}\n'
                                   f'Hata sayısı: {len(errors)}')
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
            self.stdout.write(
                self.style.ERROR(traceback.format_exc())
            )