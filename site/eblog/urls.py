from django.urls import path
from . import views
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

urlpatterns = [
    path("about", views.about, name="about"),
    path("registration", views.registration, name="registration"),
    path("login", views.login, name="login"),
    path("blogs", views.blogs, name="blogs"),
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
    path('logout' , views.logout_view, name="logout"),
    path('makepost' , views.makepost, name="makepost"),
    path('videos',views.videos,name="videos"),
    path('feedback',views.feedback,name="feedback"),
    path('contacts',views.contacts,name="contacts"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()