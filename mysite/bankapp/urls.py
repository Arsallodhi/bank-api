from django.urls import path

from . import views

app_name = 'bankapp'
urlpatterns = [
    path('banks/', views.LBankAPI.as_view()),
    path('banks/create', views.CBankAPI.as_view()),
    path('banks/<int:pk>/', views.RUDBankAPI.as_view()),
    path('accounts/', views.LCAccountAPI.as_view()),
    path('accounts/<int:pk>/', views.RUDAccountAPI.as_view()),
]