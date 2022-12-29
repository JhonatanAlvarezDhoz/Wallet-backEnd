from django.urls import path
from apps.QRrecord.api.views import ListQRCategoryAPIView, CreateQRCategoryAPIView, UpdateQRCategoryAPIView, DeleteQRCategoryAPIView, ListQRrecordAPIView, CreateQRrecordAPIView, UpdateQRrecordAPIView, DeleteQRrecordAPIView


urlpatterns =[

    path('list/qr_category/', ListQRCategoryAPIView.as_view()),
    path('create/qr_category/', CreateQRCategoryAPIView.as_view()),
    path('update/qr_category/<int:pk>', UpdateQRCategoryAPIView.as_view()),
    path('dlete/qr_category/<int:pk>', DeleteQRCategoryAPIView.as_view()),

    #QRrecord

    path('list/qr_record/', ListQRrecordAPIView.as_view()),
    path('create/qr_record/', CreateQRrecordAPIView.as_view()),
    path('update/qr_record/<int:pk>', UpdateQRrecordAPIView.as_view()),
    path('delete/qr_record/<int:pk>', DeleteQRrecordAPIView.as_view())
]