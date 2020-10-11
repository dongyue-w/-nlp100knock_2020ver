#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Chapter 1 Warm-up


# 00. Reversed string
# Obtain the string that arranges letters of the string “stressed” in reverse order (tail to head).

# In[1]:


s = 'stressed'
s[::-1]


# 01. “schooled”
# Obtain the string that concatenates the 1st, 3rd, 5th, and 7th letters in the string “schooled”.

# In[2]:


s = 'schooled'
s[:7:2]


# 02. “shoe” + “cold” = “schooled”
# Obtain the string “schooled” by concatenating the letters in “shoe” and “cold” one after the other from head to tail.

# 

# 03. Pi
# Split the sentence “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics”. into words, and create a list whose element presents the number of alphabetical letters in the corresponding word.

# In[45]:


s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics'
list(map(len, s.replace(',','').split()))


# In[ ]:





# 04. Atomic symbolsPermalink
# Split the sentence “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can”. into words, and extract the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words and the first two letters from the other words. Create an associative array (dictionary object or mapping object) that maps from the extracted string to the position (offset in the sentence) of the corresponding word.

# In[64]:


s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can'
l = [1, 5, 6, 7, 8, 9, 15, 16, 19]
d = {}

for i, value in enumerate(s.replace('.', '').split()):
    if i+1 in l:
        value = value[:1]
    else:
        value = value[:2]
    d[value] = i+1
    
print(d)


# In[67]:


s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can'
l = [1, 5, 6, 7, 8, 9, 15, 16, 19]
d = {}
for i, value in enumerate(s.replace('.', '').split()):
    d[value[:2-int((i+1)in l)]] = i+1
print(d)


# 05. n-gram
# Implement a function that obtains n-grams from a given sequence object (e.g., string and list). Use this function to obtain word bi-grams and letter bi-grams from the sentence “I am an NLPer”

# In[92]:


def ngram(s, n):
    l = []
    a = 0
    while a < len(s) - n + 1:
        l.append(s[a:a+n])
        a = a + 1
    return l
print(ngram('I am an NLPer'.replace(' ', ''), 2))
print(ngram('I am an NLPer'.split(), 2))


# 06. Set
# Let the sets of letter bi-grams from the words “paraparaparadise” and “paragraph” $X$ and $Y$, respectively. Obtain the union, intersection, difference of the two sets. In addition, check whether the bigram “se” is included in the sets $X$ and $Y$

# In[103]:


def ngram(s, n):
    j = set()
    a = 0
    while a < len(s) - n + 1:
        j.add(s[a:a+n])
        a = a + 1
    return j
X = ngram('paraparaparadise', 2)
Y = ngram('paragraphe', 2)
print(X)
print(Y)
print(X & Y)
print(X | Y)
print(X - Y)
print(Y - X)
print(X ^ Y)
print(Y ^ X)
print('se' in X)
print('se' in Y)


# 07. Template-based sentence generation
# Implement a function that receives arguments, x, y, and z and returns a string “{y} is {z} at {x}”, where “{x}”, “{y}”, and “{z}” denote the values of x, y, and z, respectively. In addition, confirm the return string by giving the arguments x=12, y="temperature", and z=22.4.

# In[108]:


def func(x, y, z):
    return ('%s is %.1f at %d' % (y, z, x))
func(12, 'temperature', 22.4)


# 08. cipher text
# Implement a function cipher that converts a given string with the specification:
# Every alphabetical lowercase letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
# Keep other letters unchanged
# Use this function to cipher and decipher an English message.

# In[4]:


def cipher(string):
    return string.replace('c', chr(219-ord('c')))

string = 'Cgdvhgcjgiucyiudhiwejiwoixxccg'
cipher(string)


# 09. Typoglycemia
# Write a program with the specification:
# 
# Receive a word sequence separated by space
# For each word in the sequence:
# If the word is no longer than four letters, keep the word unchanged
# Otherwise,
# Keep the first and last letters unchanged
# Shuffle other letters in other positions (in the middle of the word)
# Observe the result by giving a sentence, e.g., “I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind “.

# In[25]:


import random

def typo(text):
    text = text.split()
    result = []
    for word in text:
        if len(word) < 4:
            result.append(word)
        else:
            middle = list(word[1:-1])
            random.shuffle(middle)
            word = word[0] + ''.join(middle) + word[-1]
            result.append(word)
    return ' '.join(result)
   
text = 'Shuffle other letters in other positions (in the middle of the word) Observe the result by giving a sentence, e.g., I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind.'

print(typo(text))

