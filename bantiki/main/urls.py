from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "conv_year")

urlpatterns = [
    path('', views.index, name='home'),
    path('<conv_year:year>', views.years),
    path('<int:cat_id>', views.categories)
]
