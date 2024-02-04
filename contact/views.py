from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact_me(request):
    contact = Contact.objects.all().order_by('-updated_on').first()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid:
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'I received your message! I will try to respond within three days.'
            )
    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact": contact,
            "contact_form": contact_form,
        },
    )
