Deploying this widgets so that there is a stream-lit way of getting the file metadata.\
Dependency:\
  1 python version <3.13 which is properly configured with tkinter.\
  2 Tested version for mac is 3.9 python with properly configured tkinter.\
Constraints on usability:\
  1 Currently not able to use the widget with st.forms.\
\
Example code:\
  import streamlit as st\
  from CutstomWidgetLoader.CustomWidgetLoaderUpload import file_upload_widget\
\
  def main():\
   st.title("File Upload Example")\
   # Call the file upload widget function
   values=file_upload_widget()  \
   return values\
\
if __name__ == "__main__":\
 a=main()

\
Photo Sample:\
  !["Uploader Widget"](https://github.com/suprithvasista/StreamLitCustomWidgetUploader/blob/main/Uploader_button.png?raw=true)
