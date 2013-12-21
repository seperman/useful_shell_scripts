# -*- coding: utf-8 -*-

"""
This will copy anything modified or new from git_status output and put them in a backup folder
"""

from git_backup_new_stuff_settings import git_status_path, destination_path, stuff_to_copy, source_path

import codecs
import os
from shutil import copy2

RED=chr(27)+'[31m'
DEFAULT=chr(27)+'[39m'

fileObj = codecs.open(git_status_path, "r", "utf-8" )

#my_file = open(git_status_path)
my_lines = fileObj.readlines()

print "copying from %s to %s" % (source_path, destination_path)
for line in my_lines:
    for stuff in stuff_to_copy: 
        if line.startswith(stuff):
            the_file = os.path.join(source_path, line.split(stuff)[1][:-1])
            print "copying %s" % the_file 
            #print 
            try:
                copy2(the_file,destination_path)
            except IOError as e:
                print RED + 'Exception error is: %s' % e + DEFAULT




