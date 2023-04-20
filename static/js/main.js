const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').forEach(link => {
    if (link.href.includes(`${activePage}`)) {
        link.classList.add('active');
    }
})

// const activePage = window.location.pathname;
// const navLinks = document.querySelectorAll('nav a');
// const menuLenght = navLinks.lenght;
// for (let i = 0; i < menuLenght; i++) {
//     if(navLinks[i].href === activePage){
//         navLinks[i].className = "active"
//     }
// }