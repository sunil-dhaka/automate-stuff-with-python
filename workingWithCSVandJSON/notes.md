## csvs
- As always, whenever you write a program that modifies files, be sure to back up the
files, first just in case your program does not work the way you expect it to. You don’t
want to accidentally erase your original files.

- CSV files are simple, lacking many of the features of an Excel spread-
sheet. For example, CSV files
    - Don’t have types for their values—everything is a string
    - Don’t have settings for font size or color
    - Don’t have multiple worksheets
    - Can’t specify cell widths and heights
    - Can’t have merged cells
    - Can’t have images or charts embedded in them

- why we need CSV module to read?
    - But not every comma in a CSV file represents the boundary
between two cells. CSV files also have their own set of escape characters to
allow commas and other characters to be included as part of the values. 

**The delimiter and lineterminator Keyword Arguments**
Say you want to separate cells with a tab character instead of a comma and
you want the rows to be double-spaced. 

- delimiter: seperater in a row
- lineterminator: seperater of rows

- Passing delimeter='\t' and lineterminator='\n\n' u changes the charac-
ter between cells to a tab and the character between rows to two newlines.

## jsons
-  You’ll have to find documentation for what URLs your program
needs to request in order to get the data you want, as well as the general
format of the JSON data structures that are returned. This documenta-
tion should be provided by whatever site is offering the API; if they have
a “Developers” page, look for the documentation there.
Using APIs, you could write programs that do the following:
    - Scrape raw data from websites. (Accessing APIs is often more convenient
than downloading web pages and parsing HTML with Beautiful Soup.)
    - Automatically download new posts from one of your social network
accounts and post them to another account. For example, you could
take your Tumblr posts and post them to Facebook.
    - Create a “movie encyclopedia” for your personal movie collection by
pulling data from IMDb, Rotten Tomatoes, and Wikipedia and putting
it into a single text file on your computer.


- To translate a string containing JSON data into a Python value, pass it to
the `json.loads()` function. (The name means “load string,” not “loads.”)
-  Note that JSON strings always use double quotes. It
will return that data as a Python dictionary. Python dictionaries are not
ordered, so the key-value pairs may appear in a different order when you
print jsonDataAsPythonValue.
- The json.dumps() function (which means “dump string,” not “dumps”) will
translate a Python value into a string of JSON-formatted data.
