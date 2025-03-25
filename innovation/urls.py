from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('m_news/', views.m_news_list, name='m_news_list'),
    path('news/create/', views.news_create, name='news_create'),
    path('m_news/create/', views.m_news_create, name='m_news_create'),
    path('news/edit/<int:news_id>/', views.news_edit, name='news_edit'),
    path('m_news/edit/<int:news_id>/', views.m_news_edit, name='m_news_edit'),
    path('news/delete/<int:news_id>/', views.news_delete, name='news_delete'),
    path('m_news/delete/<int:news_id>/', views.m_news_delete, name='m_news_delete'),
    path('more1/', views.more1, name='more1'),
    path('more2/', views.more2, name='more2'),
    path('more3/', views.more3, name='more3'),
    path('news3/<int:news_id>/', views.news3_detail, name='news3_detail'),
    path('news2/<int:news_id>/', views.news2_detail, name='news2_detail'),
    path('news1/<int:news_id>/', views.news1_detail, name='news1_detail'),
]
