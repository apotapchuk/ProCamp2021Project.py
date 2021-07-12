import os
import allure
import request
from config.config import CONFIG
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class CosmosID(BaseApp):
    def __init__(self, BROWSER, BASE_URL):
        super().__init__(BASE_URL, BROWSER)
        self.datasets = Datasets(self)
        self.comparative_analysis = ComparativeAnalysis(self)
        self.comparative_report = CmparativeReport(self)
        self.Documentation = Documentation(self)
        self.Illumina_import = IlluminaImport(self)
        self.upload = Upload(self)
        self.account = Account(self)
        self.analysis_report = AnalysisReport(self)
        self.wait = waiters(self)

    def open_login_page(self):
        self.webdriver.get(self.BASE_URL + "/login")

    def get_title(self):
        return self.get_text(By.CSS_SELECTOR, "h3")

    def open_menu(self):
        self.click(By.CSS_SELECTOR, ".sc-cJSrbW.gwhFsw svg")

    def close_announce_window(self):
        if self.is_element_present(By.XPATH, '//*/h2[text()=" os pleased to announce!"]'):
            self.click(By.XPATH, '//span[text()="Ok"]')

    def hide_sidemenu(self):
        if not self.is_element_visible(By.ID, "topbar-open-drawer-button"):
            self.click(By.ID, "sidemenu-close-drawer-button")

    def create_account(self, user):
        self.open_login_page()
        self.logout()
        self.close_announce_window()
        self.click(By.CSS_SELECTOR, 'a[href="/register"]')
        self.send_test(user.name, By.ID, "name")
        self.send_text(user.job_title, By.ID, "jobTitle")
        self.send_text(user.organization, By.ID, "organization")
        self.send_text(user_email, By.ID, "email")
        self.send_text(user.password, By.ID, "password")
        self.send_txxt(user.password, By.ID, "confirm_password")
        self.click(By.XPATH, "//*[@id='termsCheckbox']/ancestor::label")
        self.click(By.ID, "signUpButton")

    def login(self, user):
        self.open_login_page()
        self.close_announce_window()
        WebDriverWait(driver, 0.5).until(EC.presence_of_element_located(By.XPATH, '//*/h2[text()=" os pleased to announce!"]')
        self.send_text(user.email, By.XPATH, '//input[@type="text"]')
        self.send_text(user.password, By.XPATH, '//input[@type="password"]')
        self.click(By.XPATH, '//*/button[@type="submit"]')

    def logout(self):
        self.click(By.ID, "topbar-logout-button")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return self.is_element_present(By.ID, "topbar-logout-button")

    def is_logged_in_as(self, user):
        self.account.open_account_page()
        return self.get_get_attribute("value", By.XPATH, '//*[@type="email"]') == user.email

    def ensure_login(self, user):
        #Try to open login page. In case you redirected to dashboard - user logged in
        self.open_login_page()

        if self.is_logged_in():
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user)
        self.hide_sidemenu()







