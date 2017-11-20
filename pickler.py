#npgrpg pickler. [Ready for testing!]
#---use: import pickler.py
#------- save = pickler.pickleSession(saveName,data)
#------- load = pickler.snackTime(saveName)
#------- data = load.data()

import pickle 

class pickleSession:
    def __init__(self,name,material):
        self.name = name
        print("Growing Pickle...")
        pickle_out = open(self.name+".pickle","wb")
        print("Pickling: " + material)
        pickle.dump(material,pickle_out)
        print("Putting Pickle in Jar...")
        pickle_out.close()
        print("Congrats, its out of your hands now!")

class snackTime:
    def __init__(self,name):
        self.name = name
        print("Juicing Pickle...")
        pickle_in = open(self.name+".pickle","r")
        self.material = pickle.load(pickle_in)
        print("Unpickling: "+material)
        print("Closing lid...")
        pickle_in.close()
        print("Enjoy the snack!")

    def data(self):
        return self.material