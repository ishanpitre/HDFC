import os
#To Copy The File
def copyFile(sdir,ddir,filename):
    try:
        fp = open(f'{sdir}/{filename}')
        data = fp.read()
        fp.close()
        moveFile(ddir,filename,data)
        return True
    except Exception as e:
        print(e)


#To move File
def moveFile(ddir,filename,data):
    try:    
        with open(f"{ddir}/{filename}","w") as fp:
            fp.write(data)
            return True
    except Exception as e:
        print(e)


# to remove files from source folder
def deleteFile(sdir, filename):
    try:
        os.remove("{}/{}".format(sdir,filename))
    except Exception as e:
        print(e)
    return True

def main():
    try:
        sdir = 'source'
        files = [file for file in os.listdir(sdir)]
        for i in files:
            ddir = 'processed dir'
            status = copyFile(sdir,ddir,i)
            if(i.endswith(".csv")):
                ddir = 'csv'
            elif(i.endswith(".pdf")):
                ddir = 'pdf'
            elif(i.endswith(".txt")):
                ddir = 'text File' 
            status = copyFile(sdir,ddir,i)
            deleteFile(sdir,i)   
        if status:
            print("Files Operation is completed")
        else:
            print("Something went wrong")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main() 