# 📝 Masterblog - A Flask Blog Application

A simple, lightweight blog application built with Flask where users can create, read, update, and delete blog posts.

## ✨ Features

- **Create** new blog posts with title, author, and content
- **Read** all blog posts on the homepage
- **Update** existing posts
- **Delete** posts with confirmation
- **JSON file storage** - posts are saved in `posts.json`
- **Clean, responsive UI** with custom CSS styling
- **Error handling** with custom error pages

## 🛠️ Technologies Used

- **Python 3.x**
- **Flask** - Web framework
- **HTML5 & CSS3** - Frontend styling
- **JSON** - Data storage
- **Jinja2** - Template rendering

## 📁 Project Structure
masterblog/
├── app.py # Main Flask application
├── posts.json # Blog posts data (auto-generated)
├── posts_template.json # Template for data structure
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
├── static/
│ └── style.css # Custom CSS styles
└── templates/
├── index.html # Homepage with all posts
├── add_post.html # Add new post form
├── update_post.html # Edit post form
└── error.html # Custom error page


## Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd masterblog

```

### 2. Run the application
python app.py




