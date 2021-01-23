data1 = 'test1'
way1 = 'test01'

dict1 = {}
list = []
i  = data1.split(',')
t = way1.split(',')
for item in range(len(i)):
    dict1[i[item]] = t[item]
print(dict1)

