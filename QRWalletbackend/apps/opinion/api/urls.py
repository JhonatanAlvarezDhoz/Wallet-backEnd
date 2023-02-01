from django.urls import path
from apps.opinion.api.views import ListOpinionAPIView, CreateOpinionAPIView, UpdateOpinionAPIView, DeleteOpinionAPIView

urlpatterns = [
    path('list/', ListOpinionAPIView.as_view()),
    path('create/', CreateOpinionAPIView.as_view()),
    path('update/<int:pk>', UpdateOpinionAPIView.as_view()),
    path('delete/<int:pk>', DeleteOpinionAPIView.as_view()),
]