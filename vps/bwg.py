import requests
import re

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    'User-Agent': userAgent,
}
def logintoindex():
    postdata = {"login":"your-ip-1","password":"yourpassword"}
    postdata2 = {"login":"your-ip-2","password":"yourpassword"}
    postUrl = "https://kiwivm.64clouds.com/index.php?mode=login"
    r = requests.session()
    r2 = requests.session()
    response = r.post(postUrl, data=postdata, headers=header)
    response2 = r2.post(postUrl, data=postdata2, headers=header)
    temp = response.text
    temp2 =response2.text
    cookie = r.cookies
    cookie2 = r2.cookies
    return(cookie,cookie2)
def checkdata():
    postUrl = "https://kiwivm.64clouds.com/kiwi-main-controls.php"
    cookie = logintoindex()
    r = requests.session()
    r2 = requests.session()
    response = r.get(postUrl, cookies=cookie[0], headers=header)
    response2 = r2.get(postUrl,cookies=cookie[1],headers=header)
    temp = response.text
    temp2 = response2.text
    result = re.findall(r"<font color=\'#a0a0a0\'>(.*?)</font>",temp)
    result2 = re.findall(r"<font color=\'#a0a0a0\'>(.*?)</font>", temp2)
    print("瓦工套餐名重置日期为："+result[3])
    print("本月套餐名流量使用情况："+result[4])
    print("瓦工套餐名重置日期为：" + result2[3])
    print("本月套餐名流量使用情况：" + result2[4])
if __name__=='__main__':
    checkdata()

