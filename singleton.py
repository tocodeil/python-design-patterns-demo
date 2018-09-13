# init the object and write a function to use it
# (logging)

# change the creation mechanism of the object
# (override new)
from configuration import Configuration

# e = Configuration()


c = Configuration.getinstance()
c.loglevel = 5

print(c.loglevel)

d = Configuration.getinstance()
# print 5
print(d.loglevel)

    