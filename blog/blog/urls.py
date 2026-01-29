from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('post.urls')),
]
# http://localhost:8000/главныйurls/urlsприложения
# http://localhost:8000/blog/posts/