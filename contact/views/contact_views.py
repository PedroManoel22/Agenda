from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from contact.models import Contact


def index(request: HttpRequest):
    contacts = Contact.objects.filter(show=True).order_by("-id")[0:20]

    # print(contacts.query)

    context = {
        "contacts": contacts,
    }

    return render(request, "contact/index.html", context)


def contact(request: HttpRequest, contact_id: int):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    # print(contacts.query)

    context = {
        "contact": single_contact,
    }

    return render(request, "contact/contact.html", context)
