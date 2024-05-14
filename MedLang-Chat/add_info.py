import json
import re
import pymysql

def add_ch_drug():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',passwd='1234',use_unicode=True,charset='utf8',db='MedLang_Chat')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('SET CHARACTER SET utf8;')
    sql = 'insert into chat_chmed(med_name,med_pic,med_ingredience,med_character,med_use,clinic) values(%s,%s,%s,%s,%s,%s)'
    with open('./CH_MED_INFO.jsonl','r',encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            imgurl = data['imgurl']
            if imgurl:
                pattern = r'([^\/]+\.(jpg|JPG|gif|png))$'
                imgurl_match = re.search(pattern,imgurl)
                if(imgurl_match):
                    imgurl = imgurl_match.group(1)
                imgurl = 'static/image/CH_MED_PIC/' + imgurl
            med_name = data['Med_name']
            med_ingredience = data['Med_substance']
            med_character = data['Med_trait']
            med_use = data['Med_function']
            clinic = data['Med_Type']
            print(med_name,imgurl,med_ingredience,med_character,med_use,clinic)
            cursor.execute(sql,[med_name,imgurl,med_ingredience,med_character,med_use,clinic])
            conn.commit()
    cursor.close()
    conn.close()

def add_west_drug():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',passwd='1234',use_unicode=True,charset='utf8',db='MedLang_Chat')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('SET CHARACTER SET utf8;')
    sql = 'insert into chat_westmed(med_name,med_pic,med_ingredience,med_use,med_warn) values(%s,%s,%s,%s,%s)'
    with open('./WEST_MED_INFO.jsonl','r',encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            imgurl = data['图片地址']
            if imgurl:
                pattern = r'([^\/]+\.(jpg|JPG|gif|png))$'
                imgurl_match = re.search(pattern,imgurl)
                if(imgurl_match):
                    imgurl = imgurl_match.group(1)
                imgurl = 'static/image/WEST_MED_PIC/' + imgurl
            med_name = data['药品名称']
            med_ingredience = data['药品成份']
            med_use = data['药品适应症']
            med_warn = data['药品禁忌']
            print(med_name,imgurl,med_ingredience,med_use,med_warn)
            cursor.execute(sql,[med_name,imgurl,med_ingredience,med_use,med_warn])
            conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    add_ch_drug()
    add_west_drug()