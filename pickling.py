#This Program converts  the content of a file into bytecode
import pickle
def pickle_data():
    data = {
                'Emp name': 'John',
                'profession': 'Python Developer',
                'country': 'America'
        }
    filename = 'D:\personalinfo.txt'
    outfile = open(filename, 'wb')
    pickle.dump(data,outfile)
    outfile.close()
pickle_data()
def unpickling_data():
    file = open('D:\personalinfo.txt','wb')
    new_data = pickle.load(file)
    file.close()
    return new_data
print(unpickling_data())