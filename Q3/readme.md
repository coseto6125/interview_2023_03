執行方法:`python answer_1.py`

1. selenium 連結網址
   * 利用 [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager) 套件自動安裝對應版本之 chromedriver
   * 調整介面大小以模擬手機模式
   * `logging` 替代 `print`，log 檔案預設存放於 `Q3/selenium.log`
2. 計算信用卡列表，有幾個項目並將畫面截圖
   * 利用 `logger` 方式依序印出所有tab並截圖
   * 截圖存放至 [Q3/screenshot/creadit_card_tab_list](./screenshot/creadit_card_tab_list/)
3. 計算頁面上所有(停發)信用卡數量並截圖
   * 依序click所有信用卡 button 並截圖
   * 截圖存放至 [Q3/screenshot/suspend_credit_card](./screenshot/suspend_credit_card/)
   * 最後用 `assert` 驗證存放截圖數量與計數是否一致
