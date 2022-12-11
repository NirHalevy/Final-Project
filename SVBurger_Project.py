from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from termcolor import colored
from selenium.webdriver.common.alert import Alert


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.get("https://svburger1.co.il/#/HomePage")
    print(colored("Test Start", "green"))
    yield driver
    driver.close()
    print(colored(" Test End", "green"))


def test_sign_up(setup):
    driver = setup
    driver.find_element(By.XPATH, '//button[text()="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys("nir")
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys("halevi")
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys("Nir23641404halevi@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()
    time.sleep(0)


def test_sign_in(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a/button[text()="Sign In"]').click()
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your email"]').send_keys("Nir1404halevi@gmail.com")
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()
    time.sleep(0)


def test_order(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a/button[text()="Sign In"]').click()
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your email"]').send_keys("Nir1404halevi@gmail.com")
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.find_element(By.XPATH, '//H5[text()="Kids Meal"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Reserve "]').click()
    driver.find_element(By.XPATH, '//button[text()="Send"]').click()
    assert driver.find_element(By.XPATH, '//h4[text()="Your order will arrive to your table in ..."]').is_displayed()
    time.sleep(0)


def test_sanity(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a/button[text()="Sign In"]').click()
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your email"]').send_keys("Nir1404halevi@gmail.com")
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.find_element(By.XPATH, '//H5[text()="Kids Meal"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Reserve "]').click()
    driver.find_element(By.XPATH, '//button[text()="Send"]').click()
    assert driver.find_element(By.XPATH, '//h4[text()="Your order will arrive to your table in ..."]').is_displayed()
    time.sleep(0)


list_of_users = [["nir", "halevi", "nir442maxy5xy5xhalevi@gmail.com", "nir442"],["nil", "levi", "nir442maxyx55yxhalevi@walla.com", "nir443"]]


@pytest.mark.parametrize("users",list_of_users)
def test_functionality_sign_up_other_users(setup,users):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.find_element(By.XPATH, '//button[text()="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys(users[0])
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys(users[1])
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys(users[2])
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys(users[3])
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys(users[3])
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()
    time.sleep(0)


@pytest.mark.parametrize("users",list_of_users)
def test_functionality_sign_in_other_users(setup,users):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.find_element(By.XPATH, '//a/button[text()="Sign In"]').click()
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your email"]').send_keys(users[2])
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your password"]').send_keys(users[3])
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()
    time.sleep(0)


def test_functionality_log_out(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a/button[text()="Sign In"]').click()
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your email"]').send_keys("Nir1404halevi@gmail.com")
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Log out "]').click()
    assert driver.find_element(By.XPATH, '//p[text()="Welcome to "]').is_displayed()
    time.sleep(0)


def test_functionality_order_combo_meal(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a/button[text()="Sign In"]').click()
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your email"]').send_keys("Nir1404halevi@gmail.com")
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Reserve "]').click()
    driver.find_element(By.XPATH, '//button[text()="Send"]').click()
    assert driver.find_element(By.XPATH, '//h4[text()="Your order will arrive to your table in ..."]').is_displayed()
    time.sleep(0)


def test_functionality_2_in_quantity_field(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a/button[text()="Sign In"]').click()
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your email"]').send_keys("Nir1404halevi@gmail.com")
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Reserve "]').click()
    driver.find_element(By.XPATH, '//input[@index="0"]').send_keys("2")
    driver.find_element(By.XPATH, '//button[text()="Send"]').click()
    assert driver.find_element(By.XPATH, '//h4[text()="Your order will arrive to your table in ..."]').is_displayed()
    time.sleep(0)


def test_functionality_order_3_meals(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a/button[text()="Sign In"]').click()
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your email"]').send_keys("Nir1404halevi@gmail.com")
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').click()
    driver.find_element(By.XPATH, '//h5[text()="Kids Meal"]').click()
    driver.find_element(By.XPATH, '//h5[text()="Burger"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Reserve "]').click()
    driver.find_element(By.XPATH, '//button[text()="Send"]').click()
    assert driver.find_element(By.XPATH, '//h4[text()="Your order will arrive to your table in ..."]').is_displayed()
    time.sleep(0)


def test_functionality_order_table_number_3(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a/button[text()="Sign In"]').click()
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your email"]').send_keys("Nir1404halevi@gmail.com")
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Reserve "]').click()
    driver.find_element(By.XPATH, '//input[@max="99"]').send_keys("3")
    driver.find_element(By.XPATH, '//button[text()="Send"]').click()
    assert driver.find_element(By.XPATH, '//h4[text()="Your order will arrive to your table in ..."]').is_displayed()
    time.sleep(0)


def test_error_handling_invalid_email_address(setup):
    driver = setup
    driver.find_element(By.XPATH, '//button[text()="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys("nir")
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys("halevi")
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys("Nir442gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    if driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').is_displayed():
        print(colored("invalid email address!", "red"))
    else: print(colored(" Test End", "green"))
    time.sleep(4)


def test_error_handling_wrong_email_address(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a/button[text()="Sign In"]').click()
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your email"]').send_keys("dogoyoto@walla.com")
    driver.find_element(By.XPATH, '//div/input[@placeholder="Enter your password"]').send_keys("nir1404")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(10)
    driver.switch_to.alert.accept()
    if driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').is_displayed():
        print(colored("invalid email address!", "red"))
    else: print(colored(" Test End", "green"))





























