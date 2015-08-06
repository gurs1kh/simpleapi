from django.forms import widgets
from rest_framework import serializers
from myapp.models import Books

class BooksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Books
		fields = ('id', 'title', 'authors', 'pub_date', 'publisher', 'summary', 'price', 'link', 'cover');
