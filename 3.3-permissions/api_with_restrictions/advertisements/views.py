from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return []

    def perform_create(self, serializer):
        """Выполняется при создании объекта."""
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        """Выполняется при обновлении объекта."""
        serializer.save()

    def perform_destroy(self, instance):
        """Выполняется при удалении объекта."""
        instance.delete()

