import streamlit as st

from apputil import *


st.write(
'''
# Week 1: String Manipulation

...
''')


pal_text = st.text_input('Check this text to see if it is a palindrome: ',
                                 value=None)

if pal_text and palindrome(pal_text):
    st.write('It\'s a  palindrome!')
elif pal_text:
    st.write('It\'s not a palindrome.')

par_text = st.text_input('Check this text for parenthetical balance: ')

if par_text and parentheses(par_text):
    st.write('It\'s balanced!')
elif par_text:
    st.write('It\'s not balanced.')