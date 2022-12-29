from rest_framework import generics
from apps.opinion.models import Opinion
from apps.opinion.api.serializers import OpinionSerializers, CreateOpinionSerializers, UpdateOpinionSerializers, DeleteOpinionSerializers
from rest_framework_api_key.permissions import HasAPIKey


#---------------  Views Opinion  ---------------
class ListOpinionAPIView(generics.ListAPIView):
    queryset = Opinion.objects.filter(is_active=True)
    serializer_class = OpinionSerializers
    permission_classes = [HasAPIKey]


class CreateOpinionAPIView(generics.CreateAPIView):
    serializer_class = CreateOpinionSerializers
    permission_classes = [HasAPIKey]


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