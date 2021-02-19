import requests
import re

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    'User-Agent': userAgent,
}
def gettoken():
    postUrl = "https://my.centerhop.com/login"
    r = requests.get(postUrl, headers=header)
    temp = r.text
    result = re.findall("(?<=csrfToken = ').*?(?=',)",temp)
    return result[0]
def logintoindex():
    postdata = {"token":gettoken(),"username":'yourusername',"password":'yourpassword'}
    postUrl = "https://my.centerhop.com/login"
    r = requests.session()
    response = r.post(postUrl, data=postdata, headers=header)
    temp = response.text
    cookie = r.cookies
    return(cookie)
def checkdata():
    postUrl = "https://my.centerhop.com/clientarea.php?action=productdetails&id=填入自己的ID"
    r = requests.session()
    response = r.get(postUrl, cookies=logintoindex(), headers=header)
    temp = response.text
    result = re.findall(r'Bandwidth(.*?)MB</p>',temp,re.S)
    final = re.findall(r'<p>(.*?)MB / Unlimited',str(result),re.S)
    #print("本月Centerhop流量使用情况："+str("%.2f" %(int(final[0])/1024))+"GB"+" "+"/"+" "+"Unlimited")
    return ("本月Centerhop流量使用情况："+str("%.2f" %(int(final[0])/1024))+"GB"+" "+"/"+" "+"Unlimited")
if __name__=='__main__':
    checkdata()
