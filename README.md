# tkinter

## Overall Purpose:
This is an example of taking Python data analytics and packaging them into a simple application so that an end user with no knowledge of programming can run it on demand.  Otherwise, the Python code is typically scheduled to run or else run by a data analyst.  In this case, the code will clean up files with *.TMP (Windows sometimes creates these as backup files for MS Office and then not delete them).  It moves the files to a designated folder, like an archive folder, just in case you need them (since they are MS Office backup).

## Useful Code Aspects:
<ul>
   <li>Tkinkter is a simple application library that comes with the Python standard library.  It is not at all fancy, but more than sufficient for packaging a simple script.</li>
   <li>The script uses the os.walk library to recursively go through subfolders to find *.TMP files and then move them.</li>
</ul>

## Notes:
At my work, I have created Windows applications using .NET and Windows Forms, which can be useful. Also, there are various other frameworks available for application development in Python.  But for a simple applicaiton that is used to just package a Python script, Tkinter can do the job.  You will need an installer program such as Pyinstaller to do this, but it is a fairly simple process.
