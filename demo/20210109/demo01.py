import requests
import json

sesson = requests.session()
header_info = {'Accept':'application/json, text/plain, */*',
               'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
               'Content-Type':'application/json',
               'Accept-Encoding':'gzip, deflate',
               'cancelToken':'true',
               'Accept-Language':'zh-CN,zh;q=0.9',
               'Host':'180.169.51.178:19081'
               }
params_info = {"account":"jintang","password":"YbjWkqAY5rEFzvztVjoD3g==","companyAccount":""}
response = sesson.post(url= 'http://180.169.51.178:19081/api/sfmdm/v1/auth/login',
           params = params_info

         )

print(response.text)


# print(json.loads(''))