from django.db import models
from config.utils import EncryptionService
from typing import Any


class EncryptedField(models.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._encryption_service = EncryptionService()

    def from_db_value(self, value: Any, expression, connection) -> str:
        if value is None:
            return value
        try:
            return self._encryption_service.decrypt_data(value)
        except Exception:
            return None

    def to_python(self, value: Any) -> str:
        if value is None:
            return value
        try:
            # Eğer veri zaten şifreli değilse
            return self._encryption_service.decrypt_data(value)
        except Exception:
            # Veri zaten şifreli değilse, olduğu gibi döndür
            return value

    def get_prep_value(self, value: Any) -> str:
        if value is None:
            return value
        try:
            # Veriyi şifrele
            return self._encryption_service.encrypt_data(str(value))
        except Exception:
            return None