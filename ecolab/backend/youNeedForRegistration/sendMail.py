import random 
import smtplib as smpt
import ssl

class Mail:
    def __init__(self,email,code):
        self.email= email
        self.code = code
    def generateNewCode(self):
        self.code = random.randint(100000,999999)
    def sendMail(self , *argc):
        port = 465
        smpt_server = "smpt.gmail.com"
        sender = "youremail@gmail.com"
        password = argc

        context = ssl.create_default_context()

        try:
            server = smpt.SMPT(smpt_server , port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender , password)

            smpt.sendmail(sender , self.email , self.code)
        except Exception as e:
            print(e)
        finally:
            server.quit()