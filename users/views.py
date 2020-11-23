from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignupPageView(generic.TemplateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
