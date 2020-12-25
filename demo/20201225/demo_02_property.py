class Test:
    @property
    def add(self):
        return 'aaa'
    def sub(self):
        return 1
if __name__ == '__main__':
    test = Test()
    print(test.add) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）
    print(test.sub())  #没有加@property , 必须使用正常的调用方法的形式，即在后面加()
