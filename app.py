import streamlit as st

st.title('Text Analyzer 📊')
st.write('This is a simple text analyzer that counts the number of words, characters, spaces, vowels, and converts the text to uppercase and lowercase. It also allows you to search for a word and replace it with another word. ✍️') 
st.write('Please enter a text in the box below and click the Analyze button 🖱️')

text = st.text_area('Enter text here 📝')
if st.button('Analyze 🔍'):
    st.write('The text has', len(text.split()), 'words 📝')
    st.write('The text has', len(text), 'characters 🔠')
    st.write('The text has', len(text.split(' ')), 'spaces 🚀')
    st.write('The text has', len(text.split(' ')), 'words 📝')
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in text if char in vowels)
    st.write('The text has', vowel_count, 'vowels 💬')
    st.write('Text in uppercase:', text.upper(), '🔠')
    st.write('Text in lowercase:', text.lower(), '🔡')

search_word = st.text_input('Enter the word to search for 🔍')
replace_word = st.text_input('Enter the word to replace it with 🔄')    

if search_word and replace_word:
    new_text = text.replace(search_word, replace_word)
    st.write('New text Generated:', new_text, '✏️')