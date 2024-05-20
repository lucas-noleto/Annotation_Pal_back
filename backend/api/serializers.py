# from rest_framework import serializers
# from .models import *

# class NoteSerializer(serializers.ModelSerializer):
#     entity_name = serializers.ReadOnlyField(source='entity.title')

#     class Meta:
#         model = Note
#         fields = ['title', 'date', 'text', 'entity_name']

# class AnimeSerializer(serializers.ModelSerializer):
#     genres = serializers.ListField(
#         child=serializers.ChoiceField(choices=Animes.GENRE_CHOICES)
#     )

#     class Meta:
#         model = Animes
#         fields = '__all__'

#     def create(self, validated_data):
#         genres = validated_data.pop('genres')
#         validated_data['genres'] = ', '.join(genres)
#         return Animes.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         genres = validated_data.pop('genres', None)
#         if genres is not None:
#             instance.genres = ', '.join(genres)
#         return super().update(instance, validated_data)

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['genres'] = instance.genres.split(', ')  # Converta de volta para uma lista
#         return representation

# class DoramaSerializer(serializers.ModelSerializer):
#     ggenres = serializers.ListField(
#         child=serializers.ChoiceField(choices=Doramas.GENRE_CHOICES)
#     )
#     class Meta:
#         model = Doramas
#         fields = '__all__'

#     def create(self, validated_data):
#         genres = validated_data.pop('genres')
#         validated_data['genres'] = ', '.join(genres)
#         return Doramas.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         genres = validated_data.pop('genres', None)
#         if genres is not None:
#             instance.genres = ', '.join(genres)
#         return super().update(instance, validated_data)

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['genres'] = instance.genres.split(', ')  # Converta de volta para uma lista
#         return representation

# class SerieSerializer(serializers.ModelSerializer):
#     genres = serializers.ListField(child=serializers.CharField(), write_only=True)

#     class Meta:
#         model = Series
#         fields = '__all__'

#     def create(self, validated_data):
#         genres = validated_data.pop('genres')
#         validated_data['genres'] = ', '.join(genres)
#         return Series.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         genres = validated_data.pop('genres', None)
#         if genres is not None:
#             instance.genres = ', '.join(genres)
#         return super().update(instance, validated_data)

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['genres'] = instance.genres.split(', ')  # Converta de volta para uma lista
#         return representation

# class FilmeSerializer(serializers.ModelSerializer):
#     genres = serializers.ListField(child=serializers.CharField(), write_only=True)

#     class Meta:
#         model = Filmes
#         fields = '__all__'

#     def create(self, validated_data):
#         genres = validated_data.pop('genres')
#         validated_data['genres'] = ', '.join(genres)
#         return Filmes.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         genres = validated_data.pop('genres', None)
#         if genres is not None:
#             instance.genres = ', '.join(genres)
#         return super().update(instance, validated_data)

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['genres'] = instance.genres.split(', ')  # Converta de volta para uma lista
#         return representation

# class LivroSerializer(serializers.ModelSerializer):
#    genres = serializers.ListField(child=serializers.CharField(), write_only=True)

#    class Meta:
#         model = Livros
#         fields = '__all__'

#    def create(self, validated_data):
#         genres = validated_data.pop('genres')
#         validated_data['genres'] = ', '.join(genres)
#         return Livros.objects.create(**validated_data)

#    def update(self, instance, validated_data):
#         genres = validated_data.pop('genres', None)
#         if genres is not None:
#             instance.genres = ', '.join(genres)
#         return super().update(instance, validated_data)

#    def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['genres'] = instance.genres.split(', ')  # Converta de volta para uma lista
#         return representation

from rest_framework import serializers
from .models import *

class EntitySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        entity_type = self.Meta.model.__name__.lower()  # Obtém o nome do modelo em minúsculas
        if entity_type in ['anime', 'dorama']:
            self.fields['genres'] = serializers.ChoiceField(choices=getattr(self.Meta.model, 'GENRE_CHOICES', ()))
        else:
            self.fields['genres'] = serializers.ListField(child=serializers.CharField(), write_only=True)

    def create(self, validated_data):
        genres = validated_data.pop('genres')
        if isinstance(genres, list):
            validated_data['genres'] = ', '.join(genres)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        genres = validated_data.pop('genres', None)
        if genres is not None:
            if isinstance(genres, list):
                instance.genres = ', '.join(genres)
            else:
                instance.genres = genres
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['genres'] = instance.genres.split(', ') if instance.genres else []  # Converta de volta para uma lista
        return representation

class NoteSerializer(EntitySerializer):
    entity_name = serializers.ReadOnlyField(source='entity.title')

    class Meta:
        model = Note
        fields = ['title', 'date', 'text', 'entity_name']

class AnimeSerializer(EntitySerializer):
    class Meta:
        model = Animes
        fields = '__all__'

class DoramaSerializer(EntitySerializer):
    class Meta:
        model = Doramas
        fields = '__all__'

class SerieSerializer(EntitySerializer):
    class Meta:
        model = Series
        fields = '__all__'

class FilmeSerializer(EntitySerializer):
    class Meta:
        model = Filmes
        fields = '__all__'

class LivroSerializer(EntitySerializer):
    class Meta:
        model = Livros
        fields = '__all__'
