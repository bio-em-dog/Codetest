import random
seed = "01"
gambler=0
for i in range(1000):
	money=1
	while True:
		k=random.choice(seed)
		if k=='0':
			gambler-=money
			money=money*2
		else:
			gambler+=money
			break
print gambler
