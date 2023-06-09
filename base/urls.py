from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path("rooms/", views.rooms, name="rooms"),
    path("room/<int:pk>/", views.room, name="room"),
    path("create-room/", views.create_room, name="create-room"),
    path("update-room/<int:pk>", views.update_room, name="update-room"),
    path("delete-room/<int:pk>", views.delete_room, name="delete-room"),
    path("delete-message/<int:pk>", views.delete_message, name="delete-message"),
    path("user/<int:pk>", views.user_profile, name='user-profile'),
]
