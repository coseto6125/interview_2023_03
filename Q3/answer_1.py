# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-04-10 22:00:05
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-04-11 01:26:42
from datetime import datetime
from logging import INFO, FileHandler, Formatter, StreamHandler, getLogger
from os import getcwd, listdir, system

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

try:  # 自動更新chrome driver套件 github: https://github.com/SergeyPirogov/webdriver_manager
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    system("pip install webdriver-manager")
    from webdriver_manager.chrome import ChromeDriverManager

PATH = "Q3/screenshot"


def setup_logger(logger_name, log_file, level=INFO):
    logger = getLogger(logger_name)
    logger.setLevel(level)

    formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")

    if log_file:
        file_handler = FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    console_handler = StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


def main() -> None:
    logger = setup_logger("selenium", "Q3/selenium.log")
    logger.info("{:=^{length}}".format(" start ", length=35))
    chrome_driver_path = ChromeDriverManager(path=getcwd()).install()
    get_date = lambda: datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    url = "https://www.cathaybk.com.tw/cathaybk/"
    driver = Chrome(service=Service(chrome_driver_path))
    wait = WebDriverWait(driver, 600)

    driver.set_window_size(414, 896)
    driver.get(url)
    logger.info("step0: 加載成功開啟網頁")

    def wait2click(xpath: str, click: bool = True) -> None:
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        driver.implicitly_wait(20)  # 隱式等待，避免顯式等待元素出現 delay issue
        if click:
            driver.find_element(By.XPATH, xpath).click()

    click_step = {
        "step1: 點選 ≡ ": "/html/body/div[1]/header/div/div[1]/a/img[2]",
        "step2: 點選 產品介紹 ": "//*[text()='產品介紹']",
        "step3: 點選 信用卡 ": "//*[text()='信用卡']",
        "step4: 取得 信用卡列表 ": "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a",
        "step5: 點選 卡片介紹 ": "//*[text()='卡片介紹']",
        "step6: 取得 停辦卡列表 ": "/html/body/div[1]/main/article/section[5]/div/div[2]/div/div[2]/span",
    }
    for i, v in click_step.items():
        logger.info(i)
        match i[4]:
            case "1" | "2" | "3" | "5":
                wait2click(v)
            case "4":
                wait2click(v, False)
                credit_tag = driver.find_elements(By.XPATH, v)
                logger.info(f"       信用卡下數量：{(len_tag:=len(credit_tag))}")
                driver.implicitly_wait(20)
                for index, tab in enumerate(credit_tag, 1):
                    if tab.text:
                        logger.info(f"       tab與截圖 - {tab.text}")
                    if index < len_tag: # 最後一個tab不點擊,避免跳到search bar 造成卡片介紹無法點擊
                        tab.send_keys(Keys.TAB)
                    driver.get_screenshot_as_file(f"{PATH}/creadit_card_tab_list/{index}_{get_date()}.png")
            case "6":
                wait2click(v, False)
                suspend = driver.find_elements(By.XPATH, v)
                wait2click(v2:=v.replace("[5]", "[6]"), False)
                suspend += driver.find_elements(By.XPATH, v2)
                for index, card in enumerate(suspend, 1):
                    card.click()
                    driver.get_screenshot_as_file(f"{PATH}/suspend_credit_card/{index}_{get_date()}.png")
                try:
                    screenshot_num,suspend_num = len(listdir(f"{PATH}/suspend_credit_card/")),len(suspend)
                    assert screenshot_num == suspend_num, f"驗證(停發)信用卡數量與截圖數量{suspend_num=},{screenshot_num=}"
                except AssertionError as e:
                    logger.error(str(e))
    logger.info("{:=^{length}}".format(" all done ", length=35))

    driver.quit()


if __name__ == "__main__":
    main()
