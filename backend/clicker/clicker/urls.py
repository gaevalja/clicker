from django.contrib import admin
from django.urls import path, include
from .views import ClickView, LeaderboardView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/click/', ClickView.as_view(), name='click'),
    path('api/leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('api/auth/', include('users.urls')),
]