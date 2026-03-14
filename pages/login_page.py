from playwright.sync_api import Page ,expect

class LoginPage:    
    def __init__(self, page: Page):
        self.page = page
        self.user_name_input= page.locator("#user-name")
        self.password_input= page.locator("#password")
        self.login_button=page.get_by_role("button",name="Login")
        self.login_error_msg = page.locator(".error-button")

    def enter_username(self,username):
        self.user_name_input.fill(username)
        
    def enter_password(self,password):
        self.password_input.fill(password)   
        
    def click_login_button(self):
        self.login_button.click() 
    
    def verify_login_success(self):
        expect(self.page).to_have_title("Swag Labs") 
      
    def verify_error_message(self):
        self.login_error_msg.wait_for(state='visible')
        errormsg = self.login_error_msg.text_content().lower() or ""
        print(errormsg)
        # assert "Sorry" in errormsg
        
    def login_to_saucelab(self,user,pwd,):
        self.enter_username(user) 
        self.enter_password(pwd)
        self.click_login_button()

    def invalid_login_to_saucelab(self,user,pwd):
        self.enter_username(user) 
        self.enter_password(pwd)
        self.click_login_button()