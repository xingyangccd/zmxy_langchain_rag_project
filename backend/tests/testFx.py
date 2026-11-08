from typing import List

from typing_extensions import TypeVar

l2:List[int]=[1,2,3,4]
l2.append("c")
print(l2)


def first_item(items:List[str]):
    return items[0]

print(first_item([1,2,3]))     # 推断 int
print(first_item(["a","b"]))   # 推断 str


t=TypeVar("T")

NumStr = TypeVar("NumStr", int, str)
str:NumStr=1.1
print(str)
def show_list2(items:List[t])->t:
    return items[0]


print(show_list2([1,2,4]))
print(show_list2(["a","b","c"]))
