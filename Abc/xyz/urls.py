from django.urls import path
from xyz import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('profile', views.profile, name="profile"),
    path('logout', views.signout, name="logout"),
    path('delete/<int:id>',views.delete, name="delete")

]