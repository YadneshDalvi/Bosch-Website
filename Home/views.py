from django.shortcuts import render,HttpResponse
from Home.models import Services
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is the about page")

def services(request):
    # return HttpResponse("This is the services page")
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        branch = request.POST.get('branch')
        reason = request.POST.get('reason')
        # file = request.POST.get('file')
        services= Services(name=name,phone=phone,email=email,branch=branch,reason=reason)
        services.save()
        
    return render(request, 'services.html')

def contact(request):
    return HttpResponse("This is the contact page")