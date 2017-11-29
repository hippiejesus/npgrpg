#npgrpg pickler. [Ready for testing!]
#---use: import pickler
#------- save = pickler.pickleSession(saveName,data)
#------- load = pickler.snackTime(saveName)
#------- data = load.data()

import pickle 
import zlib
import os

class pickleSession:
    def __init__(self,name,material):
        self.name = name
        print("Growing Pickle...")
        pickle_out = open("/storage/emulated/0/qpython/npgrpg-master/npgrpg-master/pickle_jar/"+self.name+".pickle","wb")
        print("Pickling: " + str(material))
        pickle.dump(material,pickle_out)
        print("Putting Pickle in Jar...")
        pickle_out.close()
        print("Congrats, its out of your hands now!")
        
        to_compress = open("/storage/emulated/0/qpython/npgrpg-master/npgrpg-master/pickle_jar/"+self.name+".pickle","rb")
        string = to_compress.read()
        compstring = zlib.compress(string)
        to_compress.close()
        
        to_save = open("/storage/emulated/0/qpython/npgrpg-master/npgrpg-master/pickle_jar/"+self.name+".zzz","wb")
        to_save.write(compstring)
        to_save.close()
        
        os.remove("/storage/emulated/0/qpython/npgrpg-master/npgrpg-master/pickle_jar/"+self.name+".pickle")
        
class snackTime:
    def __init__(self,name):
        self.name = name
        to_decompress = open("/storage/emulated/0/qpython/npgrpg-master/npgrpg-master/pickle_jar/"+self.name+".zzz","rb")
        string = to_decompress.read()
        decompstring = zlib.decompress(string)
        to_decompress.close()
        
        to_save = open("/storage/emulated/0/qpython/npgrpg-master/npgrpg-master/pickle_jar/"+self.name+".pickle","wb")
        to_save.write(decompstring)
        to_save.close()
        
        print("Juicing Pickle...")
        pickle_in = open("/storage/emulated/0/qpython/npgrpg-master/npgrpg-master/pickle_jar/"+self.name+".pickle","rb")
        self.material = pickle.load(pickle_in)
        print("Unpickling: "+str(self.material))
        print("Closing lid...")
        pickle_in.close()
        print("Enjoy the snack!")

    def data(self):
        return self.material
