from django.urls import path
from . import views
from .views import UserRecordView, MobileUserRecordView,DataSupirRecordView
urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('notes/create/', views.createNote),
    path('notes/<str:pk>/update/', views.updateNote),
    path('notes/<str:pk>/delete/', views.deleteNote),
    path('notes/<str:pk>/', views.getNote),
    path('users/', UserRecordView.as_view(), name='users'),
    path('mobile-users/', MobileUserRecordView.as_view(), name='mobile-users'),
    path('data-supir/', DataSupirRecordView.as_view(), name='data-supir'),
    path('data-supir/create/', views.createDataSupir, name='create-data-supir'),
]