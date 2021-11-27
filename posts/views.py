from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')
        else:
            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())

    # Get all posts, Limit = 20

    posts = Post.objects.all()[:20]

    # Show
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/")


def edit(request,post_id):
    post=Post.objects.get(id=post_id)
    if request.method == 'POST':
          form=PostForm(request.POST,request.FILES,instance = post)
          
          if form.is_valid():
             post.save()
             return HttpResponseRedirect('/')
    else:
        form=PostForm(PostForm)
        return render(request,'edit.html',{'post':post, 'form':form})