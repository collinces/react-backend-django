# views is the file that contains functions handleling incoming requests

from customers.models import Customer
from customers.serializers import CustomerSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
# adding api restriction to customers page
def customers(request):
    # invoke serializer and return to client
    if request.method == 'GET':
        data = Customer.objects.all()
        serializer = CustomerSerializer(data, many=True)
        return Response({'customers': serializer.data})

    elif request.method == 'POST':
        # the post method here writes(add) data to database
        # data base generates new customer id for us
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
# api_view defines which methods are allowed in customer function below
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
# adding api restriction to customer page
def customer(request, id):
    # invoke serializer and return to client
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(data)
        return Response({'customer': serializer.data})

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        # the post method here modify data to database
        # data refers to the current and data=request.data is the new data we are passing coming from request
        serializer = CustomerSerializer(data, data=request.data)
        if serializer.is_valid():  # if data has been serialize
            serializer.save()
            return Response({'customer': serializer.data})
        # if serializer got failed throw error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    # data is coming from request.data
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # getting refresh/access token for new user
        refresh = RefreshToken.for_user(user)
        tokens = {'refresh': str(refresh), 'access': str(refresh.access_token)}
        return Response(tokens, status=status.HTTP_201_CREATED)

    # if serializer not valid throw error
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
