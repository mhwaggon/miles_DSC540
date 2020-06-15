#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import statistics
import re
from collections import Counter


# In[2]:


df = pd.read_excel('world-population.xlsm')


# In[18]:


# create a list and fill it with 25 random integers between 1 and 100.
number_list = [random.randint(1,100) for x in range(25)]

#iterate through printing our list numbers
for x in number_list:
    print(x)
    
# sorting our list from low to high
number_list = sorted(number_list)

#printing our list
print(number_list)


# In[4]:


df.head()


# In[7]:


#line plot of the dataframe
df.plot(kind='line', x='Year', y='Population')
plt.show


# In[26]:


######################### ACTIVITY 1 #####################################################################################################################

#create a list of 100 random numbers
random_nums = [random.randint(1,100) for x in range(100)]

# list using previous list with numbers that are div by 3
random_nums_3 = [x for x in random_nums if x%3==0]

# difference of two list lengths
list_diff = len(random_nums) - len(random_nums_3)



diff_vals = []

#for loop
for x in range(3):
    #random int list
    random_nums = [random.randint(1,100) for x in range(100)]
    #divisible by 3
    random_nums_3 = [x for x in random_nums if x%3==0]
    #differencve
    list_diff = len(random_nums) - len(random_nums_3)
    #adding them to list
    diff_vals.append(list_diff)

#calc mean of our differences    
statistics.mean(diff_vals)    


# In[38]:


######################### ACTIVITY 2 #####################################################################################################################
#Pride and Predjudice text
multiline_text = """It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.

However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters.

"My dear Mr. Bennet," said his lady to him one day, "have you heard that Netherfield Park is let at last?"

Mr. Bennet replied that he had not.

"But it is," returned she; "for Mrs. Long has just been here, and she told me all about it."

Mr. Bennet made no answer.

"Do you not want to know who has taken it?" cried his wife impatiently.

"You want to tell me, and I have no objection to hearing it."

This was invitation enough.

"Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week."

"What is his name?"

"Bingley."

"Is he married or single?"

"Oh! Single, my dear, to be sure! A single man of large fortune; four or five thousand a year. What a fine thing for our girls!"

"How so? How can it affect them?"

"My dear Mr. Bennet," replied his wife, "how can you be so tiresome! You must know that I am thinking of his marrying one of them."

"Is that his design in settling here?"

"Design! Nonsense, how can you talk so! But it is very likely that he may fall in love with one of them, and therefore you must visit him as soon as he comes."

"I see no occasion for that. You and the girls may go, or you may send them by themselves, which perhaps will be still better, for as you are as handsome as any of them, Mr. Bingley may like you the best of the party."

"My dear, you flatter me. I certainly have had my share of beauty, but I do not pretend to be anything extraordinary now. When a woman has five grown-up daughters, she ought to give over thinking of her own beauty."

"In such cases, a woman has not often much beauty to think of."

"But, my dear, you must indeed go and see Mr. Bingley when he comes into the neighbourhood."

"It is more than I engage for, I assure you."

"But consider your daughters. Only think what an establishment it would be for one of them. Sir William and Lady Lucas are determined to go, merely on that account, for in general, you know, they visit no newcomers. Indeed you must go, for it will be impossible for us to visit him if you do not."

"You are over-scrupulous, surely. I dare say Mr. Bingley will be very glad to see you; and I will send a few lines by you to assure him of my hearty consent to his marrying whichever he chooses of the girls; though I must throw in a good word for my little Lizzy."

"I desire you will do no such thing. Lizzy is not a bit better than the others; and I am sure she is not half so handsome as Jane, nor half so good-humoured as Lydia. But you are always giving her the preference."

"They have none of them much to recommend them," replied he; "they are all silly and ignorant like other girls; but Lizzy has something more of quickness than her sisters."

"Mr. Bennet, how can you abuse your own children in such a way? You take delight in vexing me. You have no compassion for my poor nerves."

"You mistake me, my dear. I have a high respect for your nerves. They are my old friends. I have heard you mention them with consideration these last twenty years at least."

"Ah, you do not know what I suffer."

"But I hope you will get over it, and live to see many young men of four thousand a year come into the neighbourhood."

"It will be no use to us, if twenty such should come, since you will not visit them."

"Depend upon it, my dear, that when there are twenty, I will visit them all."

Mr. Bennet was so odd a mixture of quick parts, sarcastic humour, reserve, and caprice, that the experience of three-and-twenty years had been insufficient to make his wife understand his character. Her mind was less difficult to develop. She was a woman of mean understanding, little information, and uncertain temper. When she was discontented, she fancied herself nervous. The business of her life was to get her daughters married; its solace was visiting and news. """

#find type
type(multiline_text)
#find len
len(multiline_text)


# In[39]:


#replacing characters 
multiline_text = multiline_text.replace('\n', "")
#regex to clean up text block
multiline_text = re.sub('\W+',' ', multiline_text)
print(multiline_text)


# In[40]:


#make a list of each word
word_list = multiline_text.split()


# In[41]:


print(word_list)


# In[42]:


len(word_list)


# In[49]:


#create unique word list
# make all lower case
word_list = [x.lower() for x in word_list]
#turning it into a set to remove duplicates then back to a list
word_list_nodupe = list(set(word_list))


# In[51]:


len(word_list_nodupe)


# In[54]:


#count word frequency
word_freq = Counter(word_list)


# In[56]:


#get our most common words
word_freq.most_common(25)


# In[57]:


######################### ACTIVITY 3 #####################################################################################################################
from itertools import permutations, dropwhile


# In[59]:


#get perm def + info
get_ipython().run_line_magic('pinfo', 'permutations')


# In[61]:


#dropwhile def + info
get_ipython().run_line_magic('pinfo', 'dropwhile')


# In[65]:


# interating through our permutations in range 3 and printing them
for nums in permutations(range(3)):
    print(nums)


# In[67]:


#dropping leading 0
for nums in permutations(range(3)):
    permu_list = list(dropwhile(lambda x: x<=0, nums))
    print(permu_list)
    


# In[97]:


# same as before getting our list
for nums in permutations(range(3)):
    permu_list = list(dropwhile(lambda x: x<=0, nums))
    #turning our list into strings
    z = [str(i) for i in permu_list]
    #splitting the list together and turning it back into an int
    num = int(''.join(z))
    print(num)
    
        
    


# In[106]:


######################### ACTIVITY 4 #####################################################################################################################
from itertools import zip_longest

#create function
def csv_header(header, line):
    #zip
    line_zipper = zip_longest(header, line, fillvalue=None)
    final_dict = {z[0]: z[1] for z in line_zipper}
    return final_dict


# In[110]:


#open our file sales_record
with open("sales_record.csv", "r") as sales:
    #read first line
    first = sales.readline()
    header = first.replace("\n", "").split(",")
    for x, y in enumerate(sales):
        y = y.replace("\n", "").split(",")
        final_dict = csv_header(header, y)
        print(final_dict)

