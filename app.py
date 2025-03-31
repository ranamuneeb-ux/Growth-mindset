import streamlit as st
st.title('Growth Mindset Challenge')
st.header('Embrace your potential!')
st.write("A growth mindset means embracing challenges, persisting in the face of setbacks, and seeing effort as a path to mastery.")
st.write("Let's take a moment to reflect on our mindset.")
st.write("Think about a recent challenge you faced. How did you respond?")
st.header("Bonus Quote")
st.write("“The only limit to our realization of tomorrow will be our doubts of today.” - Franklin D. Roosevelt")
st.write("Remember, challenges are opportunities for growth.")
st.write("Embrace them!")

button = st.button('Take the challenge')
if button:
    st.write('You are on your way to a growth mindset!')
    st.write('Remember, every expert was once a beginner.')
    st.write('Believe in yourself and your abilities.')