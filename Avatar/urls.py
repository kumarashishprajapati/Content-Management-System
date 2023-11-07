from .import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login_request,name="login"),
    path('logout/',views.logout_request,name="logout"),
    path('profile/',views.profile_view,name="profile"),
    path('create/',views.create_profile,name="create"),
    path('update/<str:pk>/',views.update_profile,name="update"),


]