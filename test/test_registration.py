import pytest
from random import randint


class TestRegistration(object):

    email = f'{randint(1, 100000)}@test.com'
    name = 'Mila'
    last_name = 'Yovovich'
    telephone = '321654987'

    @pytest.mark.e2e
    @pytest.mark.user_registration
    def test_1_user_registration(self, base_page, login, password,
                               name=name,
                               last_name=last_name,
                               email=email,
                               telephone=telephone,
                               ):

        """Go to http://localhost page"""
        """Register a new account using fake userdata (My Account -> Register). Not private connection fix"""

        registration_page = base_page.go_to_registration()

        assert registration_page.first_name.is_displayed(), "Name is not shown"
        assert registration_page.last_name.is_displayed(), "Last Name is not shown"
        assert registration_page.email.is_displayed(), "Email is not shown"
        assert registration_page.telephone.is_displayed(), "Phone is not shown"
        assert registration_page.password.is_displayed(), "Password is not shown"
        assert registration_page.confirm_password.is_displayed(), "Confirm password is not shown"
        assert registration_page.privacy_policy.is_displayed(), "privacy policy checkbox is not shown"
        assert registration_page.submit_button.is_displayed(), "Confirm button is not shown"

        registration_page.enter_name(name=name)
        registration_page.enter_last_name(last_name=last_name)
        registration_page.enter_email(email=email)
        registration_page.enter_telephone(telephone=telephone)
        registration_page.enter_password(password=password)
        registration_page.enter_confirm_password(password=password)
        registration_page.tick_privacy_policy()
        account_page = registration_page.click_submit()

        assert account_page.rhs.is_displayed(), "RHS is not shown"

        """Logout from account"""

        account_page.logout()

    @pytest.mark.e2e
    @pytest.mark.user_registration
    def test_2_user_registration_data(self, base_page, login, password,
                                    name=name,
                                    last_name=last_name,
                                    email=email,
                                    telephone=telephone, ):

        """Login to the account and verify registration data"""

        login_page = base_page.go_to_login()
        account_page = login_page.do_login(email=email, password=password)
        edit_account_page = account_page.go_to_edit_account()
        assert edit_account_page.rhs.is_displayed(), "RHS is not shown"
        assert edit_account_page.get_first_name() == name, "First name is wrong"
        assert edit_account_page.get_last_name() == last_name, "Last name is wrong"
        assert edit_account_page.get_email() == email, "Email is wrong"
        assert edit_account_page.get_telephone() == telephone, "Telephone is wrong"
