from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Product, OrderItem

User = get_user_model()

class ContactForm(forms.Form):
    
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': _("Your e-mail")
    }), label=_('Email'))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': _('Your message')
    }), label=_('Message'))


class AddToCartForm(forms.ModelForm):
    class Meta:
        model =OrderItem
        fields = ['quantity']