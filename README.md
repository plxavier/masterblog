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

```
masterblog/
├── app.py                 # Main Flask application
├── posts.json             # Blog posts data (auto-generated)
├── posts_template.json    # Template for data structure
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── static/
│   └── style.css         # Custom CSS styles
└── templates/
    ├── index.html        # Homepage with all posts
    ├── add_post.html     # Add new post form
    ├── update_post.html  # Edit post form
    └── error.html        # Custom error page
```

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/masterblog.git
cd masterblog
```

### 2. Create a virtual environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask flask-cors
```

Or use `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

## 📋 Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Homepage - view all posts |
| `/add` | GET/POST | Add a new post |
| `/update/<id>` | GET/POST | Update a post |
| `/delete-post/<id>` | POST | Delete a post |

## 💡 Usage Examples

### Adding a Post

1. Click "Add New Post"
2. Fill in Title, Author, and Content
3. Click "Add Post"

### Updating a Post

1. Click "Update" on any post
2. Edit the fields
3. Click "Update Post"

### Deleting a Post

1. Click "Delete" on any post
2. Confirm deletion

## 📝 Data Structure

Each blog post follows this structure:

```json
{
    "id": 1,
    "title": "Post Title",
    "author": "Author Name",
    "content": "Post content goes here..."
}
```



