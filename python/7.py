import requests
import re
hd = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}

def download(data_1):
    pat_1 = '"positionName":"(.*?)"'#工作
    pat_2 = '"positionNames":"(.*?)"'#职业类别
    pat_3 = '"placeName":"(.*?)"'#所在地区
    pat_4 = '"agentCompanyName":"(.*?)"'#公司名称
    pat_5 = '"detailedAddress":"(.*?)"'#工作地址
    pat_6 = '"salaryRangeNameStart":"(.*?)"'#最低工资
    pat_7 = '"salaryRangeNameEnd":"(.*?)"'#最高工资
    pat_8 = '"degreeDemandNameStart":"(.*?)"'#学历
    pat_9 = '"recruitmentNum":(.*?),'#招聘人数
    pat_10 = '"industryName":"(.*?)"'#行业
    pat_11 = '"reivewTime":"(.*?)"'#发布时间
    pat_12 ='"qrCodePath":"/QCCode/recruitment_(.*?)_'#id
    try:
        for i in range(0,10):
            job = re.compile(pat_1,re.S).findall(data_1)[i]
            job_type = re.compile(pat_2,re.S).findall(data_1)[i]
            area = re.compile(pat_3, re.S).findall(data_1)[i]
            company = re.compile(pat_4, re.S).findall(data_1)[i]
            job_address = re.compile(pat_5, re.S).findall(data_1)[i]
            min_money = re.compile(pat_6, re.S).findall(data_1)[i]
            max_money = re.compile(pat_7, re.S).findall(data_1)[i]
            education = re.compile(pat_8, re.S).findall(data_1)[i]
            person_num = re.compile(pat_9, re.S).findall(data_1)[i]
            profession = re.compile(pat_10, re.S).findall(data_1)[i]
            time = re.compile(pat_11, re.S).findall(data_1)[i]
            id = re.compile(pat_12, re.S).findall(data_1)[i]
            this_url = "http://www.hjiuye.com/page/positionManager/positionInfo?recruitmentInfo.id=" + str (id)
            with open("工作.doc","a+",encoding="utf_8")as f:
                f.write("发布时间：" + time + "\r\n" + "工作："+job + "\r\n" + "职位类别："+job_type + "\r\n" + "所在地区："+area + "\r\n" + "公司名称：" + company + "\r\n" + "工作地址：" + job_address + "\r\n" + "薪资：" + min_money + "~" + max_money + "\r\n" + "学历：" + education + "以上" + "\r\n" + "招聘人数：招聘" + person_num + "人" + "\r\n" + "行业：" + profession + "\r\n" + this_url  + "\r\n" + "------------------------------" + "\r\n")
        #        print(job)
    except :
        pass

def get_data():
    #前十页
    for j in range (1,11):
        url = "http://xiaozhao.hjiuye.com/Site/Position/list?collegeId=1808&keyword=&pageSize=10&pageNumber=" + str(j)
    #    print("第" + str(j) + "页------------------")
        res = requests.get(url,headers =hd)
        data_1 = res.text
        download(data_1)


if __name__ == "__main__" :
    get_data()
