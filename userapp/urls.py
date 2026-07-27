from django.urls import path
from.import views



urlpatterns = [
    path('auth/', views.auth_page, name='auth'),
    path('logout/', views.user_logout, name='logout')
]
