from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


GECKODRIVER = "/home/michael/geckodriver"
DURCHLAEUFE = 10000


def wait_for_element(webdriver, by: By, query: str, timeout: int = 1000) -> WebElement:
    try:
        return WebDriverWait(webdriver, timeout).until(
            expected_conditions.element_to_be_clickable((by, query)))
    except TimeoutException:
        raise NoSuchElementException


print("Das Skript kann jederzeit durch Ctrl+C gestoppt werden")
try:
    print("Webdriver wird gestartet")
    service = Service(GECKODRIVER)
    options = Options()
    options.headless = True
    driver = Firefox(service=service, options=options)
    print("Webdriver erfolgreich gestartet")
    print("Lade https://www.krone.at/2560444")
    driver.get("https://www.krone.at/2560444")
    for i in range(DURCHLAEUFE):
        print(f"Starte Durchlauf {str(i+1).zfill(len(str(DURCHLAEUFE)))}/{DURCHLAEUFE}")
        wait_for_element(driver, By.XPATH, "(//p[@class='fc-button-label'])[1]").click()
        wait_for_element(driver, By.XPATH, "(//button[@class='btn wp__btn'])[2]").click()
        driver.delete_all_cookies()
        driver.refresh()
except KeyboardInterrupt:
    print("\n\nDas Skript wurde gestoppt")
finally:
    print("\n\nWebdriver wird geschlossen")
    driver.quit()
    print("Fertig")
    print("Danke für deinen Beitrag!")
