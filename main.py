import threading 
from threading import*
import time

key_data={} 

def create(key,value,timeout=0):
    if key in key_data:
        print("error: key exists") 
    else:
        if(key.isalpha()):
            if len(key_data)<(1073741824) and value<=(16777216):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    key_data[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalid key_name!!")

            
def read(key):
    if key not in key_data:
        print("error: key does not exist") 
    else:
        b=key_data[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri


def delete(key):
    if key not in key_data:
        print("error: given key does not exist") 
    else:
        b=key_data[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del key_data[key]
                print("successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            del key_data[key]
            print("successfully deleted")


def modify(key,value):
    b=key_data[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in key_data:
                print("error: given key does not exist") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                key_data[key]=l
        else:
            print("error: time-to-live of",key,"has expired") 
    else:
        if key not in key_data:
            print("error: given key does not exist") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            key_data[key]=l
