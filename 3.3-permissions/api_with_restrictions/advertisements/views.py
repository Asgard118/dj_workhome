from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .permissions import IsAuthor

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    ordering_fields = ['created_at']



    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAuthor()]
        return []

    def perform_create(self, serializer):
        """Выполняется при создании объекта."""
        open_ads_count = Advertisement.objects.filter(
            creator=self.request.user, status=Advertisement.OPEN
        ).count()

        if open_ads_count >= 10 and статус != CLOSED:
            # Находим первое открытое объявление и закрываем его
            open_ad = Advertisement.objects.filter(
                creator=self.request.user, status=Advertisement.OPEN
            ).first()
            open_ad.status = Advertisement.CLOSED
            open_ad.save()

        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        """Выполняется при обновлении объекта."""
        serializer.save()

    def perform_destroy(self, instance):
        """Выполняется при удалении объекта."""
        instance.delete()

