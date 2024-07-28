import streamlit as st
import requests
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection and model definition
Base = declarative_base()


class CatFact(Base):
    __tablename__ = 'cat_facts'

    id = Column(Integer, primary_key=True)
    fact = Column(String)



# Create SQLite database
engine = create_engine('sqlite:///cat_facts.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()


def fetch_cat_facts():
    """Fetch cat facts from the API."""
    url = "https://cat-fact.herokuapp.com/facts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API request failed. Status code: {response.status_code}")
        return None


def save_cat_facts(facts):
    """Save cat facts to the database."""
    for fact in facts:
        new_fact = CatFact(fact=fact['text'])
        session.add(new_fact)
    session.commit()


def display_cat_facts():
    """Display cat facts from the database."""
    facts = session.query(CatFact).all()
    for fact in facts:
        st.write(f"Fact {fact.id}: {fact.fact} ")


def main():
    st.title("Cat Facts Application")

    if st.button("Fetch and Save New Cat Facts"):
        facts = fetch_cat_facts()
        if facts:
            save_cat_facts(facts)

    if st.button("Display Cat Facts from Database"):
        display_cat_facts()

    session.close()


if __name__ == "__main__":
    main()