from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('register',views.registerUser,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('',views.profile,name="profile"),
    path('profile/<str:pk>/',views.userProfile,name="user-profile"),
    path('account/',views.userAccount,name="account"),
    path('edit-account/',views.editAccount,name="edit-account"),
    path('dashboard/',views.custpanel,name="dashboard"),
]