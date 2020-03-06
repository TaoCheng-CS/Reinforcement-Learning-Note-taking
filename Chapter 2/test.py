class test:
    def __init__(self):
        self.a=[0 for i in range(1000)]

    def update(self):
        self.a[0]=2/3

ab=test()
ab.update()
print(ab.a[0])