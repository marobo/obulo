# Django Customize User Creation With Confirmation Email

Make sure your django project is setup already ([https://onydev.pykafe.org/tet/detail/kria-projetu-uza-django/](https://onydev.pykafe.org/tet/detail/kria-projetu-uza-django/))

### Let's Get started
Git clone this repository into your existing django project
```
git clone https://github.com/marobo/user_registration.git
```

To include the app in your project, you need to add a reference to its configuration class in the **INSTALLED_APPS** section in `setting.py`. 

Edit the `your_project/settings.py` file and add the `user_registration` app to the **INSTALLED_APPS** setting. It’ll look like this:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_profile', # New app
]
```

We need to configure the email host server as well in the `settings.py` for confirmation mail. Add the below configuration in the `your_project/settings.py` file.

```
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = 'youremail@gmail.com'  
EMAIL_HOST_PASSWORD = 'yourpassword'  
EMAIL_PORT = 587
```

It will send out the text confirmation mail via terminal on your running server, if the creation account form is valid

Add a app url to the project/base configuration URL in `yourproject`/urls.py 
```
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_profile.urls')), # New app urls
    path('accounts/', include('django.contrib.auth.urls')), # New or maybe you have added already
]
```

Make a link for the user to click and visit the Create new account form in somewhere place, (i.e. in `index.html` or in `base_site.html`)
```
<a href="{% url 'create_account' %}">Create New Account</a>
```

Let's run server and then, try to clikc on that link, you will see the Create you new account form

# Note
This is just for playing in locally. If you wanna like to send the confirmation email to the real email address that user entering in the creations from, you need to change:
```
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" to EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
```

Please don't use your real email password in EMAIL_HOST_PASSWORD. Try generate it from gmail app password.


To Generate/create an app password in Gmail, you can do the following:
1. Log in to your Google account
2. Go to [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Select Security
4. Under "Signing in to Google," select 2-Step Verification
5. At the bottom of the page, select App passwords
6. Select Other from the Select app drop-down
7. Name the app password
8. Click Generate
9. Copy the new app password to the EMAIL_HOST_PASSWORD = 'yournewpassword' in settings.py file
10. Click Don

Visit this more instruction [https://support.google.com/mail/answer/185833?sjid=4090351568356337842-AP](https://support.google.com/mail/answer/185833?sjid=4090351568356337842-AP)
