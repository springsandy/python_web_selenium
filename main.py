from selenium import webdriver

# idol = input("찾고 싶은 아이돌을 입력해주세요!\n")
idol = "비투비"

driver = webdriver.Chrome()
driver.get("http://www.naver.com/")

search = driver.find_element_by_id('query')
search.send_keys(idol)

driver.find_element_by_class_name('btn_submit').click()