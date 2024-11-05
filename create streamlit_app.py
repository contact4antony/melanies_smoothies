# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
        """ Choose the fruit you want in your custom Smoothie!
    """
)

title = st.text_input("Name on Smoothie:", "")
st.write("The Name on the Smoothie will be:", title)

session = get_active_session()
df = session.table('SMOOTHIES.PUBLIC.FRUIT_OPTIONS').select(col('Fruit_Name'))
#st.dataframe(df,use_container_width=True)

ingredient_list = st.multiselect(
    'Choose up to 5 Ingerdients:',
    df, max_selections = 5
)

if ingredient_list:
    #st.write(ingredient_list)
    #st.text(ingredient_list)

    ingredients_string =''

    for selectedfruit in ingredient_list:
        ingredients_string+= selectedfruit + ' '
  
    if ingredients_string:
        my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
                values ('"""+  ingredients_string + """', '"""+ title + """')"""

        #st.write(my_insert_stmt)
        
        time_to_order = st.button('Submit Order!')

        if time_to_order:
            session.sql(my_insert_stmt).collect()
            st.success('Your smoothie is Ordered ' + title + '!', icon="✅")
