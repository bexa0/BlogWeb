from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author_post', 'title', 'description_post', 'quantity_likes', 'tags']

    author_post = forms.CharField()
    title = forms.CharField()
    description_post = forms.Textarea()
    quantity_likes = forms.IntegerField()
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),widget=forms.CheckboxSelectMultiple)