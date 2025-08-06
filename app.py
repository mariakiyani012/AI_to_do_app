import streamlit as st
from db.database import init_db, add_task_to_db, get_all_tasks, mark_task_complete, update_translation
from services.groq_service import generate_subtasks, translate_task
import json

# Hide Streamlit's menu and footer
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center;'>AI-Powered To-Do Application</h1>", unsafe_allow_html=True)
init_db()

# --------------------- Add New Task Section ---------------------
st.header("Add a New To-Do Item")

# Input box and button
new_task = st.text_input("Enter a new task:")

if st.button("Add Task"):
    if new_task.strip():
        # Generate subtasks using Groq service
        subtasks = generate_subtasks(new_task)
        # Add task to the database
        add_task_to_db(new_task, subtasks)
        st.session_state.task_added = True
        st.rerun()
    else:
        # Display error toast if task is empty
        st.toast("🚫 Task cannot be empty.")

# Display success toast (on rerun)
if st.session_state.get("task_added"):
    st.toast("✅ Task added successfully!")
    st.session_state.task_added = False


# --------------------- Task Manager Section  ---------------------


st.header("Task Manager")
# Expander for viewing all tasks
with st.expander("View All Tasks"):
    # Fetch all tasks from the database
    tasks = get_all_tasks()
    # If no tasks are found, display an info message
    if not tasks:
        st.info("No tasks found. Add a new one above!")
    else:
        # Loop through each task and display its details
        for task in tasks:
            task_id, task_text, subtasks, completed, translated_task, language = task
            
            # Display task details in an expander
            with st.expander(f"{task_text}"):
                st.markdown("**Subtasks:**")
                for subtask in json.loads(subtasks or "[]"):
                    st.write(f"- {subtask}")
                
                # Display completion status
                st.write(f"Completed: {'✅' if completed else 'No'}")
                
                # Display translated task if available
                if translated_task:
                    st.write(f"Translated Task ({language}): `{translated_task}`")

                # Completion Option
                if not completed:
                    if st.button(f"Mark as Completed", key=f"complete_{task_id}"):
                        mark_task_complete(task_id)
                        st.rerun()

                # Translation Option
                lang_input = st.text_input(
                    f"Translate task to:",
                    key=f"lang_input_{task_id}"
                )
                if st.button(f"Translate", key=f"translate_btn_{task_id}"):
                    if lang_input:
                        translated = translate_task(task_text, lang_input)
                        update_translation(task_id, translated, lang_input)
                        st.toast(f"✅ Task translated to {lang_input}")
                        st.rerun()
                    else:
                        st.toast("🚫 Language cannot be empty.")
