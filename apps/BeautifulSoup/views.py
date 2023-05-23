# from selenium import webdriver
# from bs4 import BeautifulSoup
#
#
# def selenium():
#     count=1
#     value=True
#     while True:
#         url2=f"https://asaxiy.uz/product/sport-i-otdyh/page={count}?size=96"
#         driver=webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
#         driver.get(url2)
#         page_source = driver.page_source
#         soup = BeautifulSoup(page_source, "html.parser")
#         link_element = soup.select('div.product__item  a')
#         line_list=[]
#         a=''
#         for link in link_element:
#             d=link.get("href").startswith('/product')
#             a=a+'\n_________\n'+d
#
#         print(a)
#         if count==1:
#             break
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     # with open('apps/BeautifulSoup/txt/index.txt', 'w', encoding="utf-8") as file:
#     #     file.write(page_source + '\n')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # BeautifulSoup ga sahifa manbasini tahlil qilish uchun uzatamiz
# # soup = BeautifulSoup(page_source, "html.parser")
# #
# # # BeautifulSoup metodlari yordamida ma'lum elementlarni topish
# # title = soup.find("h1").text
# # links = soup.find_all("a")
# #
# # # Olingan ma'lumotlarni chop qilish
# # print("Sarlavha:", title)
# # print("Havolalar:")
# # for link in links:
# #     print(link.get("href"))
# #
# # # Brauzerni yopish
# # driver.quit()
