# import allure
import pytest
import time

# pytest -n 2 -m testing --conf=test/conf/env_setup.yml


class TestPagesLogo(object):
    """
    Test Definition Layer
    """

    # @allure.title("Verify that StackOverflow main page shows correctly")
    @pytest.mark.e2e
    @pytest.mark.emirates_holidays
    def test_main_page_logo(self, main_page, destination, password, github_username, github_password):
        assert main_page.emiratesholidays_logo.is_displayed(), "Emirates Holidays Logo is not shown"

    @pytest.mark.e2e
    @pytest.mark.emirates_holidays
    def test_main_page_cookies(self, main_page, destination, password, github_username, github_password):
        assert main_page.cookies.is_displayed(), "Cookies is not shown"
        main_page.accept_cookies()

    @pytest.mark.e2e
    @pytest.mark.destination
    def test_main_page_destination(self, main_page, destination, password, github_username, github_password):
        main_page.enter_destination(destination)
        time.sleep(1)

    @pytest.mark.e2e
    @pytest.mark.date
    def test_main_page_date(self, main_page, destination, password, github_username, github_password):
        main_page.enter_date_from()
        time.sleep(1)

    @pytest.mark.e2e
    @pytest.mark.airport
    def test_main_page_departure_airport(self, main_page, destination, password, github_username, github_password):
        assert main_page.departure_airport.is_displayed(), "Departure airport field is not shown"
        assert main_page.departure_airport_field.is_displayed(), "Departure airport result field is not shown"
        main_page.enter_departure_airport()
        time.sleep(1)

    @pytest.mark.e2e
    @pytest.mark.test_search_error
    def test_main_page_search_error_message(self, main_page, destination, password, github_username, github_password):
        assert main_page.search_button.is_displayed(), "Search button is not shown"
        main_page.click_search()
        time.sleep(1)

    @pytest.mark.e2e
    @pytest.mark.occupancy
    def test_main_page_enter_occupancy(self, main_page, destination, password, github_username, github_password):
        main_page.enter_occupancy()
        time.sleep(1)

    @pytest.mark.e2e
    @pytest.mark.do_search
    def test_main_page_do_search(self, main_page, destination, password, github_username, github_password):
        main_page \
            .accept_cookies() \
            .enter_departure_airport() \
            .enter_destination(destination) \
            .enter_date_from() \
            .enter_occupancy() \
            .click_search()

    @pytest.mark.e2e
    @pytest.mark.go_to_search_result_page
    def test_search_result_page(self, main_page, destination, password, github_username, github_password):
        main_page.go_to_search_result_page()
        time.sleep(5)

    @pytest.mark.e2e
    @pytest.mark.booking_flow
    def test_booking_flow(self, main_page, destination, password, github_username, github_password):
        search_result_page = main_page.go_to_search_result_page()
        hotel_page = search_result_page.go_to_hotel_page()
        options_page = hotel_page.go_to_option_page()
        booking_page = options_page.go_to_booking_page()
        booking_page.book_holiday()
        time.sleep(20)

    @pytest.mark.e2e
    @pytest.mark.live_booking_flow
    def test_live_booking_flow(self, main_page, destination, password, github_username, github_password):
        search_result_page = main_page.go_to_search_result_page()
        hotel_page = search_result_page.go_to_hotel_page()
        options_page = hotel_page.go_to_option_page()
        booking_page = options_page.go_to_booking_page()
        time.sleep(20)

    @pytest.mark.e2e
    @pytest.mark.testing
    @pytest.mark.parametrize("country, lang", (
            # ('Kuwait', 'English'),
            # ('Germany', 'English'),
            # ('Sweden', 'English'),
            # ('Denmark', 'English'),
            ('Ireland', 'English'),
            # ('Oman', 'English'),
            # ('Oman', 'Arabic'),
            ('United Arab Emirates', 'English'),
            # ('Egypt', 'English')
    ))
    def test_testing(self, main_page, destination, password, github_username, github_password, country, lang):
        assert main_page.country_selector.is_displayed(), "Country selector is not shown"
        assert main_page.emiratesholidays_logo.is_displayed(), "emiratesholidays_logo is not shown"
        assert main_page.signup_button.is_displayed(), "signup_button is not shown"
        assert main_page.cookies.is_displayed(), "cookies is not shown"
        home_page = main_page.select_domain(country=country, lang=lang)
        assert home_page.emiratesholidays_logo.is_displayed(), "logo is not shown"
        search_result_page = home_page.go_to_search_result_page()
        hotel_page = search_result_page.go_to_hotel_page()
        options_page = hotel_page.go_to_option_page()
        booking_page = options_page.go_to_booking_page()
        confirmation_page = booking_page.book_holiday()
        confirmation_page.write_id()
        assert confirmation_page.booking_id.is_displayed(), "booking if is not shown"
        time.sleep(2)

    @pytest.mark.e2e
    @pytest.mark.text
    def test_signup_text_element(self, main_page, destination, password, github_username, github_password):
        assert main_page.signup_text_element.is_displayed(), "Signup text element is not shown"
        assert len(main_page.signup_text_element.text) > 100, "Len of Signup text element is less than 100"
        time.sleep(2)