from django.urls import path

from . import views
urlpatterns = [
    path('login',views.login, name='login'),
    path('xerox',views.xerox, name='xerox'),
    path('store',views.store, name='store')
]