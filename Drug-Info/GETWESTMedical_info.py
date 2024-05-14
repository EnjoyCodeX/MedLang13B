<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:8980d4b4421e8c3e329725126edc5bb59a9547793b2a1eb7b32cd10ae0942eeb
size 3815
=======
import requests
from bs4 import BeautifulSoup
import re
import jsonlines

# 获取全部西药
# 逐一爬取
CH_List = ['a','b','c','d','e','f','g','h','j','k','l','m','n','p','q','r','s','t','w','x','y','z']
# CH_Med_Info = []
for chartype in CH_List:
    url = "https://www.yaopinnet.com/huayao1/"+ chartype + "1.htm"
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text,'lxml')
    area = soup.find(attrs={'id':'sms_page'})
    # 获取当前字母检索页数
    pages = int(re.findall('[\d]+(?=</a>[\s]+页)',str(area))[0])
    i = 1
    while(i <= pages):
        url = "https://www.yaopinnet.com/huayao1/"+ chartype + "{}.htm".format(i)
        html = requests.get(url)
        html.encoding = 'utf-8'
        # 获取 左侧 边栏 药物链接
        soup = BeautifulSoup(html.text,'lxml')
        area = soup.find(attrs={'id':'c_list1'})
        med_left = re.findall('[\w]+(?=.htm)',str(area))
        # 获取 右侧 边栏 药物链接
        soup = BeautifulSoup(html.text,'lxml')
        area = soup.find(attrs={'id':'c_list2'})
        med_right = re.findall('[\w]+(?=.htm)',str(area))
        med_list = med_left + med_right
        # 逐条进入页面
        for med in med_list:
            url = "https://www.yaopinnet.com/huayao/" + med + ".htm"
            html = requests.get(url)
            html.encoding = 'utf-8'
            # 收集药物信息 (图片、名称、成分、性状、功能主治)
            soup = BeautifulSoup(html.text,'lxml')
            area = soup.find_all(attrs={'class':'smsli'})
            area = str(area).replace('\s','')
            # 药物名称 
            Med_name = re.search('[\u4e00-\u9fa5\w():]+(?=<)',area)
            if Med_name:
                Med_name = Med_name.group()
            else:
                continue
            print(Med_name," ")

            # 药物成份
            Med_substance = re.search('【成份】(.*?)(?=<)',area)
            if Med_substance:
                Med_substance = Med_substance.group()
            print(Med_substance," ")

            # 药物适应性
            Med_function = re.search('【适应症】(.*?)(?=</li>)',area)
            if Med_function:
                Med_function = Med_function.group()
                Med_function = str(Med_function).replace('<br>','').replace('</br>','').replace('</br>','').replace('<br/>','')
            print(Med_function," ")

            # 药物禁忌（难搞）
            Med_warning = re.search('【禁忌】(.*?)(?=</li>)',area)
            if Med_warning:
                Med_warning = Med_warning.group()
                Med_warning = str(Med_warning).replace('<br>','').replace('</br>','').replace('</br>','').replace('<br/>','')
            print(Med_warning," ")

            # 药物图片信息url （ 可能没有图片信息 ）
            img = soup.find(attrs={'id':'yaopintupian'})
            imgurl = re.search('(https://[\w./]+)',str(img))
            if imgurl:
                imgurl = imgurl.group()
            print(imgurl, " ")
            print(url, "\n")
            # 将数据存入字典中
            med_dict = {
                "详情": url,
                "图片地址":imgurl,
                "药品名称":Med_name,
                "药品成份":Med_substance,
                "药品适应症":Med_function,
                "药品禁忌":Med_warning
            }
            # CH_Med_Info.append(med_dict)
            with jsonlines.open('WEST_MED_INFO.jsonl',mode='a') as writer:
                writer.write(med_dict)
        # 逐步获取每一页的所有药物信息
        i = i + 1

# 存入json
# with open('CH_MED_Info.json','w') as file:
#     json.dump(CH_Med_Info,file,indent=4)
# 可能存在问题，数据量太大，数组无法全部保存
>>>>>>> cdf77237dbde4d726b04054648ecfe983fb177ad
