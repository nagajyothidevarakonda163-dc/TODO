import streamlit as st

# Page title
st.set_page_config(page_title="To-Do List", page_icon="✅")

st.title("✅ My To-Do List")
st.write("Manage your daily tasks easily!")

# Create task list
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add task
st.subheader("Add a Task")

task = st.text_input("Enter your task:")

if st.button("➕ Add Task"):
    if task.strip() != "":
        st.session_state.tasks.append({
            "task": task,
            "completed": False
        })
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task.")

# Display tasks
st.subheader("📋 Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks yet. Add your first task!")

else:
    for i, item in enumerate(st.session_state.tasks):

        col1, col2 = st.columns([4, 1])

        with col1:
            completed = st.checkbox(
                item["task"],
                value=item["completed"],
                key=f"task_{i}"
            )

            st.session_state.tasks[i]["completed"] = completed

        with col2:
            if st.button("🗑️", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

# Clear completed tasks
if st.session_state.tasks:
    if st.button("🧹 Clear Completed Tasks"):
        st.session_state.tasks = [
            item for item in st.session_state.tasks
            if not item["completed"]
        ]
        st.rerun()