from rest_framework import viewsets, permissions
from .models import MiniProject
from .serializers import MiniProjectSerializer

class MiniProjectViewSet(viewsets.ModelViewSet):
    serializer_class = MiniProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return MiniProject.objects.all()
        return MiniProject.objects.filter(assigned_to=user)
