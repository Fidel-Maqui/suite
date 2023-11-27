let searcher = document.getElementById("searcher");
let resp = document.getElementById("resp");
let trabs = document.querySelectorAll("ul.list-group a.list-group-item");
resp.addEventListener("click", toggleSearch)
resp.addEventListener("input", searchResp)

function passIt(id, nombre, input_id) {
    // console.log("found", nombre, id);
    document.getElementById(input_id).value = id;
    resp.value = nombre;
    toggleSearch()
}
function toggleSearch() {
    if (searcher.classList.contains("d-none")) {
        searcher.classList.remove("d-none")
    } else {
        searcher.classList.add("d-none")
    }
}

function searchResp() {
    for (let i = 0; i < trabs.length; i++) {
        if (!trabs[i].textContent.toLowerCase().includes(resp.value.toLowerCase())) {
            trabs[i].classList.add("d-none");
        }
        else {
            trabs[i].classList.remove("d-none");
        }
    }
}