# -*- coding: utf-8 -*- 
import json
from collections import defaultdict

#Read JSON file
with open('workshops.json',"r") as data_file:    
    workshops_list = json.load(data_file)
 
#Create counters
workshops_kids_num = defaultdict(int)
workshops_all_num = defaultdict(int)

print u'Всего мастерских - %d.'  % (len(workshops_list))

#Read data into integer dictionary
count = 0
while (count < len(workshops_list)):
	
	kids_allowed=workshops_list[count]['accepts_underage']
	if len(workshops_list[count]['dates']) == 1:
		workshop_cycles=workshops_list[count]['dates'][0]['cycle_n']
		workshops_all_num[workshop_cycles]+=1
		workshops_kids_num[workshop_cycles]+=1*int(kids_allowed)
	else:
		count_dates=0
		while (count_dates < len(workshops_list[count]['dates'])):
			workshop_cycles=workshops_list[count]['dates'][count_dates]['cycle_n']
			workshops_all_num[workshop_cycles]+=1
			workshops_kids_num[workshop_cycles]+=1*int(kids_allowed)
			count_dates = count_dates + 1			
	count = count + 1

#Print data
count_cycles=1
while count_cycles<len(workshops_all_num)+1:
	print u'Цикл %d: всего программ %d, из них школьных: %d.' % (count_cycles, workshops_all_num[count_cycles], workshops_kids_num[count_cycles])
	count_cycles = count_cycles + 1




