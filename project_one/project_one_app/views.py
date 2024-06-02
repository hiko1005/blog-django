from django.shortcuts import render, redirect
from .models import Post
from .PostCreateService import PostCreate

# Create your views here.
def home(request):
    context = {
        "Title": "Home"
    }
    
    return render(request, template_name="home.html", context=context)

def create_post(request):
    if request.method == "GET":
        context = {
            "Title": "Create post"
        }
        
        return render(request, template_name="post_form.html", context=context)
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        PostCreate.save(title, text)
        return redirect("index")

def index(request):
    context = {
        "Title": "Main"
    }
    
    return render(request, template_name="index.html", context=context)
