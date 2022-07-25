s= int (input ('введите количество секунд:'))
print ('вы ввели ', s, 'секунд')
d = s / 86400
print (round (d,3),'суток')
h = s / 3600
print (round (h,3),'часов')
m = s / 60
print (round (m,3),'минут')
print (s,'секунд')
print ('ответ',round (d,3),'суток',':',round (h,3),'часов'':',round (m,3),'минут'':',s,'секунд')
