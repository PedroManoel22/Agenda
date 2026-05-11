from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# category (foreign key), show(boolean), picture (imagem)
# depois
# owner (foreign key)


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True) # blank -> opcional
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True) # blank -> opcional
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True) # blank -> opcional
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to="pictures/%Y/%m/") # blank -> opcional
    category = models.ForeignKey(Category, 
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True) # -> quando eu apagar uma category esse campo fique null
    
    owner = models.ForeignKey(User, 
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)
    

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
