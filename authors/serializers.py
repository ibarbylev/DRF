from rest_framework import serializers

from .models import Author, Book


class AuthorModelSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    birthday_year = serializers.IntegerField()

    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('first_name', instance.first_name)
        instance.content = validated_data.get('last_name', instance.last_name)
        instance.created = validated_data.get('birthday_year', instance.birthday_year)
        instance.save()
        return instance


class BookModelSerializer(serializers.ModelSerializer):
    authors = AuthorModelSerializer(many=True)
    title = serializers.CharField(max_length=255)

    class Meta:
        model = Book
        fields = '__all__'
