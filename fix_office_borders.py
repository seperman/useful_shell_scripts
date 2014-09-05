#!/usr/bin/env python

from bs4 import BeautifulSoup

import sys
from os import getcwd
from os.path import isfile, exists as fexists, join as fjoin



def remove_office_duplicates(file_path):

    current_folder = getcwd()

    if not ("/" in file_path or "\\" in file_path):
        file_path = fjoin(current_folder, file_path)

    if not fexists(file_path) or not isfile(file_path):
        print "File does not exist: %s" % file_path
        return False

    print "\nFixing: %s" % file_path


    with open(file_path, 'r+') as the_f:
        data = the_f.read()
        soup = BeautifulSoup(data, "lxml")

        divs_list = soup.find_all('div')

        # import ipdb
        # ipdb.set_trace()

        duplicate_total_num = 0

        prev_div = None

        for div in divs_list:
            # print len(div.contents)
            try:
                if prev_div['style'] == div['style']:
                    prev_div.replace_with(div)
                    duplicate_total_num+=1
                    
                # print div['style']
            except (KeyError, TypeError):
                pass

            prev_div=div

        
        if duplicate_total_num:
            print "%s duplicate borders are removed" % duplicate_total_num

            the_f.seek(0)
            the_f.write(str(soup))
            the_f.truncate()

        else:
            print "No duplicate borders were found."





if __name__=="__main__":
    args = sys.argv
    del args[0]
    args_len = len(args)
    # print args_len
    if not args_len:
        print "This tool will cleanup Microsoft Office Word Duplicate Borders in HTML saving bug.\nYou need to type the name of the file to be cleaned."
    else:
        for f in args:
            remove_office_duplicates(f)
