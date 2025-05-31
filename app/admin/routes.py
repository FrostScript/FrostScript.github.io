from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from app.admin import bp
from app.admin.forms import PostForm, CategoryForm, TagForm
from app.models import Post, Category, Tag
from app import db
from datetime import datetime

@bp.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        abort(403)
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('admin/dashboard.html', posts=posts)

@bp.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if not current_user.is_admin:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user,
            category=form.category.data,
            published=form.published.data
        )
        for tag in form.tags.data:
            post.tags.append(tag)
        db.session.add(post)
        db.session.commit()
        flash('文章已创建！')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/post_form.html', title='新建文章', form=form)

@bp.route('/post/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    if not current_user.is_admin:
        abort(403)
    post = Post.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        post.published = form.published.data
        post.tags = form.tags.data
        post.updated_at = datetime.utcnow()
        db.session.commit()
        flash('文章已更新！')
        return redirect(url_for('admin.dashboard'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.category.data = post.category
        form.published.data = post.published
        form.tags.data = post.tags
    return render_template('admin/post_form.html', title='编辑文章', form=form)

@bp.route('/post/<int:id>/delete', methods=['POST'])
@login_required
def delete_post(id):
    if not current_user.is_admin:
        abort(403)
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('文章已删除！')
    return redirect(url_for('admin.dashboard'))

@bp.route('/category/new', methods=['GET', 'POST'])
@login_required
def new_category():
    if not current_user.is_admin:
        abort(403)
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        flash('分类已创建！')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/category_form.html', title='新建分类', form=form)

@bp.route('/tag/new', methods=['GET', 'POST'])
@login_required
def new_tag():
    if not current_user.is_admin:
        abort(403)
    form = TagForm()
    if form.validate_on_submit():
        tag = Tag(name=form.name.data)
        db.session.add(tag)
        db.session.commit()
        flash('标签已创建！')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/tag_form.html', title='新建标签', form=form) 