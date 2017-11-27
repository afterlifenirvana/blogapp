from rest_framework import serializers
from models import Blog, Author
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Author 
        exclude = ('about_him',)

class BlogListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Blog
        exclude = ('tags','created_on','update_on','content')        
        depth = 2


class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Blog
        exclude = ('created_on','update_on')        
        depth = 2
        
