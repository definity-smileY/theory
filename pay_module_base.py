import pyautogui as pg

# 결제 정보, 관리 모듈
version = 2.0

def printAuthor():
    print("스타트")

class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time
    
    def get_pay_info(self):
        return f"{self.time} {self.id} {self.price}"

# 해당 파일을 실행
if __name__ == '__main__':
    print("Pay Module 실행")