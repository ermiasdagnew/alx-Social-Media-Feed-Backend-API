from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    """
    Lists all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
