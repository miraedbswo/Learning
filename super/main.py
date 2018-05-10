class father():  # 부모 클래스
    def handsome(self):
        print("He's handsome!")


class brother(father):
    # 자식클래스(부모클래스) 아빠매소드를 상속받겠다
    '''아들'''


class sister(father):
    # 자식클래스(부모클래스) 아빠매소드를 상속받겠다
    def pretty(self):
        print("She's pretty!")

    def handsome(self):
        super().handsome()


brother = brother()
brother.handsome()

girl = sister()
girl.handsome()    # 누락
girl.pretty()

print()


class father():
    def __init__(self, who):
        self.who = who

    def handsome(self):
        print("{}를 닮아 잘생겼다".format(self.who))


class sister(father):    # 자식클래스(부모클래스) 아빠매소드를 상속받겠다
    def __init__(self, who, where):
        super().__init__(who)
        self.where = where

    def choice(self):
        print("{} 말이야".format(self.where))

    def handsome(self):
        super().handsome()

        # who 와 handsome()은 부모에게 물려받은 것이기 때문에
        # 자식에서 사용하려면 무조건 super()를 사용해야 합니다.
        self.choice()


girl = sister("Dad", "Face")
girl.handsome()
