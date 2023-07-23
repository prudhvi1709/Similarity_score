import streamlit as st
import pandas as pd

# Load the pre-computed data from the H5 file
data = pd.read_hdf('semantic_similarity_scores.h5', key='data')

# Streamlit app
def main():
    st.title('Semantic Similarity App')
    st.write('Enter two texts to calculate their semantic similarity.')

    text1 = st.text_area('Text 1', '')
    text2 = st.text_area('Text 2', '')

    if st.button('Calculate Similarity'):
        if not text1 or not text2:
            st.warning('Please enter both text inputs.')
        else:
            # Find the row in the 'data' DataFrame that matches the given text inputs
            row = data[(data['text1'] == text1) & (data['text2'] == text2)]
            if len(row) > 0:
                similarity_score = row['semantic_similarity'].iloc[0]
                st.success(f'Semantic Similarity Score: {similarity_score:.4f}')
            else:
                st.warning('Semantic similarity score not found for the given text inputs.')

if __name__ == '__main__':
    main()
