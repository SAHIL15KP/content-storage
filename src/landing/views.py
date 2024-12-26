from django.shortcuts import render
<<<<<<< HEAD
from items.models import Item
# Create your views here.
from projects.decorators import project_required

@project_required
def dashboard_view(request):
    return render(request, "dashboard/home.html", {})

def home_page_view(request):
    if not request.user.is_authenticated:
        return render(request, "landing/home.html", {})
    return dashboard_view(request)

def about_page_view(request):
    print(request.project)
    return render(request, "landing/home.html", {})

def server_error_page(request):
    raise Exception
    return render(request, "landing/error.html", {})
=======

# Create your views here.
def hello(request):
    return render(request , "home.html")
>>>>>>> 7aaa06d17b82687db3714004d4251da1285ce34f
