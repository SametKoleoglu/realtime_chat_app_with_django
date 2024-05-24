from django import forms
from django.forms import ModelForm

from .models import *


class ChatMessageForm(ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(
        attrs={'class': 'forms', 'rows': 2, 'cols': 20, "placeholder": "Type your message here",}))

    class Meta:
        model = ChatMessage
        fields = ['body',]
