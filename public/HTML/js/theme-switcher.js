document.addEventListener('DOMContentLoaded', () => {
    const themeSwitcher = document.getElementById('theme-switcher');
    const html = document.documentElement;

    // 1. Set initial theme
    const currentTheme = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', currentTheme);
    if (themeSwitcher) {
        themeSwitcher.textContent = currentTheme === 'dark' ? '☀️' : '🌙';
    }

    // 2. Add click listener
    if (themeSwitcher) {
        themeSwitcher.addEventListener('click', () => {
            let targetTheme = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', targetTheme);
            localStorage.setItem('theme', targetTheme);
            themeSwitcher.textContent = targetTheme === 'dark' ? '☀️' : '🌙';
        });
    }
});
