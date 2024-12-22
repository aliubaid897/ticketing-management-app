# import streamlit as st
# import pandas as pd
# from datetime import date
# import mysql.connector

# # Database connection
# def get_connection():
#     return mysql.connector.connect(
#         host="localhost",   # Replace with your MySQL host
#         user="root",        # Replace with your MySQL username
#         password="password", # Replace with your MySQL password
#         database="ticketing_tool"
#     )

# # CRUD operations
# def create_ticket(title, description, status, priority, assigned_to):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         INSERT INTO tickets (title, description, status, priority, date, assigned_to)
#         VALUES (%s, %s, %s, %s, %s, %s)
#     """, (title, description, status, priority, date.today(), assigned_to))
#     conn.commit()
#     conn.close()

# def view_tickets():
#     conn = get_connection()
#     df = pd.read_sql("SELECT * FROM tickets", conn)
#     conn.close()
#     return df

# def update_ticket(ticket_id, status, priority):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         UPDATE tickets
#         SET status = %s, priority = %s
#         WHERE id = %s
#     """, (status, priority, ticket_id))
#     conn.commit()
#     conn.close()

# def delete_ticket(ticket_id):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM tickets WHERE id = %s", (ticket_id,))
#     conn.commit()
#     conn.close()

# # Streamlit app layout
# st.title("Ticketing Management Tool")

# # Create a new ticket
# st.header("Create New Ticket")
# with st.form("ticket_form"):
#     title = st.text_input("Title")
#     description = st.text_area("Description")
#     status = st.selectbox("Status", ["Open", "In-Progress", "Closed"])
#     priority = st.selectbox("Priority", ["Low", "Medium", "High"])
#     assigned_to = st.text_input("Assigned To")
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         create_ticket(title, description, status, priority, assigned_to)
#         st.success("Ticket Created!")

# # View tickets
# st.header("View Tickets")
# if st.checkbox("Show Tickets"):
#     tickets = view_tickets()
#     st.dataframe(tickets)

# # Update ticket
# st.header("Update Ticket")
# ticket_id = st.number_input("Enter Ticket ID to Update", min_value=1)
# new_status = st.selectbox("New Status", ["Open", "In-Progress", "Closed"])
# new_priority = st.selectbox("New Priority", ["Low", "Medium", "High"])
# if st.button("Update Ticket"):
#     update_ticket(ticket_id, new_status, new_priority)
#     st.success("Ticket Updated!")

# # Delete ticket
# st.header("Delete Ticket")
# ticket_id_to_delete = st.number_input("Enter Ticket ID to Delete", min_value=1)
# if st.button("Delete Ticket"):
#     delete_ticket(ticket_id_to_delete)
#     st.warning("Ticket Deleted!")

# from login import login

# import streamlit as st
# import pandas as pd
# from datetime import date
# import psycopg2
# from psycopg2 import sql

# # Database connection
# def get_connection():
#     return psycopg2.connect(
#         host="localhost",     # Replace with your PostgreSQL host
#         user="postgres",      # Replace with your PostgreSQL username
#         password="infotech@1",  # Replace with your PostgreSQL password
#         database="postgres" # Replace with your PostgreSQL database
#     )

# # CRUD operations
# def create_ticket(title, description, status, priority, category, assigned_to, due_date):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         INSERT INTO tickets (title, description, status, priority, category, assigned_to, date, due_date)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#     """, (title, description, status, priority, category, assigned_to, date.today(), due_date))
#     conn.commit()
#     cursor.close()
#     conn.close()

# def view_tickets():
#     conn = get_connection()
#     query = "SELECT * FROM tickets"
#     df = pd.read_sql_query(query, conn)
#     conn.close()
#     return df

# def update_ticket(ticket_id, status, priority, due_date):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         UPDATE tickets
#         SET status = %s, priority = %s, due_date = %s
#         WHERE id = %s
#     """, (status, priority, due_date, ticket_id))
#     conn.commit()
#     cursor.close()
#     conn.close()

# def delete_ticket(ticket_id):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM tickets WHERE id = %s", (ticket_id,))
#     conn.commit()
#     cursor.close()
#     conn.close()

# # Streamlit app layout
# st.set_page_config(page_title="Ticketing Management Tool", layout="centered", initial_sidebar_state="expanded")

# st.title("🎫 Ticketing Management Tool")
# st.subheader("Easily Manage Your Tickets with Enhanced Functionality")

# # Create a new ticket
# st.sidebar.header("Create New Ticket")
# with st.sidebar.form("ticket_form"):
#     title = st.text_input("Title")
#     description = st.text_area("Description")
#     category = st.selectbox("Category", ["Application Restoration", "Application Rejection", "Challan Uploading Issue", "Current Status of application", "File Transfer"])
#     status = st.selectbox("Status", ["Open", "In-Progress", "Closed"])
#     priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
#     assigned_to = st.text_input("Assigned To")
#     due_date = st.date_input("Due Date")
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         create_ticket(title, description, status, priority, category, assigned_to, due_date)
#         st.success("🎉 Ticket Created Successfully!")

# # View tickets
# st.header("📋 View All Tickets")
# if st.checkbox("Show Tickets"):
#     tickets = view_tickets()
#     st.dataframe(tickets)

# # Update ticket
# st.header("✏️ Update Ticket")
# ticket_id = st.number_input("Enter Ticket ID to Update", min_value=1, step=1)
# new_status = st.selectbox("New Status", ["Open", "In-Progress", "Closed"], key="update_status")
# new_priority = st.selectbox("New Priority", ["Low", "Medium", "High", "Critical"], key="update_priority")
# new_due_date = st.date_input("New Due Date", key="update_due_date")
# if st.button("Update Ticket"):
#     update_ticket(ticket_id, new_status, new_priority, new_due_date)
#     st.success("✅ Ticket Updated Successfully!")

# # Delete ticket
# st.header("🗑️ Delete Ticket")
# ticket_id_to_delete = st.number_input("Enter Ticket ID to Delete", min_value=1, step=1, key="delete_ticket_id")
# if st.button("Delete Ticket"):
#     delete_ticket(ticket_id_to_delete)
#     st.warning("🚫 Ticket Deleted!")

# # Footer
# st.sidebar.markdown("---")
# st.sidebar.info("Developed by Ubaid Ali")



#After adding login

# import streamlit as st
# import pandas as pd
# from datetime import date
# import psycopg2
# from psycopg2 import sql
# from io import BytesIO  # Import BytesIO for handling file download

# # Admin credentials
# ADMIN_USERNAME = "admin"
# ADMIN_PASSWORD = "admin123"

# # Database connection
# def get_connection():
#     return psycopg2.connect(
#         host="localhost",     # Replace with your PostgreSQL host
#         user="postgres",      # Replace with your PostgreSQL username
#         password="infotech@1",  # Replace with your PostgreSQL password
#         database="postgres"   # Replace with your PostgreSQL database
#     )

# # CRUD operations
# def create_ticket(title, description, status, service_name, priority, category, assigned_to, due_date):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         INSERT INTO tickets (title, description, status, service_name, priority, category, assigned_to, date, due_date)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """, (title, description, status, service_name, priority, category, assigned_to, date.today(), due_date))
#     conn.commit()
#     cursor.close()
#     conn.close()

# def view_tickets():
#     conn = get_connection()
#     query = "SELECT * FROM tickets"
#     df = pd.read_sql_query(query, conn)
#     conn.close()
#     return df

# def update_ticket(ticket_id, status, priority, due_date):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         UPDATE tickets
#         SET status = %s, priority = %s, due_date = %s
#         WHERE id = %s
#     """, (status, priority, due_date, ticket_id))
#     conn.commit()
#     cursor.close()
#     conn.close()

# def delete_ticket(ticket_id):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM tickets WHERE id = %s", (ticket_id,))
#     conn.commit()
#     cursor.close()
#     conn.close()

# # Admin authentication
# def authenticate(username, password):
#     """Authenticates admin credentials."""
#     return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

# # Streamlit app layout
# st.set_page_config(page_title="Ticketing Management Tool", layout="centered", initial_sidebar_state="expanded")

# # Initialize authentication state
# if "authenticated" not in st.session_state:
#     st.session_state.authenticated = False

# # Login page (instant login after submit or Enter press)
# # Login page (instant login after submit or Enter press)
# if not st.session_state.authenticated:
#     st.title("DDA-Ticket Register")
#     st.title("🔒 Admin Login")

#     def on_login_submit():
#         """Trigger login on Enter key press or form submission."""
#         username = st.session_state.username
#         password = st.session_state.password
#         if authenticate(username, password):
#             st.session_state.authenticated = True
#             st.success("✅ Login successful!")
#         else:
#             st.error("❌ Invalid credentials. Please try again.")

#     with st.form("login_form"):
#         # Capture username and password
#         username = st.text_input("Username", key="username")
#         password = st.text_input("Password", type="password", key="password")
        
#         # Simulate form submission when 'Enter' is pressed
#         login_button = st.form_submit_button("Login", on_click=on_login_submit)

#     # Using a fallback button outside the form is also an option.
#     # But we already trigger submit when "Enter" is pressed in form fields above.



# else:
#     # Main app after authentication
#     st.title("🎫 DDA Ticket Register Tool")
#     st.sidebar.header("Create New Ticket")
#     with st.sidebar.form("ticket_form"):
#         title = st.text_input("Issue Title")
#         description = st.text_area("Issue Description")
#         service = st.selectbox("Service Name", ["Housing","RWA","Addition and Alteration","Other"])
#         category = st.selectbox("Category", ["Application Restoration", "Application Rejection", "Challan Uploading Issue", "Current Status of application", "File Transfer", "Reset Password"])
#         status = st.selectbox("Status", ["Open", "In-Progress", "Closed"])
#         priority = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
#         assigned_to = st.text_input("Assigned To")
#         due_date = st.date_input("Due Date")
#         submitted = st.form_submit_button("Submit")
#         if submitted:
#               create_ticket(title, description, status, service, priority, category, assigned_to, due_date)
#     st.success("🎉 Ticket Created Successfully!")

#     # View tickets
#     st.header("📋 View All Tickets")
#     if st.checkbox("Show Tickets"):
#         tickets = view_tickets()
#         st.dataframe(tickets)

#         # Export tickets to Excel
#         st.subheader("🔽 Export Tickets to Excel")
#         if st.button("Download Excel"):
#             # Create a BytesIO buffer to save Excel in memory
#             excel_buffer = BytesIO()
#             tickets.to_excel(excel_buffer, index=False)  # Save the dataframe to Excel
#             excel_buffer.seek(0)
            
#             # Provide a download link
#             st.download_button(
#                 label="Download Excel file",
#                 data=excel_buffer,
#                 file_name="tickets_report.xlsx",
#                 mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             )

#     # Update ticket
#     st.header("✏️ Update Ticket")
#     ticket_id = st.number_input("Enter Ticket ID to Update", min_value=1, step=1)
#     new_status = st.selectbox("New Status", ["Open", "In-Progress", "Closed"], key="update_status")
#     new_priority = st.selectbox("New Priority", ["Low", "Medium", "High", "Critical"], key="update_priority")
#     new_due_date = st.date_input("New Due Date", key="update_due_date")
#     if st.button("Update Ticket"):
#         update_ticket(ticket_id, new_status, new_priority, new_due_date)
#         st.success("✅ Ticket Updated Successfully!")

#     # Delete ticket
#     st.header("🗑️ Delete Ticket")
#     ticket_id_to_delete = st.number_input("Enter Ticket ID to Delete", min_value=1, step=1, key="delete_ticket_id")
#     if st.button("Delete Ticket"):
#         delete_ticket(ticket_id_to_delete)
#         st.warning("🚫 Ticket Deleted!")

#     # Logout option
#     if st.sidebar.button("Logout"):
#         st.session_state.authenticated = False
#         st.experimental_rerun()

# # Footer
# from PIL import Image

# # Load the logo
# st.sidebar.markdown("---")
# logo = Image.open("image.png")

# # Display the logo with text in the sidebar
# st.sidebar.image(logo, caption="3i-Infotech", use_container_width=True)
# st.sidebar.markdown("---")
# st.sidebar.info("Developed by Ubaid Ali")


# Data Analysis

# import streamlit as st
# import pandas as pd
# from datetime import date
# import psycopg2
# from psycopg2 import sql
# from io import BytesIO
# import matplotlib.pyplot as plt

# # Admin credentials
# ADMIN_USERNAME = "admin"
# ADMIN_PASSWORD = "admin123"

# # Database connection
# def get_connection():
#     return psycopg2.connect(
#         host="localhost",     # Replace with your PostgreSQL host
#         user="postgres",      # Replace with your PostgreSQL username
#         password="infotech@1",  # Replace with your PostgreSQL password
#         database="postgres"   # Replace with your PostgreSQL database
#     )

# # CRUD operations
# def create_ticket(title, description, status, service_name, priority, category, assigned_to, due_date):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         INSERT INTO tickets (title, description, status, service_name, priority, category, assigned_to, date, due_date)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """, (title, description, status, service_name, priority, category, assigned_to, date.today(), due_date))
#     conn.commit()
#     cursor.close()
#     conn.close()

# def view_tickets():
#     conn = get_connection()
#     query = "SELECT * FROM tickets"
#     df = pd.read_sql_query(query, conn)
#     conn.close()
#     return df

# def update_ticket(ticket_id, status, priority, due_date):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         UPDATE tickets
#         SET status = %s, priority = %s, due_date = %s
#         WHERE id = %s
#     """, (status, priority, due_date, ticket_id))
#     conn.commit()
#     cursor.close()
#     conn.close()

# def delete_ticket(ticket_id):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM tickets WHERE id = %s", (ticket_id,))
#     conn.commit()
#     cursor.close()
#     conn.close()

# # Admin authentication
# def authenticate(username, password):
#     """Authenticates admin credentials."""
#     return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

# # Streamlit app layout
# st.set_page_config(page_title="Ticketing Management Tool", layout="centered", initial_sidebar_state="expanded")

# # Initialize authentication state
# if "authenticated" not in st.session_state:
#     st.session_state.authenticated = False

# if not st.session_state.authenticated:
#     st.title("DDA-Ticket Register")
#     st.title("🔒 Admin Login")

#     def on_login_submit():
#         """Trigger login on Enter key press or form submission."""
#         username = st.session_state.username
#         password = st.session_state.password
#         if authenticate(username, password):
#             st.session_state.authenticated = True
#             st.success("✅ Login successful!")
#         else:
#             st.error("❌ Invalid credentials. Please try again.")

#     with st.form("login_form"):
#         # Capture username and password
#         username = st.text_input("Username", key="username")
#         password = st.text_input("Password", type="password", key="password")
        
#         # Simulate form submission when 'Enter' is pressed
#         login_button = st.form_submit_button("Login", on_click=on_login_submit)

# else:
#     # Main app after authentication
#     st.title("🎫 DDA Ticket Register Tool")
#     st.sidebar.header("Create New Ticket")
#     with st.sidebar.form("ticket_form"):
#         title = st.text_input("Issue Title")
#         description = st.text_area("Issue Description")
#         service = st.selectbox("Service Name", ["Housing","RWA","Addition and Alteration","Other"])
#         category = st.selectbox("Category", ["Application Restoration", "Application Rejection", "Challan Uploading Issue", "Current Status of application", "File Transfer", "Reset Password"])
#         status = st.selectbox("Status", ["Open", "In-Progress", "Closed"])
#         priority = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
#         assigned_to = st.text_input("Assigned To")
#         due_date = st.date_input("Due Date")
#         submitted = st.form_submit_button("Submit")
#         if submitted:
#             create_ticket(title, description, status, service, priority, category, assigned_to, due_date)
#     st.success("🎉 Ticket Created Successfully!")

#     # View tickets
#     st.header("📋 View All Tickets")
#     if st.checkbox("Show Tickets"):
#         tickets = view_tickets()
#         st.dataframe(tickets)

#         # Export tickets to Excel
#         st.subheader("🔽 Export Tickets to Excel")
#         if st.button("Download Excel"):
#             excel_buffer = BytesIO()
#             tickets.to_excel(excel_buffer, index=False)
#             excel_buffer.seek(0)
            
#             st.download_button(
#                 label="Download Excel file",
#                 data=excel_buffer,
#                 file_name="tickets_report.xlsx",
#                 mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             )

#     # Data analysis (Bar chart)
#     st.header("📊 Data Analysis")
#     if st.button("Generate Data Analysis"):
#         tickets = view_tickets()
#         if not tickets.empty:
#             # Example: Bar chart for ticket status distribution
#             status_count = tickets["status"].value_counts()
#             priority_count = tickets["priority"].value_counts()

#             # Create the plot
#             fig, ax = plt.subplots(1, 2, figsize=(12, 5))

#             # Status Distribution Bar Chart
#             ax[0].bar(status_count.index, status_count.values, color='skyblue')
#             ax[0].set_title("Tickets by Status")
#             ax[0].set_xlabel("Status")
#             ax[0].set_ylabel("Number of Tickets")

#             # Priority Distribution Bar Chart
#             ax[1].bar(priority_count.index, priority_count.values, color='lightgreen')
#             ax[1].set_title("Tickets by Priority")
#             ax[1].set_xlabel("Priority")
#             ax[1].set_ylabel("Number of Tickets")

#             # Show the plot in Streamlit
#             st.pyplot(fig)

#     # Update ticket
#     st.header("✏️ Update Ticket")
#     ticket_id = st.number_input("Enter Ticket ID to Update", min_value=1, step=1)
#     new_status = st.selectbox("New Status", ["Open", "In-Progress", "Closed"], key="update_status")
#     new_priority = st.selectbox("New Priority", ["Low", "Medium", "High", "Critical"], key="update_priority")
#     new_due_date = st.date_input("New Due Date", key="update_due_date")
#     if st.button("Update Ticket"):
#         update_ticket(ticket_id, new_status, new_priority, new_due_date)
#         st.success("✅ Ticket Updated Successfully!")

#     # Delete ticket
#     st.header("🗑️ Delete Ticket")
#     ticket_id_to_delete = st.number_input("Enter Ticket ID to Delete", min_value=1, step=1, key="delete_ticket_id")
#     if st.button("Delete Ticket"):
#         delete_ticket(ticket_id_to_delete)
#         st.warning("🚫 Ticket Deleted!")

#     # Logout option
#     if st.sidebar.button("Logout"):
#         st.session_state.authenticated = False
#         st.experimental_rerun()

# # Footer
# from PIL import Image

# # Load the logo
# st.sidebar.markdown("---")
# logo = Image.open("image.png")

# # Display the logo with text in the sidebar
# st.sidebar.image(logo, caption="3i-Infotech", use_container_width=True)
# st.sidebar.markdown("---")
# st.sidebar.info("Developed by Ubaid Ali")

import streamlit as st
import pandas as pd
from datetime import date
import psycopg2
from psycopg2 import sql
from io import BytesIO
import matplotlib.pyplot as plt
import re

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Database connection
def get_connection():
    return psycopg2.connect(
        host="localhost",  # Replace with your PostgreSQL host
        user="postgres",  # Replace with your PostgreSQL username
        password="infotech@1",  # Replace with your PostgreSQL password
        database="postgres"  # Replace with your PostgreSQL database
    )

# CRUD operations
def create_ticket(application_no, title, description, status, service_name, priority, category, assigned_to, due_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tickets (application_no,title, description, status, service_name, priority, category, assigned_to, date, due_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (application_no, title, description, status, service_name, priority, category, assigned_to, date.today(), due_date))
    conn.commit()
    cursor.close()
    conn.close()

def view_tickets():
    conn = get_connection()
    query = "SELECT * FROM tickets"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def update_ticket(ticket_id, status, priority, due_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tickets
        SET status = %s, priority = %s, due_date = %s
        WHERE id = %s
    """, (status, priority, due_date, ticket_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_ticket(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE id = %s", (ticket_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Admin authentication
def authenticate(username, password):
    """Authenticates admin credentials."""
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

# Streamlit app layout
st.set_page_config(page_title="Ticketing Management Tool", layout="centered", initial_sidebar_state="expanded")

# Initialize authentication state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("DDA-Ticket Register")
    st.title("🔒 Admin Login")

    def on_login_submit():
        """Trigger login on Enter key press or form submission."""
        username = st.session_state.username
        password = st.session_state.password
        if authenticate(username, password):
            st.session_state.authenticated = True
            st.success("✅ Login successful!")
        else:
            st.error("❌ Invalid credentials. Please try again.")

    with st.form("login_form"):
        # Capture username and password
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        
        # Simulate form submission when 'Enter' is pressed
        login_button = st.form_submit_button("Login", on_click=on_login_submit)

else:
    # Load the logo
    from PIL import Image
    logo = Image.open("image.png")

# Display the logo at the top of the sidebar
    st.sidebar.image(logo, caption="DDA Project", use_container_width=True)
    st.sidebar.markdown("---")
    # Main app after authentication
    st.title("🎫 DDA Ticket Register Tool")
    st.sidebar.header("Create New Ticket")
    
    with st.sidebar.form("ticket_form"):
        application_no = st.text_input("Application Number") #error in this line
        title = st.text_input("Issue Title")
        description = st.text_area("Issue Description")
        service = st.selectbox("Service Name", ["Housing", "RWA", "Addition and Alteration", "Other"])
        category = st.selectbox("Category", ["Application Restoration", "Application Rejection", "Challan Uploading Issue", "Current Status of application", "File Transfer", "Reset Password"])
        status = st.selectbox("Status", ["Open", "In-Progress", "Closed"])
        priority = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
        assigned_to = st.text_input("Assigned To")
        due_date = st.date_input("Due Date")
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            create_ticket(application_no, title, description, status, service, priority, category, assigned_to, due_date)
            st.success("🎉 Ticket Created Successfully!")

    # View tickets
    st.header("📋 View All Tickets")
    if st.checkbox("Show Tickets"):
        tickets = view_tickets()
        st.dataframe(tickets)

        # Export tickets to Excel
        st.subheader("🔽 Export Tickets to Excel")
        if st.button("Download Excel"):
            excel_buffer = BytesIO()
            tickets.to_excel(excel_buffer, index=False)
            excel_buffer.seek(0)
            
            st.download_button(
                label="Download Excel file",
                data=excel_buffer,
                file_name="tickets_report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    # Data analysis (Bar chart)
    st.header("📊 Data Analysis")
    if st.button("Generate Data Analysis"):
        tickets = view_tickets()
        if not tickets.empty:
            # Example: Bar chart for ticket status distribution
            status_count = tickets["status"].value_counts()
            priority_count = tickets["priority"].value_counts()

            # Create the plot
            fig, ax = plt.subplots(1, 2, figsize=(12, 5))

            # Status Distribution Bar Chart
            ax[0].bar(status_count.index, status_count.values, color='skyblue')
            ax[0].set_title("Tickets by Status")
            ax[0].set_xlabel("Status")
            ax[0].set_ylabel("Number of Tickets")

            # Priority Distribution Bar Chart
            ax[1].bar(priority_count.index, priority_count.values, color='lightgreen')
            ax[1].set_title("Tickets by Priority")
            ax[1].set_xlabel("Priority")
            ax[1].set_ylabel("Number of Tickets")

            # Show the plot in Streamlit
            st.pyplot(fig)

    # Update ticket
    st.header("✏️ Update Ticket")
    with st.form("update_ticket_form"):
        ticket_id = st.number_input("Enter Ticket ID to Update", min_value=1, step=1)
        new_status = st.selectbox("New Status", ["Open", "In-Progress", "Closed"], key="update_status")
        new_priority = st.selectbox("New Priority", ["Low", "Medium", "High", "Critical"], key="update_priority")
        new_due_date = st.date_input("New Due Date", key="update_due_date")
        
        update_button = st.form_submit_button("Update Ticket")
        if update_button:
            update_ticket(ticket_id, new_status, new_priority, new_due_date)
            st.success("✅ Ticket Updated Successfully!")

    # Delete ticket
    st.header("🗑️ Delete Ticket")
    with st.form("delete_ticket_form"):
        ticket_id_to_delete = st.number_input("Enter Ticket ID to Delete", min_value=1, step=1, key="delete_ticket_id")
        
        delete_button = st.form_submit_button("Delete Ticket")
        if delete_button:
            delete_ticket(ticket_id_to_delete)
            st.warning("🚫 Ticket Deleted!")

    # Logout option
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.experimental_rerun()

# Footer
from PIL import Image

# Load the logo
st.sidebar.markdown("---")
logo = Image.open("image.png")

#Display the logo with text in the sidebar
st.sidebar.image(logo, caption="DDA Project", use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.info("Developed by Ubaid Ali")
