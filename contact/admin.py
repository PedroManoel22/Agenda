# flake8: noqa

from django.contrib import admin
from contact import models

@admin.register(models.Contact) 
class ContactAdmin(admin.ModelAdmin): # type: ignore
    list_display = "id", "first_name","last_name", "phone",
    ordering = "-id",
    # list_filter = "created_date", # filtro por data de criação
    search_fields = "id","first_name", "last_name", # campo de pesquisa
    list_per_page = 10
    list_max_show_all = 200
    list_editable = "first_name", "last_name",
    list_display_links = "id", "phone",


@admin.register(models.Category) 
class CategoryAdmin(admin.ModelAdmin): # type: ignore
    list_display = "name",
    ordering = "-id",
    