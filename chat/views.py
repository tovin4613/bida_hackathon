# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from openai import OpenAI
from django.core import serializers
from .api import *
import json
from .models import Message, ChatRoom
chat_data = []
def index(request):

    if request.method == 'POST':

        prompt = request.POST.get('question')

        # completion_executor = CompletionExecutor(
        #     host='https://clovastudio.stream.ntruss.com',
        #     api_key='NTA0MjU2MWZlZTcxNDJiYwbOU8C6YbcVmMu3aJBaodWZoI8dR6vOrKMQ1xbcQovxwfDupOqJtgfub+cLbH+sFqmfgeVe2vDqmLj/3vYD6TE3ZM/NoK5rHkx6YMbQzCgE1qYGq6SzWY/YerMXf/7qaYKyYCR+VbC9JrFTF36TZC8tej/zTdnrVT8edk3FPA6f12g0TAfNvvqxITigglKjoGyepGyBQMbCVlDA7msneC4=',
        #     api_key_primary_val='hqpU6sPqZ9yY5qS1Ig4CV2UuypRg4u9tH02JO7mw',
        #     request_id='e32760fd0a314c2e8ba2c5299e09d9ae'
        # )

        # preset_text = [{"role":"system",
        #                 "content":"주어진 원문장을 순화하시오."},
        #             {"role":"user","content":prompt}]

        # request_data = {
        #     'messages': preset_text,
        #     'topP': 0.8,
        #     'topK': 0,
        #     'maxTokens': 256,
        #     'temperature': 0.5,
        #     'repeatPenalty': 5.0,
        #     'stopBefore': [],
        #     'includeAiFilters': True
        # }
        
        # result = completion_executor.execute(request_data)

        # chat_data.append(result[-2]['message']['content'])
        # context = {
        #     'question': prompt,
        #     'result': chat_data  # 원하는 값을 context에 추가
        # }
        completion_executor = LanguageSublimation(
        host='clovastudio.apigw.ntruss.com',
        api_key='NTA0MjU2MWZlZTcxNDJiY9FyfNOLt0sYZhNCkHNULyQERr8sje6NrFDMGtVr0Zoamx90Q5aeXoGo59AXtx5q2L/szwtD3BhW2WOfAMIwvRH+jLTov2twOL9A5nkT7K8M8WjIXNigUaNyORmqyjBxu6A2oDJZscCko6Q1RouRyu85929+ueId2Lt6haFhdWP/JdVgbB2EdNwETofoW09vK6RW08g/UV50guHrNGRFo0E=',
        api_key_primary_val = 'hqpU6sPqZ9yY5qS1Ig4CV2UuypRg4u9tH02JO7mw',
        request_id='1cf71e28c17a43bbbdf6a6404c14eb7f'
        )

        preset_text = '주어진 원문장을 순화하시오.' + prompt

        request_data = {
            'text': preset_text,
            'start': '\n순화된 문장:',
            'restart': '###\n원문장:',
            'includeTokens': True,
            'topP': 0.8,
            'topK': 0,
            'maxTokens': 100,
            'temperature': 0.3,
            'repeatPenalty': 5.0,
            'stopBefore': ['###', '원문장:', '순화된 문장:', '###'],
            'includeAiFilters': True
        }

        response_text = completion_executor.execute(request_data)
        print(response_text)
        start = '순화된 문장: '
        end = '.\n###\n원문장:'
        messages = response_text.split(start)[1].split(end)[0]

        print('추출:', messages)
        return render(request, 'gpt/index.html', {'messages': messages})
    
    return render(request, 'gpt/index.html')

def chat(request):
    
    return render(request, 'gpt/result.html') 

