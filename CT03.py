from selenium import webdriver

from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
# driver = webdriver.Edge(service=Service("./edgedriver_win64/msedgedriver.exe"))

driver.get("http://sga.leiteviana.com:8080")

try:

    # Fazendo Login
    campoUsername = driver.find_element(By.ID, "user")
    campoSenha = driver.find_element(By.ID, "senha")

    campoUsername.send_keys("DavidLucas")
    campoSenha.send_keys("DavidLucas123456")

    driver.find_element(By.TAG_NAME, "button").send_keys(Keys.RETURN)

    # Clicando no botão de cadastro de aluno
    driver.find_element(By.LINK_TEXT, "Cadastrar Aluno").click()

    # Preenchendo os campos de cadastro de aluno
    campoNome = driver.find_element(By.ID, "nome")
    campoNome.send_keys("Gabriel Victor")

    campoCurso = Select(driver.find_element(By.ID, "curso"))
    campoCurso.select_by_index(1)

    # Clicando no botão de gerar matrícula
    driver.find_element(By.CLASS_NAME, "btn-primary").click()

    campoTurno = Select(driver.find_element(By.ID, "turno"))
    campoTurno.select_by_index(0)

    campoStatus = Select(driver.find_element(By.ID, "status"))
    campoStatus.select_by_index(0)

    # Clicando no botão de salvar cadastro do aluno
    driver.find_element(By.CLASS_NAME, "btn-outline-success").click()
    
    # Clicando no botão de editar
    driver.find_element(By.CLASS_NAME, "btn-primary").click()

    # Editando informações do aluno
    campoNome = driver.find_element(By.ID, "nome")
    campoNome.clear()
    campoNome.send_keys("César Cavalcanti")

    campoCurso = Select(driver.find_element(By.ID, "curso"))
    campoCurso.select_by_index(2)

    # Clicando no botão de salvar edição do aluno
    driver.find_element(By.CLASS_NAME, "btn-outline-success").click()
    
    # Clicando no botão de excluir aluno
    driver.find_element(By.CSS_SELECTOR, "a.btn-danger").click()

except:
    print("Algo deu errado com seu teste automatizado.")

input("Pressione Enter para fechar o navegador...")

driver.quit()
