from rest_framework import generics, status
from rest_framework.response import Response
from apps.opinion.models import Opinion, Category
from apps.opinion.api.serializers import OpinionSerializers, CreateOpinionSerializers, UpdateOpinionSerializers, DeleteOpinionSerializers
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated


#---------------  Views Opinion  ---------------
class ListOpinionAPIView(generics.ListAPIView):
    queryset = Opinion.objects.filter(is_active=True)
    serializer_class = OpinionSerializers
    permission_classes = [HasAPIKey, IsAuthenticated]


class CreateOpinionAPIView(generics.CreateAPIView):
    serializer_class = CreateOpinionSerializers
    permission_classes = [HasAPIKey, IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        if(not "opinion_category" in data):
            raise Exception("opinion_category is required")

        opinion_category_id = data["opinion_category"]
        
        opinion_category = Category.objects.get(id=opinion_category_id)
        data.pop("opinion_category")


        try:
            Opinion.objects.create(**data, opinion_category=opinion_category, user=self.request.user)
            return Response({"status_code": "OK"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            raise e


class UpdateOpinionAPIView(generics.UpdateAPIView):
    queryset = Opinion.objects.filter
    serializer_class = UpdateOpinionSerializers
    permission_classes = [HasAPIKey]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.id = request.data.get("id")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class DeleteOpinionAPIView(generics.ListAPIView):
    queryset = Opinion.objects.filter()
    serializer_class = DeleteOpinionSerializers
    permission_classes = [HasAPIKey]


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.id = request.data.get("id")
        instance.delete()
        return null