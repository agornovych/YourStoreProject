import pytest


class TestWishlist(object):

    @pytest.mark.e2e
    @pytest.mark.wishlist
    def test_buy_product(self, base_page, login, password):
        """Login"""
        login_page = base_page.go_to_login()
        account_page = login_page.do_login(email=login, password=password)
        home_page = account_page.go_to_home_page()

        """Add product to Wishlist"""
        home_page.add_product_to_wishlist()
        wishlist_page = home_page.go_wishlist()

        """Remove product from Wishlist"""
        wishlist_page.remove_item()
        assert "Success:" in wishlist_page.remove_message.text.split(), "There is no success message"

