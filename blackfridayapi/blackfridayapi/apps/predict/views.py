from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class TestView(APIView):

    # 测试接口
    def get(self, request):
        return Response('首页，get方法')

    def post(self, request):

        return Response('首页，post方法')
