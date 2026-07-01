document.addEventListener("DOMContentLoaded", function () {

    const menuBtn = document.querySelector(".menu-btn");
    const menuIcon = document.querySelector(".menu-btn i");
    const navLinks = document.querySelector(".nav-links");
    const navbar = document.querySelector(".navbar");

    // Toggle Mobile Menu
    menuBtn.addEventListener("click", function (e) {

        e.stopPropagation();

        navLinks.classList.toggle("active");

        if (navLinks.classList.contains("active")) {
            menuIcon.classList.remove("fa-bars");
            menuIcon.classList.add("fa-xmark");
            document.body.style.overflow = "hidden";
        } else {
            closeMenu();
        }

    });

    // Close Menu Function
    function closeMenu() {
        navLinks.classList.remove("active");
        menuIcon.classList.remove("fa-xmark");
        menuIcon.classList.add("fa-bars");
        document.body.style.overflow = "auto";
    }

    // Close when clicking a menu item
    document.querySelectorAll(".nav-links a").forEach(link => {

        link.addEventListener("click", function () {

            closeMenu();

        });

    });

    // Close when clicking outside
    document.addEventListener("click", function (e) {

        if (!navLinks.contains(e.target) && !menuBtn.contains(e.target)) {

            closeMenu();

        }

    });

    // Close on window resize
    window.addEventListener("resize", function () {

        if (window.innerWidth > 992) {

            closeMenu();

        }

    });

    // Navbar Shadow
    window.addEventListener("scroll", function () {

        if (window.scrollY > 40) {

            navbar.classList.add("navbar-scroll");

        } else {

            navbar.classList.remove("navbar-scroll");

        }

    });

    // Highlight Active Menu
    const currentPage = window.location.pathname;

    document.querySelectorAll(".nav-links a").forEach(link => {

        if (link.getAttribute("href") === currentPage) {

            link.classList.add("active-link");

        }

    });

});