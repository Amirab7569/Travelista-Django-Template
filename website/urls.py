from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('contact/', views.contact_view, name='contact' ),
    path('about/', views.about_view, name='about' ),
    path('nwsletter/', views.newsletter_view , name='newsletter')
]
