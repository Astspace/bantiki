from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "conv_year")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('bnt/<int:bnt_id>/', views.bnts, name='bnts'),
    path('contacts/', views.contacts, name='contacts'),
]
