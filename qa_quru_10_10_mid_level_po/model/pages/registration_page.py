from selene import browser, have, command, be, by
from selene.support.shared.jquery_style import s
from qa_quru_10_10_mid_level_po import resources


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).should(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        s('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        s('#lastName').should(be.blank).type(value)
        return self

    def fill_user_email(self, value):
        s('#userEmail').should(be.blank).type(value)
        return self

    def select_gender_male(self, value):
        s('[for=gender-radio-1]').click()
        return self

    def fill_mobile_number(self, value):
        s('#userNumber').type(text='9241330303').should(have.value('9241330303'))
        return self

    def scroll_down(self, value):
        s('#state').perform(command.js.scroll_into_view)
        return self

    def fill_birdthday(self, year, month, day):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__year-select').click().element('option[value="2000"]').click()
        s('.react-datepicker__month-select').click().element('option[value="3"]').click()
        s('.react-datepicker__day--030').click()
        s('.react-datepicker__month-container').should(be.hidden)
        return self

    def fill_subjects(self, value):
        s('#subjectsInput').should(be.blank).type(text='English').press_enter()
        return self

    def fill_hobbies(self, Sports, Reading, Music):
        s('[for="hobbies-checkbox-1"]').click()
        s('[for="hobbies-checkbox-2"]').click()
        s('[for="hobbies-checkbox-3"]').click()
        return self

    def fill_upload_picture(self, value):
        s('#uploadPicture').set_value(resources.path('cat.jpeg'))
        return self

    def fill_address(self, value):
        s('#currentAddress').should(be.blank).type('Centralnya QA')
        return self

    def select_state(self, value):
        s('#state').click().element(by.text('NCR')).click()
        return self

    def select_city(self, value):
        s('#city').click().element(by.text('Delhi')).click()
        return self

    def click_submit(self, value):
        s('#submit').click()
        return self

    def registrated_user_data(self, assert_submitting_info):
        s('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        return s('.table').all('td:nth-child(2)')

