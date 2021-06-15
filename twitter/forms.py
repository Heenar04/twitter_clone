from django import forms
from django import forms
from .models import Tweetclone, Contact
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Tweetclone
        fields = '__all__'
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'