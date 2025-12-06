---
title: Hexo 使用完整指南
date: 2025-11-20 16:00:00
tags: [Hexo, 静态博客, 教程]
categories: 技术教程
---

# Hexo 使用完整指南

Hexo 是一个快速、简洁且高效的博客框架，它基于 Node.js 开发，能够帮助你轻松地创建个人博客网站。本文将带你从零开始搭建和使用 Hexo 博客。

## 一、环境准备

在开始使用 Hexo 之前，需要先安装以下软件：

1. [Node.js](https://nodejs.org/) (建议版本 12.0 及以上)
2. Git

检查是否已安装：

```bash
node -v
npm -v
git --version
```

## 二、安装 Hexo

使用 npm 安装 Hexo CLI 工具：

```bash
npm install -g hexo-cli
```

## 三、初始化博客

创建博客目录并初始化：

```bash
hexo init <folder>
cd <folder>
npm install
```

或者在现有空目录中初始化：

```bash
cd <existing-folder>
hexo init .
npm install
```

## 四、目录结构

初始化完成后，你会看到如下目录结构：

```
.
├── _config.yml       # 站点配置文件
├── package.json      # 应用数据
├── scaffolds         # 模板文件夹
├── source            # 资源文件夹
|   ├── _drafts       # 草稿
|   └── _posts        # 文章
└── themes            # 主题文件夹
```

## 五、基本操作

### 1. 新建文章

```bash
hexo new "文章标题"
```

会在 `source/_posts` 目录下生成 Markdown 文件。

### 2. 新建页面

```bash
hexo new page "页面名称"
```

### 3. 本地预览

```bash
hexo server
# 或简写
hexo s
```

默认访问地址：http://localhost:4000/

### 4. 生成静态文件

```bash
hexo generate
# 或简写
hexo g
```

生成的静态文件会保存在 `public` 文件夹中。

### 5. 清除缓存

```bash
hexo clean
```

清除缓存文件 (`db.json`) 和已生成的静态文件 (`public`)。

## 六、部署发布

### 1. 配置部署参数

编辑 `_config.yml` 文件，添加部署设置：

```yaml
deploy:
  type: git
  repo: <repository url>
  branch: [branch]
```

### 2. 安装部署插件

```bash
npm install hexo-deployer-git --save
```

### 3. 一键部署

```bash
hexo deploy
# 或简写
hexo d
```

也可以生成并部署一起执行：

```bash
hexo generate --deploy
# 或
hexo deploy --generate
```

## 七、常用命令简写

| 命令                | 简写      | 说明         |
|---------------------|-----------|--------------|
| hexo generate       | hexo g    | 生成静态文件 |
| hexo server         | hexo s    | 启动服务     |
| hexo deploy         | hexo d    | 部署         |
| hexo clean          |           | 清除缓存     |
| hexo new            | hexo n    | 新建文章     |
| hexo help           | hexo h    | 帮助         |
| hexo version        | hexo v    | 版本信息     |

## 八、主题更换

### 1. 安装主题

可以通过 Git 安装主题：

```bash
git clone <theme-repo> themes/<theme-name>
```

或者使用 npm 安装：

```bash
npm install <theme-name> --save
```

### 2. 启用主题

修改 `_config.yml` 中的 `theme` 设置：

```yaml
theme: <theme-name>
```

### 3. 更新主题

如果是通过 Git 安装的主题：

```bash
cd themes/<theme-name>
git pull
```

## 九、写作语法

Hexo 支持 Markdown 语法，同时也支持一些特殊标记：

### 1. Front-matter

每篇文章顶部可以设置文章相关信息：

```yaml
---
title: 文章标题
date: 发布日期
tags: [标签1, 标签2]
categories: 分类
---
```

### 2. 摘要

使用 `<!-- more -->` 标记文章摘要：

```markdown
这是摘要部分
<!-- more -->
这是正文部分
```

### 3. 标签插件

Hexo 提供了一些内置标签插件：

```ejs
{% youtube video_id %}
{% img 图片地址 %}
```

## 十、优化技巧

1. **SEO优化**：合理设置标题、关键词和描述
2. **访问统计**：接入 Google Analytics 等统计工具
3. **评论系统**：集成 Disqus、Valine 等评论插件
4. **图片优化**：使用 CDN 加速图片加载
5. **代码高亮**：选择合适的代码主题

## 结语

通过本文档，你应该能够掌握 Hexo 的基本使用方法。更多详细信息请参考 [Hexo 官方文档](https://hexo.io/zh-cn/docs/)。开始你的博客之旅吧！