from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/")
time.sleep(1)

page.click("button.Aside_searchButton__Xhqq3")
time.sleep(1)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("DataEngineer")
time.sleep(1)

page.keyboard.down("Enter")
time.sleep(1)

page.click("a#search_tab_position")
time.sleep(1)

# page.keyboard.down("PageDown")
# time.sleep(1)

content = page.content()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_ = "JobCard_container__FqChn")

jobs_db = []

for job in jobs:
    link = job.find("a")["href"]
    jobs_db.append(link)  # 딕셔너리가 아닌 링크를 직접 저장합니다.

for i in range(0, 5):
    time.sleep(3)
    page.goto(f"https://www.wanted.co.kr{jobs_db[i]}")  # 링크를 딕셔너리에서 가져오지 않고 직접 사용합니다.
    time.sleep(3)
    page.goto("https://www.wanted.co.kr/")