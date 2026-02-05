from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('register/', include('userAcc.urls')),
    path('login/', auth_views.LoginView.as_view(
        template_name='userAcc/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),
         name='logout')
]



# http://localhost:8000/главныйurls/urlsприложения
# http://localhost:8000/blog/posts/