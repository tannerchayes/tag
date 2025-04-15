from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.PromptDetailView.as_view(), name="prompt-detail"),
]