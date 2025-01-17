import streamlit as st
from PIL import Image
import os







# Set page configuration
st.set_page_config(
    page_title="Fintastic Data",
    page_icon="📊",
    initial_sidebar_state="collapsed"
)

#st.sidebar.title("Navigation")
#page = st.sidebar.selectbox("Choose a page:", ["Home", "Forecasting Demonstration"])



# Hide the Streamlit menu and footer
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Helper function to load images
def load_image(image_path, width=None):
    img = Image.open(image_path)
    if width:
        img = img.resize((width, int(img.height * width / img.width)))
    return img

# Interactive grouping for services
def display_service(title, description, icon):
    st.markdown(f"### {title}")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(icon, width=80)
    with col2:
        st.markdown(description)

# Header Section
def header_section():
    logo_path = os.path.join("assets", "Logo1.png")
    #st.image(load_image(logo_path, width=200))
    bigPic = os.path.join("assets", "bigPic.png")
    st.image(load_image(bigPic, width=600))
    col2, col3 = st.columns([3, 1])
    with col2:
        #logo_path = os.path.join("assets", "Logo1.png")
        #st.image(load_image(logo_path, width=100))
        st.markdown(
            """
            <h1>Transforming Data into Actionable Insights</h1>
            <p>Unlock the potential of your business with our cutting-edge AI, Data Solutions, and Automation services.</p>
            """,
            unsafe_allow_html=True
        )
    col4, col5 = st.columns([1, 1])
    with col4:
        if st.button("Get Started"):
            st.experimental_rerun()
    with col5:
        if st.button("Learn More"):
            st.experimental_rerun()


# About Us Section
def about_us_section():
    st.markdown("<div class='section' id='about'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Who We Are</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        At **Fintastic Data**, we specialize in delivering innovative solutions that harness the power of Artificial Intelligence, Data Science, and Automation to drive business growth.
        Our team of experts is dedicated to transforming complex data into strategic assets, enabling organizations to make informed decisions and achieve their objectives.
        """,
        unsafe_allow_html=True
    )

# Services Section
def services_section():
    st.markdown("<h2 class='section-title'>Our Services</h2>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Delivering Comprehensive Solutions Across Various Domains</div>", unsafe_allow_html=True)

    services = [
        {
            "title": "Artificial Intelligence (AI)",
            "description": "Leverage AI to automate processes, enhance decision-making, and create personalized customer experiences. AI allows businesses to improve efficiency, reduce costs, and gain a competitive edge in the market through intelligent insights and predictions.",
            "icon": os.path.join("assets", "ai_icon.PNG")
        },
        {
            "title": "Data Solutions",
            "description": "Transform your data into valuable insights with advanced analytics and visualization. From data warehousing to reporting, our solutions ensure that your organization derives maximum value from its data assets.",
            "icon": os.path.join("assets", "data_icon.PNG")
        },
        {
            "title": "Automations",
            "description": "Streamline operations with robotic process automation and workflow systems. Automation reduces human errors, enhances consistency, and frees up valuable time for your teams to focus on strategic initiatives.",
            "icon": os.path.join("assets", "automation_icon.PNG")
        },
        {
            "title": "Data Science",
            "description": "Harness data science techniques for predictive modeling and data-driven decisions. Our expertise in machine learning and statistical modeling helps uncover hidden patterns and forecast trends effectively.",
            "icon": os.path.join("assets", "data_science_icon.PNG")
        },
        {
            "title": "Applications (Apps)",
            "description": "Develop custom applications to enhance user engagement and business operations. Our tailored app solutions cater to specific business needs, ensuring scalability, usability, and impactful outcomes.",
            "icon": os.path.join("assets", "apps_icon.PNG")
        },
        {
            "title": "AI and Data Outsourcing",
            "description": "Outsource AI and data tasks to our expert team, freeing your resources for strategic initiatives. Our services allow you to scale your operations effectively without compromising on quality or efficiency.",
            "icon": os.path.join("assets", "ai_icon.PNG")
        }
    ]

    service_groups = st.tabs([service["title"] for service in services])

    for idx, service in enumerate(services):
        with service_groups[idx]:
            display_service(service["title"], service["description"], service["icon"])

# eBook Launch Section
def ebook_launch_section():
    st.markdown("<div class='section' id='ebook'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Our eBook Launch</h2>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Discover Insights into Shopper Profiles</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        # Path to eBook cover image
        ebook_cover_path = os.path.join("assets", "ebook_cover.PNG")
        st.image(load_image(ebook_cover_path, width=141), caption="Shopper Profiles eBook")
    with col2:
        st.markdown(
            """
            Our latest eBook, **Shopper Profiles**, provides in-depth insights into consumer behavior, preferences, and trends.
            Learn how to leverage data-driven strategies to personalize marketing, boost customer satisfaction, and drive sales growth.

            **Highlights Include:**
            - Detailed case studies on successful AI-driven campaigns.
            - Strategies for segmenting customers effectively.
            - Tips for forecasting shopper trends using predictive analytics.

            Pre-order your copy today and take the first step towards revolutionizing your approach to understanding your customers.
            """,
            unsafe_allow_html=True
        )
        if st.button("Pre-order Now"):
            st.success("Thank you for your interest! We'll notify you when the eBook is available.")

# Contact Us Section
def contact_section():
    st.markdown("<div class='section' id='contact'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Contact Us</h2>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Ready to Transform Your Business?</div>", unsafe_allow_html=True)

    st.markdown(
            """
                Contact us:
                clinton@fintasticdata.co.za , 
                akshar@fintasticdata.co.za , 
                eugene@fintasticdata.co.za 
            """,
            unsafe_allow_html=True
        )
    

            

    
# Main App Layout
def main():
    header_section()
    about_us_section()
    services_section()
    ebook_launch_section()
    contact_section()

if __name__ == "__main__":
    main()
