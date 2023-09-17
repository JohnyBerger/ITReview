from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer

class UserApiView(APIView):
    queryset = User.objects.all()
    def get(self, request):

        users = User.objects.all()
        user_serializer = UserSerializer(instance=users, many=True)
        return Response(user_serializer.data)