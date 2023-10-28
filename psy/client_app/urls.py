from django.urls import path,include

from .views import *

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', sign_in, name='sig_up'),
    path('session_record/', SessionRecordView.as_view(), name='session_record'),
    path('sessions/', SessionsList.as_view(), name='sessions'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),

]