// 初始化 Markdown 编辑器
const easyMDE = new EasyMDE({
    element: document.getElementById('post-content'),
    spellChecker: false,
    autosave: {
        enabled: true,
        uniqueId: 'blog-post',
        delay: 1000,
    },
    toolbar: [
        'bold', 'italic', 'heading', '|',
        'quote', 'unordered-list', 'ordered-list', '|',
        'link', 'image', '|',
        'preview', 'side-by-side', 'fullscreen', '|',
        'guide'
    ]
});

// 侧边栏切换
document.getElementById('sidebar-toggle').addEventListener('click', function() {
    document.querySelector('.admin-sidebar').classList.toggle('active');
});

// 文章表单处理
const postForm = document.getElementById('post-form');
postForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = {
        title: document.getElementById('post-title').value,
        category: document.getElementById('post-category').value,
        tags: document.getElementById('post-tags').value.split(',').map(tag => tag.trim()),
        content: easyMDE.value(),
        status: 'published',
        publishDate: new Date().toISOString()
    };

    // 保存文章
    savePost(formData);
});

// 保存草稿
document.querySelector('.btn-draft').addEventListener('click', function() {
    const formData = {
        title: document.getElementById('post-title').value,
        category: document.getElementById('post-category').value,
        tags: document.getElementById('post-tags').value.split(',').map(tag => tag.trim()),
        content: easyMDE.value(),
        status: 'draft',
        lastModified: new Date().toISOString()
    };

    // 保存草稿
    saveDraft(formData);
});

// 保存文章到本地存储
function savePost(post) {
    const posts = JSON.parse(localStorage.getItem('blog-posts') || '[]');
    posts.push(post);
    localStorage.setItem('blog-posts', JSON.stringify(posts));
    
    // 更新文章列表
    updatePostList();
    
    // 清空表单
    postForm.reset();
    easyMDE.value('');
    
    // 显示成功消息
    showNotification('文章发布成功！');
}

// 保存草稿到本地存储
function saveDraft(draft) {
    const drafts = JSON.parse(localStorage.getItem('blog-drafts') || '[]');
    drafts.push(draft);
    localStorage.setItem('blog-drafts', JSON.stringify(drafts));
    
    // 显示成功消息
    showNotification('草稿保存成功！');
}

// 更新文章列表
function updatePostList() {
    const posts = JSON.parse(localStorage.getItem('blog-posts') || '[]');
    const tbody = document.querySelector('.post-table tbody');
    tbody.innerHTML = '';
    
    posts.forEach(post => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${post.title}</td>
            <td>${post.category}</td>
            <td>${post.tags.join(', ')}</td>
            <td>${new Date(post.publishDate).toLocaleDateString()}</td>
            <td>${post.status}</td>
            <td>
                <button class="btn-edit" onclick="editPost('${post.title}')">
                    <i class="fas fa-edit"></i>
                </button>
                <button class="btn-delete" onclick="deletePost('${post.title}')">
                    <i class="fas fa-trash"></i>
                </button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

// 编辑文章
function editPost(title) {
    const posts = JSON.parse(localStorage.getItem('blog-posts') || '[]');
    const post = posts.find(p => p.title === title);
    
    if (post) {
        document.getElementById('post-title').value = post.title;
        document.getElementById('post-category').value = post.category;
        document.getElementById('post-tags').value = post.tags.join(', ');
        easyMDE.value(post.content);
    }
}

// 删除文章
function deletePost(title) {
    if (confirm('确定要删除这篇文章吗？')) {
        const posts = JSON.parse(localStorage.getItem('blog-posts') || '[]');
        const updatedPosts = posts.filter(p => p.title !== title);
        localStorage.setItem('blog-posts', JSON.stringify(updatedPosts));
        
        // 更新文章列表
        updatePostList();
        
        // 显示成功消息
        showNotification('文章删除成功！');
    }
}

// 显示通知
function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // 2秒后移除通知
    setTimeout(() => {
        notification.remove();
    }, 2000);
}

// 搜索和筛选功能
document.querySelector('.post-filters input').addEventListener('input', function(e) {
    const searchTerm = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('.post-table tbody tr');
    
    rows.forEach(row => {
        const title = row.cells[0].textContent.toLowerCase();
        row.style.display = title.includes(searchTerm) ? '' : 'none';
    });
});

document.querySelector('.post-filters select').addEventListener('change', function(e) {
    const category = e.target.value;
    const rows = document.querySelectorAll('.post-table tbody tr');
    
    rows.forEach(row => {
        const rowCategory = row.cells[1].textContent;
        row.style.display = !category || rowCategory === category ? '' : 'none';
    });
});

// 初始化文章列表
updatePostList(); 