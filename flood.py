from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("NOT: Sadece Takip Ettiğiniz Hesapları ya da Hesabı Açık Olan Kullanıcılarda Çalışır !\nŞaka Tooludur :)")
username = input("Lütfen Kullanıcı Adınızı Giriniz : ") 
password = input("Lütfen Şifrenizi Giriniz : ") 
dogrulama = input("Çift Haneli Doğrulamanız Aktif mi ? E/H : ")
targetName = input("Flood Atılacak Kişinin Kullanıcı Adını Giriniz : : ")
text = input("Flood Metnini Giriniz : ")

driver = webdriver.Chrome() #Kullandıgınız Tarayıcıya Göre Değiştirin Firefox Kullanıyorsanız .Firefox() Yapın
driver.maximize_window()

def login():
    driver.get("https://www.instagram.com/accounts/login/") 

    time.sleep(5) 

    kullaniciAdi = driver.find_element(By.NAME,"username") 
    sifre = driver.find_element(By.NAME,"password") 
    button = driver.find_element(By.CLASS_NAME,"y3zKF") 

    kullaniciAdi.click()
    kullaniciAdi.send_keys(username) 

    sifre.click()
    sifre.send_keys(password) 

    button.click() 

    time.sleep(5) 

    if dogrulama == "E" or dogrulama == "e":
        code = input("Lütfen Telefonunuza Gelen Doğrulama Kodunu Giriniz : ") 
        securitCode = driver.find_element(By.NAME,"verificationCode") 
        securitCode.click()
        securitCode.send_keys(code) 
        secondButton = driver.find_element(By.CLASS_NAME,"y3zKF")
        secondButton.click() 

    elif dogrulama == "H" or dogrulama == "h":
        pass

    else:
        pass

def dm():
    driver.get("https://www.instagram.com/"+targetName)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button")
    message.click()
    time.sleep(5)
    print("Saldırı Başlıyor...")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("Başladı (DURDURMAK İÇİN CTRL + C) !")
    while True:
        textarea = driver.find_element(By.TAG_NAME,"textarea") 
        textarea.send_keys(text)
        textarea.send_keys(Keys.RETURN)


login()
dm()

