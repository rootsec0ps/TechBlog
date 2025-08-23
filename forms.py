from django import forms

from .models import Post, Reply

class ReplyForm(forms.ModelForm):
    name = forms.CharField(label="Your name", max_length=100, required=True)

    class Meta:
        model = Reply
        fields = ['text', 'name']
        labels = {'text': '', 'name': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}