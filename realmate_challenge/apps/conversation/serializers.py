from rest_framework import serializers

from realmate_challenge.apps.message.serializers import MessageSerializer

from .models import Conversation

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = '__all__'
        read_only_fields = ['last_message_at']
