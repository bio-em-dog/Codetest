# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver


# 定位到关注者列表
def find_strangers():
    list_sel = 'div.List-item'
    elems = driver.find_elements_by_css_selector(list_sel)
    return elems


# 点击"关注"按钮
def add_fren(item):
    try:
        button_sel = 'div.ContentItem-extra > button.Button--blue'
        button = item.find_element_by_css_selector(button_sel)
        button.click()
        # print(button.text)
        print("关注成功！")
    except NoSuchElementException as e:
        print("已经关注过该用户")


# 获取关注者的信息，并进行判断
def judge(item):
    follower_count = 0
    answer_count = 0

    name_sel = 'span.UserLink.UserItem-name > div > div > a'
    name = item.find_element_by_css_selector(name_sel)
    try:
        infos_sel = 'div >div >div.ContentItem-head > div.ContentItem-meta > div > div.ContentItem-status > span'
        infos = item.find_elements_by_css_selector(infos_sel)
        for info in infos:
            if "回答" in info.text:
                answer_count = int(info.text.split(" ")[0])
            if "关注者" in info.text:
                follower_count = int(info.text.split(" ")[0])
    except:
        pass
    print("{}||粉丝数：{}||回答数：{}".format(name.text, follower_count, answer_count))
    if follower_count > 500 and answer_count > 3:
        return True
    else:
        return False


# 查看是否是最后一页，根据有无"下一页"按钮来判断
def get_page():
    next_page_button_sel = '#Profile-following > div:nth-child(2) > div.Pagination > button.Button.PaginationButton.PaginationButton-next.Button--plain'
    try:
        next_page_button = driver.find_element_by_css_selector(next_page_button_sel)
        return True
    except NoSuchElementException as e:
        return False


# 点击"下一页"按钮
def next_page():
    next_page_button_sel = '#Profile-following > div:nth-child(2) > div.Pagination > button.Button.PaginationButton.PaginationButton-next.Button--plain'
    next_page_button = driver.find_element_by_css_selector(next_page_button_sel)
    next_page_button.click()


url = 'https://www.zhihu.com/'
# 需替换成你的知乎url，点击【我的主页】→【关注者】可进入该页面
follower_url = 'https://www.zhihu.com/people/mugglecode/followers'
driver = start_chrome()
driver.get(url)
time.sleep(20) # wait login
driver.get(follower_url)
time.sleep(5) # wait for loading page & users

i = 1
while get_page():
    strangers = find_strangers()
    for s in strangers:
        if judge(s):
            add_fren(s)
            time.sleep(3)
    print('第{}页已经完成'.format(i))
    i += 1
    next_page()
    time.sleep(5)
