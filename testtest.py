import getpass
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException


timeout = 60
url = "https://www.facebook.com/"


password = getpass.getpass("Enter password for martynas.markevicius97@gmail.com : ")



chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options) 


def navigate_to_url(self):

    """ Makes the browser window fullscreen and navigates to the web page
        TODO: Parameterise the target URL
    """

    browser.fullscreen_window()
    browser.get(url)


def login_process(self, password):

    email_entry = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.ID, "email")))
    email_entry.send_keys("martynas.markevicius97@gmail.com")

    password_entry = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.ID, "pass")))
    password_entry.send_keys(password)

    login_btn = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.ID, "loginbutton")))
    login_btn.click()


def look_for_page(self):
    
    """ Looks for a Facebook using a search bar 
        TODO: Parameterise the search values
    """

    try:
        search_bar_element = '//input[@placeholder = "Search"]'
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, search_bar_element)))
        search_bar = browser.find_element_by_xpath(search_bar_element)
        search_bar.send_keys("Dank Memes")

    except WebDriverException: 
         look_for_page(browser)

    search_btn = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, "_585_")))
    search_btn.click()

    dank_memes_page = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.LINK_TEXT, "Dank Memes")))
    dank_memes_page.click()


def press_like(self): 

    """ Likes the last 30 posts on the timeline 
        It will first unlike any posts that have been liked already
        TODO: Parameterise the amount of posts it will like
    """

    liked_xpath = '//a[@aria-pressed = "true"]'
    not_liked_xpath = '//a[@aria-pressed = "false"]'

    random_wait = random.uniform(1, 1.99)

    try:
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, liked_xpath)))
        liked_btns = browser.find_elements_by_xpath(liked_xpath)
        not_liked_btns = browser.find_elements_by_xpath(not_liked_xpath)
        
        print("Starting unliking loop")
        for like_button in liked_btns:
            print("Checking if like button is not a comment like")
            if not like_button.get_attribute("data-testid") == 'fb_ufi_comment_like_link':
                like_button.click()
                time.sleep(random_wait)

    except TimeoutException: 
        print("No liked posts found")

    
    WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, not_liked_xpath)))

    liked_posts = 0

    for like_button in not_liked_btns:
        like_button.click()
        time.sleep(random_wait)
        liked_posts += 1

        if liked_posts == 30:
            print("30 most recent posts have been liked")
            break


navigate_to_url(browser)
login_process(browser, password)
look_for_page(browser)
press_like(browser)