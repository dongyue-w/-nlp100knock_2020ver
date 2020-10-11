#!/usr/bin/env python
# coding: utf-8

# Chapter 2
# The file popular-names.txt stores names of babies born in US with their genders, numbers of births, and years of births in tab-separated format. Create a program with the specifications below. Run the program with popular-names.txt as an input. Furthermore, confirm that the same (similar) result can be obtained by running a UNIX command.

# Commands to be used: wc, tr, cut, paste, head, tail, split, sort, uniq

# 10. Line count
# Count the number of lines of the file. 
# Confirm the result by using wc command.

# In[82]:


with open('/Users/wdy940211/Desktop/popular-names.txt', 'r') as f:
    for count, line in enumerate(f):
        count += 1
print(count)


# In[11]:


# Unix

get_ipython().system('wc -l /Users/wdy940211/Desktop/popular-names.txt')


# 11. Replace tabs into spaces
# Replace every occurrence of a tab character into a space. 
# Confirm the result by using sed, tr, or expand command.

# In[90]:


with open('/Users/wdy940211/Desktop/popular-names.txt', 'r') as f, open('/Users/wdy940211/Desktop/popular-names_python.txt', 'w') as f_new:
    for line in f:
        line = line.replace('\t', ' ')
        f_new.write(line)


# In[91]:


# Unix

get_ipython().system("tr '\\t' ' ' < '/Users/wdy940211/Desktop/popular-names.txt' > '/Users/wdy940211/Desktop/popular-names_unix.txt'")


# 12. col1.txt from the first column, col2.txt from the second column
# Extract the value of the first column of each line, and store the output into col1.txt. 
# Extract the value of the second column of each line, and store the output into col2.txt. 
# Confirm the result by using cut command.

# In[98]:


with open('/Users/wdy940211/Desktop/popular-names.txt', 'r') as f, open('/Users/wdy940211/Desktop/col1_python.txt', 'w') as f_col1, open('/Users/wdy940211/Desktop/col2_python.txt', 'w') as f_col2:
    for line in f:
        l = line.split('\t')
        f_col1.write('%s\n' % l[0])
        f_col2.write('%s\n' % l[1])


# In[244]:


# Unix

get_ipython().system("cut -f 1 < '/Users/wdy940211/Desktop/popular-names.txt' > '/Users/wdy940211/Desktop/col1_unix.txt'")
get_ipython().system("cut -f 2 < '/Users/wdy940211/Desktop/popular-names.txt' > '/Users/wdy940211/Desktop/col2_unix.txt'")


# 13. Merging col1.txt and col2.txt
# Join the contents of col1.txt and col2.txt, and create a text file whose each line contains the values of the first and second columns (separated by tab character) of the original file. 
# Confirm the result by using paste command.

# In[117]:


import pandas as pd

df1 = pd.read_csv('/Users/wdy940211/Desktop/col1_python.txt')
df2 = pd.read_csv('/Users/wdy940211/Desktop/col2_python.txt')
df = pd.concat([df1, df2], axis=1)
df.to_csv('/Users/wdy940211/Desktop/merge_python.txt', sep='\t', index=False)


# In[118]:


# Unix

get_ipython().system("paste '/Users/wdy940211/Desktop/col1_python.txt' '/Users/wdy940211/Desktop/col2_python.txt' > '/Users/wdy940211/Desktop/merge_unix.txt'")


# 14. First N lines
# Receive a natural number $N$ from a command-line argument, and output the first $N$ lines of the file. 
# Confirm the result by using head command.

# In[127]:


with open('/Users/wdy940211/Desktop/popular-names.txt', 'r') as f:
    for i in range(10):
        line = next(f).strip()
        print(line)


# In[41]:


# Unix

get_ipython().system("head -n 10 '/Users/wdy940211/Desktop/popular-names.txt'")


# 15. Last N lines
# Receive a natural number $N$ from a command-line argument, and output the last $N$ lines of the file. 
# Confirm the result by using tail command.

# In[141]:


with open('/Users/wdy940211/Desktop/popular-names.txt', 'r') as f:
    f = f.readlines()[-10:]
