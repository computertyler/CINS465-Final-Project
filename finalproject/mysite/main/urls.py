from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test 1"),
    path("about/", views.about, name="about"),
    path("update/", views.update, name="update"),
    path("addGame/", views.addGame, name="addGame"),
    path("addLocation/", views.addLocation, name="addLocation"),
    path("updateLocation/", views.updateLocation, name="updateLocation"),
]

urlpatterns += staticfiles_urlpatterns()