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
        output = []
        with requests.post(self._host + '/testapp/v1/chat-completions/HCX-002',
                           headers=headers, json=completion_request, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    decoded_line = line.decode("utf-8")
                    if decoded_line.startswith('data:'):
                        json_string = decoded_line[5:]  # 'data:' 이후 부분만 잘라내어 JSON 문자열 추출

                        try:
                            json_line = json.loads(json_string)  # JSON 형식의 문자열을 파이썬 딕셔너리로 변환
                            output.append(json_line)
                        except json.JSONDecodeError:
                            print('This line is not a valid JSON.')
        return output