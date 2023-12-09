# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from openai import OpenAI
from django.core import serializers
import requests
import json

class CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def execute(self, completion_request):
        headers = {
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'text/event-stream'
        }

        with requests.post(self._host + '/testapp/v1/chat-completions/HCX-002',
                           headers=headers, json=completion_request, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    print(line.decode("utf-8"))
                    
def index(request):
    
    completion_executor = CompletionExecutor(
        host='https://clovastudio.stream.ntruss.com',
        api_key='NTA0MjU2MWZlZTcxNDJiYwbOU8C6YbcVmMu3aJBaodWZoI8dR6vOrKMQ1xbcQovxwfDupOqJtgfub+cLbH+sFqmfgeVe2vDqmLj/3vYD6TE3ZM/NoK5rHkx6YMbQzCgE1qYGq6SzWY/YerMXf/7qaYKyYCR+VbC9JrFTF36TZC8tej/zTdnrVT8edk3FPA6f12g0TAfNvvqxITigglKjoGyepGyBQMbCVlDA7msneC4=',
        api_key_primary_val='hqpU6sPqZ9yY5qS1Ig4CV2UuypRg4u9tH02JO7mw',
        request_id='e32760fd0a314c2e8ba2c5299e09d9ae'
    )

    preset_text = [{"role":"system","content":""},{"role":"user","content":""}]

    request_data = {
        'messages': [{"role":"system","content":""},{"role":"user","content":"안녕이라고 답해줘"}],
        'topP': 0.8,
        'topK': 0,
        'maxTokens': 256,
        'temperature': 0.5,
        'repeatPenalty': 5.0,
        'stopBefore': [],
        'includeAiFilters': True
    }

    result = completion_executor.execute(request_data)
    print(result)
    return render(request, 'gpt/index2.html')

def chat(request):
    
    return render(request, 'gpt/result2.html') 