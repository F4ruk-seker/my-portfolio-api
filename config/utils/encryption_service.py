from cryptography.fernet import Fernet
from typing import Optional
import os
from config.settings.base import env


class EncryptionService:
    def __init__(self):
        self.key = env('ENCRYPTION_KEY')
        if not self.key:
            self.key = Fernet.generate_key()
            with open('.env', 'a') as f:
                f.write(f'\nENCRYPTION_KEY={self.key.decode()}')
        else:
            self.key = self.key.encode()

        self.cipher = Fernet(self.key)

    def encrypt_data(self, data: str) -> Optional[str]:
        try:
            if not data or len(data) > 520:
                return None
            encrypted_data = self.cipher.encrypt(data.encode())
            return encrypted_data.decode()
        except Exception:
            return None

    def decrypt_data(self, encrypted_data: str) -> Optional[str]:
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data.encode())
            return decrypted_data.decode()
        except Exception:
            return None