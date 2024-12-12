from selenium import webdriver

from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
# driver = webdriver.Edge(service=Service("./edgedriver_win64/msedgedriver.exe"))

driver.get("http://sga.leiteviana.com:8080")

try:
    campoUsername = driver.find_element(By.ID, "user")
    campoSenha = driver.find_element(By.ID, "senha")

    campoUsername.send_keys("DavidLucas")
    campoSenha.send_keys("DavidLucas123456")

    driver.find_element(By.TAG_NAME, "button").send_keys(Keys.RETURN)

    driver.find_element(By.LINK_TEXT, "Cadastrar Aluno")
except:
    print("Algo deu errado com seu teste automatizado.")

input("Pressione Enter para fechar o navegador...")

driver.quit()