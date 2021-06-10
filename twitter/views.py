from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tweetclone
from .forms import PostForm

# Create your views here.
def Tweet(request):
    # if method is post
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        # if form is valid
        if form.is_valid():
        # yes,save
            form.save()
        # redirect to home page 
            return HttpResponseRedirect('/')
        # else error
        else:
            return HttpResponseRedirect(form.errors.as_json())


    tweet = Tweetclone.objects.order_by('created_at').reverse().all()[:20]
    return render(request, 'tweet.html',
                   {'tweet': tweet})


  
# def index(request):
#     pictures = Tweetclone.objects.all()
#     return render(request,'tweet.html',
#                 {'tweet': tweet},)

def delete(request, id):
    #  find user
    
    post = Tweetclone.objects.get(id = id)
    post.delete()
    return HttpResponseRedirect('/')
    