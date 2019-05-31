from rest_framework import serializers
from Library.models import Author,Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["name","id","author"]
        depth = 1
    def create(self, validated_data):
    
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.published = validated_data.get('published', instance.published)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Author
        fields = "__all__"
    def create(self, validated_data):
    
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

