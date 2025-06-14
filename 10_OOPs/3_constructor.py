class employee:
    language="python"
    salary=120000

    def __init__(self,salary,language):  # dunder method which is automatically called
        self.salary=salary
        self.language=language
        print("i am creat an object")


    
kartik=employee(130000,"kartik")
print(kartik.salary,kartik.language)
