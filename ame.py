import os
list=os.listdir()
for i in list:
    os.replace(i, i[3:].lower().replace(' ', '_'))
