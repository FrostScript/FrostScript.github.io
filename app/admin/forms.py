from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length
from app.models import Category, Tag

class PostForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), Length(min=1, max=200)])
    content = TextAreaField('内容', validators=[DataRequired()])
    category = SelectMultipleField('分类', coerce=int, validators=[DataRequired()])
    tags = SelectMultipleField('标签', coerce=int)
    published = BooleanField('发布')
    submit = SubmitField('提交')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.category.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
        self.tags.choices = [(t.id, t.name) for t in Tag.query.order_by('name')]

class CategoryForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('提交')

class TagForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('提交') 