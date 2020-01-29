from .models import Article
from rest_framework import serializers

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "description", "tags", "image")