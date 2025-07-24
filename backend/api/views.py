
from django.forms import model_to_dict
from django.http import JsonResponse
from products.models import Product
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    data={}
    model_data = Product.objects.all().order_by("?").first()
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])        
    return Response(data)







# def api_home(request, *args, **kwargs):
#     data={}
#     model_data = Product.objects.all().order_by("?").first()
    
#     # if model_data:
#     #     data['id'] = model_data.id
#     #     data['title']= model_data.title
#     #     data['content'] = model_data.content
#     #     data['price'] = model_data.price
#     # print(data)
#     #different way to serialize the data
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title'])
    
   
#     return JsonResponse(data)

