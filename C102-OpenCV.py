import cv2
import dropbox
import random
import time

startTime = time.time()

def takeSnapshot():

    number = random.randint(0,100)
    
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = videoCaptureObject.read()

        imageName = "pic" + str(number) + ".jpg"

        cv2.imwrite(imageName, frame)

        startTime = time.time()

        result = False


    return imageName

    print("Image Captured, now get out")

    videoCaptureObject.release()

    cv2.destroyAllWindows()


def uploadDbx(imageName):
    access_token = "29ex7SstAzgAAAAAAAAAASERgGzDdX_lwyNwPn-dPkGsg_zA0i9gHDhYb-tKx_Ox"

    file_from = imageName
    file_to = "/somethingC102/" + imageName

    dbx = dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")


def main():
    while(True):
        if((time.time() - startTime) >= 5):
            name = takeSnapshot()
            uploadDbx(name)


main()

    
    
