import requests
from fake_useragent import UserAgent
from lxml import etree
import pymysql

# 双色球彩票的url
url = 'http://datachart.500.com/ssq/'
# 提取数据
response = requests.get(url, headers={"User-Agent":UserAgent().chrome})
# 通过xpath解析
e = etree.HTML(response.text)
date_times = e.xpath('//tbody[@id="tdata"]/tr/td[1]/text()')
trs = e.xpath('//tbody[@id="tdata"]/tr[not(@class="tdbck")]')

# 连接数据库
client = pymysql.connect(host='localhost',port=3306, user='root', password='123456', charset='utf8', db='ball')
cursor = client.cursor()
# 插入数据的sql
sql = 'insert into t_ball values(0, %s, %s, %s)'
# 查看数据是否存在
select_new_sql = "select * from t_ball where date_time = %s"
date_times.reverse()

#记录有多少条新数据没有被塞进去,比如新的一期来，数据库有原来的数据，要检查有几个新数据，记录个数
index = 0
for date_time in date_times:
    result = cursor.execute(select_new_sql,[date_time])
    # 如果数据不存在会返回1
    if result == 1:
        break;
    index += 1
# print(index)
# 数据从新到旧排序
trs.reverse() # 因为数据是第一个进来，一层一层压上去的，所以新数据在最下面，需要reverse获取新数据
for i in range(index):
    # 提取红球
    red_ball = '-'.join(trs[i].xpath('./td[@class="chartBall01"]/text()'))
    blue_ball = trs[i].xpath('./td[@class="chartBall02"]/text()')[0]
    print("第" + date_times[i] + "红球是：" + red_ball + " 蓝球：" + blue_ball)
    cursor.execute(sql, [date_times[i], red_ball, blue_ball])
    client.commit()

# for date_time, tr in zip(date_times, trs):
#     red_ball = '-'.join(tr.xpath('./td[@class="chartBall01"]/text()'))
#     blue_ball = tr.xpath('./td[@class="chartBall02"]/text()')[0]
#     print("第"+date_time+"红球是： " + red_ball + " 蓝球是 ： " + blue_ball)
#     cursor.execute(sql,[date_time, red_ball, blue_ball])
#     client.commit()
cursor.close()
client.close()