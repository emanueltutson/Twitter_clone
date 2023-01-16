
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.
def index(request):
    #If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #If the form is valid
        if form.is_valid():
            #If yes, save
            form.save()
            #redirect to home
            return HttpResponseRedirect('/')
            #If no, show error
        else:
            return HttpResponseRedirect(form.errors.as_json())


    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form=PostForm
    #show
    return render(request, 'posts.html',
                  {'posts': posts})

def delete(request, post_id):
#Find user
 post= Post.objects.get(id=post_id)
 post.delete()
 return HttpResponseRedirect('/')

def likeview(request, post_id):
    newcount = Post.objects.get(id=post_id)
    newcount.like_count +=1
    newcount.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    posts = Post.objects.get(id =post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = PostForm
    return render(request,'edit.html',{"posts":posts, 'form':form})
            
        
