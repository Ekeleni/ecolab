nums = [1,2,3,4,5,6,7,8,9,0]
symb = ['!','@' , "#" , "$" , "%" , "^", "&","*","(" , ")" , "-" , "=" , "+" , "{" , "}", ";" , ":" , "'" , '"',"<" , ">" , "?" , "." , "/" , "|" , ',']


# 303 -- Password hasn't got numbers
# 304 -- Special symbols not in password

class CheckPassword:
    def __init__(self,password):
        self.password = password
    def lenCheck(self):
        if len(self.password) > 6:
            return "Status : OK"
        else:
             return "Status : BAD"
    def sybolsChecker(self):
        if self.lenCheck == "Status : OK":
            flagN = False
            flagS = False
            for i in nums:
                if i in self.password:
                    flagN =True

            if flagN == True:
                for j in symb:
                    if j in self.password:
                        flagS = True
                
                if flagS == True:
                    return "Status : OK"
            else:
                return "Status : 303"
        else:
            return "Status : BAD"