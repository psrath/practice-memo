def isValid(s:str) -> bool:
    if len(s)<1 :
        return False
    for ch in s:
        print(ch)
    #print(s1)
    result = None
    return result

if __name__ == "__main__":
    line = input()
    if isValid(line):
        print("valid")
    else:
        print("Invalid")

