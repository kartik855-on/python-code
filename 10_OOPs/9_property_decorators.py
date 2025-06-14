class Student:
   
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

    @name.deleter
    def name(self):
        print("Deleting name...")
        self.fname = ""
        self.lname = ""

                                # Object बनाना
e = Student()

                                # Setter use
e.name = "kartik jaat"

                                # Getter use
print(e.fname, e.lname)  

                                # Deleter use
del e.name

# Check after delete
print(e.fname, e.lname)         # Output: (empty strings)
