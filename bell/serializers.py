from rest_framework import serializers
from bell.models import *


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ('id', 'name', 'surname', 'welcome')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('id', 'visitor', 'date')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'visit', 'message_text')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'visitor', 'notification_text', 'date')


    """
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=200)
    surname = serializers.CharField(required=False, allow_blank=True, max_length=200)
    welcome = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Visitor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.welcome = validated_data.get('welcome', instance.welcome)
    """