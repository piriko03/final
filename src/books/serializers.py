from rest_framework import serializers
from .models import Author, Genre, Book, BookRequest

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    author_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    genre_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('owner', 'status')

    def create(self, validated_data):
        author_ids = validated_data.pop('author_ids', [])
        genre_ids = validated_data.pop('genre_ids', [])
        book = Book.objects.create(**validated_data)
        book.authors.set(author_ids)
        book.genres.set(genre_ids)
        return book

class BookRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRequest
        fields = '__all__'
        read_only_fields = ('requester', 'status')