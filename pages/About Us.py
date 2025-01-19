# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:31:14 2024

@author: dell
"""

import streamlit as st
import plotly.express as px
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Fintastic Data Solutions for FMCG", page_icon="📈", layout="wide")

# Add your logo at the top of the page
st.image("fdLogo.png")

# Hide the Streamlit header and footer
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Title of the page
st.title("Fintastic Data Solutions for FMCG Companies")

# Introduction
st.write("""
FMCG companies generate a large volume of fast-moving data. This data can become cumbersome to work with due to its size and the limited capabilities of tools like Excel. Fintastic Data uses modern tools and software to overcome these challenges.
""")

# Key Services
st.header("Our Services")
st.write("""
Fintastic Data helps FMCG companies with the following:
1. **Business intelligence and data visualization**
2. **Data Science** e.g., Sales forecasting and customer clustering
3. **AI applications in business**, providing executive summaries across diverse data sources
4. **Workflow Automation** e.g., sending out daily reports, handling data, responding to requests
""")

# Comparison with Excel
st.header("Why Upgrade from Excel?")
st.write("""
- **Excel** has a 1 million row limitation and starts slowing down excessively around the 300,000-row mark.
- **Upgrade from Excel-based manual trend analysis** to automated predictive analytics, enabling faster and more accurate market and demand forecasting.
- **Transition from Excel spreadsheets for inventory management** to AI-driven systems that predict optimal stock levels, reducing waste and improving availability.
- **Shift from static Excel reports** to dynamic, real-time data visualizations and dashboards, offering instant insights for strategic decision-making.
- **Move from manually segmenting customers in Excel** to using machine learning for precise customer segmentation, personalizing marketing efforts effectively.
- **Replace time-consuming Excel calculations for supply chain optimization** with AI algorithms, enhancing efficiency and responsiveness in logistics and distribution.
""")

# Our Tools and Technologies
st.header("Our Tools and Technologies")
st.write("""
- **Power BI**
- **Power Automate**
- **Power Apps**
- **Database connections** (SQL, SAP, Oracle)
- **Python**
- **API Connections**

With these tools, we can:
- **Connect to big data**
- **Visualize data instantly for quick insights**
- **Integrate diverse data sources seamlessly**
- **Customize dashboards to specific needs**
- **Automate data refreshes and reporting**
- **Drive data-driven decisions efficiently**
""")

# Benefits
st.header("Benefits")
st.write("""
- **Leverage** machine learning for precise demand forecasting and inventory optimization.
- **Harness** customer data analytics for tailored marketing and improved loyalty.
- **Streamline** operations with data-driven supply chain management.
- **Gain** a competitive edge with real-time market intelligence insights.
- **Enhance** strategic decisions with actionable data insights for better business outcomes.
""")

# Automated Solutions
st.header("Automated Solutions")
st.write("""
- **Automate Inventory Replenishment**: Trigger purchase orders when stocks run low, ensuring seamless supply chain operations.
- **Efficient Sales Order Processing**: Streamline order processing from receipt to fulfillment, reducing manual errors and improving customer satisfaction.
- **Automated Quality Control Checks**: Conduct automated quality checks on products, identifying and addressing issues promptly.
- **Targeted Marketing Campaigns**: Reach customers with tailored promotions based on their preferences, driving engagement and sales.
- **Real-time Supply Chain Visibility**: Monitor shipment statuses and detect issues instantly, ensuring smooth logistics operations.
""")

# Conclusion
st.header("Transform Your FMCG Operations with Fintastic Data")
st.write("""
The integration of AI and data analytics transforms the FMCG industry. Unlock valuable insights, optimize operations, and drive growth with automated predictive analytics and AI-driven inventory management. Real-time data visualizations enable smarter decisions faster.

Embrace these technologies for personalized customer experiences and supply chain optimization. Shift from manual Excel-based analysis to data-driven excellence. AI and data analytics pave the way for innovation and profitability in the FMCG sector.
""")

# Call to Action
st.write("---")
st.header("Get Started with Fintastic Data")
st.write("Contact us today to learn more about how we can help transform your FMCG operations.")
st.button("Contact Us", on_click=lambda: st.write("Visit [Fintastic Data](https://yourwebsite.com) for more information."))

# Footer link
st.write("---")
st.write("[Explore More >](https://yourwebsite.com)")
