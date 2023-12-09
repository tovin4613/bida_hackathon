# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from openai import OpenAI
from django.core import serializers
from .api import CompletionExecutor
import json

def index(request):
    
    completion_executor = CompletionExecutor(
        host='https://clovastudio.stream.ntruss.com',
        api_key='NTA0MjU2MWZlZTcxNDJiYwbOU8C6YbcVmMu3aJBaodWZoI8dR6vOrKMQ1xbcQovxwfDupOqJtgfub+cLbH+sFqmfgeVe2vDqmLj/3vYD6TE3ZM/NoK5rHkx6YMbQzCgE1qYGq6SzWY/YerMXf/7qaYKyYCR+VbC9JrFTF36TZC8tej/zTdnrVT8edk3FPA6f12g0TAfNvvqxITigglKjoGyepGyBQMbCVlDA7msneC4=',
        api_key_primary_val='hqpU6sPqZ9yY5qS1Ig4CV2UuypRg4u9tH02JO7mw',
        request_id='e32760fd0a314c2e8ba2c5299e09d9ae'
    )

    preset_text = [{"role":"system",
                    "content":"너는 상냥한 상담인이야"},
                   {"role":"user","content":"머신러닝을 설명해줘"}]

    request_data = {
        'messages': preset_text,
        'topP': 0.8,
        'topK': 0,
        'maxTokens': 256,
        'temperature': 0.5,
        'repeatPenalty': 5.0,
        'stopBefore': [],
        'includeAiFilters': True
    }

    result = completion_executor.execute(request_data)
    print('=' * 50)
    print(result[-2]['message']['content'])
    return render(request, 'gpt/index2.html')

def chat(request):
    
    return render(request, 'gpt/result.html') 