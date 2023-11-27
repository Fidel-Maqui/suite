let search_input = document.getElementById("search_input");
search_input.addEventListener("input", filterTrabs)
let rows = document.querySelectorAll("tbody#comps tr");

function filterTrabs() {
    // console.log(rows[0].children[0].textContent);
    if (search_input.value == "") {
        for (let i = 0; i < rows.length; i++) {
            addClass(rows[i], "fel");
        }
    } else {
        for (let i = 0; i < rows.length; i++) {
            if (!rows[i].children[0].textContent.toLowerCase().includes(search_input.value.toLowerCase())) {
                addClass(rows[i], "d-none");
                remClass(rows[i], "fel");
            }
            else {
                remClass(rows[i], "d-none");
                addClass(rows[i], "fel");
            }
        }
    }
    countTrabs();
}

function addClass(elem, clase) {
    if (!elem.classList.contains(clase)) {
        elem.classList.add(clase)
    }
}
function remClass(elem, clase) {
    if (elem.classList.contains(clase)) {
        elem.classList.remove(clase)
    }
}
function countTrabs() {
    let cantTrabs = 0;
    for (let i = 0; i < rows.length; i++) {
        if (rows[i].classList.contains("fel")) {
            cantTrabs++;
        }
    }
    document.getElementById("cantTrabs").textContent = cantTrabs;
}
countTrabs();