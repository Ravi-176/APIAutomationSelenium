from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_website():
    driver=webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    sign_in_btn1=driver.find_element(By.XPATH,"//span[@id='nav-link-accountList-nav-line-1' and @class='nav-line-1 nav-progressive-content']")
    sign_in_btn1.click()
    id_box=driver.find_element(By.XPATH,"//input[@id='ap_email'and @name='email']")
    id_box.send_keys("somesh065@gmail.com")
    continue_btn=driver.find_element(By.XPATH,"//input[@id='continue' and @class='a-button-input']")
    continue_btn.click()
    password_box=driver.find_element(By.XPATH,"//input[@id='ap_password' and @name='password']")
    password_box.send_keys("Somesh@1995")
    sign_in_btn2=driver.find_element(By.XPATH,"//input[@id='signInSubmit' and @class='a-button-input']")
    sign_in_btn2.click()
    search_box=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox' and @name='field-keywords']")
    search_box.send_keys("smartphones under 15000")
    # < input
    # id = "nav-search-submit-button"
    # type = "submit"
    # class ="nav-input nav-progressive-attribute" value="Go" tabindex="0" >
    search_btn=driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button' and @class='nav-input nav-progressive-attribute']")
    search_btn.click()
    #<span class="a-button-inner"><i class="a-icon a-icon-cart"></i><button class="a-button-text"
    # type="button" id="a-autoid-1-announce">Add to cart</button></span>
    add_to_cart_btn=driver.find_element(By.XPATH,"//button[@class='a-button-text' and @type='button' and text()='Add to cart']")
    add_to_cart_btn.click()
    go_to_cart_btn=driver.find_element(By.XPATH,"//a[@href='/cart?ref_=ewc_gtc' and @class='a-button-text' and normalize-space(text())='Go to Cart']")
    go_to_cart_btn.click()
    #< input
    #name = "proceedToRetailCheckout"
    #data - feature - id = "proceed-to-checkout-action"
    #class ="a-button-input" type="submit" value="Proceed to checkout" aria-labelledby="sc-buy-box-ptc-button-announce" >
    buy_btn=driver.find_element(By.XPATH,"//input[@name='proceedToRetailCheckout' and @data-feature-id='proceed-to-checkout-action' and @class='a-button-input' and @type='submit' and @value='Proceed to checkout']")
    buy_btn.click()
    time.sleep(5)
    driver.quit()