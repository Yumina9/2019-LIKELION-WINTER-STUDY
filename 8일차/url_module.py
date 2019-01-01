def get_web(url) :
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('웹 페이지 주소?')
content = get_web(url)
print(content)

#실습

import math
print("파이의 값은 {}입니다.".format( math.pi ))

