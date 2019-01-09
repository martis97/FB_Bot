# Selenium Webdriver
from selenium import webdriver

# Selenium Exceptions
from selenium.common.exceptions import NoSuchElementException,\
    TimeoutException, WebDriverException

# Explicit Wait (To be replaced with WaitFor module)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Misc.
import getpass
import time
import random


class FBBot(object):
    """Facebook bot class defining actions required to log in to Facebook,
    find a page ("Crazy Programmer" by default), and like the first 30 
    (default amount) posts on the timeline.
    """

    def __init__(self):
        """Class initialisation."""
        self.browser = None  
        self.timeout = 60
        self.url = "https://www.facebook.com/"
        self.username = input("Enter username: ")
        self.password = getpass.getpass \
                ("Enter password for %s : " % self.username)

    def create_browser(self, notifications_off=True):  
        """Creates a Webdriver instance of Chrome to drive the automation.
        
        Args:
            notifications_off: (Default: True) Boolean value if browser 
                required with notifications off. FB requires access to 
                notifications when first time accessed.
        Returns:
            browser: Webdriver element used to drive automation.
        TODO: Add more Chrome settings 
        """

        if notifications_off: 
            # Changing settings to disable notifications
            chrome_options = webdriver.ChromeOptions()
            prefs =  \
                {"profile.default_content_setting_values.notifications" : 2}
            chrome_options.add_experimental_option("prefs",prefs)
            self.browser = webdriver.Chrome(chrome_options=chrome_options)

            return self.browser.fullscreen_window()
            
        else:
            self.browser = webdriver.Chrome()
            return self.browser.fullscreen_window()

    def navigate_to_url(self):
        """ Makes the browser window fullscreen and navigates to the web page
        """

        self.browser.get(self.url)

    def login_process(self):
        """Enters username and password to the respective fields and
        presses 'Log in'

        Exceptions:
            TimeoutException: Will look for the 'Incorrect Credentials'
            error message - if this message is not displayed within 4 seconds,
            it will carry on executing the rest of the script 
        """

        email_entry = WebDriverWait(self.browser, self.timeout) \
            .until(EC.presence_of_element_located((By.ID, "email")))   # This will

        email_entry.send_keys(self.username)

        password_entry = WebDriverWait(self.browser, self.timeout) \
            .until(EC.presence_of_element_located((By.ID, "pass")))    # be replaced with

        password_entry.send_keys(self.password)

        login_btn = WebDriverWait(self.browser, self.timeout) \
            .until(EC.element_to_be_clickable((By.ID, "loginbutton"))) # WaitFor module

        login_btn.click()                                              
        try:
            WebDriverWait(self.browser, 4) \
                .until(EC.visibility_of_element_located \
                ((By.CLASS_NAME, "_4rbf")))                            # for cleaner code

            incorrectCredsElement = self.browser.find_element_by_class_name("_4rbf")

            if incorrectCredsElement.is_displayed():
                print("Incorrect credentials have been entered!")
                self.browser.quit()

        except TimeoutException:
            pass

    def enter_to_search(self,search_value):
        """Looks for a Facebook using a search bar.

            Exceptions:
                WebDriverException - will re-enter the search value if the 
                    exception is raised.  
        """

        try:
            search_bar_element = '//input[@placeholder = "Search"]'

            WebDriverWait(self.browser, 4) \
                .until(EC.visibility_of_element_located \
                ((By.XPATH, search_bar_element))) # Again needs WaitFor
        except TimeoutException:
            self.enter_to_search(search_value)
        
        search_bar = self.browser.find_element_by_xpath(search_bar_element)
        search_bar.send_keys(search_value)

    def press_search(self):
        """ Initiating the search by pressing the 'Search' button """

        search_btn = WebDriverWait(self.browser, self.timeout) \
            .until(EC.element_to_be_clickable((By.CLASS_NAME, "_585_"))) # And again

        search_btn.click()

    def select_page_index(self,number):
        """Selects the search result by its position, starting from 1."""

        WebDriverWait(self.browser, self.timeout) \
            .until(EC.element_to_be_clickable \
            ((By.CLASS_NAME, "_52eh"))) # And again lol

        all_pages = self.browser.find_elements_by_class_name("_52eh")
        all_pages[number + 1].click()

    def select_page_name(self,name):
        """Selects the search result, given expected page name."""

        WebDriverWait(self.browser, self.timeout) \
            .until(EC.element_to_be_clickable \
            ((By.CLASS_NAME, "_52eh"))) # And again 

        all_pages = self.browser.find_elements_by_class_name("_52eh")

        for page in all_pages: 
            if page.text == name:
                page.click()
            else:
                continue

    def press_like(self, num_posts): 
        """ Likes the last 30 posts on the timeline 
            It will first unlike any posts that have been liked already

            Exceptions:
                TimeoutException - Will look for liked posts for 3 seconds 
                upon timeout, it will continue running the script
        """

        liked_xpath = '//a[@aria-pressed = "true"]'
        not_liked_xpath = '//a[@aria-pressed = "false"]'
        post_like = 'fb-ufi-likelink'
        random_wait = random.uniform(1, 1.99)

        try:
            WebDriverWait(self.browser, 5) \
                .until(EC.element_to_be_clickable((By.XPATH, liked_xpath)))
            liked_btns = self.browser.find_elements_by_xpath(liked_xpath)

            print("Unliking pages that have been already liked...")
            for like_button in liked_btns:
                if like_button.get_attribute("data-testid") == post_like:
                    like_button.click()
                    time.sleep(random_wait)
                else:
                    continue
        except TimeoutException: 
            print("No liked posts found")

        WebDriverWait(self.browser, self.timeout) \
            .until(EC.element_to_be_clickable((By.XPATH, not_liked_xpath)))

        liked_posts = 0
        not_liked_btns = self.browser.find_elements_by_xpath(not_liked_xpath)
        print("Liking the latest %d posts on the timeline.." % num_posts)
        for like_button in not_liked_btns:
            if like_button.get_attribute("data-testid") == post_like:
                like_button.click()
                time.sleep(random_wait)
                liked_posts += 1
            else:
                continue

            if liked_posts == num_posts:
                print("%d most recent posts have been liked" % num_posts)
                break

def mr_robot():
    """Function call and parameter definition"""

    # Param definitions
    search_value = "Crazy Programmer"
    page_number = 1
    number_likes = 25

    # Class instance
    fb = FBBot()

    # Orchestra
    fb.create_browser()
    fb.navigate_to_url()
    fb.login_process()
    fb.enter_to_search(search_value)
    fb.press_search()
    fb.select_page_index(page_number)
    fb.press_like(number_likes)

mr_robot()