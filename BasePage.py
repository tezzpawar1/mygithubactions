from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta


class BasePage:
    chrome_usr_dir = "user-data-dir=C:/Users/spa6a5t.AppData/Local/Google/Chrome/User Data/test1"
    grp_name_css = (By.XPATH, "//div[@role='listitem']/descendant::span[@title='+91 99853 04064']")
    plus_btn = (By.XPATH, "//span[@data-icon='attach-menu-plus']")
    dropdown_item = (By.XPATH, "//li[@data-animate-dropdown-item]")
    toggle_btn = (By.XPATH, "//input[@id='polls-single-option-switch']/following-sibling::div")
    save_btn = (By.XPATH, "//span[@data-icon='send']")
    inputtext = (By.XPATH, "//div[@title='Type a message']")
    selectable_text_template = "(//p[contains(@class,'selectable-text')])['{0}']"

    def __init__(self, driver):
        self.driver = driver;

    def driver_init(self):
        options = webdriver.ChromeOptions()
        options.add_argument(self.chrome_usr_dir)
        self.driver = webdriver.Chrome(options=options)

    def scroll_into_view(self, element):
        js_executor = Base.driver
        js_executor.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center', behavior: 'smooth'});", element)

    def check_day(self):
        today = datetime.now()
        day_of_week = today.weekday()
        return day_of_week != 5 and day_of_week != 6 and not self.compare_date()

    @staticmethod
    def add_summary_and_options(self):
        summary = self.date_formatting()
        arr = [summary, "Home", "Office", "Leave"]
        for i, value in enumerate(arr):
            self.driver.f(By.XPATH, f"(//p[contains(@class,'selectable-text')])[{i + 1}]").send_keys(value)

    @staticmethod
    def add_projwest_summary_poll(self):
        arr = ["Have you filled out your Projwest? If not, please take a moment to do so promptly.", "Yes", "No",
               "Leave"]
        for i, value in enumerate(arr):
            self.driver.find_element(By.XPATH, "(//p[contains(@class,'selectable-text')])[{i + 1}]").send_keys(value)

    @staticmethod
    def date_formatting():
        today = datetime.now()
        return today.strftime("dd-MMMM-yyyy (EEEE)")

    @staticmethod
    def compare_date():
        holiday_list = ["2024-01-01", "2024-01-26", "2024-08-15", "2024-10-02", "2024-10-31"]
        todays_date = datetime.now().strftime("%Y-%m-%d")

        return todays_date in holiday_list

    def wait_for_load_by(self, css):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=2, ignored_exceptions=NoSuchElementException)
        return wait.until(EC.visibility_of_element_located(css))

    @staticmethod
    def is_last_day_of_month():
        current_date = datetime.now().date()
        last_day_of_month = (current_date.replace(day=1) + timedelta(days=32 - current_date.replace(day=1).day)).replace(day=1) - timedelta(days=1)

        return current_date == last_day_of_month

