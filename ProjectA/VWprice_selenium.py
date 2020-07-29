# -*- coding: utf-8 -*-
"""
采集大众品牌汽车在网上的报价
数据源：易车网大众品牌汽车 http://car.bitauto.com/xuanchegongju/?l=8&mid=8
"""
import pandas as pd
from selenium import webdriver
import time
from fake_useragent import UserAgent

base_url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8&page={}'
chrome_options = webdriver.ChromeOptions()

def get_page(page):
    """
    :param page: 页码
    :return: 结果的dataframe
    """
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    #替代网页format
    new_url = base_url.format(page)
    chrome_options.add_argument('user-agent=%s'% headers)
    #指定webdriver地址
    chrome_driver="D:\Program Files (x86)\Anaconda3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chrome_driver,options=chrome_options)
    browser.get(new_url)
    #查找元素
    items = browser.find_elements_by_class_name('search-result-list-item')
    print(items[1].text)
    print(items[1].find_element_by_class_name('img').get_attribute('src'))
    name=[]
    min_price=[]
    max_price=[]
    link=[]
    #文本字段分列
    for i in items:
        temp=i.text.split("\n")
        print(temp)
        if len(temp)>3:
            temp_price=str(temp[2]).split('-')
            name.append(temp[1])
            if len(temp_price)==1:
                min_price.append(temp_price[0])
            else:
                min_price.append(temp_price[0]+u'万')
            max_price.append(temp_price[len(temp_price)-1])
            link.append(i.find_element_by_class_name('img').get_attribute('src'))
        else:
            temp_price=str(temp[1]).split('-')
            name.append(temp[0])
            if len(temp_price)==1:
                min_price.append(temp_price[0])
            else:
                min_price.append(temp_price[0]+u'万')
            max_price.append(temp_price[len(temp_price)-1])
            link.append(i.find_element_by_class_name('img').get_attribute('src'))
    #构建输出Dateframe
    result=pd.DataFrame(columns=['name','min_price','max_price','link'])
    result.name=name
    result.min_price=min_price
    result.max_price=max_price
    result.link=link
    return result


if __name__ == '__main__':
    print('开始爬取...')
    start_time = time.time()
    for page_num in range(1,2):
        print('正在爬取第%s页'%page_num)
        if page_num == 1:
            df_init = get_page(page_num)
            # print(df_init)
        else:
            df_new = get_page(page_num)
            df_init = df_init.append(df_new, ignore_index=True)
            # print(df_init)
    df_init.to_csv('./car_price.csv', sep=',', header=True, index=False, encoding='gbk')
    print('爬取完成')
    end_time = time.time()
    cost_time = end_time - start_time
    print("爬取任务完成，共耗时%s分钟！" % str(round(cost_time / 60, 2)))
