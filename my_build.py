def create_file(filename):

    f = open(filename, "w")
    string = "this is test\n"
    f.write(string)
    f.close()

create_file("try_jenkins.txt")
