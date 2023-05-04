import pymongo
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

myclient = pymongo.MongoClient('mongodb://root:password@localhost:27017/')

mydb = myclient['mydatabse']
mycol = mydb['customers']

# i have already inserted into the database, do not need to keep inserting
#dict = {'name':'john', 'address':'highway'}
#x = mycol.insert_one()

print(myclient.list_database_names())

print(mycol.find_one())
print(type(mycol.find_one()))

#df = pd.DataFrame({'names': 'john', 'address' : '24'})

st.write('attempt at showing data')
# need the index parameter as i am only using 1 entry
st.write('showing 1 entry')
st.write(pd.DataFrame(mycol.find_one(), index = [0]))
# do not need the index parameter
st.write('showing all entries')
# with id
st.write(pd.DataFrame(mycol.find({})))
# projecting so that id doesnt show
st.write(pd.DataFrame(mycol.find({}, projection = {'_id': 0})))

# text input
name = st.text_input('name', "Name")
town = st.text_input('town', "Town")

age = st.number_input('age', 0, 100)

st.write(name, town, age)

### function to insert document into database
def mongoInput(name, town, age):
    inserted = mycol.insert_one({'name':name, 'city':town, 'age':age})
    return inserted
# button to insert
if st.button('insert'):
    st.write(mongoInput(name, town, age))
    st.experimental_rerun()

# testing to display a graph 
if st.button('display'):
    nameAge = mycol.find({}, projection = {'name':1, 'age':1, '_id':0})
    arr = []
    for doc in nameAge:
        arr.append(doc)
    st.write(pd.DataFrame(nameAge))

    print('name age') 
    print(arr)


