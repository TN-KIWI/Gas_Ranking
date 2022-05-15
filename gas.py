from selenium.webdriver.common.by import By
from selenium import webdriver
import time, datetime
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
dic = {}
for i in range(1,48):
    driver.get('https://gogo.gs/ranking/' + str(i))
    stats = driver.find_elements_by_class_name("price")[0].text
    dic.setdefault(driver.title[:-12],int(stats))
    if i % 10 == 0:
        print("約" + str(int(i/10)) + "/5終了")
    time.sleep(1)
        
items_sorted = sorted(dic.items(), key=lambda x:x[1])

driver.quit() 

for i in items_sorted[:5]:
    print(i[0],str(i[1]) + "円")

today = datetime.datetime.fromtimestamp(time.time())
today.strftime('%Y/%m/%d %H:%M:%S')
print(today)