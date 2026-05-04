from django.db import models
from django.utils import timezone

# category (foreign key), show(boolean), picture (imagem)
# depois
# owner (foreign key)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True) # blank -> opcional
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True) # blank -> opcional
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True) # blank -> opcional
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to="pictures/%Y/%m/") # blank -> opcional

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


