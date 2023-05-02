import time
import allure
from selene import browser
import pytest

login = '/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/input[1]'
password = '/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/input[1]'
fields = 'div.layout-main div.layout-main__container div.layout-main__content div.main-page div.main-page__success div.main-page__content div.grid.grid-cols-1.gap-5 div.grid.grid-cols-4.gap-5 div.col-start-1.col-end-4:nth-child(1) div:nth-child(1) table.kit-table.kit-table--hover tbody:nth-child(2) tr:nth-child(3) > td:nth-child(1)'
button_create_task = 'div.layout-main div.layout-main__container div.layout-main__content div.main-page div.main-page__success div.main-page__content div:nth-child(1) div.grid.grid-cols-4.gap-5.mb-5 div.col-span-1:nth-child(3) a.kit-button.kit-button--lg.kit-button--primary.w-full:nth-child(3) > span.mr-auto'
scout_input = '#app > div > div > div.layout-main__content > div > div > div > div.main-page__content > form > div.grid.grid-cols-2.gap-5 > div:nth-child(2) > div > div:nth-child(3) > div > div.kit-select__box > div.kit-select__field'
search_input = '#app > div > div > div.layout-main__content > div > div > div > div.main-page__content > form > div.grid.grid-cols-2.gap-5 > div:nth-child(2) > div > div:nth-child(3) > div > div.kit-select__box > div.kit-select__drop > div.kit-select__search > div > input[type=text]'
first = '//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/div[1]'
sumbit = 'div.layout-main div.layout-main__container div.layout-main__content div.main-page div.main-page__success div.main-page__content form.grid.grid-cols-1.gap-10 div.kit-bottom-panel.is-show:nth-child(3) div.kit-bottom-panel__fixed div.kit-bottom-panel__container > button.kit-button.kit-button--lg.kit-button--primary.mr-5:nth-child(1)'


@pytest.mark.skip
def test_add_task():
    browser.config.hold_browser_open = True
    browser.config.window_height = 780
    browser.config.window_width = 1220

    with allure.step('Открываем главную страницу "ProfitLand-test"'):
        browser.open('https://profitland-test.agrotek.com/auth/login')

    with allure.step('Вводим логин и пароль'):
        browser.element('[data-test=phoneKitInput]').type('72024561111')
        browser.element('[data-test=passwordKitInput]').type('C369Fdetufm5')
        browser.element('.kit-button').click()

    with allure.step('Вводим название хозяйства "За тридевять земель"'):
        browser.element('.kit-search-input__field').type('За тридевять земель').press_enter()
        browser.element('.farm-card__header').click()

    with allure.step('Выбираем поле "Поле Маркиза де Карабаса"'):
        browser.element(fields).click()
        browser.element('[data-test=rowField-2136]').click()

    with allure.step('Заполняем обязательные поля'):
        browser.element('.kit-textarea__field').type('Описание для теста').press_enter()

    with allure.step('Выбираем скаута из выпадающего списка'):
        browser.element('[data-test=performer_id-itemKitSelect__Option_0]').click()
        time.sleep(2)
        browser.element(first).click()

    with allure.step('Скроллим страницу'):
        browser.execute_script("window.scrollBy(0, 500)")

    with allure.step('Кликаем по кнопке "Создать задание"'):
        browser.element(sumbit).click()
