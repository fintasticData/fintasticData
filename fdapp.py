import streamlit as st
from PIL import Image, ImageOps
import os

# Set page configuration
st.set_page_config(
    page_title="Fintastic Data",
    page_icon="📊",
    #layout="wide",
    initial_sidebar_state="collapsed",
)

# Helper function to load images
def load_image(image_path, width=None, invert_colors=False):
    """
    Load an image from the specified path, optionally resize it, and invert colors if specified.

    Args:
        image_path (str): Path to the image file.
        width (int, optional): Desired width of the image.
        invert_colors (bool, optional): Whether to invert the image colors.

    Returns:
        Image: The processed image.
    """
    img = Image.open(image_path)
    if invert_colors:
        img = ImageOps.invert(img.convert("RGB"))  # Invert colors for dark mode
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
    # Determine if dark mode is selected
    is_dark_mode = st.get_option("theme.base") == "dark"

    col1, col2 = st.columns([1, 2])
    with col1:
        logo_path = os.path.join("assets", "fdLogo.PNG")
        st.image(load_image(logo_path, width=150, invert_colors=is_dark_mode))
    with col2:
        st.markdown("<h1 style='text-align: center;'>Transforming Data into Actionable Insights</h1>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: center; font-size:20px;'>Unlock the potential of your business with our cutting-edge AI, Data Solutions, and Automation services.</p>",
            unsafe_allow_html=True
        )
        col3, col4 = st.columns([1,1])
        with col3:
            if st.button("Get Started"):
                st.experimental_rerun()
        with col4:
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
            "description": "Leverage AI to automate processes, enhance decision-making, and create personalized customer experiences.",
            "icon": os.path.join("assets", "ai_icon.PNG")
        },
        {
            "title": "Data Solutions",
            "description": "Transform your data into valuable insights with advanced analytics and visualization.",
            "icon": os.path.join("assets", "data_icon.PNG")
        },
        {
            "title": "Automations",
            "description": "Streamline operations with robotic process automation and workflow systems.",
            "icon": os.path.join("assets", "automation_icon.PNG")
        },
        {
            "title": "Data Science",
            "description": "Harness data science techniques for predictive modeling and data-driven decisions.",
            "icon": os.path.join("assets", "data_science_icon.PNG")
        },
        {
            "title": "Applications (Apps)",
            "description": "Develop custom applications to enhance user engagement and business operations.",
            "icon": os.path.join("assets", "apps_icon.PNG")
        },
        {
            "title": "AI and Data Outsourcing",
            "description": "Outsource AI and data tasks to our expert team, freeing your resources for strategic initiatives.",
            "icon": os.path.join("assets", "ai_icon.PNG")
        }
    ]

    service_groups = st.tabs([service["title"] for service in services])

    for idx, service in enumerate(services):
        with service_groups[idx]:
            display_service(service["title"], service["description"], service["icon"])

# Contact Us Section
def contact_section():
    st.markdown("<div class='section' id='contact'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Contact Us</h2>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Ready to Transform Your Business?</div>", unsafe_allow_html=True)

    # Contact Form
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
        with col2:
            phone = st.text_input("Phone")
            subject = st.text_input("Subject")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thank you for reaching out! We will get back to you shortly.")

# Main App Layout
def main():
    header_section()
    about_us_section()
    services_section()
    contact_section()

if __name__ == "__main__":
    main()
