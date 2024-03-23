class carshowroom:
    def _init_(self,cgst,sgst,insurance):
        self.cgst=cgst
        self.sgst=sgst
        self.ins=insurance
        
    def company(self):
        while True:
            print("select a car from tata,mercedez,hyundai")
            self.n=input("select a car")
            if self.n=="tata":
                print("welcome to tata")
                self.model()
                break
            elif self.n=="mercedez":
                print("welcome to mercedez")
                self.model()
                break
            elif self.n=="hyndai":
                print("welcome to hyundai")
                self.model()
                break
            else:
                print("enter valid company")
                break
    def model(self):
      if self.n=="tata":
        while True:
            print("the models are harriar and nexon")
            self.m=input("enter car")
            if self.m=="harriar":
                self.price(self.m)
                break
            elif self.m=="nexon":
                self.price(self.m)
                break
            else:
                print("enter valid model")
                break
      if self.n=="mercedez":
          while True:
              print("the model are amg and gwagon")
              self.m=input("enter car")
              if self.m=="amg":
                  self.price(self.m)
                  break
              elif self.m=="gwagon":
                  self.price(self.m)
                  break
              else:
                  print("enter valid model")

      if self.n=="hyundai":
          while True:
              print("the model are i10 and xcent")
              self.m=input("enter car")
              if self.m=="i10":
                  self.price(self.m)
                  break
              elif self.m=="xcent":
                  self.price(self.m)
                  break
              else:
                  print("enter valid")
    def price(self,m):
        if m=="harriar":
            self.price=3567854
        elif m=="nexon":
            self.price=1500000
        elif m=="amg":
            self.price=2457000
        elif m=="gwagon":
            self.price=54000000
        elif m=="i10":
            self.price=125855525
        elif m=="xcent":
            self.price=956526232
        total=self.price+self.cgst+self.sgst+self.ins
        print(total)

ob=carshowroom(0.18,0.18,100000)
ob.company()
