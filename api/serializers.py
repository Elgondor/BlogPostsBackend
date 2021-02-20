from rest_framework import serializers
from .models import Post, Tag

class TagSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
         return value.name
    class Meta:
        model = Tag


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    authorId = serializers.CharField(source='author.id')
    author = serializers.CharField(source='author.author')
    class Meta:
        model = Post
        fields = ('id', 'author', 'authorId',  'likes', 'popularity', 'reads',  'tags')