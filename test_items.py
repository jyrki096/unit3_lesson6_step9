import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button_presence(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "Кнопка не найдена"
