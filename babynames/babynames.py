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
  f = open(filename, 'rU')
  #Pattern for year: Popularity in \d\d\d\d
  def find_year(f):
    year_match = re.search(r'Popularity in \d\d\d\d', f.read())
    if year_match==None:
      return 0
    year = re.search(r'\d\d\d\d', year_match.group())
    return year.group()
  
  year = find_year(f)
  #print year
  
  def find_names_and_ranks(f):
    dict = {}
    f.seek(0)
    names = re.findall(r'<td>([0-9]+)</td><td>\s*([a-zA-Z]+)\s*</td><td>\s*([a-zA-Z]+)\s*</td>', f.read())
    for row in names:
      #print row[0] + ' ' + row[1] + ' ' + row[2]
      if not row[1] in dict.keys():
        dict[row[1]] = int(row[0])
      else:
        if int(row[0])<dict[row[1]]:
          dict[row[1]] = int(row[0])
      
      if not row[2] in dict.keys():
        dict[row[2]] = int(row[0])
      else:
        if int(row[0])<dict[row[2]]:
          dict[row[2]] = int(row[0])
  
    return dict
  
  dict = find_names_and_ranks(f)
  #print dict
  
  my_list = []
  my_list.append(year)
  for name in sorted(dict.keys()):
    my_list.append(name +' '+str(dict[name]))
  f.close()
  #print my_list
  return my_list

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for file in args:
    name_list = extract_names(file)
    if not summary:
      print '\n'.join(name_list)
    else:
      summaryfile = file+'.summary'
      sf = open(summaryfile, 'w')
      names = '\n'.join(name_list)
      sf.write(names)
      sf.close()

if __name__ == '__main__':
  main()
