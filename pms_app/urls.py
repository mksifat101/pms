from django.urls import path
from pms_app import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('company/', views.company, name='company'),
    path('add_company/', views.addcompany, name='addcompany'),
    path('manager/', views.manager, name='manager'),
    path('add_manager/', views.addmanager, name='addmanager'),
    path('developer/', views.developer, name='developer'),
    path('add_developer/', views.adddeveloper, name='adddeveloper'),
    path('project/', views.project, name='project'),
    path('add_project/', views.addproject, name='addproject')
]
