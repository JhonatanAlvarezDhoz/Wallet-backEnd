from django.urls import path
from apps.opinion.api.views import ListOpinionAPIView, CreateOpinionAPIView, UpdateOpinionAPIView, DeleteOpinionAPIView

urlpatterns = [
    path('list/opinion/', ListOpinionAPIView.as_view()),
    path('create/opinion/', CreateOpinionAPIView.as_view()),
    path('update/opinion/<int:pk>', UpdateOpinionAPIView.as_view()),
    path('delete/opinion/<int:pk>', DeleteOpinionAPIView.as_view()),
]