import time

time1 = int(time.strftime('%H'))
nowtime = time.strftime('%H:%M:%S')


print('this is',nowtime)
if(time1<5):
    print("Good Moening Sir")
elif(time1<=12):
    print("This script was made to greet you at morning\nplease run in morning.")
else:
    if(time1<=24):
      print('This script was made to greet you at morning\nplease run in morning.')
    elif(time1<=0):
        print('Good morning Sir')