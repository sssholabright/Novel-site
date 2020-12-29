from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'picture', 'category', 'published',  'author', 'excerpt', 'content', 'status')
        model = Post
        
