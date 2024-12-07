from django.db import models

# Create your models here.
# side bar
class Nav(models.Model):
    nav_image = models.ImageField(upload_to="static/")
    nav_name = models.CharField(max_length=100)
    

class Header(models.Model):
    header_image = models.ImageField(upload_to="static/")
    header_heading = models.CharField(max_length=100)
    header_title = models.CharField(max_length=100)


# About
class About(models.Model):
    about_heading = models.CharField(max_length=100)
    about_details = models.CharField(max_length=1000)
    about_image = models.ImageField(upload_to="static/")
    about_sub_title = models.CharField(max_length=100)
    about_sub_details = models.CharField(max_length=1000)
    about_birthday = models.CharField(max_length=100)
    about_age = models.IntegerField()
    about_website = models.CharField(max_length=100)
    about_degree = models.CharField(max_length=100)
    about_phone = models.CharField(max_length=50)
    about_email = models.CharField(max_length=100)
    about_city= models.CharField(max_length=100)
    about_freelance = models.CharField(max_length=100)
    about_bootm_details= models.CharField(max_length=1000)

class Happyclient(models.Model):
    happy_number = models.IntegerField()
    happy_title = models.CharField(max_length=100)
    happy_image = models.ImageField(upload_to="static/")

# Skill
class Skill(models.Model):
    skill_heading = models.CharField(max_length=100)
    skill_progress = models.CharField(max_length=100)

#Portfolio
# class Portfolio(models.Model):
#     portfolio_text = models.CharField(max_length=1000)
#     portfolio_filed = models.CharField(max_length=100)
#     portfolio_appimage_1 =models.ImageField(upload_to="static/")
#     portfolio_appimage_2 =models.ImageField(upload_to="static/")
#     portfolio_appimage_3 =models.ImageField(upload_to="static/")
#     portfolio_subtext = models.CharField(max_length=100)
    
#Services
class Services(models.Model):
    services_text = models.CharField(max_length=100)
    services_title = models.CharField(max_length=100)
    services_details = models.CharField(max_length=1000)
    services_image = models.ImageField(upload_to="static/")

    #Testimonials
class Testimonials(models.Model):
    testimonials_review = models.CharField(max_length=100)
    testimonials_image = models.ImageField(upload_to="static/")
    testimonials_name = models.CharField(max_length=100)
    testimonails_post = models.CharField(max_length=100)
#Contact
class Contact(models.Model):
    contact_Address = models.CharField(max_length=100)
    contact_Call = models.CharField(max_length=100)
    contact_Email = models.CharField(max_length=100)
    contact_map = models.CharField(max_length=100)

# py manage.py makemigrations
# py manage.py migrate