from time import sleep


def test_check_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com")

    search_field = browser.find_element_by_name("q")
    search_field.send_keys("Coders at Work")

    search_button = browser.find_element_by_xpath("//*[@class='navbar-form navbar-right']/input")
    search_button.click()

    book = browser.find_element_by_css_selector(".thumbnail")
    book.click()

    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-add-to-basket").is_displayed()
    # sleep(10)