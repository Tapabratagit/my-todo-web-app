import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_to_add = st.session_state['new_todo'] + '\n'
    todos.append(todo_to_add)
    functions.write_todos(todos)


st.title("My Todo app")
st.subheader("This is my todo app.")
st.write("This app is to bust your productivity.")

for index, todo in enumerate(todos):
    st.checkbox(todo, key=todo)
    if st.session_state[todo]:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label='', placeholder='Add new todo....',
              on_change=add_todo, key='new_todo')
