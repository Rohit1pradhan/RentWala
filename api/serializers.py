from rest_framework import serializers

from api.models import user, reset, activations, addhouse, varify_mail


class userserializer(serializers.Serializer):
    email_id = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=30)
    mobile_number = serializers.CharField(max_length=15)
    city = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return user.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.email_id=validated_data.get('email_id',instance.email_id)
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance


class resetserializer(serializers.Serializer):
    user_id=serializers.IntegerField()
    OTP=serializers.IntegerField()

    def create(self, validated_data):
        return reset.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.user_id=validated_data.get('user_id',instance.user_id)
        instance.OTP = validated_data.get('OTP_id', instance.OTP)
        instance.save()
        return  instance


class activationserializer(serializers.Serializer):
    user_id=serializers.IntegerField()
    activation=serializers.CharField(max_length=10)
    current_city=serializers.CharField(max_length=30)

    def create(self, validated_data):
        return activations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id=validated_data.get('user_id',instance.user_id)
        instance.activation = validated_data.get('activation', instance.activation)
        instance.current_city = validated_data.get('current_city', instance.current_city)
        instance.save()
        return  instance


class addhousezerializer(serializers.Serializer):
    owner_id = serializers.IntegerField()
    house_type = serializers.CharField(max_length=100)
    rent = serializers.CharField(max_length=20)
    facing = serializers.CharField(max_length=30)
    area = serializers.CharField(max_length=30)
    conditions = serializers.CharField(max_length=200)
    facillities = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return addhouse.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.owner_id = validated_data.get('owner_id', instance.owner_id)
        instance.house_type = validated_data.get('house_type', instance.house_type)
        instance.rent = validated_data.get('rent', instance.rent)
        instance.facing = validated_data.get('facing', instance.facing)
        instance.area = validated_data.get('area', instance.area)
        instance.conditions = validated_data.get('conditions', instance.conditions)
        instance.facillities = validated_data.get('facillities', instance.facillities)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
class varifyserializer(serializers.ModelSerializer):
    class Meta:
        model=varify_mail
        fields=['user_id','verify_otp']