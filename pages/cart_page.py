from playwright.sync_api import expect , Page

class CartPage:
    def __init__(self,page:Page):
        self.page = page
        self.cart_logo=page.locator('#shopping_cart_container')
        self.checkout_btn= page.get_by_role('button',name='Checkout')
        self.continue_shopping_btn=page.get_by_role('button',name='Continue Shopping')
        self.remove_item_btn = page.locator('#remove-sauce-labs-bolt-t-shirt')
        self.first_name = page.get_by_placeholder('First Name')
        self.last_name = page.locator('#last-name')
        self.postal_code = page.locator('#postal-code')
        self.continue_btn = page.get_by_role('button',name='Continue')
        self.cancel_btn = page.get_by_role('button',name='Cancel')
        self.item_name = page.locator('.inventory_item_name')
        self.payment_info = page.locator('[data-test="payment-info-value"]')
        self.shipping_info= page.locator('[data-test="shipping-info-value"]')
        self.total_price = page.locator('.summary_total_label')
        self.finish_button = page.get_by_role('button',name='Finish')
        self.back_home_button = page.get_by_role('button',name='Back Home')
    
    def chekout_item(self):
        expect(self.checkout_btn).to_be_visible()
        self.checkout_btn.click()
        
    def fill_details(self,config):
        self.first_name.fill(config['first name'])
        self.last_name.fill(config['last name'])
        self.postal_code.fill(config['postal code'])
        self.click_continue_btn()
    
    def click_continue_btn(self):
        self.continue_btn.click()
     
    def click_finish_btn(self):
        expect(self.finish_button).to_be_visible()
        self.finish_button.click()
        
    def verify_checkout_complete(self):
        expect(self.back_home_button).to_be_visible()
            
    def check_product_overview(self):
        # itemname=self.item_name.text_content()
        # print(itemname)
        paymentinfo = self.payment_info.text_content()
        print("\n",paymentinfo)
        shippinfo = self.shipping_info.text_content()
        print(shippinfo)
        totalprice=self.total_price.text_content()
        print(totalprice)
        
        
            