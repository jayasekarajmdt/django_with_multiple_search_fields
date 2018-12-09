from django.shortcuts import render
from .serializers import freelancerSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import freelancer

# Create your views here.
class searchAPIView(ListAPIView):
  # whatever serializer class
  serializer_class=freelancerSerializer

  def get_queryset(self):
    query_params = self.request.query_params
    id = query_params.get('id', None)
    first_name = query_params.get('first_name', None)
    last_name = query_params.get('last_name', None)
    age=query_params.get('age',None)
    skill=query_params.get('skill',None)

    print( id) 
    print( first_name)
    print( last_name)
    print( skill)

    queryset_list=freelancer.objects.all()
    queryset_list=queryset_list.filter(first_name=first_name)
    print(queryset_list)
    queryset_list=queryset_list.filter(age__gte=age)
    print(queryset_list)
    
    print(queryset_list[1].skills[0])
    return(queryset_list)