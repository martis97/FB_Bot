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


password = getpass.getpass \
    ("Enter password for martynas.markevicius97@gmail.com : ")



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

    """ Enters username and password to the respective fields and
        presses 'Log in'

        Exceptions:
            TimeoutException: Will look for the 'Incorrect Credentials'
            error message - if this message is not displayed within 4 seconds,
            it will carry on executing the rest of the script

    """

    email_entry = WebDriverWait(self, timeout) \
        .until(EC.presence_of_element_located((By.ID, "email")))

    email_entry.send_keys("martynas.markevicius97@gmail.com")

    password_entry = WebDriverWait(self, timeout) \
        .until(EC.presence_of_element_located((By.ID, "pass")))

    password_entry.send_keys(password)

    login_btn = WebDriverWait(self, timeout) \
        .until(EC.element_to_be_clickable((By.ID, "loginbutton")))

    login_btn.click()

    try:
        WebDriverWait(self, 4) \
            .until(EC.visibility_of_element_located \
            ((By.CLASS_NAME, "_4rbf")))

        incorrectCredsElement = browser.find_element_by_class_name("_4rbf")

        if incorrectCredsElement.is_displayed():
            print("Incorrect credentials have been entered!")
            browser.quit()

    except TimeoutException:
        pass
    
    

def enter_to_search(self):
    
    """ Looks for a Facebook using a search bar 
        TODO: Parameterise the search values

        Exceptions:
            WebDriverException - will re-enter the search value if the 
            exception is raised  
    """

    try:
        search_bar_element = '//input[@placeholder = "Search"]'

        WebDriverWait(self, timeout) \
            .until(EC.visibility_of_element_located \
            ((By.XPATH, search_bar_element)))

        search_bar = self.find_element_by_xpath(search_bar_element)
        search_bar.send_keys("Dank Memes")

    except WebDriverException: 
         enter_to_search(self)


def press_search(self):

    """ Initiating the search by pressing the 'Search' button """

    search_btn = WebDriverWait(self, timeout) \
        .until(EC.element_to_be_clickable((By.CLASS_NAME, "_585_")))

    search_btn.click()


def select_first_page(self):

    """ Selects the first search result """

    WebDriverWait(self, timeout) \
        .until(EC.element_to_be_clickable \
        ((By.CLASS_NAME, "_52eh")))

    available_pages = self.find_elements_by_class_name("_52eh")
    available_pages[0].click()


def select_second_page(self):

    """ Selects the second search result """

    WebDriverWait(self, timeout) \
        .until(EC.element_to_be_clickable \
        ((By.CLASS_NAME, "_52eh")))

    available_pages = self.find_elements_by_class_name("_52eh")
    available_pages[1].click()


def select_third_page(self):

    """ Selects the third search result """
    
    WebDriverWait(self, timeout) \
        .until(EC.element_to_be_clickable \
        ((By.CLASS_NAME, "_52eh")))

    available_pages = self.find_elements_by_class_name("_52eh")
    available_pages[2].click()


def press_like(self): 

    """ Likes the last 30 posts on the timeline 
        It will first unlike any posts that have been liked already
        TODO: Parameterise the amount of posts it will like

        Exceptions:
            TimeoutException - Will look for liked posts for 3 seconds 
            upon timeout, it will continue running the script
    """

    liked_xpath = '//a[@aria-pressed = "true"]'
    not_liked_xpath = '//a[@aria-pressed = "false"]'
    comment_like = 'fb_ufi_comment_like_link'
    random_wait = random.uniform(1, 1.99)

    try:
        WebDriverWait(self, 3) \
            .until(EC.element_to_be_clickable((By.XPATH, liked_xpath)))

        liked_btns = self.find_elements_by_xpath(liked_xpath)
        
        print("Unliking pages that have been already liked...")
        for like_button in liked_btns:
            if not like_button.get_attribute("data-testid") == comment_like:
                like_button.click()
                time.sleep(random_wait)

    except TimeoutException: 
        print("No liked posts found")

    
    WebDriverWait(self, timeout) \
        .until(EC.element_to_be_clickable((By.XPATH, not_liked_xpath)))

    liked_posts = 0
    not_liked_btns = self.find_elements_by_xpath(not_liked_xpath)

    for like_button in not_liked_btns:
        if not like_button.get_attribute("data-testid") == comment_like:
            like_button.click()
            time.sleep(random_wait)
            liked_posts += 1

        if liked_posts == 30:
            print("30 most recent posts have been liked")
            break


navigate_to_url(browser)
login_process(browser, password)
enter_to_search(browser)
press_search(browser)
select_first_page(browser)
press_like(browser)