# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from openai import OpenAI
from django.core import serializers
from .api import CompletionExecutor
import json
from .models import Message, ChatRoom
chat_data = []
def index(request):

    if request.method == 'POST':

        prompt = request.POST.get('question')

        completion_executor = CompletionExecutor(
            host='https://clovastudio.stream.ntruss.com',
            api_key='NTA0MjU2MWZlZTcxNDJiYwbOU8C6YbcVmMu3aJBaodWZoI8dR6vOrKMQ1xbcQovxwfDupOqJtgfub+cLbH+sFqmfgeVe2vDqmLj/3vYD6TE3ZM/NoK5rHkx6YMbQzCgE1qYGq6SzWY/YerMXf/7qaYKyYCR+VbC9JrFTF36TZC8tej/zTdnrVT8edk3FPA6f12g0TAfNvvqxITigglKjoGyepGyBQMbCVlDA7msneC4=',
            api_key_primary_val='hqpU6sPqZ9yY5qS1Ig4CV2UuypRg4u9tH02JO7mw',
            request_id='e32760fd0a314c2e8ba2c5299e09d9ae'
        )

        preset_text = [{"role":"system",
                        "content":"너는 상냥한 상담인이야"},
                    {"role":"user","content":prompt}]

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

        chat_data.append(result[-2]['message']['content'])
        context = {
            'question': prompt,
            'result': chat_data  # 원하는 값을 context에 추가
        }
        return render(request, 'gpt/index.html',context)
    return render(request, 'gpt/index.html')

def chat(request):
    
    return render(request, 'gpt/result.html') 

def chat_view(request, room_name):
    if request.method == "POST":
        author = request.user
        message = request.POST.get('message')
        room = ChatRoom.objects.get(name=room_name)

        Message.objects.create(author=author, content=message, room=room)

    messages = Message.objects.filter(room__name=room_name)
    return render(request, 'gpt/chat.html', {'messages': messages})