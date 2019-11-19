# -*- coding: utf-8 -*-

'''
Created on 2019.11.19
@author: BMA

this is a script to modify txt file, including replace one word and 
delete some column. Notice that if we give 1 to the delete column,it means 
printing first column, 2 means printing first and second columns, etc. 
'''
file_path = '10-1.txt' # change file name
with open(file_path) as file_object:
	lines = file_object.readlines()
contexts = ''
for line in lines:
	contexts += line
class Txt():
	#this is a class for modify txt file
	def __init__(self,word):
		#initialize
		self.word = word
	def change_one_word(self):
		#this is a function to replace the word
		return contexts.replace('python',self.word)
	def delete_some_column(self,column):
		#this is a function to remove some column
		column_list = [ i.strip().split(' ')[:column] for i in lines ]
		column_out = '\n'.join([' '.join(i) for i in column_list])
		return column_out

new_file = Txt('c')
#print(new_file.change_one_word())
file_out = new_file.delete_some_column(3)
with open('output.txt','w') as f:
	f.write(file_out)