// const modals =['modal1-window', 'modal2-window']


function showmodal() {
    modal('modal1');
    modaloff('modal1');
}


showmodal()



function modal(id)
{  
    let div = document.getElementById('modal1-window');
    let el = document.getElementById(id);  // can also use a query selector 
    let bg = document.createElement("div");
    bg.className = "modal-js-overlay";
    bg.id = "modal-js-overlay";

    let close = document.createElement("span");
    close.className = "modal-js-close";
    close.innerHTML = "x";
    close.addEventListener('click', function () {
    div.style.display = 'none';
    });

    div.appendChild(bg);
    bg.appendChild(el);
    el.appendChild(close);
    
}

function modaloff(id) {
    let body = document.querySelector("body");
    let el = document.querySelector(id);
    let overlay = body.querySelector(".modal-js-overlay");
    
    el.classList.remove('on');
    body.removeChild(overlay);
}


function  closeDetails() {
    document.getElementById('details-modals').style.display = "none";
}

// Vente
// ==============================

function showmodal1() {
    modal1('modal2');
    modaloff1('modal2');
}
showmodal1()

function modal1(id)
{  
    let div = document.getElementById('modal2-window');
    let el = document.getElementById(id);  // can also use a query selector 
    let bg = document.createElement("div");
    bg.className = "modal-js-overlay";
    bg.id = "modal-js-overlay";

    let close = document.createElement("span");
    close.className = "modal-js-close";
    close.innerHTML = "x";
    close.addEventListener('click', function () {
    div.style.display = 'none';
    });

    div.appendChild(bg);
    bg.appendChild(el);
    el.appendChild(close);
    
}

function modaloff1(id) {
    let body = document.querySelector("body");
    let el = document.querySelector(id);
    let overlay = body.querySelector(".modal-js-overlay");
    
    el.classList.remove('on');
    body.removeChild(overlay);
}

function  closeDetails() {
    document.getElementById('details-modals').style.display = "none";
}

function openmodal2() {
    document.getElementById('modal2-window').style.display = "block";
}

// Depense
// =============================

function showmodal3() {
    modal3('modal3');
    modaloff3('modal3');

}

showmodal3();

$(document).on('click', '.otr-prense', function () {
    document.getElementById('modal3-window').style.display = "block";

})


function modal3(id)
{  
    let div = document.getElementById('modal3-window');
    let el = document.getElementById(id);  // can also use a query selector 
    let bg = document.createElement("div");
    bg.className = "modal-js-overlay";
    bg.id = "modal-js-overlay";

    let close = document.createElement("span");
    close.className = "modal-js-close";
    close.innerHTML = "x";
    close.addEventListener('click', function () {
    div.style.display = 'none';
    });

    div.appendChild(bg);
    bg.appendChild(el);
    el.appendChild(close);
    
}

function modaloff3(id) {
    let body = document.querySelector("body");
    let el = document.querySelector(id);
    let overlay = body.querySelector(".modal-js-overlay");
    
    el.classList.remove('on');
    body.removeChild(overlay);
}

function  closeDetails() {
    document.getElementById('details-modals').style.display = "none";
}



