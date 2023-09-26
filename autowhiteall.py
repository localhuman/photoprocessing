
# import required module
import os
# assign directory



directory = '/home/tom/Pictures/work_9_21_23/'
wb_output = '%sauto/' % directory 
sharp_output = '%ssharpened/' % directory
vivid_output = '%svivid/' % directory
final_output = '%sfinal/' % directory
final_output_resized = '%sresized/' % final_output




def autowhite(inputdir, outputdir, test=False):
    runcmd('./autowhite', inputdir, outputdir, test)

def autosharpedge(inputdir, outputdir, amount = 1.2, test=False):
    runcmd('./sharpedge -f %s' % amount, inputdir, outputdir, test)

def autosharp(inputdir, outputdir, test=False):
    runcmd('./sharp', inputdir, outputdir, test)

def autovivid(inputdir, outputdir, amount = 10,  test=False):
    runcmd('./vividize -a %s ' % amount, inputdir, outputdir, test)

def autovibrant(inputdir, outputdir, test=False):
    runcmd('./vibrance', inputdir, outputdir, test)

def smartcrop(w,h,inputdir,outputdir,test=False):
    runcmd('./smartcrop -w %s -h %s -m canny -s basic -g maximum -n equalize -b 20' % (w, h), inputdir, outputdir, test)

def downsize(inputdir,outputdir,size=2000, test=False):
    runcmd('./downsize -s %s -t 1 -S no' % size, inputdir, outputdir, test)

def runcmd(cmdtorun, inputdir, outputdir, test=False):

    for filename in os.listdir(inputdir):
        f = os.path.join(inputdir, filename)
        # checking if it is a file
        if os.path.isfile(f):
            command = "%s %s %s" % (cmdtorun, f, os.path.join(outputdir, filename))
            print("Command: %s " % command)
            if not test:
                os.system(command)        
                print("PRocessed file %s " % filename)
        #        print(filename)
    
    


def copyTo(inputdir, outputdir):
    os.system('cp -R %s* %s' % (inputdir, outputdir))
    print("Copied!")

def resizeTo(targetW, targetH, inputdir, outputdir, test=False):

    for filename in os.listdir(inputdir):
        f = os.path.join(inputdir, filename)
        # checking if it is a file
        if os.path.isfile(f):
            command = "convert %s -resize  %sx%s^ %s" % (f, targetW, targetH, os.path.join(outputdir, filename))
            print("Command: %s " % command)
            if not test:
                os.system(command)        
                print("PRocessed file %s " % filename)
        #        print(filename)
    

def cleanDirectories():
    try:
        os.system("rm -rf %s " % wb_output)
        os.system("rm -rf %s " % sharp_output)
        os.system("rm -rf %s " % vivid_output)
        os.system("rm -rf %s " % final_output)

    except Exception as e:
        print("Could not clean directories: %s " % e)
        pass    

def mkDirectories():
    try:
        os.mkdir(wb_output)
        os.mkdir(sharp_output)
        os.mkdir(vivid_output)
        os.mkdir(final_output)
        os.mkdir(final_output_resized)
    except Exception as e:
        print("Could mk directories: %s " % e)
        pass

def processImages():
    cleanDirectories()
    mkDirectories()

    autowhite(directory, wb_output)
    ##autosharpedge(wb_output, sharp_output)
    autovibrant(wb_output, vivid_output)    
    copyTo(vivid_output, final_output)
    downsize(final_output, final_output_resized)
    #resizeTo(2400, 1600, final_output, final_output_resized, False)


#cropdir = "%scropped" % final_output_resized
#os.mkdir(cropdir)
#smartcrop(1600, 1600, final_output_resized, cropdir)

#a = '/home/tom/Pictures/work_09_23/final/good'
#b = '%s/resized' % a
#os.mkdir(b)

#downsize(a, b, 2000)
processImages()
