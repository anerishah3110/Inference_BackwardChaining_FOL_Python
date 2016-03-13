# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 11:19:52 2016

@author: Aneri
"""


import re
import collections
#import sys
#file=open(sys.argv[2])
file=open("C:\Users\Aneri\.spyder2\sample05.txt",'r')
data=file.readlines()
goal=data[0].strip('\n')
Num_clause=int(data[1])
#print goal
#print Num_clause
count=2
i=0
l=[]
c=0
temp_file=open("output.txt","w+")
pr=[]
#print data[count]
while (i<Num_clause):
#    print i
#    print count
#    print data[count]
    l.append(data[count])

    count=count+1
    i=i+1
#print l

O={}

d = collections.defaultdict(__builtins__.list)

for i in xrange(len(l)):
    s=l[i].strip('\n')
  #  print"s:"+ s
    
    if '=>' in s:
        k=s.split('=>')
        n= k[1].strip(' ')
        m= n.split('(')[0]
        d[m].append(s.strip('\n'))
        
        
        #hash[m]=s.strip('\n')
    else:
        #fact.append(s.strip('\n'))
        m=s.split('(')[0]
        d[m].append(s.strip('\n'))
        
        #hash[m]=s.strip('\n')
        
        
#print d
def isvariable(a):
     if( a[0].islower()):
        # print "var"
         if (islist(a)):
            # print "hi"
             return 0
         else:
             return 1
     else:
        return 0
     
     
def isconstant(a):
        if (a[0].isupper()):
            
            if'(' in a:
                return 0
            else:
                return 1
        else:
            return 0

def iscompound(a):
    if(a[0].isupper()):
        if '(' in a:
            return 1
        else :
            return 0
    else:
        return 0
        
        


def islist(a):
    if  isinstance(a,__builtins__.list):
        return 1
    else:
        return 0
        
def extend(O,v,b):
    print "in extend"
    print O
    OO=O.copy()
    OO[v]=b
    return OO


def unify_var(v,b,O):
    if v in O:
        return unify(O[v],b,O)
    else:
        return extend(O,v,b)
        
def unify(rhs,goal,O):
    if (O==None):
        return None
    elif(rhs==""):
        return O
    elif rhs==goal:
        return  O
    elif (isvariable(rhs)):
        return unify_var(rhs,goal,O)
    elif(isvariable(goal)):
        return unify_var(goal,rhs,O)
    elif(iscompound(rhs) and iscompound(goal)):
        print "compund"
        
        x=rhs.split('(')[1].split(')')[0].split(',')
        y=goal.split('(')[1].split(')')[0].split(',')
        xop=rhs.split('(')[0]
        yop=goal.split('(')[0]
        print x
        print y
        print xop
        print yop
        print unify(xop,yop,O)
        return unify(x,y,unify(xop,yop,O))
    elif(islist(rhs) and islist(goal)):
        print "list"
        x_first=rhs[0].strip(' ')
        print x_first
        y_first=goal[0].strip(' ')
        print y_first
        del rhs[0]
        print "hhhhh"
        print unify(x_first,y_first,O)
        del goal[0]
        return unify(rhs,goal,unify(x_first,y_first,O))

    else:
        return None

def Standard(r):
    global c
    c=c+1 
    print c

    all = re.findall(r"\([a-z]|,\s[a-z]",r)
    s=set(all)
    l=list(s)
    print l
    
    
    
    for i in l:
        
       if ',' in i:
           
           m=","+" "+i[2]+str(c)
           r=re.sub(i,m,r)

       else:
           
            p="\\"+i[0]+i[1]
            
           
            m="("+i[1]+str(c)
            
                
            r=re.sub(p,m,r)

    
   
    return r


def fetch_rules(d,goal):
    
    a=goal.split('(')[0]
    
    print a
    for k,v in d.items():
   #     print "k;"+k
        if(a==k):
            return d[a]

def subst(O,x):
    
    
    w=x.split('(')[1].split(')')[0].split(',')

        
    for i in w:
       i=i.strip(' ') 
       if i in O:
           
           print i
           n=O[i]
           print n
           x=re.sub(i,n,x)
           if n in O:
               m=O[n]
               print m
               x=re.sub(n,m,x)
               
           
              

   
    return x

  



def FOL_BC_OR(d,goal,O):
    
    print fetch_rules(d,goal)     

    for i in fetch_rules(d,goal):
        f=goal.split('(')[1].split(')')[0].split(',')
        temp=goal
        for j in f:
                j=j.strip(' ')
                if(isvariable(j)):
                    m="_"
                    temp=re.sub(j,m,temp)
                    

        
        #temp_file.write("Ask: %s\n" %temp)
       
        print "ask:"+temp
       
        print "i:"+i
        u=Standard(i)
        print "u:"+u
       # u="hate(y3,e3)=>love(e3,x3)"
        if '=>' in u:
          y=u.split('=>')
        
          lhs=y[0].strip(' ')
        
          rhs=y[1].strip(' ')
          print lhs
          print rhs
          temp_file.write("Ask: %s\n" %temp)
          pr.append(goal)
        else:
           lhs=""
           rhs=u
           
         
        
        O1 =  FOL_BC_AND(d,lhs,unify(rhs,goal,O))
        
        if(O1==None):
            continue
        else:
         print "mmmmmmm"
         print O1
         return O1

def FOL_BC_AND(d,goal,O):
    print O
    print "hii"
    print goal
    if (O==None):
        return None
    elif(len(goal)==0):
        print "0 len"
        print O
        return O
    else:
        if '&&' in goal:
            
             f=goal.split('&&')
             print f
            
             first=f[0].strip(' ')
             lenth=len(first)
             
             print "first:"+first
             rest=goal[lenth+4:]
            
             print rest
        else:  
             first=goal
             rest=""
        print "before subst"
        print O
        tempfirst=subst(O,first)
        print tempfirst
        O1 = FOL_BC_OR(d,tempfirst,O)
        if(O1==None):
                    print "False:"+tempfirst
                    temp_file.write("Ask: %s\n" %tempfirst)
                    temp_file.write("False: %s\n" %tempfirst)
                    return None
        else:
                    print O1
                    temp=subst(O1,tempfirst)
                    if(not cmp(O,O1)):
                         temp_file.write("Ask: %s\n"%temp)
                    else:
                             if tempfirst not in pr:
                                 f=tempfirst.split('(')[1].split(')')[0].split(',')
                                 temp1=tempfirst
                                 flag=0
                                 for j in f:
                                     j=j.strip(' ')
                                     if(isvariable(j)):
                                         flag=1
                                         m="_"
                                         temp1=re.sub(j,m,temp1)
                                 if(flag==1):
                                    temp_file.write("Ask: %s\n"%temp1)
                                
                    print "True:"+temp
                    print O1
                    temp_file.write("True: %s\n"%temp)
                    O2 = FOL_BC_AND(d,rest,O1)
                    return O2

#def my_generator(d,goal,O):
#    print("Inside my generator")
#    print "hii"
#    print "goal"+goal
#    if (O==-1):
#        print "Inside o=-1"
#        return None
#    return 'a'
#    
#                    
#print "helo"
#if(my_generator(d,goal,-1) == None):
#    print "none123"
#else:
#    for char in my_generator(d,goal,-1):
#        print(char)
O=FOL_BC_AND(d,goal,O)
if(O==None):
   print "false"
   temp_file.write("false")
else:
    print "True"
    temp_file.write("True")

print "after and"