import json
import requests
def get(url,p_para):
                try:
                        str1 = url+'?'+p_para
                        # print(str1)
                        res = requests.get(str1)
                        # print(res)
                        json_result = json.loads( res.text)
                        #doc = json.loads(res.read().decode('utf-8'))
                        # print(json_result)
                        return json_result
                except Exception as e:
                        print(res.text)
                        pass
                        raise
def post(url,p_text):
                # print(body)
                res = requests.post(url=url,data=p_text,headers={'Content-Type':'text/xml'})
                json_result = json.loads(res.text)
                #doc = json.loads(res.read().decode('utf-8'))
                return json_result
     
     
if __name__=='__main__':
        post("http://127.0.0.1:8333/","{123}")
