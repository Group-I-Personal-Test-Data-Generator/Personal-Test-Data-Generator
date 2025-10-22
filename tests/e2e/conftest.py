import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:5500/frontend/index.html"

@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        yield page
        browser.close()