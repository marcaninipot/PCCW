from playwright.sync_api import Page


class Login:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practicetestautomation.com/practice-test-login/"

    def go_to(self):
        self.page.goto(self.url)

    def userName(self):
        return self.page.locator("#username")

    def password(self):
        return self.page.locator("#password")

    def submit_btn(self):
        return self.page.locator("#submit")

    def Logged_in_successfully_lbl(self):
        return self.page.locator("//h1[text()='Logged In Successfully']")

    def invalid_username_err(self):
        return self.page.locator("//div[text()='Your username is invalid!']")

    def invalid_password_err(self):
        return self.page.locator("//div[text()='Your password is invalid!']")