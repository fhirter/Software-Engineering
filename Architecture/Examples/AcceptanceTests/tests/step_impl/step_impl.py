from getgauge.python import step, before_scenario, Messages, after_scenario
import re
from playwright.sync_api import sync_playwright, expect

# --------------------------
# Gauge step implementations
# --------------------------

playwright = None
browser = None
page = None

@step("go to <url>")
def go_to_url(url):
    page.goto(url)

@step("<text> should be visible")
def assert_visible(text):
    expect(page).to_have_title(re.compile(text))


# ---------------
# Execution Hooks
# ---------------

@before_scenario()
def before_scenario_hook():
    global browser
    global playwright
    global page
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

@after_scenario()
def after_scenario_hook():
    browser.close()
    playwright.stop()
