class father():    # class parent
    def handsome(self):
        print("He's handsome!")


class brother(father):
    """son"""    # brother is handsome


class sister(father):
    def pretty(self):
        print("She's pretty!")

    def handsome(self):    # sister is pretty
        self.pretty()    # it's override

# 추가로 딸이 상속받은 메소드를 변형시켜도 다른 자식이나 부모까지 영향을 주지 않습니다!
# 왜냐하면 물려받은 것일 뿐이니까요


brother = brother()
brother.handsome()
# class 아들은 아빠에게 상속받아 잘생겼다가 출력되었고,

girl = sister()
girl.handsome()
# class 딸은 이미 상속을 받았지만 예쁘다 라고 사용중이기 때문에
# 잘생겼다를 무시하게 됩니다. (이것을 오버라이딩)

