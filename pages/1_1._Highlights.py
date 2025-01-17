import streamlit as st
import pandas as pd
import plotly.express as px
import base64
from streamlit_extras.stylable_container import stylable_container


# Set page configuration
st.set_page_config(page_title="Machine Learning Highlights", page_icon="🤖", layout="wide")
# Add your logo at the top of the page
# st.image("fdLogo.png", width =200)  # Adjust the width as needed

# st.image("fdLogo.png")
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Read the contents of the CSS file
with open("styles.css") as f:
    css_styles = f.read()

myContainerStyle = "{background-color: rgba(0, 0, 0, 0.9); border: 2px solid rgba(255, 255, 255, 0.3);   border-radius: 15px;padding: 20px; margin: 10px 0;  box-shadow: 0 0 15px rgba(255, 255, 255, 0.6);}"
css_styles=""" 
                        {background-color: rgba(0, 0, 0, 0.9); border: 2px solid rgba(255, 255, 255, 0.3);   border-radius: 15px;padding: 20px; margin: 10px 0;  box-shadow: 0 0 15px rgba(255, 255, 255, 0.6);}
                        """
# Inject the CSS into the Streamlit app
st.markdown(f"<style>{css_styles}</style>", unsafe_allow_html=True)

add_bg_from_local('C:/MyPy/Streamlit/Concept/images/bg3.png')
# Hide the Streamlit header and footer
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



with stylable_container(key="styledContainer", css_styles=css_styles):
    # Title of the page
    st.title("Machine Learning Highlights")
    
    tabs = st.tabs(["Highlights", "Proposal"])
    
    
    text = """
    ### Executive Summary
    
    Artificial intelligence (AI) is rapidly transforming the way businesses operate. AI-powered forecasting software can help businesses make more informed decisions, improve efficiency, and increase profits. This proposal outlines a new AI software forecasting product that will provide businesses with the tools they need to succeed in the digital age.
    
    ### Problem Statement
    
    Businesses of all sizes are facing increasing challenges in accurately forecasting demand. Traditional forecasting methods are often inaccurate and time-consuming. This can lead to lost sales, overstocking, and missed opportunities.
    
    ### Solution
    
    Our new AI software forecasting product will solve these problems by providing businesses with:
    - Accurate and timely forecasts
    - Automated data analysis
    - Real-time insights
    - Easy-to-use interface
    
    ### Benefits
    
    Businesses that use our AI software forecasting product will benefit from:
    - Increased sales
    - Reduced costs
    - Improved efficiency
    - Better decision-making
    - Competitive advantage
    
    ### Market Opportunity
    
    The market for AI software forecasting products is large and growing. Businesses of all sizes are looking for ways to improve their forecasting accuracy. Our product is well-positioned to capture a significant share of this market.
    
    ### Competitive Advantages
    
    Our AI software forecasting product has several competitive advantages, including:
    - **Accuracy**: Our product uses the latest AI algorithms to provide the most accurate forecasts possible.
    - **Automation**: Our product automates the data analysis process, saving businesses time and money.
    - **Real-time insights**: Our product provides real-time insights into demand trends, so businesses can make informed decisions quickly.
    - **Easy to use**: Our product is designed to be easy to use, even for businesses with no prior experience with AI.
    
    ### Pricing
    
    Our AI software forecasting product will be priced on a subscription basis. The pricing will be based on the number of users and the amount of data that is being processed.
    
    ### Implementation
    
    Our AI software forecasting product is easy to implement. Businesses can simply sign up for a subscription and start using the product immediately.
    
    ### Conclusion
    
    Our AI software forecasting product is a powerful tool that can help businesses of all sizes improve their forecasting accuracy, increase sales, and reduce costs. We believe that our product has the potential to revolutionize the way businesses forecast demand.
    
    ### Call to Action
    
    We urge you to consider investing in our AI software forecasting product. We believe that our product can help your business achieve its goals and succeed in the digital age.
    """
    
    # Display the text in Streamlit
    
    with tabs[0]:
        # Infographic styled highlights
        st.header("Key Highlights of fintastic Datas Machine Learning services")
        
        # Display highlights in columns using KPI widgets
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Growth in Data", value="44 Zettabytes", delta="Exponential Growth")
            st.write("Machine learning thrives on data. The volume of data generated is growing exponentially each year.")
        
        with col2:
            st.metric(label="Algorithm Advancements", value="100+ New Algorithms", delta="Yearly")
            st.write("Algorithms are becoming more sophisticated, allowing for better predictions and insights.")
        
        with col3:
            st.metric(label="Computational Power", value="10x Increase", delta="Last 5 Years")
            st.write("With the rise of powerful GPUs and TPUs, machine learning models can be trained faster than ever.")
        
        # Another row of highlights
        col4, col5, col6 = st.columns(3)
        with col4:
            st.metric(label="Real-World Applications", value="Every Industry")
            st.write("Machine learning is being applied across various industries, from healthcare to finance to retail.")
        
        with col5:
            st.metric(label="Automation and Efficiency", value="70% Tasks Automated", delta="Increasing")
            st.write("ML models automate repetitive tasks, leading to increased efficiency and productivity.")
        
        with col6:
            st.metric(label="AI and Ethics", value="Ongoing Research")
            st.write("As machine learning advances, it is important to consider the ethical implications and ensure fair use.")
        
        # Highlight some stats with charts
        st.header("Interesting Statistics")
        
        # Static bar chart example
        st.subheader("Investment in AI and ML (in Billion $)")
        investment_data = {
            'Year': ['2016', '2017', '2018', '2019', '2020', '2021'],
            'Investment': [12, 15, 20, 24, 30, 35]
        }
        investment_df = pd.DataFrame(investment_data)
        
        fig = px.bar(investment_df, x='Year', y='Investment', text='Investment', color='Investment', 
                     color_continuous_scale=px.colors.sequential.Plasma)
        
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
        # Static pie chart example
        st.subheader("Popular ML Algorithms")
        algorithm_data = {
            'Algorithm': ['Linear Regression', 'Decision Trees', 'SVM', 'Neural Networks', 'K-Means'],
            'Usage': [25, 20, 15, 30, 10]
        }
        algorithm_df = pd.DataFrame(algorithm_data)
        
        fig2 = px.pie(algorithm_df, names='Algorithm', values='Usage', title='Usage of ML Algorithms',
                      color_discrete_sequence=px.colors.sequential.RdBu)
        
        st.plotly_chart(fig2, use_container_width=True)


    with tabs[1]:
        st.markdown(text)
        
with stylable_container(key="styledContainer", css_styles=css_styles):
    st.header("Learn More About Machine Learning")
    st.write("Machine learning is a rapidly evolving field with countless opportunities. Explore more to stay ahead in this exciting domain.")
    st.button("Explore More", on_click=lambda: st.write("Visit [our website](https://yourwebsite.com) for more information."))
    
