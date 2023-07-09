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
from cars.views import add_car, car_models, car_models_details, car_details
from profiles.views import profiles, register_user, register_profile, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("profiles/", profiles, name="profiles"),
    path("register_user/", register_user, name="register_user"),
    path("register_profile/", register_profile, name="register_profile"),
    path("add_car/", add_car, name="add_car"),
    path("", car_models, name="index"),
    path("car_details/<int:car_id>/", car_details, name="car_details"),
    path("car_models_details/<carmodel_title>/", car_models_details, name="car_models_details"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
