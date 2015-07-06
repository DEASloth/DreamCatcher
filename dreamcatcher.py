import urllib
import os


# Grabs images in sequence from the Psychin - VR - Lab web interface for Google's Deep Dream image processing software
# start is the index# you want to begin at
# stop is how many images starting from the start index you wish to grab i.e. if start = 50 and stop = 50 you will download images at indexs 50-100
def get_images(start, stop):
    counter = 0
    imgIndex = start
    for i in range(start, start+stop+1):
        urllib.urlretrieve("http://d11cbnttr0b724.cloudfront.net/img_dreamed/"+str(imgIndex)+".jpg", str(imgIndex)+".jpg")
        print("Image# "+str(counter)+" of "+str(stop)+" captured.")
        counter += 1
        imgIndex += 1
    print("Finished")


# checks to see if the subfolder "dreams" exists if not creates it
def change_folders():
    cur_folder = os.getcwd()
    if not os.path.exists(cur_folder+"/dreams/"):
         print("Dreams folder not found, Creating...")
         os.makedirs(cur_folder+"/dreams/")
         os.chdir(cur_folder+"/dreams/")
    else:
         os.chdir(cur_folder+"/dreams/")

# Displays Program name and version
# Asks user for starting index and how many images to download
def main():
    print("Deep Dream Catcher v.01-ALPHA\n")
    start = raw_input("What index to start at?:")
    stop  = raw_input("How many images to download?:")
    print("Catching Dreams...\n")
    change_folders()
    get_images(int(start), int(stop))


main()