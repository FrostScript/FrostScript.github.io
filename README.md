# Flask 个人博客系统

一个使用 Flask 构建的现代化个人博客系统，支持 Markdown 编辑、分类标签、评论等功能。

## 功能特点

- 文章管理（发布、编辑、删除）
- Markdown 编辑器支持
- 文章分类与标签
- 用户认证系统
- 评论功能
- 响应式设计
- SEO 优化
- 代码高亮
- 图片懒加载
- 阅读进度条
- 暗色模式支持

## 技术栈

- Python 3.8+
- Flask
- SQLAlchemy
- Bootstrap 5
- EasyMDE (Markdown 编辑器)
- Highlight.js (代码高亮)

## 安装步骤

1. 克隆项目：

```bash
git clone https://github.com/yourusername/flask-blog.git
cd flask-blog
```

2. 创建虚拟环境：

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

4. 配置环境变量：

创建 `.env` 文件并添加以下配置：

```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///app.db
```

5. 初始化数据库：

```bash
flask db init
flask db migrate
flask db upgrade
```

6. 创建管理员用户：

```bash
flask shell
>>> from app import db
>>> from app.models import User
>>> admin = User(username='admin', email='admin@example.com', is_admin=True)
>>> admin.set_password('your-password')
>>> db.session.add(admin)
>>> db.session.commit()
```

7. 运行应用：

```bash
flask run
```

访问 http://localhost:5000 即可看到博客首页。

## 项目结构

```
flask-blog/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── main/
│   ├── auth/
│   ├── admin/
│   ├── static/
│   └── templates/
├── migrations/
├── tests/
├── venv/
├── .env
├── .gitignore
├── config.py
├── requirements.txt
└── README.md
```

## 使用说明

1. 访问 `/admin` 进入管理后台
2. 使用管理员账号登录
3. 创建分类和标签
4. 开始撰写文章

## 开发说明

- 使用 `flask db migrate` 创建数据库迁移
- 使用 `flask db upgrade` 应用数据库迁移
- 使用 `flask shell` 进入 Python 交互式环境

## 部署

1. 配置生产环境变量
2. 使用 Gunicorn 作为 WSGI 服务器
3. 配置 Nginx 作为反向代理
4. 启用 HTTPS

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License 