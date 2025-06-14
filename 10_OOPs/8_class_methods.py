class employ:
    a=1

    @classmethod
    def show(cls):
        print(f"the class atribut of {cls.a}")
    
o=employ()
o.a=56
o.show()
