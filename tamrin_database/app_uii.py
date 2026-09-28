import streamlit as st
import app_dbb

st.title('STREAMLIT DATABASE UI')

option = st.sidebar.selectbox('Select Your Option: ',
                    ('select_record_by_title',
                     'select_record_by_imdb_rate',
                     'delete_record_by_title',
                     'update_record_by_title'))


if option == 'select_record_by_title':
    
    search_title = st.text_input('Enter Record title:')
    if st.button('FIND RECORD'):
        record = app_dbb.select_record_by_title(search_title)
        st.write(record)
        
elif option == 'select_record_by_imdb_rate':
    
    search_imdb_rate = st.number_input('Enter Record imdb_rate:', min_value=0.0, max_value=10.0, step=0.1   )
    if st.button('FIND RECORD'):
        record = app_dbb.select_record_by_imdb_rate(search_imdb_rate)
        st.write(record)        
        

elif option == 'update_record_by_title':
    
    update_title = st.text_input('Enter Record title to Update:',)
    new_year = st.text_input('Enter New Year:')
    new_country = st.text_input('Enter New country:')
    new_imdb = st.number_input('Enter New IMDb Rating:', min_value=0.0, max_value=10.0, step=0.1)
    
    if st.button('UPDATE RECORD'):
        app_dbb.update_record_by_title(update_title, new_year,new_country , new_imdb)
        st.success(f"Record title {update_title} updated successfully!")

elif option == 'delete_record_by_title':
    
    delete_title = st.text_input('Enter Record title to Delete:')
    if st.button('DELETE RECORD'):
        
        msg = app_dbb.delete_record_by_title(delete_title)
        st.success(msg)