def chat_view(request, room_name):
    question = None
    if request.method == "POST":
        author = request.user

        prompt = request.POST.get('question')
        chat_data = None
        
        
        if room_name == '언어순화':
            completion_executor = LanguageSublimation(
            host='clovastudio.apigw.ntruss.com',
            api_key='NTA0MjU2MWZlZTcxNDJiY9FyfNOLt0sYZhNCkHNULyQERr8sje6NrFDMGtVr0Zoamx90Q5aeXoGo59AXtx5q2L/szwtD3BhW2WOfAMIwvRH+jLTov2twOL9A5nkT7K8M8WjIXNigUaNyORmqyjBxu6A2oDJZscCko6Q1RouRyu85929+ueId2Lt6haFhdWP/JdVgbB2EdNwETofoW09vK6RW08g/UV50guHrNGRFo0E=',
            api_key_primary_val = 'hqpU6sPqZ9yY5qS1Ig4CV2UuypRg4u9tH02JO7mw',
            request_id='1cf71e28c17a43bbbdf6a6404c14eb7f'
            )

            preset_text = '주어진 원문장을 순화하시오.\n\n원문장: ' + prompt

            request_data = {
                'text': preset_text,
                'start': '\n순화된 문장:',
                'restart': '###\n원문장:',
                'includeTokens': True,
                'topP': 0.8,
                'topK': 0,
                'maxTokens': 100,
                'temperature': 0.3,
                'repeatPenalty': 5.0,
                'stopBefore': ['###', '원문장:', '순화된 문장:', '###'],
                'includeAiFilters': True
            }

            response_text = completion_executor.execute(request_data)
            print(response_text)
            start = '\n순화된 문장:'
            end = '###\n원문장:'
            messages = response_text.split(start)[1].split(end)[0]

            chat_data = messages

        elif room_name == '업무도우미':
            completion_executor = CompletionExecutor(
                host='https://clovastudio.stream.ntruss.com',
                api_key='NTA0MjU2MWZlZTcxNDJiYwbOU8C6YbcVmMu3aJBaodWZoI8dR6vOrKMQ1xbcQovxwfDupOqJtgfub+cLbH+sFqmfgeVe2vDqmLj/3vYD6TE3ZM/NoK5rHkx6YMbQzCgE1qYGq6SzWY/YerMXf/7qaYKyYCR+VbC9JrFTF36TZC8tej/zTdnrVT8edk3FPA6f12g0TAfNvvqxITigglKjoGyepGyBQMbCVlDA7msneC4=',
                api_key_primary_val='hqpU6sPqZ9yY5qS1Ig4CV2UuypRg4u9tH02JO7mw',
                request_id='e32760fd0a314c2e8ba2c5299e09d9ae'
            )

            preset_text = [{"role":"system",
                            "content":"클로바는 업무와 관련한 전문 지식을 일반인이 쉽게 이해할 수 있도록 설명해주는 친절한 AI 어시스턴트입니다."},
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
            chat_data = result[-2]['message']['content']
            question = prompt

        elif room_name == '고객데이터수집':
            completion_executor = CustomerAnalysis(
            host='clovastudio.apigw.ntruss.com',
            api_key='NTA0MjU2MWZlZTcxNDJiY44xlJWDyzKD5/UTTThHxEnJFL7QcShkgo3dTe6ihmuFqgcKFgRFvbY+byIBbK9CEYfsU9YM4wppeVCHtgyq20fPwWSP438qqjnHOjOcZ/vnp+MDe5qT5Fo9eqgNygczXX9oDpVZ6+IhqVBbYEhDyu6138vapqGGlhvPGtmfH36qSZ8MyLbWt6IeHrxf98H4EI823+2RgYsX3AMnxbPDgiY=',
            api_key_primary_val = 'hqpU6sPqZ9yY5qS1Ig4CV2UuypRg4u9tH02JO7mw',
            request_id='3a09e3d6e0c347b180f32d66967890fd'
            )

            preset_text = '진서연은 패션, 화장 등 본인을 꾸미는 것에 관심이 많은 18세 여자 고등학생입니다.\n진서연는 고유의 아이덴티티가 존재하며 다음 정의된 정보를 따릅니다.\n\n###\n진서연의 기본정보\n이름:클로바\n성별:여성\n혈액형:AB형\n별명:대연동 뉴진스\n생일:2005년 3월 2일\n특기:틱톡에 최신 댄스스 밈 영상 찍어서 올리기\n취미:패션, 화장 유튜버 영상 찾아서 보기기\n성격:누구에게나 친절함\n장점:사교성이 밝음\n단점:학업에 소홀함\n버릇:손톱을 물어뜯음\n종교:무교\n\n사용자:' + prompt

            request_data = {
                'text': preset_text,
                'start': '\n진서연:',
                'restart': '\n사용자:',
                'includeTokens': True,
                'topP': 0.8,
                'topK': 0,
                'maxTokens': 100,
                'temperature': 0.5,
                'repeatPenalty': 5.0,
                'stopBefore': ['사용자:', '진서연:'],
                'includeAiFilters': True
            }

            response_text = completion_executor.execute(request_data)
            start = '진서연:'
            end = '사용자:'
            messages = response_text.split(start)[1].split(end)[0]
            chat_data = messages
            question = prompt


        room = ChatRoom.objects.get(name=room_name)

        Message.objects.create(author=author, content=chat_data, room=room)
    
    messages = Message.objects.filter(room__name=room_name)
    context = {
        'messages': messages,
        # 'question': question,
    }
    return render(request, 'gpt/chat.html', context)