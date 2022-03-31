from django.urls import *
from . import views

urlpatterns = [
    # ex: /shopping/
    #path('', views.index, name='index')

    path('', views.home, name='home'),
	path('login.html', views.login, name='login'),
	path('login.html/submit', views.loginSubmit, name='loginSubmit'),

### Signup customer webpages
	path('signup.html', views.signup, name='signup'),
	path('signup.html/submit', views.signupSubmit, name='signupSubmit'),
]