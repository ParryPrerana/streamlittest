import streamlit as st
import os
import pandas as pd
import sqlite3
import io
from azure.ai.formrecognizer import DocumentModelAdministrationClient
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ResourceNotFoundError
from PIL import Image
import toml



# Main Streamlit app
def main():
    st.set_page_config(page_title="KPMG Contract RDE Extracter", layout="wide")
    st.write("Hello world")



if __name__ == "__main__":
    main()
