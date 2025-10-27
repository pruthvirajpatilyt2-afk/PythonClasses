class data:
    def __init__(self):
        super().__init__()
        self.name='APP'
        self.version='1.0.0.0'
        self.app_title=self.name +' '+ self.version
        self.LoadingSize='666x444+400+300'
        print(self.app_title)

if __name__=='__main__':
    data()