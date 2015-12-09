#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  names_and_ranks = []

  f = open(filename)
  while True:
    readed = f.readline()
    if readed == "": break
    finds = re.search(r"<td>(\w+)</td><td>(\w+)</td><td>(\w+)", readed)
    try:
      names_and_ranks.append(finds.group(2) + " " + str(finds.group(1)))
      names_and_ranks.append(finds.group(3) + " " + str(finds.group(1)))
    except:
      pass
    if finds != None: 
      continue

    year_match = re.search(r"<h3 align=\"center\">Popularity in (\d+)</h3>", 
      readed)
    if year_match != None:
      year = year_match.group(1)

  f.close()
  names_and_ranks.sort()
  return [year] + names_and_ranks

def main(args):
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for record in args:
    data = extract_names(record)

    if summary == False:
      print(str(data))
      continue

    out_file = open(record + ".data", "w")
    for line in data:
      out_file.write(str(line) + "\n")
    out_file.close()

  return
  
if __name__ == '__main__':
  #args = sys.argv[1:]
  #quick conversion so I can simulate inputs from cli
  args = ['--summaryfile', 'baby1990.html', 'baby2000.html' ]
  main(args)
