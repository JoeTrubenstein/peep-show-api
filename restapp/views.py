from django.contrib.auth.models import User, Group
from restapp.models import Character
from rest_framework import viewsets
from restapp.serializers import UserSerializer, GroupSerializer, CharacterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import render
from django.utils import timezone
from django.views import generic

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

def home_page(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'restapp/index.html', {'data': " "})

