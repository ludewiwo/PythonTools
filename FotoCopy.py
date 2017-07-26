import sys
import os
import exifread
from shutil import copyfile

source_path='C:\\Users\\wolfg\\Pictures\\2014-09'
#source_path='C:\\Users\\wolfg\\Pictures'
dest_path='C:\\Users\\wolfg\\TMP\\'

def read_exif_created(picture_name):
    """
       extract exif metadata from picture
    """
    # Open image file for reading (binary mode)
    f = open(picture_name, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)

    infos ={}
    original =''
    digitized=''

    # move data into dict
    for tag in tags.keys():
        infos[tag]=tags[tag]
    try: ## read exif data
        original=str(infos['EXIF DateTimeOriginal'])
        digitized=str(infos['EXIF DateTimeDigitized'])
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
    
    if len(original)>=18:
        return original
    if len(digitized)>=18:
        return digitized
    else: ## if no exif data found
        return 'unknown'
        
def get_exif_year(exif_date):
    """
       extract year value from creation date
    """
    return exif_date[0:4]

def get_exif_month(exif_date):
    """
       extract month value from creation date
    """
    return exif_date[5:7]

processed_counter=0
ignored_counter=0

## find files with filter
for path, subdirs, files in os.walk(source_path):
    for name in files:
        if name.endswith(('.jpg', '.jpeg', '.gif', '.JPG', '.JPEG')):
            processed_counter+=1
            ## extract metadata create date
            created=read_exif_created(os.path.join(path, name))
            year=get_exif_year(created)
            month=get_exif_month(created)
            ## source file for copy
            old_filename=os.path.join(path, name)
            ## dest file for copy
            dest=os.path.join(dest_path,year,month)            
            new_filename=os.path.join(dest,name)
            ## log message
            print (old_filename,new_filename)
            ## directory create if needed
            if not os.path.exists(dest):
                os.makedirs(dest)
            ## file copy
            copyfile(old_filename,new_filename)
        else:
            print ( 'file ignored:',name)
            ignored_counter+=1
            
## summary output
print('Files  copied:',processed_counter)
print('Files ignored:',ignored_counter)

