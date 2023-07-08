"""briscoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from auto_show import settings
from cars.views import add_car, car_models, taycan_models, nine_hundred_eleven_models, seven_hundred_eighteen_models, \
    panamera_models, macan_models, cayenne_models
from profiles.views import profiles, register_user, register_profile, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("profiles/", profiles, name="profiles"),
    path("register_user/", register_user, name="register_user"),
    path("register_profile/", register_profile, name="register_profile"),
    path("add_car/", add_car, name="add_car"),
    path("", car_models, name="index"),
    path("taycan_models", taycan_models, name="taycan_models"),
    path("911_models", nine_hundred_eleven_models, name="nine_hundred_eleven_models"),
    path("718_models", seven_hundred_eighteen_models, name="seven_hundred_eighteen_models"),
    path("panamera_models", panamera_models, name="panamera_models"),
    path("macan_models", macan_models, name="macan_models"),
    path("cayenne_models", cayenne_models, name="cayenne_models"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
