# python-apps
## single codes
	1. directory.py
		1. description
			- show directoryies and files in tree structure
			
		2. how to use
			- Just place in directory where you want to see its subdir structure, Execute with python(ver>=3)
				
		3. how it works
			- needs os, sys
			- class Directory
				- member : name, dir\_list, file\_list, temp_list
				- methods
					- \_\_init\_\_([name]) : if called, automatically get name and using os.listdir(), save file names to file\_list, directory names to dir\_list. For each dir\_list`s indexs, make Directory class recursively.
					- tree([depth=0]) : print dir structure
                    
        4. improvement plan
            1. Can use in any OS. current version works only in linux and Windows10. Encoding raises this problem. (win7 = cp949)
            2. 