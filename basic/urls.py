from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.home, name='home'),
	path('signin/',views.signin,name='signin'),
	path('topic/',views.viewtopic,name='viewtopic'),
	path('signup/',views.signup,name='signup'),
	path('<int:topic_id>/playlist/<int:p_id>/',views.playvideo,name='playvideo'),
	path('<int:topic_id>/',views.collection,name='collection'),
	path('createplayll/',views.createplay,name='createplay'),
	path('<int:topic_id>/<int:pid>/addurl/',views.addurl,name='addurl'),
	path('logout/',views.signout,name='signout'),
]