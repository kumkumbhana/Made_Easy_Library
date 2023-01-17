from django.urls import path
from . import  views
urlpatterns = [

    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('login', views.login_view,name='login'),
    path('logout', views.handlelogout,name='handlelogout'),
    path('signup', views.handlesignup,name='handlesignup'),
    path('feedback', views.feedback,name='feedback'),
    path('addbook', views.addbook,name='addbook'),
    path('home', views.home,name='home'),
    path('fiction', views.fiction,name='fiction'),
    path('nonfiction', views.nonfiction,name='nonfiction'),
    path('novel', views.novel,name='novel'),
    path('story', views.story,name='story'),
    path('programming', views.programming,name='programming'),
    path('engineering', views.engineering,name='engineering'),

]