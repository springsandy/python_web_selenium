from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')

# idol = input("찾고 싶은 아이돌을 입력해주세요!\n")
idol = "비투비"

driver = webdriver.Chrome(chrome_options=options)
driver.get("http://www.naver.com/")

search = driver.find_element_by_id('query')
search.send_keys(idol)

driver.find_element_by_class_name('btn_submit').click()

profile_pictures = driver.find_elements_by_xpath('//div[@class="detail_info"]//a//img')
for profile_picture in profile_pictures:
    print("프로필 사진 : " + profile_picture.get_attribute('src'))
time.sleep(1)

profile_datas = driver.find_elements_by_xpath('//dl[@class="info txt_3"]//div[@class="info_group"]')
for profile_data in profile_datas:
    print(profile_data.find_element_by_tag_name('dt').get_property('textContent') + " : " + profile_data.find_element_by_tag_name('dd').get_property('textContent'))