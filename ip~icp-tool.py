import tkinter as tk
import requests
from tkinter import messagebox
import random,re
from requests.packages import urllib3
import my_fake_useragent
import re,html
import json
import nmap
import sys
from requests.packages import urllib3
import my_fake_useragent
import re,html
from bs4 import BeautifulSoup

urllib3.disable_warnings()
ua = my_fake_useragent.UserAgent().random()
urllib3.disable_warnings()
ua = my_fake_useragent.UserAgent().random()
headers = {
'Cache-Control': 'max-age=0"',
'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="99"',
'Sec-Ch-Ua-Mobile': '?0"',
'Sec-Ch-Ua-Platform': '"Linux"',
'Upgrade-Insecure-Requests': '1',
'User-Agent':ua,
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9',
'Connection': 'close'
}

def generate_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        # 添加更多的用户代理...
    ]
    return random.choice(user_agents)
headers1 = {
    "User-Agent": generate_random_user_agent(),
}
def check_url_alive():
    ip = entry.get("1.0",tk.END)
    if not ip:
        messagebox.showerror("错误", "请输入IP地址或域名")
        return
    items = ip.split("\n")
    print(items)
    result_text.delete(1.0, tk.END)
    for item in items:
        result = ""
        item=jinghua(item)
        print("!!!!!")
        print(item)
        if not item.strip():
            continue
        try:
            print(item+"$$$$$$")
            if ip_is(item)=="True":
                result=result+"\n"+item+"\n"+get_address_by_ip(item.strip())
                a = get_site_by_ip(item.strip())
                print("%%%%%"+a)
                if a!="False":
                    result = result + "\n主域名：" + str(a)
                    print(a + "域名")
                    print(get_right_domain(a))
                    print("#######")
                    result = result + domain_get(get_right_domain(a))
                    print(result)
                    result_text.insert(tk.END, result)  # 将结果插入文本框
                elif a=="False":
                    result=result+"该ip无解析域名"
                    print(result)
                    result_text.insert(tk.END, result)  # 将结果插入文本框
            else:
                print("@@@@@")
                result = result + "\n"+item+domain_get(get_right_domain(item))
                print(result)
                result_text.insert(tk.END, result)  # 将结果插入文本框

        except requests.ConnectionError:
            result = f"URL: {item}\nFailed to connect to the URL\n"
        print("******"+result)



def html_code(text):
    decoded_text = html.unescape(text)
    return decoded_text
def jinghua(ipu):
    a=ipu.replace("https://","").replace("http://","").split(":")[0].split("/")[0].strip()
    return a
#通过IP获取地址
def get_address_by_ip(ip):
    try:
        url = "https://www.ip138.com/iplookup.asp?ip="+str(ip)+"&action=2"
        req = requests.get(url,timeout=3,headers=headers,verify=False)
        req.encoding = "gbk"
        address=re.findall('"ASN归属地":"(.*?)",\s"iP段":',req.text)
        if address != "":
            print("[+]Address:"+address[0])
            return "[+]Address:"+address[0]
    except:
        return "[+]Address:null"
        pass

#get_address_by_ip("114.116.33.180")
#通过IP获取网站域名
def get_site_by_ip(ip):
    try:
        url = "https://site.ip138.com/"+str(ip)+"/"
        req = requests.get(url,timeout=4,headers=headers,verify=False)
        req.encoding = "utf-8"
        site=re.findall('<li><span\sclass="date">[\d\-\s]+</span><a\shref=".*?"\starget="_blank">(.*?)</a></li>',req.text)
        if site != "":
            print("[+]Site:"+site[0])
            return site[0]
    except:
        return "False"
        pass

def ip_is(ip):
    result="False"
    try:
        iplist = ip.split(".")
        if len(iplist) == 4:
            check_count = 0
            for i in iplist:
                if not (int(i) <= 255 and int(i) >= 0):
                    break
                else:
                    check_count += 1
            if check_count == 4: return "True"  # ip
    except Exception as e:
        return "False"

