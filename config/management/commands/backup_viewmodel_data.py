from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder
from analytical.models import ViewModel
import json
from datetime import datetime
import os


class Command(BaseCommand):
    help = 'ViewModel verilerinin yedeğini alır'

    def handle(self, *args, **kwargs):
        try:
            # Yedekleme dizini oluştur
            backup_dir = 'data_backups'
            os.makedirs(backup_dir, exist_ok=True)

            # Tüm kayıtları al
            records = ViewModel.objects.all()
            total = records.count()
            backup_data = []

            self.stdout.write(f"Toplam {total} kayıt yedekleniyor...")

            for i, record in enumerate(records, 1):
                backup_data.append({
                    'id': record.id,
                    'visit_time': record.visit_time.isoformat(),
                    'reload_count_in_a_clock': record.reload_count_in_a_clock,
                    'ip_address': record.ip_address,
                    'ip_data': record.ip_data,
                    'is_i_am': record.is_i_am,
                    'user_agent': record.user_agent,
                    'query_string': record.query_string,
                    'request_type': record.request_type,
                    'http_sec_ch_ua': record.http_sec_ch_ua,
                    'request_data': record.request_data,
                    'time_tick_count': record.time_tick_count,
                })

                if i % 1000 == 0:  # Her 1000 kayıtta bir durum bildirimi
                    self.stdout.write(f"İşlenen: {i}/{total}")

            # Yedek dosyası oluştur
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = os.path.join(backup_dir, f'viewmodel_backup_{timestamp}.json')

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, cls=DjangoJSONEncoder, ensure_ascii=False, indent=2)

            self.stdout.write(
                self.style.SUCCESS(f'Yedekleme başarılı! Dosya: {filename}')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Yedekleme hatası: {str(e)}')
            )