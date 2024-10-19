import streamlit as st
from CutstomWidgetLoader.CustomWidgetLoaderUpload import file_upload_widget


def main():
    st.title("File Upload Example")

    values=file_upload_widget()  # Call the file upload widget function
    return values

if __name__ == "__main__":
    a=main()
