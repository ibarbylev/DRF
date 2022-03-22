from rest_framework import serializers

from .models import Kid, Sleep


class KidModelSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    birthday_year = serializers.IntegerField()

    class Meta:
        model = Kid
        fields = '__all__'

    def create(self, validated_data):
        return Kid.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('first_name', instance.first_name)
        instance.content = validated_data.get('last_name', instance.last_name)
        instance.created = validated_data.get('birthday_year', instance.birthday_year)
        instance.save()
        return instance


class SleepModelSerializer(serializers.ModelSerializer):
    authors = KidModelSerializer(many=True)
    date = serializers.DateTimeField()

    class Meta:
        model = Sleep
        fields = '__all__'
