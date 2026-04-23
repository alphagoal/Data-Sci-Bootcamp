import selenium
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from time import sleep

url='https://www.apple.com/hk/store?afid=p238%7CsLSlMaCri-dc_mtid_18707vxu38484_pcrid_684980984055_pgrid_15185291117_pntwk_g_pchan__pexid__&cid=aos-hk-kwgo-brand--slid---product-'
driver.get(url)

#CSS Selector syntax:
#https://www.w3schools.com/cssref/css_selectors.phpc
# driver.find_element(By.CSS_SELECTOR,'[href="/hk/shop/buy-iphone"]').click()

url = "https://www.apple.com/hk/shop/buy-iphone/iphone-15-pro"
driver.get(url)

#note: value=xxx is actually css selector syntax
size_button = driver.find_element(By.CSS_SELECTOR,'[value="6_7inch"]')
size_button.click()
sleep(0.5)
color_button = driver.find_element(By.CSS_SELECTOR,'[value="bluetitanium"]~label')
color_button.click()
sleep(0.5)
storage_button = driver.find_element(By.CSS_SELECTOR,'[value="1tb"]~label')
storage_button.click()

sleep(0.5)
trade_in_button = driver.find_element(By.CSS_SELECTOR,'[value="noTradeIn"]~label')
trade_in_button.click()
sleep(0.5)
applecare_button=driver.find_element(By.ID,'applecareplus_59_noapplecare')
applecare_button.click()
sleep(0.5)
addtobag_button = driver.find_element(By.CSS_SELECTOR,'[value="add-to-cart"]')
addtobag_button.click()
sleep(0.5)
review_button = driver.find_element(By.CSS_SELECTOR,'[value="proceed"]')
review_button.click()
sleep(0.5)
checkout_button =driver.find_element(By.ID,'shoppingCart.actions.navCheckout')
checkout_button.click()
