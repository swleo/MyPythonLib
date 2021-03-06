#!/usr/bin/python
#coding=utf8
"""
# Author: Bill
# Created Time : 2015年11月24日 星期二 01时22分05秒

# File Name: Progressbar.py
# Description:

"""
import sys
class Progressbar(object):
	def __init__(self,finalcount,block_char='.'):
		self.finalcount = finalcount
		self.blockcount = 0
		self.block_char = block_char

		# print information 
		self.f = sys.stdout
		if not self.finalcount:return
		self.f.write('\n------------------%Progress-----------------------\n')
		#self.f.write('    1    2    3    4    5    6    7    8    9    0\n')
		#self.f.write('----0----0----0----0----0----0----0----0----0----0\n')

	def progress(self,count):
		count = min(count,self.finalcount)
		if self.finalcount:
			# 返回浮点数x的四舍五入值
			percentcomplete = int(round(100.0*count/self.finalcount))
			if percentcomplete <1:percentcomplete =1
		else:
			percentcomplete=100

		# '/'是传统除法，'//'是浮点数除法，结果四舍五入
		blockcount = int(percentcomplete//2)

		# 保证下次输入的值比下次的值大
		if blockcount <= self.blockcount:
			return
		for i in range(self.blockcount,blockcount):
			self.f.write(self.block_char)
		self.f.flush( )
		self.blockcount = blockcount
		if percentcomplete == 100:
			self.f.write("\n")
	
if __name__ == "__main__":
	from time import sleep
	pb = Progressbar(8,"#")
	for count in range(1,9):
		pb.progress(count)
		sleep(0.2)


