from django.urls import path
from . import views
from . views import ServiceHome, CompressorDetail, AddRequestService

urlpatterns = [
    path('', ServiceHome.as_view(), name='service'),
    path('compressor/<int:id>/', CompressorDetail.as_view(), name='compressor'),
    path('compressor/<int:id>/add_request', AddRequestService.as_view(), name='add_request_service'),
    path('compressor/<int:id>/history/', views.history, name='history'),
    path('compressor/<int:id>/history_request/', views.history_request, name='history_request'),
    path('compressor/<int:id>/history_request/<id_post>', views.history_request_post, name='history_request_post'),
    path('compressor/<int:id>/history_request/<id_post>/shut',views.request_shut, name='request_shut'),
    path('compressor/<int:id>/history_inspection/', views.history_inspection, name='history_inspection'),
    path('compressor/<int:id>/add-inspection', views.add_inspection, name='add_inspection'),
    path('compressor/<int:id>/history_inspection/<int:id_post>/', views.history_inspection_post, name='history_inspection_post'),
    path('compressor/<int:id>/statistic/', views.statistic, name='statistic'),
    path('compressor/<int:id>/add-statistic/', views.add_statistic, name='add_statistic'),
    path('inventory/', views.inventory, name='inventory'),
]