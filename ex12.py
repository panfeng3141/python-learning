#pydoc 帮助查看命令，例如,在命令行输入pydoc raw_input
#raw_input(提示内容)
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
