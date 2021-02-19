import requests
import re

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    'User-Agent': userAgent,
}
def gettoken():
    postUrl = "https://hosting.netfront.net/clientarea.php"
    r = requests.get(postUrl, headers=header)
    temp = r.text
    result = re.findall("(?<=csrfToken = ').*?(?=',)",temp)
    return result[0]
def logintoindex():
    postdata = {"token":gettoken(),"username":'yourusername',"password":'yourpassword'}
    postUrl = "https://hosting.netfront.net/dologin.php"
    r = requests.session()
    response = r.post(postUrl, data=postdata, headers=header)
    temp = response.text
    cookie = r.cookies
    return(cookie)
def checkdata():
    postUrl = "https://hosting.netfront.net/clientarea.php?action=productdetails&id=填入自己的ID"
    r = requests.session()
    response = r.get(postUrl, cookies=logintoindex(), headers=header)
    temp = response.text
    #print(temp)
    result = re.findall(r'pm-resource-description">\n    (.*?) of',temp,re.S)
    #print(result)
    print("本月Netfront流量使用情况："+result[3]+" "+"/"+" "+"1000 GB")
if __name__=='__main__':
    checkdata()
