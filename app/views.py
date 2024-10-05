# Pagination

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from django.contrib.auth import authenticate

from .serializer import PasswordSerializer
from .models import Password
from .forms import LoginForm
from .utils import does_not_exist


class LoggedIn(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Check if token is valid
        """
        return Response({'success': 'Token is valid.'})


class Login(APIView):
    def post(self, request):
        """
        Generates Login token
        """
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # user_json = User(user)
                return Response({
                    "token": AuthToken.objects.create(user)[1],
                    # "user": user_json.data
                })

        return Response({"error": "Invalid credentials or user does not exist"})


class PasswordCRUD(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Query Password
        """
        query = request.GET.get('q')
        page = request.GET.get('p')
        if query:
            entries = Password.search(query)
        else:
            entries = Password.objects.all()

        serialized_entries = [PasswordSerializer(x).data for x in entries][::-1]
        return Response(serialized_entries)

    def post(self, request):
        """
        Create Password
        """
        _serializer = PasswordSerializer(data=request.data)
        if _serializer.is_valid():
            _serializer.save()
            return Response({'success': 'Created Password', 'data': _serializer.data})
        return Response({'error': 'An Error occured with the form'})

    def put(self, request):
        """
        Edit Password
        """
        try:
            _password_object = Password.objects.get(id=request.data.get('id'))
        except:
            return does_not_exist()
        _serializer = PasswordSerializer(_password_object, data=request.data)
        if _serializer.is_valid():
            _serializer.save()
            return Response({'success': 'Updated Password', 'data': _serializer.data})
        return Response({'error': 'Something Happending'})

    def delete(self, request):
        """
        Delete Password
        """
        try:
            _password_object = Password.objects.get(id=request.data.get('id'))
            _password_object.delete()
            _serializer = PasswordSerializer(_password_object)
            return Response({'success': 'Deleted Password', 'data': _serializer.data})
        except:
            return does_not_exist()
