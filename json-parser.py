obj1 = {
  "num": 1,
  "test": [
    {
      "name":'Purnendu',
      "Age":29,
      "sex":'male'
    },
    {
      "Dept":'Finance',
      "sal":1000,
      "DOJ":18970,
      "city":'Bangalore'
    }
  ],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66,
      "abc":'xyz',
      "pqr":'False'
    }
  }
}
def findJson(j,strg,value=None):
  for key in j:
      if isinstance(j[key],dict):
        value = findJson(j[key],strg,value)
      elif isinstance(j[key],list):
        for items in j[key]:
         value=findJson(items,strg,value)
      else:
        if key == strg:
           value=j[key]
  return value


print(findJson(obj1,'sal'))


def dict_get(x, key, here=None):

  if here is None:
    here = []
  if x.get(key):
    here.append(x.get(key))

  else:
    for i, j in x.items():
      if isinstance(x[i], list):
        for items in x[i]:
          dict_get(items, key, here)
      if isinstance(x[i], dict):
        dict_get(x[i], key, here)
  return here

#print(dict_get(obj1,'sex'))