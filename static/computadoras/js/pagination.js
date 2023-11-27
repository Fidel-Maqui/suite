const ROWS = 15

const father_element = document.getElementById("comps");
const children_elements = father_element.querySelectorAll('.fel');
const cant_elems = children_elements.length

const num_pages = Math.ceil(cant_elems / ROWS)
let current_pos = 0

let first_btn = document.getElementById("first_btn");
first_btn.addEventListener("click", primera_page)

let prev_btn = document.getElementById("prev_btn");
prev_btn.addEventListener("click", anterior_page)

let next_btn = document.getElementById("next_btn");
next_btn.addEventListener("click", siguiente_page)

let last_btn = document.getElementById("last_btn");
last_btn.addEventListener("click", ultima_page)

function iniciar() {
    // console.log(cant_elems);
    last_btn.textContent = num_pages;

    // siempre oculto la prev_btn pero solo oculto el next_btn si hay una sola page
    if (num_pages <= 1) {
        // next_btn.classList.add('d-none')
        hideBtn(next_btn)
        hideBtn(last_btn)
    }
    // prev_btn.classList.add('d-none')
    hideBtn(prev_btn)

    if (cant_elems > ROWS) {
        // for (let i = ROWS; i < cant_elems; i++) {
        //     children_elements[i].classList.add("d-none");
        // }
        hideRows(ROWS, cant_elems)
        current_pos = ROWS;
    }

}
//ok
function siguiente_page() {
    // console.log("next");
    hideRows(0, current_pos)
    let new_pos = Math.min(current_pos + ROWS, cant_elems)

    showRows(current_pos, new_pos)
    current_pos = new_pos;


    showBtn(prev_btn)

    if (current_pos == cant_elems) {
        hideBtn(next_btn)
    }
}
//ok
function anterior_page() {
    // console.log("prev");
    let new_pos = 0
    if (current_pos == cant_elems) {
        new_pos = (Math.floor(cant_elems / ROWS)) * ROWS;
        if (new_pos >= cant_elems) {
            new_pos -= ROWS
        } 
    } else {
        new_pos = current_pos - ROWS;
    }
    showRows(new_pos - ROWS, new_pos)
    hideRows(new_pos, cant_elems)
    showBtn(next_btn)
    current_pos = new_pos
    if (current_pos <= ROWS) {
        hideBtn(prev_btn)
    }
}
//ok
function primera_page() {
    // siempre oculto la prev_btn pero solo oculto el next_btn si hay una sola page
    if (num_pages == 1) {
        hideBtn(next_btn)
    }
    hideBtn(prev_btn)

    if (cant_elems > ROWS) {
        hideRows(ROWS, cant_elems)
        current_pos = ROWS;
        showBtn(next_btn)
    }
    showRows(0, ROWS)

}
//ok
function ultima_page() {
    current_pos = cant_elems - ROWS;

    let last_elems = (Math.floor(cant_elems / ROWS)) * ROWS

    hideRows(0, last_elems)
    if (last_elems == cant_elems) {
        showRows(last_elems - ROWS, cant_elems)
    } else {
        showRows(last_elems, cant_elems)
    }
    showBtn(prev_btn)
    hideBtn(next_btn)
    current_pos = cant_elems

}

function hideRows(start, end) {
    // console.log("hiding");
    // console.log("start: ", start, " end: ", end);
    for (let i = start; i < end; i++) {
        if (!children_elements[i].classList.contains("d-none")) {
            children_elements[i].classList.add("d-none");
        }
    }
}
function showRows(start, end) {
    // console.log("showing");
    // console.log("start: ", start, " end: ", end);
    for (let i = start; i < end; i++) {
        if (children_elements[i].classList.contains("d-none")) {
            children_elements[i].classList.remove("d-none");
        }
    }
}
function showBtn(btn) {
    if (btn.classList.contains('d-none')) {
        btn.classList.remove('d-none')
    }
}
function hideBtn(btn) {
    if (!btn.classList.contains('d-none')) {
        btn.classList.add('d-none')
    }
}


iniciar()