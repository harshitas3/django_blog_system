from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Blog
from .serializers import BlogSerializer
import requests

@api_view(['GET'])
def blog_list(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

@api_view(['GET'])
def get_country_info(request, country_name):
    response = requests.get(f'https://restcountries.com/v3.1/name/{country_name}')
    return Response(response.json())
