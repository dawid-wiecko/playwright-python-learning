from playwright.sync_api import sync_playwright, Page, expect


def test_dismiss_cookies_popup():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=["--disable-cookies"],)
        page = browser.new_page()
        page.goto("https://automationexercise.com/")
        dismiss_cookies_popup(page)

def dismiss_cookies_popup(page: Page):
    button_manage_options = page.get_by_role("button", name="Zarządzaj opcjami")
    is_visible = button_manage_options.is_visible()
    if not is_visible:
        return
    button_manage_options.click()

    button_confirm_selected_options = page.get_by_role("button", name="Potwierdź wybrane opcje")
    expect(button_confirm_selected_options).to_be_visible()
    elements = page.locator("//input[contains(@id, 'fc-preference-slider-purpose')]/..").all()
    for el in elements:
        expect(el).to_be_checked()
        el.click()
        expect(el).not_to_be_checked()
    button_confirm_selected_options.click()
    expect(button_confirm_selected_options).not_to_be_visible()

def test_add_item_to_cart_shows_confirmation_popup():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=["--disable-cookies"],)
        page = browser.new_page()
        page.goto("https://automationexercise.com/")
        dismiss_cookies_popup(page)
        page.get_by_role("link", name="View Product").first.click()
        page.get_by_role("button", name="Add to cart").click()
        expect(page.get_by_text("Your product has been added to cart.")).to_be_visible()
