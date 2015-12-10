#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request
import functools

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  # re_str = "((?:(?:[\/][^\/^\s]+)+\w)(\.jpg))"
  re_str = "GET (.+) HTTP"
  try:
    log = open(filename)
  except:
    print("Log not found")
    return

  l = []
  url = re.search("_(.+)", filename)
  url_head = "http://" + url.group(1)
  for line in log:
    if line.find('images/puzzle') != -1:
      l.append(url_head + re.search(re_str, line).group(1))

  l = list(set(l))
  
  #handling Part C solution
  image_name = l[0][l[0].rfind('/') + 1:]
  if image_name.count('-') > 1:
    def compa(a,b):
      a_obj = re.search("-\w+-(\w+).jpg", a)
      b_obj = re.search("-\w+-(\w+).jpg", b)
      if a_obj.group(1) > b_obj.group(1):
        return 1
      return -1

    c_sort = sorted(l, key = functools.cmp_to_key(compa))
    return c_sort
  else:
    l.sort()
  return l
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  try:
    os.mkdir(dest_dir)
  except:
    print("mkdir failed")

  html = open(dest_dir + "/page.html", 'w')
  html.write('<html>\n<body>\n')

  count = 0
  for url in img_urls:
    print("saving " + url)
    pic_loc, headers = urllib.request.urlretrieve(url, 
      filename = (dest_dir + "/img" + str(count)))
    html.write("<img src=\"img" + str(count) + "\">")
    count += 1

  html.write('\n</html>\n</body>')
  html.close()
  return
  

def main(args):
  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  #args = sys.argv[1:]
  args = ['--todir', 'imgs', 'place_code.google.com']
  main(args)
