import requests
import urllib3

links = [
        "links example"
        ]


n=0
for i in links:
    n+=1
    try:
        r = requests.get(i, verify=False)
        urllib3.disable_warnings()
        print(n, 'link: ', r.url , r.status_code)
    except:
        print(n, 'error', i)
print(n)
