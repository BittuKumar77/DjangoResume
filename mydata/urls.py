from django.urls import path
from .import views

app_name = 'data'
urlpatterns = [
    path('login',views.login,name='login'),
    path('/mydata',views.resume,name='mydata'),
    path('/logout',views.logout,name='logout')


]
