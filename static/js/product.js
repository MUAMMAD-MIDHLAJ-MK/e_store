
document.addEventListener("DOMContentLoaded", function () {

    const slides = document.querySelectorAll(".banner-item");
    let current = 0;

    setInterval(() => {
        slides[current].classList.remove("active");

        current = (current + 1) % slides.length;

        slides[current].classList.add("active");
    }, 3000);

});
