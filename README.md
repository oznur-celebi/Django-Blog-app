# to add a new column(email, surname, name) in our classical UserCreateForm add a new py named forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name =forms.CharField(max_length=20)
    last_name =forms.CharField(max_length=20)


    class Meta:
        model =User
        fields = ['username', 'first_name' , 'last_name','email', 'password1', 'password2']

# to make more beatiful Form install crispy-forms
pip install django-crispy-forms

# register crispy-forms to INSTALLED_APPS into the main project settings.

'crispy_forms',
# add  crispy template pack to the bottom of settings
CRISPY_TEMPLATE_PACK ='bootstrap4'

# for login and logaout , we don not need to aview code,because django has it als builtin- view.
from django.contrib.auth import views as auth_views # import these builtins on the project.url

# the paths are to be added, too.
path('login/',auth_views.LoginView.as_view(template_name ="users/login.html"), name ='login'),
path('logout/',auth_views.LogoutView.as_view(template_name ="users/logout.html"), name ='logout'),

# create the login and logout htmls and a a code block to  the base.html

 # under the navbar <div class="navbar-nav">
              
              {% if user.is_authenticated  %}
                <a class="nav-item nav-link" href="{% url 'profile' %}">Profile</a>
                <a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>
              {% else %}
                <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
                <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
              {% endif %}
# craete Profile and Profile html and write function in blog/views.
 @login_required
def profile(request):
    return render(request, 'users/profile.html')
# we are using the login_required decarotor- one musst to be login to see the his page
from django.contrib.auth.decorators import login_required 
# http://127.0.0.1:8000/accounts/login/?next=/profile/... here next means--login because of login_required decorator
Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/accounts/login/?next=/profile/--
# to avoid this error go to the settings.py add this code at the bottom of the page
LOGIN_URL ='login'--# now it goes to the directly to the login page

# Now we are creating the profile func and profile.html
# For the func, we are extending the model,in oerder to load a userpicture

from  django.contrib.auth.models import User

# this is a one to one reletion model 
class Profile(models.Model)
      user = models.OneToOneField(User, on_delete=models.CASCADE)
# Here the user has a onetoonerelation with the UserModel. Wenn one the profile delete, the user is not deleted.--Thanks to the CASCADE

# the model is:
class Profile(models.Model):
      user = models.OneToOneField(User, on_delete =models.CASCADE)
      image =models.ImageField(default ='default.jpg', upload_to ='profile_pics')

      def __str__(self):
          return f'{self.user.user.name} Profile'
# install Pillow to use ImageField in to the Database
---pip install Pillow or python -m pip install Pillow

# if one a new model,as it were ,a new table in Databese created, one muss it  register on Admin.py and makemigrations und migrate.

from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

# add this code to the settings

MEDIA_ROOT = BASE_DIR / 'media' # this creates a folder called media for the userprofile pictures.
MEDIA_URL = '/media/'

# go to the database and add a userprofile, then media folder is automatic created.
# make a new profile html

{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
      <div class="media">
        <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
        <div class="media-body">
          <h2 class="account-heading">{{ user.username }}</h2>
          <p class="text-secondary">{{ user.email }}</p>
        </div>
      </div>
      <!-- FORM HERE -->
    </div>
{% endblock content %}

# go the this webpage ann add the given url by given way to the main urls.py
https://docs.djangoproject.com/en/4.0/howto/static-files/

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# my code is because of the security reason
if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#  create signals.py in to userapp
-----------code block.............
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from.models import Profile

@receiver(post_save, sender =User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender =User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()


# Creat a new model for the Profile edit

class Bio(models.Model):
     user = models.OneToOneField(User, on_delete =models.CASCADE)
     bio = models.TextField(max_length=500, blank=True)
     location = models.CharField(max_length=30, blank=True)
     birth_date = models.DateField(null=True, blank=True)
     def __str__(self):
          return f'{self.user.username} Profile'

# Create a multyform in forms.py for the Profile edit

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    #bio = RichTextField(blank =True, null =True)
   #bio = forms.TextField()
    class Meta:
        model =User
        fields = ['username', 'email',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta :
        model =Profile
        fields =['image']

class BioUpdateForm (forms.ModelForm):
     class Meta:
        model = Bio
        fields = ['bio','location','birth_date']


# Create a view func in views for the Profile edit

@login_required
def profile_edit(request):
    u_form =UserUpdateForm(instance =request.user) 
    p_form =ProfileUpdateForm(instance =request.user.profile)
    b_form =BioUpdateForm(instance =request.user.bio)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'b_form': b_form,

    } 

    return render(request, 'users/edit.html', context)


................codeblock end..................
#with signal,a Porfile Page will be automatically created and saved for every new user 


# edit html
<form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
   
        <fieldset class='form-group'>
          <legend class="border-bottom mb-4">Profile Info</legend>
          {{u_form|crispy}}
          {{p_form|crispy}}
          {{b_form|crispy}}
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-info" type="submit">Update</button>
   
        </div>
       </form>
# Becase of the reason  multiparty form, "enctype="multipart/form-data"" must be added