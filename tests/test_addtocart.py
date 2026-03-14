from playwright.sync_api import expect , Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.common import CommonPage

def test_add_product_to_cart(page:Page,config):
    loginpage = LoginPage(page)
    inventorypage= InventoryPage(page,config)
    commonpage = CommonPage()
    
    commonpage.navigate_to_url(page,url=config['base_url'])
    loginpage.login_to_saucelab(config['username'], config['password'])
    inventorypage.select_product()
