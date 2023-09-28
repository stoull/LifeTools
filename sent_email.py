#-- coding:UTF-8 --
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class Email_Helper(object):
	"""docstring for Email_Helper"""
	def __init__(self, email_content):
		self.email_content = email_content

		# 第三方服务
		# self.mail_host = "smtp.gmail.com"
		# self.mail_user = "xxxx@gmail.com"
		# self.mail_pass = "xxxx"
		# self.sender = "xxxx@gmail.com"
		# self.receivers = ["xxxx@163.com"]
        
		self.mail_host = "smtp.163.com"
		self.mail_user = "xxxx@163.com"
		self.mail_pass = "xxxx"
		self.sender = "xxxx@163.com"
		self.receivers = ["xxxx@163.com"]

		self.content = email_content["content"]
		self.subject = email_content["title"]	# 邮件主主题
		
	def sendEmail(self):
		message = MIMEText(self.content, 'plain', 'utf-8')
		message['From'] = "{}".format(self.sender)
		message['To'] = ",".join(self.receivers)
		message['Subject'] = self.subject

		try:
			# smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
			smtpObj = smtplib.SMTP(self.mail_host)
			smtpObj.ehlo()
			smtpObj.starttls()
			# smtpObj.set_debuglevel(True)
			smtpObj.login(self.mail_user, self.mail_pass)
			smtpObj.sendmail(self.sender, self.receivers, message.as_string())
			print("mail has been send successfully")
		except smtplib.SMTPException as e:
			print(e)

	def sendTheLastImage(self):
		self.sendEmailWithImage('/Users/hut/Documents/洛阳市.png')

	def sendEmailWithImage(self, imgFilePath):
		message = MIMEMultipart()
		message['From'] = "{}".format(self.sender)
		message['To'] = ",".join(self.receivers)
		message['Subject'] = self.subject

		text = MIMEText(self.content, 'plain', 'utf-8')
		message.attach(text)

		print(f"image file path: {imgFilePath}")

		with open(imgFilePath, 'rb') as f:
			img_data = f.read()
		image = MIMEImage(img_data, name=os.path.basename(imgFilePath))
		message.attach(image)

		try:
			# smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
			smtpObj = smtplib.SMTP(self.mail_host)
			smtpObj.ehlo()
			smtpObj.starttls()
			# smtpObj.set_debuglevel(True)
			smtpObj.login(self.mail_user, self.mail_pass)
			smtpObj.sendmail(self.sender, self.receivers, message.as_string())
			print("mail has been send successfully")
		except smtplib.SMTPException as e:
			print(e)

if __name__ == '__main__':
	emil_content = {"content":"Hi Kevin, it's been longtime not hear from you. How are you now?","title":"Hi, there is a new notification!"}
	emil_helper = Email_Helper(emil_content)
	emil_helper.sendTheLastImage()
