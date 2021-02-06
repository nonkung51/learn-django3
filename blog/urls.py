from django.urls import path

from . import views

urlpatterns = [
    path('blog/<int:id>', views.post_detail),
    path('', views.hello),
]