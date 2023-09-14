from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from content.forms import ContactForm
from django.views.generic.list import ListView
from core.models import Faq


class FaqView(ListView):
    model = Faq
    template_name = 'pages/faq.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] =  Faq.objects.filter(status="True").order_by("ordernumber")

        return context
    
  
    


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'pages/contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We have received your message.")
        email = form.cleaned_data.get(_('email'))
        message = form.cleaned_data.get(_('message'))

        full_message = f"""
            Received message below from , {email}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)