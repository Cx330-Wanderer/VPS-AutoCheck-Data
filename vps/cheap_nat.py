import requests
import re

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    'User-Agent': userAgent,
}
def gettoken():
    postUrl = "https://www.cheapnat.com/clientarea.php"
    r = requests.get(postUrl, headers=header)
    temp = r.text
    result = re.findall("(?<=csrfToken = ').*?(?=',)",temp)
    return result[0]
def logintoindex():
    postdata = {"token":gettoken(),"username":'yourusername',"password":'yourpassword'}
    postUrl = "https://www.cheapnat.com/dologin.php"
    r = requests.session()
    response = r.post(postUrl, data=postdata, headers=header)
    temp = response.text
    cookie = r.cookies
    return(cookie)
def checkdata():
    postUrl = "https://www.cheapnat.com/clientarea.php?action=productdetails&id=填入自己的ID"
    r = requests.session()
    response = r.get(postUrl, cookies=logintoindex(), headers=header)
    temp = response.text
    result = re.findall('(?<="pull-right">).*?(?= <i>)', temp)
    print("本月Cheap-Nat流量使用情况："+result[0])
if __name__=='__main__':
    checkdata()

