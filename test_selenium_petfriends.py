import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\projects\Skillfactory\chromedriver.exe')
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   myDynamicElement = pytest.driver.find_element(By.ID, "pass")
   yield
   pytest.driver.quit()


def test_show_my_pets():
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   pytest.driver.find_element(By.ID,'email').send_keys('okiro@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('15051987')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы находимся на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


   pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')

   # список всех обьектов питомца, в котром есть атрибут ".text" с помощью которого,
   # можно получить информацию о питомце в виде строки: 'meow  cat	2'
   all_my_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr')

   # этот список image объектов, который имееют метод get_attribute('src') ,
   # благодаря которому можно посмотреть есть ли изображение питомца или нет.
   all_pets_images = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr/th/img')

   # проверяем что список своих питомцев не пуст
   assert len(all_my_pets) > 0

   pets_info = []
   for i in range(len(all_my_pets)):
      # получаем информацию о питомце из списка всех своих питомцев
      pet_info = all_my_pets[i].text

      # избавляемся от лишних символов '\n×'
      pet_info = pet_info.split("\n")[0]

      # добавляем в список pets_info информацию рода: имя, тип, возраст,  по каждому питомцу
      pets_info.append(pet_info)
   print(pet_info)