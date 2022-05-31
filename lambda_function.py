import requests
import json
import os

def send_msg(msg):
    url = os.getenv('web_hook_url')
    print(url)
    #url = "https://oapi.dingtalk.com/robot/send?access_token=71c8f9abb341891b6fc9cbbee5dc946a09ff058f714600c3e646fcb39cb4d4ff"
    headers = {'Content-Type': 'application/json'}
    values = """{
      "msgtype":"text",
      "text":{
        "content": "%s"
      }
      }""" %msg
    
    print(values)
    request = requests.post(url, values,headers=headers)
    return request.text

#if __name__ == "__main__":
def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event))
    instance = event['detail']['instance-id']
    state = event['detail']['state']
    msg = 'AWS Notifition: EC2 instance: ' + instance + ' state changed to ' + state 
    send_msg(msg)