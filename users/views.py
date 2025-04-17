from django.shortcuts import render
from .models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model

User = get_user_model()


class UserLoginView(LoginView):
    template_name = "game/user_login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

