# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:34:08 2021

@author: Manoj
"""

STAFFS=["YUVAN","ANTONY","HARRIS"]
fristweek=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
secondweek=["Monday","Tuesday","Wednesday","Thursday","Friday"]
week=1
m=0                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
while( week<=4):
    if(week%2==1):
        for a in fristweek:
            print(STAFFS[m],'=',a,)
            m=m+1
            if(m==3):
                m=0
    else:
        for j in secondweek:
            print(STAFFS[m],'=',j)
            m=m+1
            if(m==3):
                m=0
    week=week+1
      
    