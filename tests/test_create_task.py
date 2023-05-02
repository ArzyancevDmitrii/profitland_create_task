from selene import browser
import allure


def test_new_task():

    browser.config.hold_browser_open = True


browser.config.window_height = 880
browser.config.window_width = 1520

with allure.step('Открываем главную страницу ProfitLand-test'):
    browser.open('https://profitland-test.agrotek.com/auth/login')

with allure.step('Вводим логин и пароль'):

    browser.element('[data-test=phoneKitInput]').type('72024561111')
    browser.element('[data-test=passwordKitInput]').type('C369Fdetufm5')
    browser.element('.kit-button').click()

with allure.step('Вводим название хозяйства "За тридевять земель"'):
    browser.element('.kit-search-input__field').type('За тридевять земель').press_enter()
    browser.element('.farm-card__header').click()

with allure.step('Выбираем поле "Поле Маркиза де Карабаса"'):
    browser.element('[data-test=rowField-2136]').click()
    browser.element('[data-test=createTaskKitButton]').click()

with allure.step('Заполняем обязательные поля'):
    browser.element('[data-test=descriptionKitTextArea]').type('Новое задание для теста')
    browser.element('[data-test=performer_id-KitSelect_field]').click()

with allure.step('Выбираем скаута из выпадающего списка'):
    browser.element('[class=kit-select__options]').element('[data-test=performer_id-itemKitSelect__Option_0]').click()

    # browser.element('[data-test=addPointKitButton]').click()

with allure.step('Скроллим страницу'):
    browser.execute_script("window.scrollBy(0, 500)")
    # browser.element('[class=kit-input__field]').element('[data-test=coordsKitInput]').click()\

with allure.step('Кликаем по кнопке "Создать задание"'):
    browser.element('[data-test=addCreateKitButton]').click()

