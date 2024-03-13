from rest_framework import viewsets
from .models import Organization
from users.models import User
from .serializers import UserSerializer, OrganizationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Ensure that the user is set to inactive until they confirm their email if that's a requirement
        serializer.save(is_active=True)

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer