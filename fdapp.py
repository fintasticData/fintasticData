import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Fintastic Data",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* General Styles */
    body {
        font-family: 'Arial', sans-serif;
    }
    .section {
        padding: 60px 0;
    }
    .section-title {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .section-subtitle {
        font-size: 24px;
        text-align: center;
        margin-bottom: 40px;
    }
    .service-icon {
        width: 80px;
        height: 80px;
        margin-bottom: 20px;
    }
    .testimonial {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
    }
    .cta-button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .footer {
        background-color: #333;
        color: white;
        padding: 20px 0;
        text-align: center;
    }
    a {
        color: #1E90FF;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
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

# Header Section
def header_section():
    col1, col2 = st.columns([1, 2])
    with col1:
        logo = load_image("fdLogo.png", width=150)
        st.image(logo)
    with col2:
        st.markdown("<h1 style='text-align: center;'>Transforming Data into Actionable Insights</h1>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: center; font-size:20px;'>Unlock the potential of your business with our cutting-edge AI, Data Solutions, and Automation services.</p>",
            unsafe_allow_html=True
        )
        col3, col4 = st.columns([1,1])
        with col3:
            st.button("Get Started", key="get_started")
        with col4:
            st.button("Learn More", key="learn_more")

# About Us Section
def about_us_section():
    st.markdown("<div class='section' id='about'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Who We Are</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>At <strong>Fintastic Data</strong>, we specialize in delivering innovative solutions that harness the power of Artificial Intelligence, Data Science, and Automation to drive business growth. Our team of experts is dedicated to transforming complex data into strategic assets, enabling organizations to make informed decisions and achieve their objectives.</p>",
        unsafe_allow_html=True
    )
    st.markdown("<h3 class='section-subtitle'>Our Mission</h3>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>To empower businesses with intelligent data-driven solutions that enhance efficiency, foster innovation, and create competitive advantages in the digital landscape.</p>",
        unsafe_allow_html=True
    )
    st.markdown("<h3 class='section-subtitle'>Our Vision</h3>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>To be a global leader in AI and data solutions, recognized for our commitment to excellence, innovation, and customer success.</p>",
        unsafe_allow_html=True
    )

# Services Section
def services_section():
    st.markdown("<div class='section' id='services'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Our Services</h2>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Delivering Comprehensive Solutions Across Various Domains</div>", unsafe_allow_html=True)
    
    services = [
        {
            "title": "Artificial Intelligence (AI)",
            "description": "Leverage AI to automate processes, enhance decision-making, and create personalized customer experiences. Our AI solutions include machine learning models, natural language processing, and computer vision applications tailored to your business needs.",
            "icon": "assets/ai_icon.PNG"
        },
        {
            "title": "Data Solutions",
            "description": "Transform your data into valuable insights with our comprehensive data solutions. From data warehousing and integration to advanced analytics and visualization, we ensure your data is accurate, accessible, and actionable.",
            "icon": "assets/data_icon.PNG"
        }
    ]
    
    cols = st.columns(3)
    for idx, service in enumerate(services):
        with cols[idx % 3]:
            # Use absolute path to load the icon
            icon_path = os.path.join(os.path.dirname(__file__), service["icon"])
            st.image(icon_path, width=80)
            st.markdown(f"### {service['title']}")
            st.markdown(service["description"])


# AI Products Section
def ai_products_section():
    st.markdown("<div class='section' id='ai_products'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>AI Products</h2>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Innovative AI Solutions to Drive Your Business Forward</div>", unsafe_allow_html=True)
    
    # Shopper Profiles eBook Launch
    st.markdown("<h3 style='text-align: center;'>Shopper Profiles eBook Launch</h3>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>We are excited to announce the upcoming launch of our <strong>\"Shopper Profiles\"</strong> eBook, a comprehensive guide that explores how AI-driven insights can revolutionize customer understanding and engagement.</p>",
        unsafe_allow_html=True
    )
    
    st.markdown("<ul style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<li>Understanding Shopper Behavior: Analyze purchasing patterns and preferences.</li>", unsafe_allow_html=True)
    st.markdown("<li>Personalized Marketing Strategies: Tailor campaigns to individual customer segments.</li>", unsafe_allow_html=True)
    st.markdown("<li>Predictive Analytics: Forecast trends and anticipate customer needs.</li>", unsafe_allow_html=True)
    st.markdown("<li>Case Studies: Real-world examples of businesses transforming their approach with AI.</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
    
    st.markdown("<div style='text-align: center; margin-top:20px;'>", unsafe_allow_html=True)
    if st.button("Pre-Order Now"):
        st.success("Thank you for your interest! Please provide your email to receive updates.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='text-align: center;'>Benefits of the eBook:</h4>", unsafe_allow_html=True)
    st.markdown(
        "<ul style='text-align: center;'>"
        "<li>Gain actionable insights to enhance your marketing strategies.</li>"
        "<li>Learn how to leverage AI for better customer segmentation.</li>"
        "<li>Implement data-driven decisions to boost sales and customer satisfaction.</li>"
        "</ul>",
        unsafe_allow_html=True
    )

# Why Choose Us Section
def why_choose_us_section():
    st.markdown("<div class='section' id='why_choose_us'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Why Choose Fintastic Data</h2>", unsafe_allow_html=True)
    
    reasons = [
        {
            "title": "Expertise and Experience",
            "description": "With years of experience in the data and AI industry, our team possesses the technical expertise and strategic vision to deliver solutions that drive measurable results."
        },
        {
            "title": "Customized Solutions",
            "description": "We understand that every business is unique. Our solutions are tailored to meet your specific challenges and objectives, ensuring maximum impact and value."
        },
        {
            "title": "Innovative Approach",
            "description": "We stay ahead of the curve by adopting the latest technologies and methodologies, enabling us to provide forward-thinking solutions that keep your business competitive."
        },
        {
            "title": "Commitment to Excellence",
            "description": "Our dedication to quality and customer satisfaction ensures that we deliver exceptional services and support throughout your journey with us."
        }
    ]
    
    cols = st.columns(2)
    for idx, reason in enumerate(reasons):
        with cols[idx % 2]:
            st.markdown(f"### {reason['title']}")
            st.markdown(reason["description"])

# Testimonials Section
def testimonials_section():
    st.markdown("<div class='section' id='testimonials'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Testimonials</h2>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>What Our Clients Say</div>", unsafe_allow_html=True)
    
    testimonials = [
        {
            "quote": "Fintastic Data transformed our data management processes, allowing us to make more informed decisions and significantly improve our operational efficiency.",
            "author": "Jane Doe, CEO of TechCorp"
        },
        {
            "quote": "The AI solutions provided by Fintastic Data have revolutionized our marketing strategies, leading to a substantial increase in customer engagement and sales.",
            "author": "John Smith, Marketing Director at RetailHub"
        },
        {
            "quote": "Their team is knowledgeable, responsive, and truly invested in our success. We couldn't be happier with the results.",
            "author": "Emily Clark, Head of Operations at FinancePlus"
        }
    ]
    
    for testimonial in testimonials:
        st.markdown("<div class='testimonial'>", unsafe_allow_html=True)
        st.markdown(f"> \"{testimonial['quote']}\"")
        st.markdown(f"— **{testimonial['author']}**")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("")

# Our Process Section
def process_section():
    st.markdown("<div class='section' id='process'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Our Process</h2>", unsafe_allow_html=True)
    
    process_steps = [
        {
            "title": "Consultation",
            "description": "We begin by understanding your business needs, challenges, and goals to identify the best solutions tailored for you."
        },
        {
            "title": "Strategy Development",
            "description": "Our experts design a strategic roadmap that outlines the implementation of AI, data solutions, and automation to achieve your objectives."
        },
        {
            "title": "Implementation",
            "description": "We deploy the chosen solutions, ensuring seamless integration with your existing systems and processes."
        },
        {
            "title": "Optimization",
            "description": "Post-deployment, we continuously monitor and optimize the solutions to ensure sustained performance and value."
        },
        {
            "title": "Support",
            "description": "Our dedicated support team is always available to assist you, ensuring your solutions remain effective and up-to-date."
        }
    ]
    
    cols = st.columns(3)
    for idx, step in enumerate(process_steps):
        with cols[idx % 3]:
            st.markdown(f"### {step['title']}")
            st.markdown(step["description"])

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
            # Here you can integrate with an email service or a database
            st.success("Thank you for reaching out! We will get back to you shortly.")
    
    # Contact Details
    st.markdown("<h4>Contact Details:</h4>", unsafe_allow_html=True)
    st.markdown("- **Email:** [info@fintasticdata.com](mailto:info@fintasticdata.com)")
    st.markdown("- **Phone:** +1 (234) 567-890")
    st.markdown("- **Address:** 123 Data Lane, Tech City, TX 78910")
    
    # Social Media Links
    st.markdown("<h4>Follow Us:</h4>", unsafe_allow_html=True)
    st.markdown(
        """
        - [LinkedIn](#)
        - [Twitter](#)
        - [Facebook](#)
        - [Instagram](#)
        """,
        unsafe_allow_html=True
    )
    
    # Newsletter Signup
    st.markdown("<h4>Newsletter Signup:</h4>", unsafe_allow_html=True)
    with st.form("newsletter_form", clear_on_submit=True):
        email_news = st.text_input("Enter your email address")
        subscribe = st.form_submit_button("Subscribe")
        if subscribe:
            # Integrate with a mailing list service
            st.success("Thank you for subscribing!")

# Footer Section
def footer_section():
    st.markdown("<div class='footer'>", unsafe_allow_html=True)
    st.markdown("<p>© 2025 Fintastic Data. All rights reserved.</p>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
            <a href="#">Privacy Policy</a> | 
            <a href="#">Terms of Service</a> | 
            <a href="#">Sitemap</a>
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<p>Powered by [Your Company/Platform]</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Main App Layout
def main():
    header_section()
    about_us_section()
    services_section()
    ai_products_section()
    why_choose_us_section()
    testimonials_section()
    process_section()
    contact_section()
    footer_section()

if __name__ == "__main__":
    main()
