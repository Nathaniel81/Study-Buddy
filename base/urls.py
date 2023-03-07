from django.urls import path
from . import views

"""
This module contains all URL patterns for the chat application.

The urlpatterns list maps URL patterns to their corresponding view functions.

URL Patterns:
- /login/: The login page.
- /logout/: The logout page.
- /register/: The registration page.
- /: The homepage.
- /room/<str:pk>/: The page for a specific chat room.
- /profile/<str:pk>/: The user profile page.
- /create-room/: The page for creating a new chat room.
- /update-room/<str:pk>/: The page for updating an existing chat room.
- /delete-room/<str:pk>/: The page for deleting an existing chat room.
- /delete-message/<str:pk>/: The page for deleting a specific message.
- /update-user/: The page for updating the current user's profile.
- /topics/: The page listing all available chat topics.
- /activity/: The page listing all recent chat activity.

"""

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
]
