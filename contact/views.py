from django.shortcuts import render
from .models import Contact
from .forms import ContactForm


def contact_me(request):
    contact = Contact.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact": contact,
            "contact_form": contact_form,
        },
    )
