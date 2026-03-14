from playwright.sync_api import Page , expect

class InventoryPage:
    def __init__(self,page:Page):
        self.page = page
        self.filter_dropdown = page.locator('.product_sort_container')
        self.inventory_items = page.locator('.inventory_item')
        self.cart_logo=page.locator('#shopping_cart_container')

    def select_product(self,config):
        self.page.wait_for_load_state('domcontentloaded')
        product=self.page.get_by_text(config['product_name'],exact=True)
        product.click()
        expect(self.page).to_have_url(config['inventory_url'])
        
    def navigate_to_cart(self):
        self.cart_logo.click()
        
        
        