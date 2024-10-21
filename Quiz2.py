class Gugudan:
    def __init__(self, num):
        self.num = num

    def output(self):
        for i in range(1, 10):
            print(f'{self.num} x {i} = {self.num * i}')

dan = int(input("출력할 구구단의 숫자를 입력하세요: "))
gugudan = Gugudan(dan)

gugudan.output()
