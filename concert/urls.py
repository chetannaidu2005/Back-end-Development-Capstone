from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),        # Home page
    path("songs/", views.songs, name="songs"),        # Songs page
    path("photos/", views.photos, name="photos"),     # Photos page
    path("login/", views.login_view, name="login"),   # Login
    path("logout/", views.logout_view, name="logout"),# Logout
    path("signup/", views.signup, name="signup"),     # Signup
    path("concerts/", views.concerts, name="concerts"), # Concerts list
    path("concert-detail/<int:id>/", views.concert_detail, name="concert_detail"),  # Concert detail
    path("concert_attendee/", views.concert_attendee, name="concert_attendee"),     # Concert attendee
]
