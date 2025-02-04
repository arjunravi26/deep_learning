from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Chrome options so that login persists
options = webdriver.ChromeOptions()
# Replace with a suitable path on your machine
options.add_argument(r"user-data-dir=folder")

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")

time.sleep(20)

# Find and click on the group chat by its title (change 'Your Group Name' accordingly)
chat = driver.find_element(By.XPATH, "//*[@title='Arjun']")
chat.click()

# Allow chat to load
time.sleep(5)

# Scrape all messages (this XPath is just an example and may require adjustment)
# Here we assume messages are in span tags that contain text
messages = driver.find_elements(By.XPATH, "//div[contains(@class, 'copyable-text')]/span")

# Get the text of each message
chat_messages = [msg.text for msg in messages if msg.text.strip() != ""]

print("Retrieved messages:")
for m in chat_messages:
    print(m)

# Close driver when done
driver.quit()
