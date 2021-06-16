#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket as s
import cv2
import pickle
import struct


# In[2]:


server_s = s.socket(s.AF_INET,s.SOCK_STREAM)
host_name  = s.gethostname()
host_ip = s.gethostbyname(host_name)
print('Host IP:',host_ip)


# In[3]:


port = 2204
s_address = ('192.168.0.107',port)
print("Socket Created Successfully")


# In[4]:


server_s.bind(s_address)
print("Socket Bind Successfully")


# In[5]:


server_s.listen(5)
print("Listening at:",s_address)


# In[ ]:


while True:
    client_s,addr = server_s.accept()
    print('GOT CONNECTION FROM:',addr)
    vid = cv2.VideoCapture(0)
    while(vid.isOpened()):
        img,frame = vid.read()
        a = pickle.dumps(frame)
        message = struct.pack("Q",len(a))+a
        client_s.sendall(message)   
        cv2.imshow('Server Video',frame)
        if cv2.waitKey(10)== 13:
            break
client_s.close()
vid.release() 
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




