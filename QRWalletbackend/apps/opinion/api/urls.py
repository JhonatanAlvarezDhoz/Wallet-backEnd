from django.urls import path
from apps.opinion.api.views import ListOpinionAPIView, CreateOpinionAPIView, UpdateOpinionAPIView, DeleteOpinionAPIView, UserOpinions

urlpatterns = [
    path('list/', ListOpinionAPIView.as_view()),
    path('user/opinions/', UserOpinions.as_view() ),
    path('create/', CreateOpinionAPIView.as_view()),
    path('update/<int:pk>', UpdateOpinionAPIView.as_view()),
    path('delete/<int:pk>', DeleteOpinionAPIView.as_view()),
]