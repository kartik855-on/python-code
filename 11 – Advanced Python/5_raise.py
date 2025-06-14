a=int(input("enter number 1 ="))
b=int(input("enter number 2 ="))

if a==0:
    raise ZeroDivisionError("check the number of 1 velue not enter 0 ")
elif b==0:
     raise ZeroDivisionError("check the number of 2 velue not enter 0 ")   
else:
     print("The division :",a/b)



# ValueError            at wrong value                 raise ValueError("Invalid value")
# TypeError	            wrong data type                raise TypeError("Wrong type")
# ZeroDivisionError	    on dividing by 0               raise ZeroDivisionError("Cannot divide by zero")
# IndexError	        List wrong index	           raise IndexError("Index out of range")
# KeyError	            key not found in dictionary	   raise KeyError("Key not found")
# AttributeError	    Invalid attribute access	   raise AttributeError("Attribute missing")
# ImportError	        Import fail                    raise ImportError("Module not found")
# FileNotFoundError	    File not found	               raise FileNotFoundError("File not found")
# PermissionError	    No permission for file access  raise PermissionError("Permission denied")
# RuntimeError	        any generic run-time error	   raise RuntimeError("Something went wrong")
# NotImplementedError	No function has been create	   raise NotImplementedError("Not implemented yet")
# AssertionError	    when assert fails	           raise AssertionError("Condition failed")
