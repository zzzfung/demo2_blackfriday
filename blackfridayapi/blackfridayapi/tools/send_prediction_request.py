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

from typing import Dict
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
import json


def send_prediction_request(project: str, endpoint_id: str, instance_dict: Dict, location: str = "us-central1") -> Dict:
    # AI Platform 服务需要使用区域 API 端点
    client_options = {"api_endpoint": f"{location}-aiplatform.googleapis.com"}
    # 初始化用于创建和发送请求的客户端。该客户端只需创建一次，可重复使用。
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    # 有关实例架构的更多信息，请使用 get_model_sample.py 并查看 instance_schema_uri 中的 yaml 文件
    instance = json_format.ParseDict(instance_dict, Value())  # 将输入数据转换为 Value 对象
    instances = [instance]  # 将单个实例放入列表中
    parameters_dict = {}  # 参数字典，如果不需要传递参数，保持为空
    parameters = json_format.ParseDict(parameters_dict, Value())
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id  # 构造端点路径
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters  # 发送预测请求
    )

    # 获取预测结果
    predictions = response.predictions

    for prediction in predictions:
        print("  预测结果:", dict(prediction))  # 打印每个预测结果
        result = json.dumps(dict(prediction))

    return result
