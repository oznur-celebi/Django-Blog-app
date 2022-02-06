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

#

