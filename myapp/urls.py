from django.urls import path
from myapp import views

urlpatterns = [
    path ("",views. index_view ),
    path('about/', views.about_view, name='about'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('contact/', views.contactpage, name='contact'),
]
