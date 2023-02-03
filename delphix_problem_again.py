'''If a software name is given then it's all dependencies should be printed'''
software_dependency_map= {
    "unittest": "testdata",
    "testdata": "metapy",
    "metapy": "colorpy",
    "colorpy": "pyruby",
    "pyfail": "colorpy",
    "pyruby": None,
    "pychecks": "colorpy",
    "pycff": "pyruby"
}
res = ''
software='unittest'
for i in range(len(software_dependency_map)):
    val1 = software_dependency_map[software]
    if val1 in software_dependency_map.keys():
        res +=val1+' '
        software=val1
print(res)


