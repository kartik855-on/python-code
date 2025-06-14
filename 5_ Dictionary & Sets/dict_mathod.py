student = {"name": "Kartik", "age": 21, "course": "Python"}

# Accessing Values
print(student["name"])   
print(student.get("age"))

# Adding or Updating Items
student["age"] = 22           
student["city"] = "Delhi"      
print(student)

# Remove Items
student.pop("age")        # key remove    
del student["course"]     # Delete key-value   
student.clear()           #remove all data

print(student)


