from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from html_handler import HtmlHandler

options = Options()
options.add_experimental_option("detach", True)


class Scrap:
    driver = webdriver.Chrome(options=options)

    def __init__(self, query_txt):
        self.driver.get("https://www.azlyrics.com/")
        self.lyrics_query = query_txt

    def _find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return element
        except (NoSuchElementException, StaleElementReferenceException):
            print("Element not found or stale. Relocating element...")
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return element

    def _search_lyrics(self) -> str:
        # locates the search field
        locator = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/form/div/div/input")
        self._find_element(locator).send_keys(self.query_txt)
        self._find_element(locator).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        
        locator = (By.XPATH, "/html/body/div[2]/div/div/div[1]/table/tbody/tr[1]/td/a")
        self._find_element(locator).click()
        self.driver.implicitly_wait(10)

        return self.driver.page_source

    def get_deposits(self) -> str:
        html_response = self._search_lyrics()
        print(html_response)
        lyrics = HtmlHandler(html_response).get_lyrics()
        return lyrics
