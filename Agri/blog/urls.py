from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', views.index,),
    path('post/', views.post_list, name='post_list'),
    path('about/', views.about, name='about'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('currentissue/', views.currentissue, name='currentissue'),
    path('article/', views.article, name='article'),
    path('editorialboard/', views.editorialboard, name='editorialboard'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('user_posts/', views.user_posts, name='user_posts'),
    path('all_posts/', views.all_posts, name='all_posts'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)