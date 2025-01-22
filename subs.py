import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timedelta


# Define the Customer table schema using SQLAlchemy ORM
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    mobile_number = Column(String(15), nullable=False, unique=True)
    email_id = Column(String(100), nullable=False, unique=True)
    event_name = Column(String(100), nullable=False)
    event_types = Column(String(500), nullable=False)
    contract_address = Column(String(500), nullable=False)
    token_id = Column(String(50), nullable=False)
    api_key = Column(String(500), nullable=False)
    frequency = Column(String(50), nullable=False)
    last_sent = Column(DateTime(timezone=True), nullable=True)
    next_due = Column(DateTime(timezone=True), nullable=True)

# Database connection
DATABASE_URL = "postgresql://kbm:U3dJbrL87alo4yx511FNhgWH95S79vQy@dpg-cu30knggph6c73blba00-a.oregon-postgres.render.com/apis_1i9f"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def insert_customer(data):
    """Insert data into the customers table."""
    session = SessionLocal()
    try:
        customer = Customer(
            name=data['name'],
            mobile_number=data['mobile_number'],
            email_id=data['email_id'],
            event_name=data['event_name'],
            event_types=data['event_types'],
            contract_address=data['contract_address'],
            token_id=data['token_id'],
            api_key=data['api_key'],
            frequency=data['frequency'],
            last_sent=datetime.now() - timedelta(days=1),  # Initially null
            next_due=datetime.now()  # Initially null
        )
        session.add(customer)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        st.error(f"Error inserting data: {e}")
        return False
    finally:
        session.close()


def subs():

    # Streamlit UI
    st.title("NFTs Predicted Price Alerts/Subscriptions")

    # Input fields for user data
    name = st.text_input("Name")
    mobile_number = st.text_input("Mobile Number (with code)")
    email_id = st.text_input("Enter the mail id ")
    contract_address = st.text_input("Contract Address")
    token_id = st.text_input("Token ID")
    api_key = st.text_input("API Key")
    frequency = st.text_input("Frequency (1 day)")

    if st.button("Submit"):
        if not (name and mobile_number  and contract_address and token_id and api_key and frequency and email_id):
            st.error("Please fill in all fields.")
        else:
            # Prepare the data dictionary
            customer_data = {
                'name': name,
                'mobile_number': mobile_number,
                'email_id': email_id,
                'event_name': 'reminder',
                'event_types': 'nfts',
                'contract_address': contract_address,
                'token_id': token_id,
                'api_key': api_key,
                'frequency': frequency
            }

            # Insert data into the database
            if insert_customer(customer_data):
                st.success("Data inserted successfully!")
