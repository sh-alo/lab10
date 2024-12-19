"""
URL configuration for lab_project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# studentapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_students, name='list_students'),
    path('add/', views.add_student, name='add_student'),
    path('<int:pk>/update/', views.update_student, name='update_student'),
    path('<int:pk>/delete/', views.delete_student, name='delete_student'),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

