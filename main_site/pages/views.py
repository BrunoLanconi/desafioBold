from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# LoginRequiredMixin is used to avoid non-authenticated access
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
