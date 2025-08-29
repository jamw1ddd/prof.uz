from rest_framework import generics
from apps.users.models import Resume
from apps.users.serializers import ResumeSerializer


class ResumeCreateView(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ResumeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    lookup_field = "id"