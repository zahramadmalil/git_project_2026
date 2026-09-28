import streamlit as st
import app_db

st.title('STREAMLIT DATABASE UI')

option = st.sidebar.selectbox('Select Your Option: ',
                    ('SELECT ALL RECORDS',
                     'SELECT RECORD BY ID',
                     'INSERT RECORD',
                     'DELETE RECORD BY ID',
                     'UPDATE RECORD BY ID'))

if option == 'SELECT ALL RECORDS':
    if st.button('SHOW DATA'):
        result = app_db.select_all_records()
        st.write(result)

elif option == 'SELECT RECORD BY ID':
    
    search_id = st.number_input('Enter Record ID:', min_value=1, step=1)
    if st.button('FIND RECORD'):
        record = app_db.select_record_by_id(search_id)
        st.write(record)

elif option == 'INSERT RECORD':
    
    title = st.text_input('Movie Title:')
    year = st.text_input('Year:')
    country = st.text_input('Country:')
    imdb_rate = st.number_input('IMDb Rating:', min_value=0.0, max_value=10.0, step=0.1)
    
    if st.button('ADD MOVIE'):
        if title:
            app_db.insert_record(title, year, country, imdb_rate)
            st.success(f"Movie '{title}' added successfully!")
        else:
             st.error("Please fill in at least Title.")

elif option == 'UPDATE RECORD BY ID':
    
    update_id = st.number_input('Enter Record ID to Update:', min_value=1, step=1)
    new_year = st.text_input('Enter New Year:')
    new_imdb = st.number_input('Enter New IMDb Rating:', min_value=0.0, max_value=10.0, step=0.1)
    
    if st.button('UPDATE RECORD'):
        app_db.update_record_by_id(update_id, new_year, new_imdb)
        st.success(f"Record ID {update_id} updated successfully!")

elif option == 'DELETE RECORD BY ID':
    
    delete_id = st.number_input('Enter Record ID to Delete:', min_value=1, step=1)
    
    if st.button('DELETE RECORD', type='primary'):
        msg = app_db.delete_record_by_id(delete_id)
        st.success(msg)
