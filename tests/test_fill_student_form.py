from selene import browser, have, be, command, by
import os

def scroll_down():
    browser.driver.execute_script('window.scrollTo(0, window.scrollY + window.innerHeight);')

def test_fill_form():
    browser.open('/automation-practice-form')
    image_path = os.path.abspath('cat.jpeg')

    browser.element('#firstName').should(be.blank).type(text='Aleksei')
    browser.element('#lastName').should(be.blank).type('Sturostov')
    browser.element('#userEmail').should(be.blank).type('styrostov94@gmail.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').should(be.blank).type('9241330303')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="2000"]').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="3"]').click()
    browser.element('.react-datepicker__day--030').click()
    browser.element('.react-datepicker__month-container').should(be.hidden)
    browser.element('#subjectsInput').should(be.blank).type(text='English').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').should(be.enabled).send_keys(image_path)
    browser.element('#currentAddress').should(be.blank).type('Centralnya QA')
    scroll_down()
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td:nth-child(2)').should(
        have.texts('Aleksei Sturostov', 'styrostov94@gmail.com', 'Male', '9241330303', '30 March,2000',
                   'English', 'Sports, Reading, Music', 'cat.jpeg', 'Centralnya QA','NCR Delhi'))









