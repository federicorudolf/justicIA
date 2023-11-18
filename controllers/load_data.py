from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_data(url):
  driver = webdriver.Chrome()
  driver.get(url)
  buttons = WebDriverWait(driver, 10).until(
      EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[id^='btnFallo']"))
  )
  links = driver.find_elements(By.CSS_SELECTOR, "a[title='Ver Fallo']")
  sentences = []
  for button, link in zip(buttons, links):
    sentence_id = button.get_attribute('id').replace('btnFallo', '')
    sentence_title = link.text
    sentences.append((sentence_id, sentence_title))
  driver.quit()
  return sentences