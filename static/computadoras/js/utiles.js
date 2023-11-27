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

function showOneOfMany(parent_id, one_id) {
    let parent = document.getElementById(parent_id).children;
    for (let i = 0; i < parent.length; i++) {
        if (parent[i].getAttribute('id') == one_id) {
            remClass(parent[i], "d-none");
        }
        else {
            addClass(parent[i], "d-none");
        }

    }
}
