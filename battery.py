b = int(input('目前電量多少?'))
battery = b
if battery > 80:
	print('玩玩手遊')
elif battery < 30:
	print('去充電吧')
else :
	print('看看小說算了')