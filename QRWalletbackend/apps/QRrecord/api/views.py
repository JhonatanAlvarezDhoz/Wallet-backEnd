from rest_framework import generics, status
from apps.QRrecord.models import QRrecord, QRCategory
from apps.QRrecord.api.serializers import QRCategorySerializers, CreateQRCategorySerializers, UpdateQRCategorySerializers, DeleteQRCategorySerilizers, QRrecordSerializers, CreateQRrecordSerializers, UpdateQRrecordSerializer, DeleteQRrecordSerializer
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


#---------------  Views QRCategory  ---------------
class ListQRCategoryAPIView(generics.ListAPIView):
    serializer_class = QRCategorySerializers
    permission_classes = [HasAPIKey, IsAuthenticated]

    def get_queryset(self):

        category_user = self.request.user
        queryset = QRCategory.objects.filter(user_id=category_user)
        return queryset.order_by('-id')
    

class CreateQRCategoryAPIView(generics.CreateAPIView):
    serializer_class = CreateQRCategorySerializers
    permission_classes = [HasAPIKey, IsAuthenticated]

class UpdateQRCategoryAPIView(generics.UpdateAPIView):
    queryset = QRCategory.objects.filter(is_active=True)
    serializer_class = QRCategorySerializers
    permission_classes = [HasAPIKey, IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.id = request.data.get("id")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class DeleteQRCategoryAPIView(generics.DestroyAPIView):
    queryset = QRCategory.objects.filter(is_active=True)
    serializer_class = DeleteQRCategorySerilizers
    permission_classes = [HasAPIKey, IsAuthenticated]


    # def delete(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.id = request.data.get("id")
    #     instance.delete()
    #     return super().delete(request, *args, **kwargs)


#---------------  Views QRrecod  ---------------
class ListQRrecordAPIView(generics.ListAPIView):
    serializer_class = QRrecordSerializers
    permission_classes = [HasAPIKey, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(user)
        categories = QRCategory.objects.filter(user_id=user)
        queryset = QRrecord.objects.filter(qr_category__in=categories)
        return queryset

class CreateQRrecordAPIView(generics.CreateAPIView):


    serializer_class = CreateQRrecordSerializers
    permission_classes = [HasAPIKey, IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        if(not "qr_category" in data): 
            raise Exception("qr_category is required")
        
        qr_category_id = data["qr_category"]

        qr_category = QRCategory.objects.get(pk=qr_category_id)
        data.pop("qr_category")

        try:
            QRrecord.objects.create(**data, qr_category=qr_category)
            return Response({"status_code": "OK"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            raise e

        

    

class UpdateQRrecordAPIView(generics.UpdateAPIView):
    queryset = QRrecord.objects.filter(is_active=True)
    serializer_class = UpdateQRrecordSerializer
    permission_classes = [HasAPIKey, IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.id = request.data.get("id")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class DeleteQRrecordAPIView(generics.DestroyAPIView):
    queryset = QRrecord.objects.filter(is_active=True)
    serializer_class = DeleteQRrecordSerializer
    permission_classes = [HasAPIKey, IsAuthenticated]


    # def delete(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.id = request.data.get("id")
    #     instance.delete()
    #     return super().delete(request, *args, **kwargs)