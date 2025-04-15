from django.contrib import admin

from .models import Prompt, Response

# Register your models here.
admin.site.register(Prompt)
admin.site.register(Response)
