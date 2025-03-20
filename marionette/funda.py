import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

gecko_path = r"C:\Users\stout\geckodriver.exe"
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
profile_path = r"C:\Users\stout\AppData\Roaming\Mozilla\Firefox\Profiles\5rbm9efm.gecko"

profile = FirefoxProfile(profile_path)
options = Options()
options.binary_location = firefox_binary_path
options.profile = profile

service = Service(executable_path=gecko_path)
driver = webdriver.Firefox(service=service, options=options)
wait = time.sleep(2)
driver.get("https://www.funda.nl/")
driver.maximize_window()
print(driver.title)

# Example: close the cookie banner
cookie_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[3]/button[3]/span")
wait
cookie_button.click()
wait

try:
    # 1. Find the reCAPTCHA iframe (example using the "title" attribute).
    #    Adjust the selector to match the actual iframe on Funda:
    captcha_iframe = driver.find_element(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")
    
    # 2. Switch context to the iframe
    driver.switch_to.frame(captcha_iframe)

    # 3. Locate the checkbox element inside the iframe
    #    Often, it's something like "div.recaptcha-checkbox-border"
    captcha_checkbox = driver.find_element(By.CSS_SELECTOR, "div.recaptcha-checkbox-border")

    # 4. Click via ActionChains (simulates a real mouse movement + click)
    actions = ActionChains(driver)
    actions.move_to_element(captcha_checkbox).click().perform()

    # 5. Switch back to the main page if needed
    driver.switch_to.default_content()

    print("Attempted to click reCAPTCHA checkbox.")
except Exception as e:
    print("ReCAPTCHA not present or could not be clicked:", e)

try:
    captcha_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div[2]/svgs")
    actions = ActionChains(driver)
    actions.move_to_element(captcha_button).click().perform()
except Exception as e:
    print(f"No google pop-up, {e}")

element = driver.find_element(By.CSS_SELECTOR, "some-selector")
loc = element.location     # returns a dict with {"x": ..., "y": ...}
size = element.size        # returns a dict with {"width": ..., "height": ...}

print(f"Element top-left corner is at X={loc['x']} / Y={loc['y']}")
print(f"Element size is {size['width']} x {size['height']}")




# element = driver.find_element(By.XPATH, "//*[@id='headlessui-combobox-input-v-0-0-0-0']")
# element.send_keys("jouw tekst hier")




# #
# click_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/ul/li[3]/a")
# driver.execute_script("arguments[0].scrollIntoView(true);", click_button)
# time.sleep(1)  # Give the browser a moment to complete scrolling
# click_button.click()


