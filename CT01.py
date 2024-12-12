from selenium import webdriver

from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.get("http://sga.leiteviana.com:8080")

driver.find_element(By.TAG_NAME, "a").send_keys(Keys.RETURN)

try:
    campoEmail = driver.find_element(By.ID, "email")
    campoUsername = driver.find_element(By.ID, "user")
    campoSenha = driver.find_element(By.ID, "senha")

    campoEmail.send_keys("david.teste@gmail.com")
    campoUsername.send_keys("DavidLucas")
    campoSenha.send_keys("DavidLucas123456")

    driver.find_element(By.TAG_NAME, "button").send_keys(Keys.RETURN)
except:
    print("Não foi possível encontrar os campos de login.")

input("Pressione Enter para fechar o navegador...")

driver.quit()
