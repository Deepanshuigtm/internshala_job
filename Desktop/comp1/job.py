import time as t

import re
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'https://internshala.com/registration/student'
driver = webdriver.Safari()
driver.get(link)
driver.maximize_window()
t.sleep(1)
try:
    close_popup = driver.find_element(By.XPATH, "//i[@id='close_popup']")
    close_popup.click()
    t.sleep(1)
except:
    pass
job = ['data-science', 'software-development', 'web-development', 'data-analytics',
       'front-end-development', 'python-django', 'javascript', 'html', 'css', 'python']

for i in job:
    try:
        login_link = driver.find_element(By.XPATH,
                                         "//span[@data-target='#login-modal']")
        login_link.click()
        username = < enter your internshala username >
        password = < enter your internshala password >

        email_input = driver.find_element(
            By.XPATH, "//input[@id='modal_email']")
        email_input.send_keys(username)
        t.sleep(1)
        password_input = driver.find_element(
            By.XPATH, "//input[@id='modal_password']")
        password_input.send_keys(password)
        t.sleep(1)
        login_submit = driver.find_element(
            By.XPATH, "//button[@id='modal_login_submit']")
        login_submit.click()
    except:
        pass
    t.sleep(4)

    try:
        close_popup = driver.find_element(By.ID, "close_popup")
        close_popup.click()
    except:
        pass

    driver.get(
        f'https://internshala.com/internships/work-from-home-{i}-internships/')
    # f'https://internshala.com/internships/work-from-home-{i}-internships/')
    # https: // internshala.com/internships/work-from-home-internships/
    t.sleep(2)
    apply_buttons = driver.find_elements(
        By.CLASS_NAME, "btn-primary.easy_apply")

    # Click on each "Apply now" button one by one
    for apply_button in apply_buttons:
        try:
            apply_buttons = driver.find_elements(
                By.CLASS_NAME, "btn-primary.easy_apply")
        except:
            pass
        try:
            apply_buttons[0].click()
            t.sleep(1)
            continue_button = driver.find_element(By.ID, "continue_button")
            continue_button.click()
            t.sleep(2)
        except:
            pass
        if i == 'software-development':
            answer = 'With hands-on web development experience, completing a rewarding internship and successful e-commerce project, I am the ideal fit for this role. Passionate about innovation and detail-oriented, I create web solutions that align with objectives. Adaptable and collaborative, I thrive in dynamic teams, delivering remarkable results that drive growth and success'

        if i == 'web-development':
            answer = 'With hands-on web development experience, completing a rewarding internship and successful e-commerce project, I am the ideal fit for this role. Passionate about innovation and detail-oriented, I create web solutions that align with objectives. Adaptable and collaborative, I thrive in dynamic teams, delivering remarkable results that drive growth and success'

        if i == 'data-analytics':
            answer = 'As a candidate with a strong passion for data analytics and a track record of hands-on experience, I believe I am the ideal fit for this role. Having completed a data analytics internship and successfully executed a project in the same field, I have honed my skills in data manipulation, visualization, and deriving valuable insights. My combination of theoretical knowledge and practical application makes me well-equipped to contribute effectively to the HR team, leveraging data-driven decisions to enhance hiring processes, optimize talent management, and drive organizational success. I am confident that my enthusiasm and expertise in data analytics will enable me to excel in this role and deliver tangible results for the company.'
        if i == 'front-end-development':
            answer = 'As a dedicated and experienced front-end developer, I am the perfect match for this role. With a completed internship in front-end development and the successful creation of an e-commerce website project, I possess the skills to design and implement captivating user interfaces, ensure seamless user experiences, and contribute to the overall growth of the companys digital presence. My commitment to staying updated with the latest technologies and my passion for delivering high-quality web solutions make me the best candidate to elevate the user experience and drive business success.'
        if i == 'python-django':
            answer = 'As an aspiring Python-Django developer with a completed internship in this domain and hands-on experience building an e-commerce website using Python-Django, I am the ideal choice for this role. My proficiency in developing scalable and efficient web applications, coupled with my problem-solving abilities and attention to detail, enable me to contribute effectively to the teams projects. I am enthusiastic about leveraging my skills to create robust and user-friendly web solutions, making me the best fit to drive innovation and deliver value to the organization.'
        if i == 'javascript':
            answer = 'With hands-on web development experience i made Bankist Web App, a fully functional and visually appealing banking application made with This web app, developed using HTML, CSS, and JavaScript.Showcases my proficiency in ECMAScript (ES6) and DOM manipulation, providing users with a seamless and intuitive banking experience.'
        if i == 'html':
            answer = 'With hands-on web development experience, completing a rewarding internship and successful e-commerce project, I am the ideal fit for this role. Passionate about innovation and detail-oriented, I create web solutions that align with objectives. Adaptable and collaborative, I thrive in dynamic teams, delivering remarkable results that drive growth and success'
        if i == 'css':
            answer = 'With hands-on web development experience, completing a rewarding internship and successful e-commerce project, I am the ideal fit for this role. Passionate about innovation and detail-oriented, I create web solutions that align with objectives. Adaptable and collaborative, I thrive in dynamic teams, delivering remarkable results that drive growth and success'
        if i == 'python':
            answer = 'As an aspiring Python developer with a completed internship in this domain and hands-on experience building an e-commerce website using Python-Django, I am the ideal choice for this role. My proficiency in developing scalable and efficient web applications, coupled with my problem-solving abilities and attention to detail, enable me to contribute effectively to the teams projects. I am enthusiastic about leveraging my skills to create robust and user-friendly web solutions, making me the best fit to drive innovation and deliver value to the organization.'
        if i == 'data-science':
            answer = 'As an aspiring Data Scientist with a completed internship in this field and hands-on experience executing successful Data Science projects, I am the perfect fit for this role. My expertise in data manipulation, statistical analysis, and machine learning empowers me to extract valuable insights and solve complex problems. I possess a strong passion for continuous learning and thrive in a collaborative environment, making me the best candidate to drive data-driven decisions and contribute significantly to the companys growth and success.'
        else:
            answer = 'With hands-on web development experience, completing a rewarding internship and successful e-commerce project, I am the ideal fit for this role. Passionate about innovation and detail-oriented, I create web solutions that align with objectives. Adaptable and collaborative, I thrive in dynamic teams, delivering remarkable results that drive growth and success'

        try:
            text_area = driver.find_element(
                By.XPATH, "//div[@id='cover_letter_holder']")
            text_area.click()
            text_area.send_keys(answer)
            t.sleep(1)
        except:
            pass
        try:
            continue_button = driver.find_element(By.ID, "continue_button")
            continue_button.click()
            t.sleep(1)
            try:
                text_area = driver.find_element(
                    By.XPATH, "//div[@id='cover_letter_holder']")
                text_area.click()
                text_area.send_keys(answer)
                t.sleep(1)
            except:
                pass
        except:
            pass

        try:
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()
        except:
            pass
        t.sleep(1)
        try:
            submit_button.click()
        except:
            pass
        try:
            continue_button = driver.find_element(By.ID, "continue_button")
            continue_button.click()
        except:
            pass
        t.sleep(1)
        easy_apply_modal_close = driver.find_element(
            By.ID, "easy_apply_modal_close")
        try:
            easy_apply_modal_close.click()
        except:
            pass
        t.sleep(2)
        easy_apply_modal_close_confirm_cancel = driver.find_element(
            By.ID, "easy_apply_modal_close_confirm_cancel")
        try:
            easy_apply_modal_close_confirm_cancel.click()
        except:
            pass
        try:
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()
        except:
            pass
        try:
            text_4769003 = driver.find_elements(
                By.XPATH, "//textarea[@placeholder='Enter text ...']")
            text_4769003[0].send_keys('YES')
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()
            text_4769003[1].send_keys('1')
            t.sleep(1)
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()
        except:
            pass
        t.sleep(2)
        try:
            backToInternshipsCta = driver.find_element(
                By.ID, "backToInternshipsCta")
            backToInternshipsCta.click()
        except:
            pass

        t.sleep(2)
