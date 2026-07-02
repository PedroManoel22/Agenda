from django.http import HttpRequest
from django.shortcuts import render


def create(request: HttpRequest):

    context = {}

    return render(request, "contact/create.html", context)  # type: ignore
