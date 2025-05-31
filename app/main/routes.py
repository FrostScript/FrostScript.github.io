from flask import render_template, request, current_app, abort
from app.main import bp
from app.models import Post, Category, Tag
from app import cache

@bp.route('/')
@bp.route('/index')
@cache.cached(timeout=300)
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(published=True)\
        .order_by(Post.created_at.desc())\
        .paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'])
    return render_template('index.html', posts=posts)

@bp.route('/post/<slug>')
@cache.cached(timeout=300)
def post(slug):
    post = Post.query.filter_by(slug=slug, published=True).first_or_404()
    return render_template('post.html', post=post)

@bp.route('/category/<slug>')
@cache.cached(timeout=300)
def category(slug):
    category = Category.query.filter_by(slug=slug).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = category.posts.filter_by(published=True)\
        .order_by(Post.created_at.desc())\
        .paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'])
    return render_template('category.html', category=category, posts=posts)

@bp.route('/tag/<slug>')
@cache.cached(timeout=300)
def tag(slug):
    tag = Tag.query.filter_by(slug=slug).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = tag.posts.filter_by(published=True)\
        .order_by(Post.created_at.desc())\
        .paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'])
    return render_template('tag.html', tag=tag, posts=posts)

@bp.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return render_template('search.html', posts=None)
    posts = Post.query.filter(
        Post.title.ilike(f'%{query}%') | 
        Post.content.ilike(f'%{query}%')
    ).filter_by(published=True).all()
    return render_template('search.html', posts=posts, query=query) 