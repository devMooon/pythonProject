from selenium.webdriver.support.ui import Select

select = Select(driver.find_element_by_xpath('셀렉트박스XPATH'))
select.select_by_value('선택할 값')