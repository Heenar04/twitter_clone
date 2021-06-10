from django import forms
from django import forms
from .models import Tweetclone 
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Tweetclone
        fields = '__all__'