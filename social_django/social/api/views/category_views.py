from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from social.models import Category
from social.api.serializers import CategorySerializer


class CategoryAPIView(APIView):
    
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(category_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        category_serializer = CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response({'message': 'Categoría creada correctamente!'}, status=status.HTTP_201_CREATED)
        
        return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):

    def get(self, request, pk):
        category = Category.objects.filter(id=pk).first()
        category_serializer = CategorySerializer(category)
        return Response(category_serializer.data)

    def put(self, request, pk):
        category = Category.objects.filter(id=pk).first()
        category_serializer = CategorySerializer(category, data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = Category.objects.filter(id=pk).first()
        if category:
            category.delete()
            return Response('Categoría eliminada')
        
        return Response({'message': 'No se ha encontrado una categoría con estos datos'}, status=status.HTTP_404_NOT_FOUND)