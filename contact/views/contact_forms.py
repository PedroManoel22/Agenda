from typing import Any

from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


def create(request: HttpRequest):

    form_action = reverse("contact:create")

    if request.method == "POST":
        form = ContactForm(request.POST)

        context: dict[str, Any] = {
            "form": form,
            "form_action": form_action,
        }

        if form.is_valid():
            contact: Contact = form.save()  # type: ignore
            return redirect("contact:update", contact_id=contact.pk)  # type: ignore
        return render(request, "contact/create.html", context)  # type: ignore

    context = {
        "form": ContactForm(),
        "form_action": form_action,
    }

    return render(request, "contact/create.html", context)  # type: ignore


def update(request: HttpRequest, contact_id: int):

    contact = get_object_or_404(Contact, pk=contact_id, show=True)

    form_action = reverse("contact:update", args=(contact_id,))

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)

        context: dict[str, Any] = {
            "form": form,
            "form_action": form_action,
        }

        if form.is_valid():
            contact = form.save()  # type: ignore
            return redirect("contact:update", contact_id=contact.pk)  # type: ignore

        return render(request, "contact/create.html", context)  # type: ignore

    context = {
        "form": ContactForm(instance=contact),
        "form_action": form_action,
    }

    return render(request, "contact/create.html", context)  # type: ignore
