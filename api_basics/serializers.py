from rest_framework import serializers

from api_basics.models import Publication, User
from api_basics.models import Users
from api_basics.models import Shelves

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['ISN', 'title', 'author', 'publisher', 'edition', 'publicationYear', 'edition', 'publicationYear',
                  'description', 'tags']

class UsersSerializer(serializers.ModelSerializer ):
    class Meta:
        model = Users
        fields = ['name', 'surname', 'location', 'emailPrivate', 'emailPublic', 'password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'password']


class ShelvesSerializer(serializers.ModelSerializer ):
    user = UsersSerializer(many = True)

    class Meta:
        model = Shelves
        fields = ['label', 'location', 'users_fk']
