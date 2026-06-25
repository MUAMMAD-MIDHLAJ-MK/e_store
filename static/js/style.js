document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript Loaded");

    const logo = document.querySelector(".logo");

    logo.addEventListener("click", function () {
        alert("Welcome to E-Store!");
    });
});