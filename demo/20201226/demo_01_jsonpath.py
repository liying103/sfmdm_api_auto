import json
import jsonpath


# # json.loads()
# list1= '["大佬","真棒","加油"]'
# dict1 = '{"a":1,"b":2,"c":3}'
# print(json.loads(list1))
# #['大佬', '真棒', '加油']
# print(json.loads(dict1))
# #{'a': 1, 'b': 2, 'c': 3}

'''#json.dumps()
list2 = ["大佬","真棒","加油"]
tuple1 = ('1','2','3')
print(json.dumps(list2,ensure_ascii=False))
#["大佬", "真棒", "加油"]
print(json.dumps(tuple1))
#["1", "2", "3"]'''

jsonobj ={
    "state":1,
    "message":"success",
    "content":{
        "data":{
            "allCitySearchLabels":{
                "A":[{"id":105795,"name":"澳门特别行政区"},
                     {"id":671,"name":"安庆"},
                     {"id":601,"name":"鞍山"}
                     ],
                "B":"haha"
                }
            },
"allCitySearchLabels":{
                "A":[{"id":795,"name":"特别行政区"},
                     {"id":71,"name":"庆"},
                     {"id":61,"name":"山"}
                     ],
                "B":"ha"
                }
        }
}
# 模糊匹配当前json数据下所有allCitySearchLabels
a = jsonpath.jsonpath(jsonobj,'$..allCitySearchLabels')
print(a[0])