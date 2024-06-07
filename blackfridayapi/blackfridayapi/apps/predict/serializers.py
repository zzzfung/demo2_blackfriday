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
