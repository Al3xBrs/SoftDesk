from rest_framework_simplejwt.views import TokenObtainPairView, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from Users.serializers import (
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    ProfileSerializer,
)
from Projects.models import Contribution, Issue, Comment
from Users.models import AnyUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Register User
class RegisterView(generics.CreateAPIView):
    queryset = AnyUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# api/profile  and api/profile/update
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class DeleteUserDataView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        user = self.request.user

        Contribution.objects.filter(user=user).delete()
        Issue.objects.filter(author=user).delete()
        Comment.objects.filter(author=user).delete()

        return Response({"message": "User data deleted successfully."})
