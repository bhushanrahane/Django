from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.~
def index(request):
    context={
        "variable":"This is send"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is home about")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is home services")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone=request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email=email , phone=phone ,desc=desc  , date=datetime.today())
        contact.save()
        
    return render(request, 'contact.html')
    # return HttpResponse("This is home contact")