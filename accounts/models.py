from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    username = models.CharField(
        'username',
        max_length=50,
        unique=True,
        help_text='50 characters atau kurang. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "Sudah ada nama akun yang sama bro.",
        },
    )
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "udah ada email akun yang sama bro.",
                              })
    gender = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    about = models.TextField(blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "gender"]

    def __unicode__(self):
        return self.email