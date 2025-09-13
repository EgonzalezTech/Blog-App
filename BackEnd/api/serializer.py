from unicodedata import category

from django.contrib.auth.password_validation import  validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from api import models as api_models

# Define a custom serializer that inherits from TokenObtainPairSerializer
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     '''
#     class MyTokenObtainPairSerializer(TokenObtainPairSerializer):: This line creates a new token serializer called MyTokenObtainPairSerializer that is based on an existing one called TokenObtainPairSerializer. Think of it as customizing the way tokens work.
#     @classmethod: This line indicates that the following function is a class method, which means it belongs to the class itself and not to an instance (object) of the class.
#     def get_token(cls, user):: This is a function (or method) that gets called when we want to create a token for a user. The user is the person who's trying to access something on the website.
#     token = super().get_token(user): Here, it's asking for a regular token from the original token serializer (the one it's based on). This regular token is like a key to enter the website.
#     token['full_name'] = user.full_name, token['email'] = user.email, token['username'] = user.username: This code is customizing the token by adding extra information to it. For example, it's putting the user's full name, email, and username into the token. These are like special notes attached to the key.
#     return token: Finally, the customized token is given back to the user. Now, when this token is used, it not only lets the user in but also carries their full name, email, and username as extra information, which the website can use as needed.
#     '''
#     @classmethod
#     # Define a custom method to get the token for a user
#     def get_token(cls, user):
#         # Call the parent class's get_token method
#         token = super().get_token(user)
#
#         # Add custom claims to the token
#         token['full_name'] = user.full_name
#         token['email'] = user.email
#         token['username'] = user.username
#         try:
#             token['vendor_id'] = user.vendor.id
#         except:
#             token['vendor_id'] = 0
#
#         # ...
#
#         # Return the token with custom claims
#         return token

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Autenticar al usuario usando correo y contraseña
        user = authenticate(email=attrs['email'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError('Credenciales inválidas o el usuario no existe.')
        if not user.is_active:
            raise serializers.ValidationError('La cuenta del usuario está desactivada.')
        self.user = user  # Establecer el usuario para get_token
        return super().validate(attrs)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.full_name
        token['email'] = user.email
        token['username'] = user.username
        # Eliminar vendor_id ya que no se usa
        return token

class RegisterSerializer(serializers.ModelSerializer):
    # Define fields for the serializer, including password and password2
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        # Specify the model that this serializer is associated with
        model = api_models.User
        # Define the fields from the model that should be included in the serializer
        fields = ('full_name', 'email', 'password', 'password2')

    def validate(self, attrs):
        # Define a validation method to check if the passwords match
        if attrs['password'] != attrs['password2']:
            # Raise a validation error if the passwords don't match
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        # Return the validated attributes
        return attrs

    def create(self, validated_data):
        # Define a method to create a new user based on validated data
        user = api_models.User.objects.create(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
        )
        email_username, mobile = user.email.split('@')
        user.username = email_username

        # Set the user's password based on the validated data
        user.set_password(validated_data['password'])
        user.save()

        # Return the created user
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.User
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Profile
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    def get_post_count(self, category):
       return category.post_count()
    class Meta:
        model = api_models.Category
        fields = ["id", "title", "image","slug", "post_count"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Comment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CommentSerializer,self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = api_models.Post
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PostSerializer,self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Bookmark
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BookmarkSerializer,self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Notification
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(NotificationSerializer,self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    views = serializers.IntegerField(default=0)
    posts = serializers.IntegerField(default=0)
    likes = serializers.IntegerField(default=0)
    bookmarks = serializers.IntegerField(default=0)

    class Meta:
        model = api_models.User
        fields = ["views", "posts", "likes", "bookmarks"]