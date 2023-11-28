from django.urls import path, include
from .views import *


app_name = 'portfolios'

urlpatterns = [
    path("", CourseListView.as_view(),name='portfolios'),
    path("category/<str:cat>",CourseListView.as_view(),name="portfolio_cat"),
    path("client/<str:client>",CourseListView.as_view(),name="portfolio_client"),
    path("search/",CourseListView.as_view(),name="course_search"),
    path("portfolio-detail/<int:pk>",CourseDetailView.as_view(),name="portfolio_detail"),
    path("api/V1/",include('main.api.V1.urls')),
]