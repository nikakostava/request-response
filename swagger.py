import requests
import urllib3

f = open("links.txt", "r")
#print(f.readline())
#f.close()
w = open('results.txt', 'a')
n=0
#for i in f:
#    n+=1
#    print(n, f.readline())
#f.close()
#n=0
for i in f:
    n+=1
    try:
        r = requests.get(i, verify=False)
        urllib3.disable_warnings()
        print(n, 'link: ', r.url , r.status_code)
        e=(n, 'link: ', r.url , r.status_code)
        w.write(str(e))
    except:
        print(n, 'error', i)

f.close()
w.close()
