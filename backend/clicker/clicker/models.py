from django.db import models
# from django.contrib.auth.models import User
from users.models import User

class ClickData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clicks = models.IntegerField(default=0)

    @property
    def username(self):
        return self.user.username