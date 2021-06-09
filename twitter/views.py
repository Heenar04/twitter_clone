from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweetclone

# Create your views here.
def Tweet(request):
    tweet = Tweetclone.objects.all()[:20]
    return render(request, 'tweet.html',
                   {'tweet': tweet})