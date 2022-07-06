from typing import List
from django.shortcuts import redirect, render
from .models import *
from .forms import ListForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    postlarim = Post.objects.all()
    return render(request, "index.html", {"postlarim":postlarim})

def details(request, id):
    postlarim = Post.objects.filter(id = id)
    context = {
        'post': postlarim
    }
    return render(request, "details.html", context)

def create(request):
    form = ListForm()
    context = {
        'form':form,
    }
    profile = request.user
    if request.method == "POST":
        form = ListForm(request.POST or None, request.FILES or None)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = profile
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Blogunuz oluşturuldu.')
            return render(request, "create.html", context)
            
    else:
        form = ListForm()
    return render(request, "create.html", context, )    


def delete(request, id):
    postlarim = Post.objects.filter(id = id)
    postlarim.delete()
    messages.add_message(request, messages.SUCCESS, 'Blogunuz silindi.')
    return redirect("index")