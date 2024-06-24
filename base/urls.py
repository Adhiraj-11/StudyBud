from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),
    path('',views.home,name='home'),
    path('room/<int:pk>/',views.room,name='room'),
    path('create-room/',views.create_room,name="create-room"),
    path('update-room/<int:pk>/',views.update_room,name="update-room"),
    path('delete-room/<int:pk>/',views.delete_room,name="delete-room"),
    path('delete-message/<int:pk>/',views.deleteMessage,name="delete-message"),
    path('profile/<str:pk>/', views.userProfile,name="user-profile"),
    path('update-user/',views.updateUser,name="update-user"),
    ]
