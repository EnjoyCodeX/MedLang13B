<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:cf264faf750aa39b55a5f96e90a219a05c9605c628a256d1a39d37bc7d9f2c54
size 4197
=======
import requests
from bs4 import BeautifulSoup
import re
import jsonlines

# # 发起请求并获取信息
# req = requests.get("https://www.yaopinnet.com/tools/sms.asp")
# print(req.status_code)

# # 获取全部中药
# soup = BeautifulSoup(req.text,'lxml')
# area = soup.find_all(attrs={'id':'huayao_mulu_nav'})
# ChMed_Link_List = area[0].find_all('a')
# length = len(ChMed_Link_List)
# # url = "<a href='/zhongyao1/a1.htm'>A</a>"
# # pattern = re.compile('/[\w]+.[\w]+.[\w]+')
# # print(pattern.search(url).group())

# 获取全部中药
# 逐一爬取
CH_List = ['a','b','c','d','e','f','g','h','j','k','l','m','n','p','q','r','s','t','w','x','y','z']
# 一个数组应该存不了最大上限
CH_Med_Info = []
for chartype in CH_List:
    url = "https://www.yaopinnet.com/zhongyao1/"+ chartype + "1.htm"
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text,'lxml')
    area = soup.find(attrs={'id':'sms_page'})
    # 获取当前字母检索页数
    pages = int(re.findall('[\d]+(?=</a>[\s]+页)',str(area))[0])
    i = 1
    while(i <= pages):
        url = "https://www.yaopinnet.com/zhongyao1/"+ chartype + "{}.htm".format(i)
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
            url = "https://www.yaopinnet.com/zhongyao/" + med + ".htm"
            html = requests.get(url)
            html.encoding = 'utf-8'
            # 收集药物信息 (图片、名称、成分、性状、功能主治)
            soup = BeautifulSoup(html.text,'lxml')
            area = soup.find_all(attrs={'class':'smsli'})
            # 药物名称
            Med_name = re.search('[:\u4e00-\u9fa5（）()]+(?=<br/>)',str(area)).group()
            print(Med_name," ")
            # 其他药物信息
            other = re.findall('[^a-z</>\s="",]+',str(area))
            # print(other)
            Med_substance = ""
            Med_trait = ""
            Med_function = ""
            for i in range(len(other)):
                if "【成份】" in other[i]:
                    Med_substance = other[i]
                elif "【性状】" in other[i]:
                    Med_trait = other[i]
                elif "【功能主治】" in other[i]:
                    Med_function = other[i]
            print(Med_trait," ",Med_function," ", Med_substance)
            # 治疗的疾病类型
            area = soup.find(attrs={"id":"top_nav"})
            project = re.findall('(?!a href)[\u4e00-\u9fa5]+',str(area))
            Med_type = ""
            for name in project:
                if "科" in name:
                    Med_type = name
            print(Med_type," ")
            # 药物图片信息url （ 可能没有图片信息 ）
            img = soup.find(attrs={'id':'yaopintupian'})
            imgurl = re.search('(https://[\w./]+)',str(img))
            if imgurl:
                imgurl = imgurl.group()
            print(imgurl, " ")
            print(url, "\n")
            
            # 将数据存入字典中
            med_dict = {
                "detail": url,
                "imgurl":imgurl,
                "Med_name":Med_name,
                "Med_substance":Med_substance,
                "Med_trait":Med_trait,
                "Med_function":Med_function,
                "Med_Type":Med_type
            }
            CH_Med_Info.append(med_dict)
            with jsonlines.open('CH_MED_INFO.jsonl',mode='a') as writer:
                writer.write(med_dict)
        # 逐步获取每一页的所有药物信息
        i = i + 1

# 存入json
# with open('CH_MED_Info.json','w') as file:
#     json.dump(CH_Med_Info,file,indent=4)
# 可能存在问题，数据量太大，数组无法全部保存
>>>>>>> cdf77237dbde4d726b04054648ecfe983fb177ad
