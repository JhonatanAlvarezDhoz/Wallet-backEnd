from rest_framework import generics, status
from apps.QRrecord.models import QRrecord, QRCategory
from apps.QRrecord.api.serializers import QRCategorySerializers, CreateQRCategorySerializers, UpdateQRCategorySerializers, DeleteQRCategorySerilizers, QRrecordSerializers, CreateQRrecordSerializers, UpdateQRrecordSerializer, DeleteQRrecordSerializer
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


#---------------  Views QRCategory  ---------------
class ListQRCategoryAPIView(generics.ListAPIView):
    queryset = QRCategory.objects.filter(is_active=True)
    serializer_class = QRCategorySerializers
    permission_classes = [HasAPIKey, IsAuthenticated]

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

class DeleteQRCategoryAPIView(generics.ListAPIView):
    queryset = QRCategory.objects.filter(is_active=True)
    serializer_class = DeleteQRCategorySerilizers
    permission_classes = [HasAPIKey, IsAuthenticated]


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.id = request.data.get("id")
        instance.delete()
        return null


#---------------  Views QRrecod  ---------------
class ListQRrecordAPIView(generics.ListAPIView):
    queryset = QRrecord.objects.filter(is_active=True)
    serializer_class = QRrecordSerializers
    permission_classes = [HasAPIKey, IsAuthenticated]

class CreateQRrecordAPIView(generics.CreateAPIView):


    serializer_class = CreateQRrecordSerializers
    permission_classes = [HasAPIKey, IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        if(not "qr_category_id" in data):
            raise Exception("qr_category_id is required")
        
        qr_category_id = data["qr_category_id"]
        qr_category = QRCategory.objects.get(id=qr_category_id, user_id=self.request.user)
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

class DeleteQRrecordAPIView(generics.ListAPIView):
    queryset = QRrecord.objects.filter(is_active=True)
    serializer_class = DeleteQRrecordSerializer
    permission_classes = [HasAPIKey, IsAuthenticated]


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.id = request.data.get("id")
        instance.delete()
        return null