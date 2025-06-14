class employee:
    compnay="RTC"
    name="defolt name"
    def show(self):
        print(f"the company name {self.compnay} employ name {self.name}")

class coder:
    language="python"
    def showlang(self):
          print(f"the employ name {self.name} and language {self.language}")

class progermer(coder,employee):
    def combo(self):
        print(f"the {self.compnay} and {self.language}")


c=progermer()
c.combo()
c.show()
c.showlang()