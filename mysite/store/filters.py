from django_filters.rest_framework import FilterSet
from .models import UserProfile, Category, Product, Rating, Review


class UserProfileFilter(FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            'first_name': ['exact'],
        }


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            'category_name': ['exact'],

        }


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt'],
            'date': ['gt', 'lt'],
            'active': ['exact'],
        }
