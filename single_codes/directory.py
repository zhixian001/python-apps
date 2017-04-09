
# coding: utf-8


from os import getcwd, chdir, listdir
from platform import system

ident_char = "/"
if system() == 'Windows':
    ident_char = "\\"

class Directory:
    def __init__(self, _name = getcwd().split(ident_char)[-1]):
        #_name의 default값이 있더라도 recursive할때는 실행이 되지 않는 것 같다.
        self.name = _name
        self.dir_list = []
        self.file_list = []
        self.temp_list = listdir()

        #예외가 throws되지 않도록 해야 한다!

        while True:
            if len(self.temp_list) != 0:
                try:
                    chdir(self.temp_list[0])
                except NotADirectoryError :
                    self.file_list.append(self.temp_list[0])
                    del self.temp_list[0]
                except FileNotFoundError :
                    #self.file_list.append(self.temp_list[0])
                    del self.temp_list[0]
                except PermissionError :
                    #self.file_list.append(self.temp_list[0] + "[NO Permission to Excess!!]")
                    del self.temp_list[0]
                else:
                    self.dir_list.append(self.temp_list[0])
                    self.dir_list[-1] = Directory(getcwd().split(ident_char)[-1])
                    del self.temp_list[0]
                    chdir("..")
            else:
                break

    def __str__(self):
        return self.name

    def tree(self, depth = 0):
        result = self.name + "\n"
        for i in self.dir_list:
            for dp in range(depth):
                result += "│"
            result += "├★ " + i.tree(depth+1)
        for j in self.file_list:
            for dp in range(depth):
                result += "│"
            result += "├" + j + "\n"
        for dp in range(depth):
                result += "│"
        result += "┘\n"

        return result
    
if __name__ == "__main__":
    a = Directory()
    print(a.tree())
    input("\n\n\npress ENTER key to end program...")
