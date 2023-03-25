from django.urls import path
from .import views
from .views import RegisterUser, LoginUser, AddRequest

urlpatterns = [
    path('', views.desktop, name='desktop'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('add-request/', AddRequest.as_view(), name='add_request'),

    path('ajax/load-compressors/', views.load_compressors, name='ajax_load_compressors'),
]