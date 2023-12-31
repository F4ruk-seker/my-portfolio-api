from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class OTPModelManager(models.Manager):
    def user_has_otp_device(self, user):
        try:
            otp_instance = self.get(user=user)
            return True
        except self.model.DoesNotExist:
            return False


class OTPModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    otp_device = models.TextField(max_length=255, editable=True)
    is_active = models.BooleanField(default=True)

    def create_hash(self):
        import pyotp
        return pyotp.TOTP(self.otp_device).provisioning_uri(name=self.user.email, issuer_name=self.user.username)

    def qr_code(self):
        import pyotp

    def load_otp(self):
        pass

    def otp_verify(self):
        pass

    def say_hi(self):
        print('hi')

    # object = OTPModelManager()

    @classmethod
    def user_has_otp_device(cls, user):
        return cls.objects.filter(user=user).exists()

