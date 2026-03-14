from playwright.sync_api import Page ,expect

def test_start(page:Page):
    page.goto("https://www.saucedemo.com/")