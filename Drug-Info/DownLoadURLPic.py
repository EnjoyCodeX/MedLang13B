<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:d9934d202fde63afbf087c6e8a920960a61bdbe057cf16f22390979e8e985eb5
size 1628
=======
import requests
import json
import re
# CH_MED
def CH_MED():
    CH_PIC_Name = []
    CH_PIC_URL = []
    with open('CH_MED_INFO.jsonl','r',encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            imgurl = str(data['imgurl'])
            CH_PIC_URL.append(imgurl)
            imgname = re.search('(\w+)(?=(.jpg|.JPG|.gif))',imgurl)
            if imgname:
                imgname = imgname.group()
            CH_PIC_Name.append(imgname)

    for i in range(len(CH_PIC_URL)):
        print(CH_PIC_URL[i])
        if CH_PIC_URL[i] == 'None':
            continue
        print(CH_PIC_Name[i])
        my_ch_url = 'CH_MED_PIC/'+ CH_PIC_Name[i] + ".jpg"
        res = requests.get(CH_PIC_URL[i])
        with open(my_ch_url,'wb') as f:
            f.write(res.content)

def West_MED():
    WEST_PIC_Name = []
    WEST_PIC_URL = []
    with open('WEST_MED_INFO.jsonl','r',encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            imgurl = str(data['图片地址'])
            WEST_PIC_URL.append(imgurl)
            imgname = re.search('(\w+)(?=(.jpg|.JPG|.gif))',imgurl)
            if imgname:
                imgname = imgname.group()
            WEST_PIC_Name.append(imgname)

    for i in range(len(WEST_PIC_URL)):
        print(WEST_PIC_URL[i])
        if WEST_PIC_URL[i] == 'None':
            continue
        print(WEST_PIC_Name[i])
        my_ch_url = 'WEST_MED_PIC/'+ WEST_PIC_Name[i] + ".jpg"
        res = requests.get(WEST_PIC_URL[i])
        with open(my_ch_url,'wb') as f:
            f.write(res.content)

# CH_MED()
West_MED()
>>>>>>> cdf77237dbde4d726b04054648ecfe983fb177ad
