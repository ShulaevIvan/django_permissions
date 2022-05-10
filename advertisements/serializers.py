from multiprocessing import context
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        
        model = User
        fields = ('id', 'username', 'first_name','last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(read_only=True,)

    class Meta:

        model = Advertisement
        fields = ('id', 'title', 'description', 'creator','status', 'created_at', )

    def create(self, validated_data):

        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

    def validate(self, data):

        counter_adv_user = Advertisement.objects.filter(creator=self.context['request'].user, status = 'OPEN').count()

        if self.context['request'].method == 'POST' or 'PATCH' and data['status'] == 'OPEN' and counter_adv_user >= 10:

            raise ValidationError('Превышен лимит открытых объявлений (10)') 

        return data
