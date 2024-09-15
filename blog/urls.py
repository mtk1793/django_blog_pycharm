from django.urls import path
from . import views

#Be careful not to use the veiw with () as we do that it means that we are trying to call the function itself while we are calling them by references
urlpatterns = [
    path('', views.index, name='starting-page'),
    path('posts',views.posts, name='posts-page'),
    path('posts/<slug:slug>',views.single_post, name='post-detail-page')
]