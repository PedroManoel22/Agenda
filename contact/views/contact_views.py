from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from contact.models import Contact


def index(request: HttpRequest):
    contacts = Contact.objects.filter(show=True).order_by("-id")[0:20]

    # print(contacts.query)

    context = {  # type: ignore
        "contacts": contacts,
        "site_title": "Contatos - ",
    }

    return render(request, "contact/index.html", context)  # type: ignore


def contact(request: HttpRequest, contact_id: int):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    site_title = f"{single_contact.first_name} {single_contact.last_name} - "

    # print(contacts.query)

    context = {"contact": single_contact, "site_title": site_title}  # type: ignore

    return render(request, "contact/contact.html", context)  # type: ignore
