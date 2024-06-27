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

from rest_framework import serializers


class PredictionRequestSerializer(serializers.Serializer):
    Product_ID = serializers.CharField(max_length=100)
    Gender = serializers.CharField(max_length=1)
    Age = serializers.CharField(max_length=10)
    Occupation = serializers.CharField(max_length=10)
    City_Category = serializers.CharField(max_length=1)
    Stay_In_Current_City_Years = serializers.CharField(max_length=10)
    Marital_Status = serializers.CharField(max_length=1)
    Product_Category_1 = serializers.CharField(max_length=10)
    Product_Category_2 = serializers.CharField(max_length=10)
    Product_Category_3 = serializers.CharField(max_length=10)
