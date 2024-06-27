# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionRequestSerializer
from blackfridayapi.tools.send_prediction_request import send_prediction_request


# Create your views here.
class TestView(APIView):

    # 测试接口
    def get(self, request):
        return Response('首页，get方法')


# 模型预测
class PredictionAPIView(APIView):
    def post(self, request):
        serializer = PredictionRequestSerializer(data=request.data)
        if serializer.is_valid():
            instance_dict = serializer.validated_data
            print("数据校验成功", instance_dict)

            # 调用你的预测函数，这里可能需要传入其他参数如project, endpoint_id等
            result = send_prediction_request(
                project="746866758104",
                endpoint_id="5133696755900088320",
                instance_dict=instance_dict)

            return Response({"prediction": result}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
