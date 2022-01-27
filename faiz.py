import os,sys,time

def mengetik(c):
  c = c + '\n'
  for x in c:
    time.sleep(0.1)
    print(x, end='', flush=True)
 
# eksekusi sample
mengetik("Aku sayang kamu")
