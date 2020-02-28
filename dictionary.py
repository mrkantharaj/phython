d={1:'kantharaja',2:'shivaraja',3:'ningappa',4:'lakshmamma'}
print(d)
print(d[3])    # print only value of key 3
print(d.get(1))
print(d.get(5,'not found'))   # 5 key not found so it prints the msg
keys=['kantharaj','shivaraj','ningappa']
values=[7259776307,8050680237,9964592859]
s= dict(zip(keys,values))
print(s)
s['amma']='08282242727'
print(s)
del s['amma']
print(s)