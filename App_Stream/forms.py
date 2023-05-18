from django.forms import ModelForm
from django import forms
from App_Stream.models import Video, Comment

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class SearchForm(forms.Form):
     search_vid = forms.TextInput(attrs={'type': 'text'})
