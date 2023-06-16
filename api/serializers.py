from rest_framework import serializers

from api.models import user, reset, activations, varify_mail, addhouse


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


class addhouseserializer(serializers.ModelSerializer):
    class Meta:
        model=addhouse
        fields='__all__'
class varifyserializer(serializers.ModelSerializer):
    class Meta:
        model=varify_mail
        fields=['user_id','verify_otp']