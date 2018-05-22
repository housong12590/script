import re

exp1 = r'var url_video_recommend = "(.*?)";'
exp2 = r'var url_video_info = "(.*?)";'
exp3 = r"var url_shop_h5 = '(.*?)';"
file = open('test/api.js', 'r', encoding='utf8')
content = file.read()

result1 = re.findall(exp1, content)
result2 = re.findall(exp2, content)
result3 = re.findall(exp3, content)
print(result1)
print(result2)
print(result3)
file.close()
