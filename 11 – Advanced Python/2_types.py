# list....

from typing import List

def total(numbers: List[int]) -> int:
    return sum(numbers)

print(total([1, 2, 3, 4]))



# union....

from typing import Union

def show(value: Union[int, str]) -> None:
    print(f"The value is: {value}")

show(42)      
show("hello")




# tuple....

from typing import Tuple

def get_user() -> Tuple[str, int]:
    return ("Kartik", 25)

a=get_user()
print(a)