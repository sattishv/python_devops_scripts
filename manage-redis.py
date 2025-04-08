#!/usr/bin/python3

# Deploy and manage Redis database server using python script

print('This is my first use-case driven python script')
import os
import sys
import subprocess 

# Only allows Sudoer or root user to execute this script.
print(os.geteuid())
if os.geteuid()==0:
  print('Allow execution of the script.')
else:
  print('You are not the root user or Sudoer.')
  sys.exit(1)
# defining global variables
packages = ['redis-server','redis-tools']  

# define functions

# install redis database server
def install_redis():
  print('Installing redis database server and tools ..')
  for package in packages
    print('Installing '+package+' ...')

# Start redis server
def start_redis():
  print('Starting redis database server')

# Stop redis server
def stop_redis():
  print('Stopping redis database server')

# Calling functions using CLI controller
if sys.argv[1]=='install':
  install_redis()
elif sys.argv[1]=='start':
  start_redis()
elif sys.argv[1]=='stop':
  stop_redis()
else:
  print('Script usage: sudo ./manage_redis.py install start stop')

