from django.shortcuts import render
from website import models

# Create your views here.
def home(req):
    nav = models.Nav.objects.all()
    header = models.Header.objects.all()
    about = models.About.objects.all()
    happyclient = models.Happyclient.objects.all()
    skill = models.Skill.objects.all()
    # portfolio = models.Portfolio.objects.all()
    services = models.Services.objects.all()
    testimonials = models. Testimonials.objects.all()
    contact = models.Contact.objects.all()



    obj = {"header":header,"about":about,"happyclient":happyclient,"skill":skill,"services":services,"testimonials":testimonials,"contact":contact,"nav":nav}
    return render(req,"home.html",obj)

def sidebar(req):
    return render(req,"sidebar.html")

def footer(req):
    return render(req,"footer.html")

# def contact(req):
#     return render(req,"contact.html")

# def skill(req):
#     return render(req,"skill.html")
