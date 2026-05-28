from django.http import HttpRequest
from django.shortcuts import render

from contact.models import Contact


def index(request: HttpRequest):
    contacts = Contact.objects.filter(show=True).order_by("-id")[0:2]

    # print(contacts.query)

    context = {
        "contacts": contacts,
    }

    return render(request, "contact/index.html", context)
