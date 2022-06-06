from django.urls import path, include
from core import views 
from django.conf.urls.static import static
from django.conf import settings
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth import views as auth_views
# url pattern
urlpatterns = [
    path('', views.index, name = 'index'),
    path('accounts/', include([
        path('login/', auth_views.LoginView.as_view(next_page = 'home/'), name='accounts/login/'),
        path('register/home/', views.home, name = 'accounts/register/home/'), 
        path('login/home/', views.home, name = 'accounts/login/home/'),
    ])),   
    path('home/', include([
        path('', views.home, name = 'home/'),
        path('new_post/', views.post, name = 'new post'),
        path('comment/', views.comment, name = 'comment'),
        path('profile/', views.profile, name = 'profile'),
    ])),
    
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)