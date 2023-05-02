from selene import browser
import os
import pytest

@pytest.mark.skip
def test_create_farm():


    browser.config.hold_browser_open = True
    browser.config.window_height = 880
    browser.config.window_width = 1520
    # browser.config.click_by_js = True

    browser.open('https://profitland-test.agrotek.com/auth/login')

    browser.element('[data-test=phoneKitInput]').type('72024561111')
    browser.element('[data-test=passwordKitInput]').type('C369Fdetufm5')
    browser.element('.kit-button').click()

    browser.element('[data-test=createFarmKitButton]').click()
    browser.element('[class=kit-input__field]').type('Висячие сады Семирамиды')
    browser.execute_script("window.scrollBy(0, 500)")
    browser.element('[data-test=addFileKitInputFile]').send_keys(os.path.abspath('./resourses/map_fields.kml'))

    # browser.element('[data-test=addFileKitInputFile]').send_keys(os.getcwd() + 'd.arzyancev\profitland_new_task\tests\map_fields.kml')
    browser.execute_script("window.scrollBy(0, 500)")
    # browser.element('[data-test=addFarmButtonBottomPanel]').click()
    # browser.element('[data-test=addFarmButtonTop]').click()
