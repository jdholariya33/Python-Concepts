# File Modes : - 
""" (IMP)
        r   :-  open for reading (Default)          --> No Truncate
        w   :-  open for writing                    --> Truncate
        x   :-  Create a new file and open it 
                for writing                         --> No Truncate
        a   :-  open for writing, appending to
                the end of the file if it exists    --> No Truncate
        b   :-  Binary mode
        t   :-  text mode (Default)
        r+  :-  read + overwrite (Pointer : start)  --> No Truncate 
        w+  :-  read + overwrite (Empty File)       --> Truncate
        a+  :-  read + append    (Pointer : End)    --> No Truncate

"""
