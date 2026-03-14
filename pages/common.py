from playwright.sync_api import expect, Page


class CommonPage:
    @staticmethod
    def navigate_to_url(page: Page,url) -> None:
        page.goto(url)