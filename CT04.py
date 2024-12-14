from selenium import webdriver

from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
# driver = webdriver.Edge(service=Service("./edgedriver_win64/msedgedriver.exe"))

# driver.get("http://sga.leiteviana.com:8080")
driver.get("http://localhost:8080")

try:
    # Fazendo Login
    campoUsername = driver.find_element(By.ID, "user")
    campoSenha = driver.find_element(By.ID, "senha")

    campoUsername.send_keys("DavidLucas")
    campoSenha.send_keys("DavidLucas123456")

    driver.find_element(By.TAG_NAME, "button").send_keys(Keys.RETURN)

    # Clicando no botão de pesquisar aluno
    driver.find_element(By.LINK_TEXT, "Pesquisar Aluno").click()

    # Pesquisando aluno pelo status de Ativo
    alunosAtivos = driver.find_element(By.CSS_SELECTOR, "a[href='/alunos-ativos']")
    alunosAtivos.click()

except:
    print("Algo deu errado com seu teste automatizado.")

input("Pressione Enter para fechar o navegador...")

driver.quit()
