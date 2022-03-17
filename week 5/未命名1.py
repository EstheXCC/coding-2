#!/usr/bin/env python
# coding: utf-8

# In[1]:



nums = '2222222222'

max = 0
max_index_1=0
max_index_2=0
result = 0
for symbol_index_1 in range(1,9):
    for symbol_index_2 in range(symbol_index_1+1,10):
        num1 = int(nums[0:symbol_index_1])
        num2 = int(nums[symbol_index_1:symbol_index_2])
        num3 = int(nums[symbol_index_2:10])
        result = num1*num2*num3
        print(' result=',result, 'symbol_index_1:',symbol_index_1,' symbol_index_2:',symbol_index_2)
        if result > max:
            max = result
            max_index_1 = symbol_index_1
            max_index_2 = symbol_index_2
print('max value:',' result=',result, 'symbol_index_1:',symbol_index_1,' symbol_index_2:',symbol_index_2)


# In[ ]:




