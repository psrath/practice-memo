obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    },
  "obj_inner":[1,3,4,5,6,7],
  "obj_in_no":4
 }
}
def sumNested(obj):
    sum=0
    for items in obj:
        if isinstance(obj[items],dict):
            sum+=sumNested(obj[items])
        elif type(obj[items]) is int:
            sum+=obj[items]
        elif isinstance(obj[items],list):
            for i in obj[items]:
                sum+=i
    return sum
def
print(sumNested(obj1))