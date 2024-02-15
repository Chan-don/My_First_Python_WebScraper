from playwright.sync_api import sync_playwright
import time
#why use time? because, time import is can be delay and prevent the code. So, that allows to view code sequentially.
from bs4 import BeautifulSoup
#bs4 == beautifulSoup4


p = sync_playwright().start()
# The 'p' is the page

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/")

time.sleep(4)
# delay 7 seconds.

page.click("button.Aside_searchButton__Xhqq3")
#click the search button

time.sleep(4)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("DataEngineer")
#find the placeholder, .fill ("Search text") / placeholder is can fill the .fill function

time.sleep(4)

page.keyboard.down("Enter")

time.sleep(10)

page.click("a#search_tab_position")

time.sleep(5)

for i in range(5):
    #do 'i' 5 times. So, under code will be run 5 times.
    time.sleep(5)
    page.keyboard.down("PageDown")
    #End = 1 page down
    #PageDown = 1 Scroll down

content = page.content()
#'print(page.content())' is get html what we see.

# p.stop()
# p is the page. so, this code say stop page. kill the page

soup = BeautifulSoup(content, "html.parser")
#import clean-up html

jobs = soup.find_all("div", class_ = "JobCard_container__FqChn")
# why use class_? Because, python is already get class function. so, we use class_ to avoid duplication.
# Jobs is list

jobs_db = []
#[ ] mean is initializes.
# Why? get data and initializes and get data and initializes and ~~~.

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    # job means each 'div'. Because, the job is soup element.
    # So, we can find("a") can find job.
    # And, ["href"] is composed of <a href = "link">.
    # So, we use ("a") followed by ["href"]
    # If you want other search, we can change ["herf"] -> ["your text"]
    # Ex) link = job.find("a")["data-position-name"] 
    # And this link (<a herf>) is not a perfect link. So, we need to write something and create a perfect link.
    # Why to use single quote?(' '). Because, we must to make link! (" ") this can't make link.

    title = job.find("strong", class_="JobCard_title__ddkwM").text
    # if you want to bring the element to text. you must write the '.text' at the end your code
    
    company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
    
    location = job.find("span", class_="JobCard_location__2EOr5").text
    
    reward = job.find("span", class_="JobCard_reward__sdyHn").text

    job = {
        "title": title,
        "company_name": company_name,
        "location": location,
        "reward" : reward,
        "link": link,
    }
    jobs_db.append(job)

print(jobs_db)
print(len(jobs_db))
# len is get the how many number(jobs)