from rest_framework import serializers
from Library.models import Author,Book


class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.CharField(source='author.id')
    author_name = serializers.CharField(source='author.name')
    class Meta:
        model = Book
        fields = ["id","name","author_id","author_name"]
    def create(self, validated_data):
    
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.published = validated_data.get('published', instance.published)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    def create(self, validated_data):
    
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.published = validated_data.get('published', instance.published)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    book = NewSerializer(many=True,read_only=True)
    class Meta:
        model = Author
        fields = ["id","name","book"]
        
    def create(self, validated_data):
    
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

