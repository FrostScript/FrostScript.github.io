# 个人静态博客网站

这是一个使用HTML5、CSS3和JavaScript构建的现代化个人静态博客网站。

## 功能特点

### 文章管理
- 支持 Markdown 编辑器（EasyMDE）
- 文章发布、编辑、删除
- 文章分类与标签管理
- 草稿箱和自动保存功能
- 文章列表分页和筛选

### 后台管理
- 简洁的管理界面
- 文章管理面板
- 分类和标签管理
- 评论管理
- 系统设置

### 内容展示
- 响应式设计（适配手机和电脑）
- 文章列表页（分页、按分类/标签筛选）
- 文章详情页（标题、发布时间、作者、正文）
- 文章导航（上一篇/下一篇）

### 社交功能
- 文章分享（微信、微博、Twitter）
- 评论系统（集成 Disqus）
- 社交媒体链接

### SEO优化
- 自定义文章URL
- 页面标题和元描述
- 文章分类和标签

## 项目结构

```
.
├── index.html          # 主页
├── post.html          # 文章详情页模板
├── admin/
│   └── index.html     # 后台管理界面
├── styles/
│   ├── main.css      # 主样式文件
│   └── admin.css     # 后台管理样式
├── js/
│   ├── main.js       # 主JavaScript文件
│   ├── admin.js      # 后台管理脚本
│   └── post.js       # 文章详情页脚本
└── README.md         # 项目说明文件
```

## 技术栈

- HTML5
- CSS3
- JavaScript (ES6+)
- Markdown 编辑器 (EasyMDE)
- Markdown 渲染器 (marked.js)
- Font Awesome 图标
- Disqus 评论系统

## 使用方法

1. 克隆仓库到本地
2. 使用任意静态文件服务器运行项目
3. 访问 `admin/index.html` 进入后台管理界面
4. 使用 Markdown 编辑器编写文章
5. 设置文章分类和标签
6. 发布或保存为草稿

## 数据存储

目前使用 localStorage 存储文章数据，包括：
- 已发布的文章
- 草稿箱
- 分类和标签

## 自定义

- 修改 `index.html` 中的内容
- 在 `styles/main.css` 中调整样式
- 在 `js/main.js` 中添加新的交互功能
- 在 `admin/index.html` 中自定义后台界面
- 在 `styles/admin.css` 中调整后台样式

## 待实现功能

- [ ] 用户认证系统
- [ ] 数据库存储
- [ ] 图片上传功能
- [ ] 高级权限管理
- [ ] 文章统计功能
- [ ] 生成 sitemap.xml
- [ ] 评论反垃圾机制

## 许可证

MIT License 