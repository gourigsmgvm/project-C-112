import shutil
import os
src = "C:/Users/gopui/Downloads"
dest_f = "C:/Users/gopui/Downloads/documentFiles"
filelist = os.listdir(src)


for filename in filelist:
    name, extension = os.path.splitext(filename)
    print(extension)



    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        src = "C:/Users/gopui/Downloads/" +filename

        dest = "C:/Users/gopui/Downloads/documentFiles/" + filename 

        shutil.move(src,dest)
            


