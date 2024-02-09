from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        contact_form = ContactForm({'message': 'I would like to ask you'})
        self.assertTrue(contact_form.is_valid(),
                        msg=' Contact form, message field - is invalid')

    def test_form_is_invalid(self):
        contact_form = ContactForm({'name': ''})
        self.assertFalse(contact_form.is_valid(), msg='Form is valid')

    def test_form_is_valid(self):
        contact_form = ContactForm({'email': ''})
        self.assertTrue(contact_form.is_valid(),
                        msg='Email field is empty but form is valid')
