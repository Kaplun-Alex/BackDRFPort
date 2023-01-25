from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, CategoriesSerializer, DescriptionSerializer, ButtonsSerializer
from .models import Categories, Description
from django.http import HttpResponse
from .utils import request_meta, full_request_meta


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]

class DescriptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ButtonsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Categories.objects.all()
    serializer_class = ButtonsSerializer
    permission_classes = [permissions.IsAuthenticated]

def category(request):
    print(request_meta(request))
    return HttpResponse('Wello pisiun')
