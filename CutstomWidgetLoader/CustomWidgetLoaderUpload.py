import streamlit as st
import subprocess
import os


def run_script(a):
    current_script = os.path.abspath(__file__)
    script_directory = os.path.dirname(current_script)
    result = subprocess.run(['python', script_directory + '/' + 'File_dialog_box.py'], capture_output=True, text=True)

    if result.returncode != 0:
        a.error(f"Error occurred while loading file: {result.stderr.strip() or result.stdout.strip()}")
        return ()

    output = result.stdout.strip()
    if output and result.returncode == 0:
        return eval(output)  # Be cautious with eval
    return ()


def file_upload_widget():
    """Creates a file upload widget and displays uploaded files."""
    con = st.container(border=True)
    con_1 = st.container(border=False)
    with con:
        # Upload section
        col1, col2 = st.columns([10, 1], vertical_alignment="center")
        with col1:
            st.subheader("Click :open_file_folder: to attach files", anchor=False)
        with col2:
            if st.button(':open_file_folder:', use_container_width=False):
                fil_paths = run_script(con_1)
                if 'key' not in st.session_state and len(fil_paths) >= 1:
                    st.session_state.key = 'Files_Uploaded'
                if 'File_uploaded' not in st.session_state:
                    st.session_state.File_uploaded = fil_paths
                elif len(fil_paths) >= 1:
                    st.session_state.File_uploaded = fil_paths  # '+' Append new files

    # Display uploaded files
    try:
        if st.session_state.key == 'Files_Uploaded':
            fil_paths = st.session_state['File_uploaded']
            if fil_paths:
                conn = st.container(height=150, border=False)
                with conn:
                    col1, col2 = st.columns([10, 1], gap="medium", vertical_alignment="center")
                    j = 0
                    for i in fil_paths:
                        with col1:
                            st.markdown("""
                            <style>
                                write {
                                    height:5px;
                                }
                            </style>
                            """, unsafe_allow_html=True)
                            st.write(':page_facing_up:', i)
                        with col2:
                            a = st.button('x', key=j, use_container_width=False)
                            if a:
                                call_back_values(j)
                                st.rerun()
                        j = j + 1
                return fil_paths
            else:
                return ()
        return ()
    except Exception as e:
        #print("Error", e)
        print('NO Files')


def call_back_values(number):
    """Removes a file from the uploaded list."""
    final_list = list(st.session_state['File_uploaded'])
    if 0 <= number < len(final_list):
        final_list.pop(number)
    if final_list:
        st.session_state.File_uploaded = tuple(final_list)
    else:
        del st.session_state['File_uploaded']
