import mymodule

mymodule.sayhi()
print 'Version',mymodule.version



from mymodule import sayhi,version
# Alternative:
#from mymodule import*

sayhi()
print 'Version',version
