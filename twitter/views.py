from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
from .models import Tweetclone
from .forms import PostForm, ContactForm


# Create your views here.
def Tweet(request):
    # if method is post
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
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
                   {'tweet': tweet, 'form':form})


  
# def index(request):
#     pictures = Tweetclone.objects.all()
#     return render(request,'tweet.html',
#                 {'tweet': tweet},)

# def loadPicture (request):
#     if request.method =='POST':
#     form = PostForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#     return HttpResponseRedirect('/')
                  
    
def Contacts(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        # if form is valid
        if form.is_valid():
        # yes,save
            form.save()
        # redirect to home page 
            return HttpResponseRedirect('/')
        # else error
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, 'contact.html')

def edit(request, id):
    #  edit post
    
    post = Tweetclone.objects.get(id = id)
    if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
        
        # if form is valid
            if form.is_valid():
        # yes,save
                form.save()
        # redirect to home page 
                return HttpResponseRedirect('/')
        # else error
            else:
                return HttpResponseRedirect(form.errors.as_json())

    else:
        form= PostForm
        return render(request,'edit.html',{'tweet': post ,'form': form})

def like(request, id):
      # Get requested tweet
        post = Tweetclone.objects.get(id = id)
        
  # Add count
        new_like_count = post.like_count + 1
        post.like_count = new_like_count
  # Save
        post.save()
        # return JsonResponse({'result': 'successful'})
        return HttpResponseRedirect('/')

def delete(request, id):
    #  delete post
    
    post = Tweetclone.objects.get(id = id)
    post.delete()
    return HttpResponseRedirect('/')
    