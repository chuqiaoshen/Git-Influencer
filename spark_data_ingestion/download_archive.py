#this is the python script for generating download links hourly from github archive open datasets
#the output file

import os
from datetime import datetime

#saved folder
saved_directory = '/home/ubuntu/download_archive/'

if __name__ == "__main__":
#generate the
    current_time = datetime.now()
    #make current download url
    current_url = "http://data.gharchive.org/{}-{}-{}-{}.json.gz".format(current_time.year,current_time.strftime('%m'),current_time.day,(current_time.hour-1))

    try:
        os.system('wget {} -P {}'.format(current_url,saved_directory))
        print('downloaded data from {} to {}'.format(current_url,saved_directory))

    except:
        print('Data not available {}'.format(current_url))