print(f)


# In[245]:


import pandas as pd

df = pd.read_csv('/Users/wdy940211/Desktop/popular-names.txt', sep='\t', header=None)
df.tail(10).to_csv('/Users/wdy940211/Desktop/last_10lines_python.txt', sep='\t', header=False, index=False)


# In[42]:


# Unix

get_ipython().system("tail -n 10 '/Users/wdy940211/Desktop/popular-names.txt'")


# 16. Split a file into N pieces
# Receive a natural number $N$ from a command-line argument, and split the input file into $N$ pieces at line boundaries. Confirm the result by using split command.

# In[252]:


n = 5
no = 1
cut = 0
with open('/Users/wdy940211/Desktop/popular-names.txt', 'r') as f:
    for count, line in enumerate(f):
        count += 1
with open('/Users/wdy940211/Desktop/popular-names.txt', 'r') as f:
    for line in f:
        cut = cut + 1
        lines.append(line)
        if cut == count / n:
            with open('/Users/wdy940211/Desktop/popular-names_python_%s.txt' % str(no), 'w') as f_cut:
                for it in lines:
                    f_cut.write(it)
            no = no + 1
            cut = 0
            lines = []
if count % n != 0:
    with open('/Users/wdy940211/Desktop/popular-names_python_%s.txt' % str(no), 'w') as f_cut_final:
        for it in lines:
            f_cut_final.write(it)


# In[249]:


# Unix

get_ipython().system("split -l 500 '/Users/wdy940211/Desktop/popular-names.txt' '/Users/wdy940211/Desktop/popular-names_unix.txt'")


# 17. Distinct strings in the first column
# Find distinct strings (a set of strings) of the first column of the file. 
# Confirm the result by using cut, sort, and uniq commands.

# In[253]:


import pandas as pd

df = pd.read_csv('/Users/wdy940211/Desktop/popular-names.txt', sep='\t', header=None)
col1 = df[0].unique()
col1.sort()
with open('/Users/wdy940211/Desktop/DistinctStrings_python.txt', 'w') as f:
    for it in col1:
        f.write('%s\n' % it)


# In[44]:


# Unix

get_ipython().system("cut -f 1 < '/Users/wdy940211/Desktop/popular-names.txt' | sort -u")


# 18. Sort lines in descending order of the third column
# Sort the lines in descending numeric order of the third column (sort lines without changing the content of each line). Confirm the result by using sort command.

# In[254]:


# sort the thrid column only

import pandas as pd
df = pd.read_csv('/Users/wdy940211/Desktop/popular-names.txt', sep='\t', header=None)
result = df[2].sort_values(ascending=False)
with open('/Users/wdy940211/Desktop/Sort3rdColumn_python.txt', 'w') as f:
    for it in result:
        f.write('%s\n' % it)


# In[255]:


# sort the whole text by the third column

import pandas as pd
df = pd.read_csv('/Users/wdy940211/Desktop/popular-names.txt', sep='\t', header=None)
df.sort_values(by=df.columns[2], ascending=False).to_csv('/Users/wdy940211/Desktop/SortBy3rdColumn_python.txt', sep='\t', header=False, index=False)


# In[61]:


# Unix

get_ipython().system("sort -nr -k 3 '/Users/wdy940211/Desktop/popular-names.txt'")


# 19. Frequency of a string in the first column in descending order
# Find the frequency of a string in the first column, and sort the strings by descending order of their frequencies. Confirm the result by using cut, uniq, and sort commands.

# In[256]:


import pandas as pd

df = pd.read_csv('/Users/wdy940211/Desktop/popular-names.txt', sep='\t', header=None)
count = df[0].value_counts().reset_index()
count[[count.columns[0], count.columns[1]]] = count[[count.columns[1], count.columns[0]]]
count.to_csv('/Users/wdy940211/Desktop/1stColumnFreq_python.txt', sep=' ', header=False, index=False)


# In[54]:


# Unix

get_ipython().system("cut -f 1 < '/Users/wdy940211/Desktop/popular-names.txt'| sort | uniq -c | sort -n -r")

