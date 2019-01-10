# Selenium Imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExplicitWait(object):
    """This class holds methods of explicit waits for elements and 
    certain conditions.
    
    Attributes:
        browser: Webdriver instance of Chrome used to drive automation.
        timeout: Amount of seconds the WebDriver will wait for a 
            specified condition.
    """

    def __init__(self, browser, timeout):
        """Module Initialisation"""
        self.browser = browser
        self.timeout = timeout

    def class_name_visible(self, element):
        """Waits for an element identified by the class name to be
        visible.

        Args:
            element: The element's class name.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.visibility_of_element_located(
                (By.CLASS_NAME, element)))

        return element

    def class_name_multiple_visible(self, element):
        """Waits for multiple elements identified by the class name to
        be visible.

        Args:
            element: The element's class name.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.visibility_of_all_elements_located(
                (By.CLASS_NAME, element)))

        return element

    def class_name_clickable(self, element):
        """Waits for an element identified by the class name to be
        clickable.

        Args:
            element: The element's class name.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.element_to_be_clickable(
                (By.CLASS_NAME, element)))

        return element

    def class_name_invisible(self, element):
        """Waits for an element identified by the class name to be
        invisible.

        Args:
            element: The element's class name.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.invisibility_of_element_located(
                (By.CLASS_NAME, element)))

        return element

    def any_class_name_multiple_visible(self, element):
        """Waits for any elements identified by the class name to be
        visible.

        Args:
            element: The element's class name.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.visibility_of_any_elements_located(
                (By.CLASS_NAME, element)))

        return element

    def css_selector_visible(self, element):
        """Waits for an element identified by the CSS selector to be 
        visible.

        Args:
            element: The element's CSS selector.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.visibility_of_element_located(
                (By.CSS_SELECTOR, element)))

        return element

    def css_selector_multiple_visible(self, element):
        """Waits for multiple elements identified by the CSS selector 
        to be visible. 

        Args:
            element: The element's CSS selector.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, element)))

        return element

    def css_selector_clickable(self, element):
        """Waits for an element identified by the CSS selector to be
        clickable.

        Args:
            element: The element's CSS selector.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.element_to_be_clickable(
                (By.CSS_SELECTOR, element)))

        return element

    def css_selector_invisible(self, element):
        """Waits for an element identified by CSS selector to be
        invisible.

        Args:
            element: The element's CSS selector.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, element)))

        return element

    def xpath_visible(self, element):
        """Waits for an element identified by the XPath to be visible.

        Args:
            element: The element's XPath.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.visibility_of_element_located(
                (By.XPATH, element)))

        return element

    def xpath_clickable(self, element):
        """Waits for an element identified by the XPath to be 
        clickable.

        Args:
            element: The element's XPath.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.element_to_be_clickable(
                (By.XPATH, element)))

        return element

    def xpath_invisible(self, element):
        """Waits for an element identified by the XPath to be 
        invisible.

        Args:
            element: The element's XPath.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.invisibility_of_element_located(
                (By.XPATH, element)))

        return element

    def link_text_visibile(self, element):
        """Waits for an element identified by the link text to be
        visible. 

        Args:
            element: The element's Link Text.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.visibility_of_element_located(
                (By.LINK_TEXT, element)))

        return element

    def link_text_clickable(self, element):
        """Waits for an element identified by the link text to be
        clickable.

        Args:
            element: The element's Link Text.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.element_to_be_clickable(
                (By.LINK_TEXT, element)))

        return element

    def tag_name_visible(self, element):
        """Waits for an element identified by the tag name to be
        visible. 

        Args:
            element: The element's Tag Name.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.visibility_of_element_located(
                (By.TAG_NAME, element)))

        return element

    def id_visible(self, element):
        """Waits for an element identified by the ID to be visible. 

        Args:
            element: The element's ID.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.visibility_of_element_located(
                (By.ID, element)))

        return element

    def id_clickable(self, element):
        """Waits for an element identified by the ID to be clickable.

        Args:
            element: The element's ID.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.element_to_be_clickable(
                (By.ID, element)))

        return element

    def id_invisible(self, element):
        """Waits for an element identified by the ID to be invisible.

        Args:
            element: The element's ID.
        """

        element = WebDriverWait(self.browser, self.timeout).until \
            (EC.invisibility_of_element_located(
                (By.ID, element)))

        return element

    def number_of_tabs(self, num_tabs):
        """Waits for a specified amount of tabs to be available.
        
        Args:
            num_tabs: The number of tabs the WebDriver should wait to
                be available.
        """

        WebDriverWait(self.browser, self.timeout).until \
            (EC.number_of_windows_to_be((num_tabs)))
        print("%d tabs detected." % num_tabs)