#获取正确域名
def get_right_domain(domain):
    b=domain.split(".")
    if b[-2]=="edu" or b[-2]=="gov":
        return b[-3]+"."+b[-2]+"."+b[-1].strip()
    else:
        return b[-2]+"."+b[-1].strip()

headers_baeanx = {
        'User-Agent':ua,
        'Cookie':'machine_str=undefined; acw_tc=781bad2516854233637791748e0730fd307911a3fb2d3528d83fecc729683f; .AspNetCore.Antiforgery.0QATIYsdRk4=CfDJ8OqkUxc-m6hMpomRyk2QNBAJ1uJcXNJS6ugFE8Uhq8AhrobPMzCQHk8D4nKT4nW7wfyRD6q81-I1QEZNZedWlXnIQUTv-mgYKrlFl3qJsoMH9MD26nIdcibinyQPkh_zT4Vh9mQB7yxakbEe1RS98P4; __51huid__JfwpT3IBSwA9n8PZ=1d7f21e2-d6f0-5799-bcd1-edc903337a29; __vtins__JfvlrnUmvss1wiTZ=%7B%22sid%22%3A%20%22c990eb0b-f462-5960-85ca-77dff7044162%22%2C%20%22vd%22%3A%208%2C%20%22stt%22%3A%20408489%2C%20%22dr%22%3A%2027615%2C%20%22expires%22%3A%201685425573339%2C%20%22ct%22%3A%201685423773339%7D; __51uvsct__JfvlrnUmvss1wiTZ=1; __51vcke__JfvlrnUmvss1wiTZ=42f97426-6b48-5ae6-92db-9eda0df76a70; __51vuft__JfvlrnUmvss1wiTZ=1685423364851; .AspNetCore.Session=CfDJ8OqkUxc%2Bm6hMpomRyk2QNBBocYzpBTiyb5mBPdKG1ytwmRoUkSr8yiC16m9H4v8ml6f%2BgLq%2F5C0ngrvG%2ByGyWgtiOYvxJUJjZDgNbN3zA9R0b4DHzImZ4rW9afQHiflbCXUjikyXkisoRXg76dFpqdJevUrni6119ytt%2BJp4T0wY; machine_str=undefined',
}
proxy={"http":"127.0.0.1:8080","https":"127.0.0.1:8080"}
#通过域名查备案注册人信息
def domain_get(domain):
    try:
        req = requests.get("https://www.beianx.cn/search/"+domain,timeout=4,headers=headers_baeanx,verify=False)
        req.encoding = "utf-8"
        bs=BeautifulSoup(req.text,"html.parser")
        html1=bs.find_all("td",class_="align-middle")
        print("主办单位名称："+html1[1].text.strip())
        print("主办单位性质：" + html1[2].text.strip() )
        print("网站备案 / 许可证号：" + html1[3].text.strip())
        print("网站首页地址：" + html1[5].text.strip())
        print("审核日期：" + html1[6].text.strip())
        return "\n主办单位名称："+html1[1].text.strip()+"\n主办单位性质：" + html1[2].text.strip()+"\n网站备案 / 许可证号：" + html1[3].text.strip()
    except :
        return "\n查不到备案信息"
        pass
#domain_get("www.baidu.com")


# 创建主窗口
window = tk.Tk()
window.title("蓝队批量溯源工具箱")

# URL输入框
url_label = tk.Label(window, text="资产列表:")
url_label.pack()
# 添加URL输入框
entry = tk.Text(window,height=10, width=50)
entry.insert(tk.END, "101.37.43.148\nwww.baidu.com\nhttps://www.zju.edu.cn/\nwww.hangzhou.gov.cn\nwww.zhen-xiaoqingxin.cn\nhttps://hunter.qianxin.com/list?search=domain%3D%22yjlogin.msa.zju.edu.cn%22")
entry.pack()

# 检测按钮
check_button = tk.Button(window, text="检测", command=check_url_alive)
check_button.pack()

# 结果文本框
result_text = tk.Text(window, height=30, width=50)
result_text.pack()

# 运行主循环
window.mainloop()
