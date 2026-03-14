from playwright.sync_api import Page,expect
from pages.common import CommonPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_e2e_workflow(page:Page,config):
    commonpage=CommonPage()
    loginpage = LoginPage(page)
    inventorypage=InventoryPage(page)
    cartpage=CartPage(page)
    

    commonpage.navigate_to_url(page, url=config['base_url'])
    loginpage.login_to_saucelab(config['username'], config['password'])
    inventorypage.select_product(config)
    inventorypage.navigate_to_cart()
    cartpage.chekout_item()
    cartpage.fill_details(config)
    cartpage.check_product_overview()
    cartpage.click_finish_btn()
    cartpage.verify_checkout_complete()
    
    