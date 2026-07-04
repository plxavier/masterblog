import json
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

POSTS_FILE_NAME = 'posts.json'
app = Flask(__name__)


#helper functions

def load_posts():
    """
    Load blog posts from the JSON file.
    Returns:
        list[dict]: A list of posts, each represented as a dictionary.
    """
    try:
        with open(POSTS_FILE_NAME, "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except Exception as error:
        print(f"Error loading posts: {error}")
        return []


def save_posts(posts):
    """
    Save the list of blog posts to the JSON file.
    Args:
        posts (list): List of post dictionaries to save.
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(POSTS_FILE_NAME, 'w', encoding='UTF-8') as file:
            json.dump(posts, file, ensure_ascii=False, indent=2)
        return True
    except Exception as error:
        print(f"Error saving posts: {error}")
        return False


def fetch_post_by_id(posts, post_id):
    """
    Find and return a blog post by its ID.
    Args:
        posts (list): List of posts.
        post_id (int): ID of the post to find.
    Returns:
        dict or None: The post if found, otherwise None.
    """
    try:
        post = next((post for post in posts if post['id'] == post_id), None)
        return post
    except Exception as error:
        print(f"Error fetching post: {error}")
        return None


def get_next_id(posts):
    """
    Generate the next ID for a new post.
    Args:
        posts (list): List of existing posts.
    Returns:
        int: Next available ID.
    """
    try:
        return max((post['id'] for post in posts), default=0) + 1
    except Exception as error:
        print(f"Error generating next ID: {error}")
        return 1


#app_routes

@app.route('/')
def index():
    """
    Render the homepage with a list of all blog posts.
    Returns:
        Response: Rendered HTML page with blog posts.
    """
    try:
        blog_posts = load_posts()
        return render_template('index.html', posts=blog_posts)
    except Exception as error:
        print(f"Error rendering index: {error}")
        return render_template('error.html', message="Unable to load posts"), 500


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Handle adding a new blog post.
    GET:
        Render the 'add_post.html' template with the form.
    POST:
        Create a new post, save it, and redirect to the homepage.
    """
    try:
        if request.method == 'POST':
            try:
                posts = load_posts()

                # Validate form data
                title = request.form.get('title', '').strip()
                content = request.form.get('content', '').strip()
                author = request.form.get('author', '').strip()

                if not title or not content or not author:
                    return render_template('add_post.html',
                                           error="All fields are required!"), 400

                new_post = {
                    "id": get_next_id(posts),
                    "title": title,
                    "content": content,
                    "author": author
                }

                posts.append(new_post)

                if save_posts(posts):
                    return redirect(url_for('index'))
                else:
                    return render_template('add_post.html',
                                           error="Failed to save post. Please try again."), 500

            except Exception as error:
                print(f"Error processing POST request: {error}")
                return render_template('add_post.html',
                                       error=f"Error: {str(error)}"), 500

        return render_template('add_post.html')

    except Exception as error:
        print(f"Error rendering add page: {error}")
        return render_template('error.html', message="Unable to load add page"), 500


@app.route('/delete-post/<int:post_id>', methods=['POST'])
def delete(post_id):
    """
    Handle deleting a blog post by its ID.
    Args:
        post_id (int): ID of the post to delete
    Returns:
        Response: Redirect to homepage or error page.
    """
    try:
        posts = load_posts()
        post = fetch_post_by_id(posts, post_id)

        if post is None:
            return render_template('error.html', message=f"Post with ID {post_id} not found"), 404

        posts = [post for post in posts if post['id'] != post_id]

        if save_posts(posts):
            return redirect(url_for('index'))
        else:
            return render_template('error.html', message="Failed to delete post"), 500

    except Exception as error:
        print(f"Error deleting post {post_id}: {error}")
        return render_template('error.html', message=f"Error deleting post: {str(error)}"), 500


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Handle updating an existing blog post.
    GET:
        Render the 'update_post.html' template with current post data.
    POST:
        Update the post's fields, save changes, and redirect to homepage.
    """
    try:
        posts = load_posts()
        post = fetch_post_by_id(posts, post_id)

        if post is None:
            return render_template('error.html', message=f"Post with ID {post_id} not found"), 404

        if request.method == 'POST':
            try:
                # Validate form data
                title = request.form.get('title', '').strip()
                content = request.form.get('content', '').strip()
                author = request.form.get('author', '').strip()

                if not title or not content or not author:
                    return render_template('update_post.html',
                                           post=post,
                                           error="All fields are required!"), 400

                post['title'] = title
                post['content'] = content
                post['author'] = author

                if save_posts(posts):
                    return redirect(url_for('index'))
                else:
                    return render_template('update_post.html',
                                           post=post,
                                           error="Failed to update post. Please try again."), 500

            except Exception as error:
                print(f"Error updating post {post_id}: {error}")
                return render_template('update_post.html',
                                       post=post,
                                       error=f"Error: {str(error)}"), 500

        return render_template('update_post.html', post=post)

    except Exception as error:
        print(f"Error rendering update page: {error}")
        return render_template('error.html', message=f"Unable to load update page: {str(error)}"), 500


# ========== ERROR HANDLERS ==========

@app.errorhandler(404)
def not_found(error):
    """Handle 404 Not Found errors."""
    try:
        return render_template('error.html', message="Page not found"), 404
    except Exception:
        return "Page not found", 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 Internal Server errors."""
    try:
        return render_template('error.html', message="Internal server error. Please try again later."), 500
    except Exception:
        return "Internal server error", 500


@app.after_request
def add_header(response):
    """Add cache-control headers to prevent caching."""
    try:
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        return response
    except Exception as error:
        print(f"Error adding headers: {error}")
        return response


if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0", port=8001, debug=True)
    except Exception as error:
        print(f"Error starting server: {error}")
