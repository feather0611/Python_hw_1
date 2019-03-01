s1,s2,s3,s4,s5=data.replace('=',':').replace(',',':').replace(' ','').replace('::',':').split(':')
avg = (int(s1)+int(s2)+int(s3)+int(s4)+int(s5))/5
print(avg)
