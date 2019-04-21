from django.views.generic.base import TemplateView
from datetime import datetime


class Home_website(TemplateView):

    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context
