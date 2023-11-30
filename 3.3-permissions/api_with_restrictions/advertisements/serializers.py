from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at',)

    def create(self, validated_data):
        """Метод для создания."""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context["request"].user

        open_ads_count = Advertisement.objects.filter(creator=self.request.user, status=Advertisement.OPEN).count()
        if open_ads_count >= 10 and статус != CLOSED:
            raise serializers.ValidationError("Превышено количество открытых объявлений (максимум 10).")

        return data

    def update(self, instance, validated_data):
        """Метод для обновления."""
        if instance.creator != self.context["request"].user:
            raise serializers.ValidationError("Вы не можете обновить объявление, которое вам не принадлежит.")
        return super().update(instance, validated_data)

