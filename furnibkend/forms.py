# forms.py
from django import forms
from .models import ContactRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest  # Ties the form to the model
        fields = ['firstname', 'lastname', 'email', 'message']  # Fields to include in the form