# -*- coding: UTF-8 -*-
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header              # Header 用来构建邮件头
from utils.file_utils import fileutils

import smtplib
from selenium import webdriver


class SmtpReport:


    def __init__(self,msg_to):
        self.host = 'smtp.qq.com'
        self.msg_from = '1134106939@qq.com' # 发送方邮箱
        self.passwd = 'ypqxltkyuiucfgjh'  # 填入发送方邮箱的授权码
        self.msg_to=msg_to


    def send_email(self,subject,image_path,report_path):
        msg = MIMEMultipart('related')
        content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')  # 正文
        msg.attach(content)
        msg['Subject'] = Header(subject)
        msg['From'] =Header(self.msg_from)
        msg['To'] =  Header(",".join(self.msg_to))
        if not os.path.exists(image_path):
            return print("图片路径不存在")
        with open(image_path, "rb") as file:
            img_data = file.read()

        img = MIMEImage(img_data)
        img.add_header('Content-ID', 'imageid')
        msg.attach(img)
        file.close()
        att1 = MIMEText(open(report_path, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename=TestReport.html'
        msg.attach(att1)
        try:
            server = smtplib.SMTP_SSL(self.host,465)
            server.login(self.msg_from, self.passwd)  # 仅smtp服务器需要验证时
            server.sendmail(self.msg_from, self.msg_to, msg.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

    def email_image_send(self, report_path, title):
        report_png = "logs\\report.png"
        driver = webdriver.Chrome(executable_path=fileutils.local_file('config/chromedriver'))
        driver.get("file://%s" %report_path)
        driver.maximize_window()
        ele_list = driver.find_elements_by_xpath('//*[@type="case"]')
        for element in ele_list:
            driver.execute_script('arguments[0].setAttribute("class","hiddenRow");', element)#block-打开详情
        time.sleep(3)
        image_path = fileutils.local_file(report_png)
        driver.save_screenshot(image_path)
        self.send_email(title, image_path,report_path)
        os.remove(image_path)  # 移除截图
        driver.close()
