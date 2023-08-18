# serializers converts database object to json data format
from rest_framework import serializers
from customers.models import Customer  # we import our define Customer class
# User class is already define, we just import it here
from django.contrib.auth.models import User


# here we define a serializer for our Customer class data. CustomerSerializer class inherit or comes from serializers.ModelSerializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# here we define a serializer for our User class data. UserSerializer class inherit or comes from serializers.ModelSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):  # create user object
        user = User.objects.create(
            username=validated_data['username'], email=validated_data['email'])

        user.set_password(validated_data['password'])
        user.save()

        return user
