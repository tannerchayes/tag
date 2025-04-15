from django.shortcuts import render
from django.views.generic import DetailView
from .models import Prompt


# Create your views here.
class PromptDetailView(DetailView):
    model = Prompt
    template_name = 'game/detail_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['prompt'] = Prompt.objects.get(pk=1)
        return context


