# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from app.models import Blog
import operator 
from django.db.models.query_utils import Q
from app.serializers import BlogListSerializer, BlogSerializer
import itertools 
# Create your views here.


def index(request):
    return render(request, 'index.html')


class PostView(APIView):

    renderer_classes = (JSONRenderer,)
    permission_classes = (AllowAny,)
## params = { action = 'search' or 'get' , by = field name, value = 'value' }
    main_params = ['action', 'by', 'value']

    def get(self, request, *args, **kwargs):
        try:
            action, by, value =  [request.GET.get(x,'') for x in self.main_params]
            if action == 'search':
                by = by.split(',')
                value = value.split(' ')
                comb = list(itertools.product(by,value))
                query = reduce(operator.or_, [Q(**{'%s__icontains':v}) for s,v in comb])
                results = Blog.objects.filter(**query)[:10]
                results = BlogListSerializer(results, many=True)
                return Response({'data': results.data})
            elif action == 'get':
                query = {by:value}
                results = Blog.objects.get(**query)
                results = BlogSerializer(results)
                return Response({'data': results.data})
            elif action == 'recents':
                results = Blog.objects.all()[:10]
                results = BlogListSerializer(results, many=True)
                return Response({'data': results.data})
        except Exception as e:
            return Response({'msg': e.message})