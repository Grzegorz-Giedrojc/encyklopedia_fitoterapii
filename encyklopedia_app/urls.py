from django.conf.urls import url, include
from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.search, name='search'),
    path('fitoterapia/',views.fitoterapia, name="fitoterapia"),
    path('o_aplikacji/',views.o_aplikacji, name="o_aplikacji"),
    path('domowa_apteczka/',views.domowa_apteczka, name="domowa_apteczka"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
