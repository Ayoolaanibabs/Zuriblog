from django.urls import path
from .views import blog_list_view, blog_detail_view, blog_create_view, blog_update_view, blog_delete_view, SignUpView, blog_create_comment

urlpatterns = [
    path('', blog_list_view.as_view(), name = 'home'),
    path('post/<int:pk>/', blog_detail_view.as_view(), name='post_detail'),
    path('post/new/', blog_create_view.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', blog_update_view.as_view(), name= 'post_edit'),
    path('post/<int:pk>/delete/', blog_delete_view.as_view(), name = 'post_delete'),
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('post/<int:pk>/comment/', blog_create_comment.as_view(), name = 'add_comment')
]