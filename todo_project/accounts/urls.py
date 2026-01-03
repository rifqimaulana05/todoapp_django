from django.urls import path
from .views import register, login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path(
    #     'logout/',
    #     LogoutView.as_view(next_page='login'),
    #     name='logout'
    # ),
    path('registration/', register, name='register'),
    path('registration/', login_view, name='login'),
]
