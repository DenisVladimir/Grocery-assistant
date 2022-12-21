
from rest_framework import status
from django.shortcuts import get_object_or_404
from requests import Response
from .serializers import SmallRecipeSerializer

from food.models import Recipe


class CustomCreateAndDeleteMixin:
    def custom_create(self, request, id, attribute, model):
        recipe = get_object_or_404(Recipe, pk=id)
        queryset = getattr(recipe, attribute)
        if not queryset.filter(
            user=request.user
        ).exists():
            model.objects.create(
                user=request.user,
                recipe=recipe
            )
            serializer = SmallRecipeSerializer(
                recipe, context={'request': request}
            )
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def custom_destroy(self, request, id, attribute):
        recipe = get_object_or_404(Recipe, pk=id)
        queryset = getattr(recipe, attribute)
        data = (
            queryset.filter(
                user=request.user
            )
        )
        if data.exists():
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
