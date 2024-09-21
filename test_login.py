from playwright.sync_api import Page
from login_page import Login


def test_success_login(page: Page):
    login = Login(page)
    login.go_to()
    login.userName().type("student")
    login.password().type("Password123")
    login.submit_btn().click()
    assert page.title() == "Logged In Successfully | Practice Test Automation"
    assert login.Logged_in_successfully_lbl().is_visible()

def test_invalid_username(page: Page):
    login = Login(page)
    login.go_to()
    login.userName().type("incorrectUser")
    login.password().type("Password123")
    login.submit_btn().click()
    assert login.invalid_username_err().is_visible()

def test_invalid_password(page: Page):
    login = Login(page)
    login.go_to()
    login.userName().type("student")
    login.password().type("incorrectPassword")
    login.submit_btn().click()
    assert login.invalid_password_err().is_visible()


