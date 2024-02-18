from selene import have
from qa_quru_10_10_mid_level_po.model.pages.registration_page import RegistrationPage


def test_fill_form():
    registration_page = RegistrationPage()
    registration_page.open()

    (
        registration_page
        .fill_first_name('Aleksei').fill_last_name('Sturostov')
        .fill_user_email('styrostov94@gmail.com')
        .select_gender_male('male')
        .fill_mobile_number('9241330303')
        .scroll_down('scroll')
        .fill_birdthday('2000', '3', '30')
        .fill_subjects('English')
        .fill_hobbies('Sports', 'Reading', 'Music')
        .fill_upload_picture('cat.jpeg')
        .fill_address('Centralnya QA')
        .select_state('NCR').select_city('Delhi')
        .click_submit('submit')
    )

    registration_page.registrated_user_data('assert_submitting_info').should(
        have.texts(
            'Aleksei Sturostov',
            'styrostov94@gmail.com',
            'Male', '9241330303',
            '30 March,2000',
            'English',
            'Sports, '
            'Reading, '
            'Music',
            'cat.jpeg',
            'Centralnya QA',
            'NCR Delhi'))
