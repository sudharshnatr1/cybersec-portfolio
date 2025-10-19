// Mobile Navigation Toggle
const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');

if (burger) {
    burger.addEventListener('click', () => {
        nav.classList.toggle('active');
        burger.classList.toggle('toggle');
    });
}

// Close mobile menu when link is clicked
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        nav.classList.remove('active');
    });
});

// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar Background on Scroll
const navbar = document.querySelector('.navbar');
if (navbar) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(5, 7, 20, 0.98)';
        } else {
            navbar.style.background = 'rgba(5, 7, 20, 0.95)';
        }
    });
}

// Console Easter Egg
console.log('%c🚀 Welcome to the Matrix...', 'color: #00f5ff; font-size: 20px; font-weight: bold;');
console.log('%c🔒 Cybersecurity Professional Portfolio', 'color: #ff006e; font-size: 16px;');
console.log('%c💻 Built with Django & Cyberpunk Aesthetics', 'color: #3fff00; font-size: 14px;');
