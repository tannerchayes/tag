from django.db import models


# Create your models here.
class Prompt(models.Model):
    question = models.TextField()


class Response(models.Model):
    text = models.TextField()
    prompt = models.ForeignKey(Prompt, on_delete=models.PROTECT, related_name="responses")
    next_prompt = models.ForeignKey(Prompt, null=True, on_delete=models.PROTECT, related_name="+")


# class Conclusion():
#     pass
