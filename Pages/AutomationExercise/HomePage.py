from playwright.sync_api import sync_playwright, Page, expect


def test_dismiss_cookies_popup():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=["--disable-cookies"])
        page = browser.new_page()
        page.goto("https://automationexercise.com/")
        dismiss_cookies_popup(page)
        browser.close()

def dismiss_cookies_popup(page: Page):
    button_manage_options = page.get_by_role("button", name="Zarządzaj opcjami")
    expect(button_manage_options).to_be_visible()
    button_manage_options.click()

    button_confirm_selected_options = page.get_by_role("button", name="Potwierdź wybrane opcje")
    expect(button_confirm_selected_options).to_be_visible()
    elements =  page.locator("//input[contains(@id, 'fc-preference-slider-purpose')]/..").all()
    for el in elements:
        expect(el).to_be_visible()
        el.click()
    button_confirm_selected_options.click()

