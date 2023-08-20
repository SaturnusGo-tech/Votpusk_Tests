from selenium.webdriver.common.by import By


class RoutsLocators:
    ROUTS_SWITCHER = (By.XPATH, '/html/body/div[2]/div/div[4]')
    FROM_WHERE = (By.CSS_SELECTOR, '[class="search__item first_auto"]')
    TO_THERE = (By.XPATH, '/html/body/section[2]/div/div[4]/form/div[2]/input')
    SEARCH_ROUTS_BUTTON = (By.XPATH, '/html/body/section[2]/div/div[4]/form/button')
