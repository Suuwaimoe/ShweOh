import streamlit as st
st.title('a small program')
st.subheader('I am Suu Wai Moe')
st.write('This is my first streamlit application')
st.write('Myanmar Exam Result')
Myanmar_score= int(input('Myanmar score:'))
English_score= int(input('English score:'))
Maths_score=int(input('Maths score:'))
Chemistry_score=int(input('Chemistry score:'))
Physics_score=int(input('Physic score:'))
Bio_score=int(input('Bio score:'))
if Myanmar_score >= 40 and English_score>= 40 and Maths_score >= 40 and Chemistry_score >= 40 and Physics_score >= 40 and Bio_score >= 40:
 print("You've passed the exam")
 if Myanmar_score >= 75:
  print('Myanmar Distinction')
 if English_score >= 75:
  print('English Distinction')
 if Maths_score >= 80:
  print('Maths Distinction')
 if Chemistry_score >= 80:
  print('Chemistry Distinction')
 if Physics_score >= 80:
  print('Physics Distinction')
 if Bio_score >= 75:
  print('Bio Distinction')
else:
 print("You fail the exam")
Total_Score=Myanmar_score+English_score+Maths_score+Chemistry_score+Physics_score+Bio_score
print('Your total score:',Total_Score)
