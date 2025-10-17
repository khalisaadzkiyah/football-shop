from django.test import TestCase, Client
from .models import Product
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from django.contrib.auth.models import User

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            name="Socceria Ball",
            price=299000,
            description="Bola sepak premium warna pink pastel.",
            category="ball",
            is_featured=True
        )
        self.assertEqual(product.category, "ball")
        self.assertTrue(product.is_featured)

    def test_product_default_values(self):
        product = Product.objects.create(
            name="Basic Jersey",
            price=150000,
            description="Jersey sederhana warna lembut."
        )
        self.assertFalse(product.is_featured)

class FootballShopFunctionalTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.quit()

    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testadmin',
            password='testpassword'
        )

    def tearDown(self):
        self.browser.delete_all_cookies()
        self.browser.execute_script("window.localStorage.clear();")
        self.browser.execute_script("window.sessionStorage.clear();")
        self.browser.get("about:blank")

    def login_user(self):
        self.browser.get(f"{self.live_server_url}/login/")
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys("testadmin")
        password_input.send_keys("testpassword")
        password_input.submit()

    def test_login_page(self):
        self.login_user()
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Socceria")

        logout_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        self.assertTrue(logout_link.is_displayed())

    def test_register_page(self):
        self.browser.get(f"{self.live_server_url}/register/")
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Register")

        username_input = self.browser.find_element(By.NAME, "username")
        password1_input = self.browser.find_element(By.NAME, "password1")
        password2_input = self.browser.find_element(By.NAME, "password2")

        username_input.send_keys("newuser")
        password1_input.send_keys("complexpass123")
        password2_input.send_keys("complexpass123")
        password2_input.submit()

        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
        login_h1 = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(login_h1.text, "Login")

    def test_create_product(self):
        self.login_user()

        add_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Add Product")
        add_button.click()

        name_input = self.browser.find_element(By.NAME, "name")
        price_input = self.browser.find_element(By.NAME, "price")
        description_input = self.browser.find_element(By.NAME, "description")
        category_select = self.browser.find_element(By.NAME, "category")
        thumbnail_input = self.browser.find_element(By.NAME, "thumbnail")
        is_featured_checkbox = self.browser.find_element(By.NAME, "is_featured")

        name_input.send_keys("Test Jersey")
        price_input.send_keys("250000")
        description_input.send_keys("Jersey Socceria edisi pink pastel")
        thumbnail_input.send_keys("https://example.com/jersey.jpg")

        select = Select(category_select)
        select.select_by_value("jersey")

        is_featured_checkbox.click()
        name_input.submit()

        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Socceria"))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Socceria")

        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Test Jersey")))
        product_name = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Test Jersey")
        self.assertTrue(product_name.is_displayed())

    def test_product_detail(self):
        self.login_user()

        product = Product.objects.create(
            name="Socceria Shoes",
            price=450000,
            description="Sepatu bola ringan warna pink lembut.",
            user=self.test_user
        )

        self.browser.get(f"{self.live_server_url}/product/{product.id}/")
        self.assertIn("Socceria Shoes", self.browser.page_source)
        self.assertIn("Sepatu bola ringan", self.browser.page_source)

    def test_logout(self):
        self.login_user()
        logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
        logout_button.click()

        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Login")

    def test_filter_main_page(self):
        Product.objects.create(
            name="Socceria Ball",
            price=299000,
            description="Bola edisi pink pastel.",
            user=self.test_user
        )
        Product.objects.create(
            name="Training Cone",
            price=99000,
            description="Cone latihan warna pink muda.",
            user=self.test_user
        )

        self.login_user()

        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "All Products")))
        all_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "All Products")
        all_button.click()
        self.assertIn("Socceria Ball", self.browser.page_source)
        self.assertIn("Training Cone", self.browser.page_source)

        my_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "My Products")
        my_button.click()
        self.assertIn("Socceria Ball", self.browser.page_source)
