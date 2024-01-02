from django.urls import path
from app_hw.views import *

urlpatterns = [
    path('', main_page_view, name='main_page'),
    path('detail/<int:post_id>/', detail_page_view, name='detail_page'),
    path('create/', CreatePost.as_view(), name='create_page'),
    path('delete/<int:pk>', delete_post_view, name='delete_page'),
    path('update/<int:pk>', update_post_view, name='update_page'),
]