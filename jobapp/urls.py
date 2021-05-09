from django.urls import path
from jobapp.views import HomeView, SignView, LoginView, logout

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('signup', SignView.as_view(), name="signup"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', logout, name='logout')
]
