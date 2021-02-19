import requests
import re

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    'User-Agent': userAgent,
}
def logintoindex():
    postdata = {"user":"yourusername","pwd":"yourpassword"}
    postUrl = "https://iplc.one/"
    r = requests.session()
    response = r.post(postUrl, data=postdata, headers=header)
    temp = response.text
    cookie = r.cookies
    return(cookie)
def checkdata():
    postUrl = "https://iplc.one/ShowFireWallPortControlGetFireWallRuleByUserDetail"
    r = requests.session()
    response = r.post(postUrl, cookies=logintoindex(), headers=header)
    temp = response.text
    result = re.findall(r'"Month_Traffic":(.*?),"LocalIP"',temp)
    count1 = int(result[0])
    count2 = int(result[1])
    return count1,count2
def calcvalue(count1,count2):
    def valuejudge(count):
        if count < (1024**2):
            return str("%.2f" %(count/1024))+"KB"
        elif (1024**2) <= count < (1024**3):
            return str("%.2f" %(count/1024**2))+"MB"
        else:
            return str("%.2f" %(count/1024**3))+"GB"
    print("IPLC-1累计使用：" + valuejudge(count1))
    print("IPLC-2累计使用：" + valuejudge(count2))
def main():
    count = checkdata()
    calcvalue(count[0], count[1])
if __name__ =='__main__':
    main()

