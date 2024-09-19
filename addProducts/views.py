from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ItemsSerializer #PopularSerializer, sortSerializer
from .models import Newbakes

# @api_view(['GET'])
# def Cakes(request, category):
#         allItemSort = ItemSort.objects.filter(category=category)
#         serializer = sortSerializer(allItemSort, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Cakes(request, category):
    allItemSort = Newbakes.objects.filter(category=category)
    serializer = ItemsSerializer(allItemSort, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Product(request, name):
     description = Newbakes.objects.filter(name = name).first()
     serializer = ItemsSerializer(description)
     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Items(request, cakecategoryIdentifier):
    try:
        allNewbakes = Newbakes.objects.filter(cakecategoryIdentifier=cakecategoryIdentifier)
        serializer = ItemsSerializer(allNewbakes, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Newbakes.DoesNotExist:
        return Response({'error': 'No items found for the given category.'}, status=status.HTTP_404_NOT_FOUND)
