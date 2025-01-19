import streamlit as st

st.set_page_config(page_title="Retail Forecasting Services", layout="wide")
# Add your logo at the top of the page
st.image("fdLogo.png")


# Title and Intro
st.title("Retail Forecasting Services")
st.write("Welcome to our Retail Forecasting Services platform. Our goal is to provide your retail business with the tools and insights needed to thrive in a competitive market.")

# Value Proposition Section
st.header("Our Value Proposition")
st.write("We offer a range of advanced services designed to help your retail business succeed. Learn more about each service and the challenges we help solve below:")

# Define service descriptions
services = {
    "Sales Trend Analysis": {
        "description": """
        **Sales Trend Analysis** helps you identify patterns and trends in your sales data to make informed predictions. By analyzing historical sales data, we can uncover seasonal trends, growth patterns, and potential opportunities for your business.
        
        **Benefits**:
        - Identify peak sales periods and plan promotions accordingly.
        - Understand product lifecycle trends to optimize inventory.
        - Gain insights into customer purchasing behaviors.
        """
    },
    "Inventory Optimization": {
        "description": """
        **Inventory Optimization** ensures that you maintain optimal stock levels to meet demand without overstocking. Using advanced algorithms, we help you balance inventory costs with service levels.
        
        **Benefits**:
        - Reduce excess inventory and associated carrying costs.
        - Minimize stockouts and improve customer satisfaction.
        - Optimize reorder points and quantities for efficient supply chain management.
        """
    },
    "Demand Forecasting": {
        "description": """
        **Demand Forecasting** predicts future demand to streamline your supply chain operations. By leveraging machine learning models, we provide accurate forecasts that help you plan production, manage inventory, and schedule deliveries.
        
        **Benefits**:
        - Improve supply chain efficiency and reduce operational costs.
        - Enhance accuracy in production planning and resource allocation.
        - Respond proactively to market changes and customer demand.
        """
    },
    "Price Optimization": {
        "description": """
        **Price Optimization** uses data-driven insights to set the best prices for your products. By analyzing market conditions, customer behavior, and competitor pricing, we help you find the optimal price points to maximize revenue and profitability.
        
        **Benefits**:
        - Increase sales and profit margins.
        - Respond dynamically to market changes.
        - Enhance customer satisfaction with competitive pricing.
        """
    },
    "Customer Segmentation": {
        "description": """
        **Customer Segmentation** helps you understand your customer base and target them more effectively. By segmenting customers based on their behaviors, preferences, and demographics, we enable personalized marketing strategies and improved customer experiences.
        
        **Benefits**:
        - Improve marketing campaign effectiveness.
        - Enhance customer loyalty and retention.
        - Identify high-value customer segments for targeted promotions.
        """
    }
}

# Define challenges and their solutions
challenges = {
    "Accurate Demand Forecasting": {
        "description": """
        **Challenge**:
        Retailers often struggle to accurately forecast demand, leading to overstocking or stockouts.

        **How We Help**:
        Our **Demand Forecasting** service leverages machine learning to provide accurate demand predictions, helping you manage inventory efficiently and reduce costs.
        """
    },
    "Inventory Management": {
        "description": """
        **Challenge**:
        Maintaining optimal inventory levels is a constant challenge, with the risk of either overstocking or running out of stock.

        **How We Help**:
        Our **Inventory Optimization** service uses advanced algorithms to balance inventory costs with service levels, ensuring you always have the right amount of stock.
        """
    },
    "Identifying Sales Trends": {
        "description": """
        **Challenge**:
        Understanding and anticipating sales trends is critical for planning promotions and stocking products.

        **How We Help**:
        Our **Sales Trend Analysis** service helps identify patterns in your sales data, enabling you to plan effectively and capitalize on peak sales periods.
        """
    },
    "Setting Competitive Prices": {
        "description": """
        **Challenge**:
        Setting the right prices is crucial for maximizing revenue while staying competitive.

        **How We Help**:
        Our **Price Optimization** service uses data-driven insights to determine optimal pricing strategies, ensuring you maximize profitability and customer satisfaction.
        """
    },
    "Targeting the Right Customers": {
        "description": """
        **Challenge**:
        Effectively targeting and retaining customers can be difficult without understanding their behaviors and preferences.

        **How We Help**:
        Our **Customer Segmentation** service enables personalized marketing strategies by segmenting customers based on their behaviors and preferences, improving engagement and loyalty.
        """
    }
}

# Display services and challenges side by side
st.write("---")
st.header("Our Services and the Challenges We Address")

# Define layout for side-by-side display
left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Services")
    for service, details in services.items():
        with st.expander(service):
            st.write(details["description"])

with right_column:
    st.subheader("Challenges")
    for challenge, details in challenges.items():
        with st.expander(challenge):
            st.write(details["description"])

# Footer with call to action
st.write("---")
st.header("Get Started")
st.write("Ready to take your retail forecasting to the next level? Contact us today to learn more about our services and how we can help your business thrive.")
st.button("Learn More", on_click=lambda: st.write("Visit [our website](https://yourwebsite.com) for more information."))

# Footer link
st.write("---")
st.write("[Learn More >](https://yourwebsite.com)")
