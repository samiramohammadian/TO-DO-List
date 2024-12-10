# Django To-Do List Project 📝

A simple and elegant **To-Do List** application built with Django. This project demonstrates how to build a task management system with the following features:

- **Add Tasks** ✍️
- **Edit Tasks** ✏️
- **Mark Tasks as Complete** ✅
- **Delete Tasks** 🗑️
- Modern **Dark Mode UI** 🌙

---

## 🖼️ Output Preview
<img width="1626" alt="Screenshot 1403-09-20 at 23 22 49" src="https://github.com/user-attachments/assets/e5dca9fd-c075-4df5-999f-3a7f0e4e5a53">

---

## 🚀 Features

1. **Add Tasks**: Easily create new tasks with a title and manage their completion status.
2. **Mark Tasks as Complete**: Check off tasks once they're done.
3. **Edit Tasks**: Update the title of tasks if needed.
4. **Delete Tasks**: Remove tasks when no longer needed.
5. **Dark Mode Design**: Beautiful UI with a dark theme that's easy on the eyes.

---

## 🛠️ Installation Instructions

Follow the steps below to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/todo_project.git
cd todo_project
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Libraries
```bash
pip install ...
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

### 6. Open in Browser
Visit the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 📋 Features in Detail

### 1. Add Tasks
- Create tasks by typing a title and clicking the "Add Task" button.
- Tasks are saved with their creation date.

### 2. Edit Tasks
- Update the title of tasks by clicking the "Edit" button.
- The application redirects you to an edit page where you can modify the task.

### 3. Mark Tasks as Complete
- Toggle the completion status of tasks by clicking the checkbox.

### 4. Delete Tasks
- Remove tasks by clicking the "Delete" button.

### 5. Responsive Dark Mode UI
- Clean and modern interface with a responsive design.
