import pytest


class TestBuyProduct(object):

    @pytest.mark.e2e
    @pytest.mark.buy_product
    def test_buy_product(self, base_page, login, password):

        """Login as user from TC_1 or register new one"""
        login_page = base_page.go_to_login()
        account_page = login_page.do_login(email=login, password=password)
        home_page = account_page.go_to_home_page()

        """"Add to cart 2 random products from “Featured” suggestion"""
        home_page.add_product_to_basket()

        """Proceed to cart page"""
        cart_page = home_page.go_to_cart()

        """Proceed to checkout page"""
        checkout_page = cart_page.go_to_checkout()

        """Fill required fields and confirm order"""
        checkout_page.new_address()
        checkout_page.enter_name('Name')
        checkout_page.enter_last_name('Last Name')
        checkout_page.enter_address_1('address')
        checkout_page.enter_city('City')
        checkout_page.enter_postcode('90210')
        checkout_page.select_country()
        checkout_page.select_region_state()
        checkout_page.press_billing_continue_button()
        checkout_page.press_shipping_address_button()
        checkout_page.press_shipping_method_button()
        checkout_page.tick_t_and_c_checkbox()
        checkout_page.press_payment_method_button()
        checkout_page.press_confirm_button()
        assert checkout_page.order_placed_message.is_displayed(), f'{checkout_page.order_placed_message.text}'

        """Verify order status is “Pending” (My Account -> Order History)"""
        order_history_page = checkout_page.go_to_order_history()
        assert order_history_page.order_status.text == "Pending", "Order status in not equal to Pending"
