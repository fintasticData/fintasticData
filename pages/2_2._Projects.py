import streamlit as st
from PIL import Image

st.set_page_config(page_title="Retail Forecasting Services - Projects", layout="wide")
# Add your logo at the top of the page
st.image("fdLogo.png")



# Title and Intro
st.title("Departmental Projects")
st.write("Explore the potential projects that can be undertaken by different departments within your retail business to enhance operations and drive growth.")

# Define projects for each department with the new icons
departments = {
    "Sales Department": {
        "projects": {
            "Sales Forecasting Improvement": {
                "description": "Enhance the accuracy of sales forecasts by implementing advanced machine learning models. Analyze historical sales data and incorporate external factors such as market trends and seasonality to improve prediction accuracy.",
                "icon": "project_icons/sales_forecasting.png"
            },
            "Customer Segmentation Analysis": {
                "description": "Segment customers based on purchasing behavior, demographics, and preferences. Use these segments to tailor marketing strategies, personalize customer interactions, and improve customer retention.",
                "icon": "project_icons/customer_segmentation.png"
            },
            "Sales Performance Dashboard": {
                "description": "Develop a comprehensive dashboard to monitor sales performance in real-time. Include key metrics such as sales targets, revenue, growth rate, and sales by region or product category.",
                "icon": "project_icons/sales_dashboard.png"
            }
        }
    },
    "Inventory Management": {
        "projects": {
            "Inventory Optimization": {
                "description": "Implement algorithms to optimize inventory levels and minimize costs. Use demand forecasting and reorder point calculations to ensure optimal stock levels and reduce the risk of stockouts or overstocking.",
                "icon": "project_icons/inventory_optimization.png"
            },
            "Warehouse Efficiency Analysis": {
                "description": "Analyze warehouse operations to identify bottlenecks and areas for improvement. Implement solutions to enhance picking, packing, and shipping processes, and improve overall warehouse efficiency.",
                "icon": "project_icons/warehouse_efficiency.png"
            },
            "Supplier Performance Monitoring": {
                "description": "Develop a system to monitor and evaluate supplier performance. Track key metrics such as lead time, order accuracy, and cost to identify reliable suppliers and negotiate better terms.",
                "icon": "project_icons/supplier_performance.png"
            }
        }
    },
    "Marketing Department": {
        "projects": {
            "Marketing Campaign Optimization": {
                "description": "Use data analytics to evaluate the effectiveness of marketing campaigns. Identify the best-performing channels, messages, and timing to maximize return on investment and customer engagement.",
                "icon": "project_icons/marketing_optimization.png"
            },
            "Customer Journey Mapping": {
                "description": "Map out the customer journey to identify key touchpoints and pain points. Use this information to improve the customer experience and design targeted marketing strategies that address specific needs.",
                "icon": "project_icons/customer_journey.png"
            },
            "Social Media Analytics": {
                "description": "Analyze social media data to understand customer sentiment and brand perception. Use insights from social media platforms to inform marketing strategies and improve customer engagement.",
                "icon": "project_icons/social_media_analytics.png"
            }
        }
    },
    "Finance Department": {
        "projects": {
            "Financial Performance Analysis": {
                "description": "Conduct a comprehensive analysis of financial performance using key financial metrics. Develop dashboards to monitor revenue, expenses, profit margins, and other important indicators.",
                "icon": "project_icons/financial_analysis.png"
            },
            "Budgeting and Forecasting": {
                "description": "Implement advanced forecasting models to improve budgeting accuracy. Use historical data and predictive analytics to create more accurate financial plans and projections.",
                "icon": "project_icons/budgeting_forecasting.png"
            },
            "Cost Reduction Strategies": {
                "description": "Identify areas where costs can be reduced without compromising quality or performance. Analyze operational expenses and develop strategies to streamline processes and improve cost efficiency.",
                "icon": "project_icons/cost_reduction.png"
            }
        }
    }
}

# Display departments and projects
st.write("---")
st.header("Potential Projects by Department")

for department, details in departments.items():
    st.subheader(department)
    for project, info in details["projects"].items():
        col1, col2 = st.columns([1, 7])
        with col1:
            st.image(info["icon"], width=80)
        with col2:
            st.markdown(f"### {project}")
            st.write(info["description"])
        st.write("---")

# Footer with call to action
st.write("---")
st.header("Get Started")
st.write("Ready to undertake these projects and drive growth in your retail business? Contact us today to learn more about how we can help you implement these solutions.")
st.button("Learn More", on_click=lambda: st.write("Visit [our website](https://yourwebsite.com) for more information."))

# Footer link
st.write("---")
st.write("[Learn More >](https://yourwebsite.com)")
