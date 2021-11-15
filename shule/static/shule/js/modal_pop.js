// popup screen register cachier && secretaire 
// cachier
var admin_modal = document.getElementById('admin-pop-screen');
window.onclick = function(event){
    if (event.target == admin_modal) {
        admin_modal.style.display = "none";
    }
}
// secretaire
var admin_modal1 = document.getElementById('admin-pop-screen1');
window.onclick = function(event){
    if (event.target == admin_modal1) {
        admin_modal1.style.display = "none";
    }
}


// close screen & onpen screen cachier && secretary
// register cachier
function closeAdminModal() {
    document.getElementById('admin-pop-screen').style.display='none';
}

function openAdminModal() {
    document.getElementById('admin-pop-screen').style.display='block';
}
// register secretary

function closeAdminModal1() {
    document.getElementById('admin-pop-screen1').style.display='none';
}

function openAdminModal1() {
    document.getElementById('admin-pop-screen1').style.display='block';
}

// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// Level popup screens
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

function closeClassesModal2() {
    document.getElementById('classes-pop-screen').style.display='none';
}

function openClassesModal2() {
    document.getElementById('classes-pop-screen').style.display='block';
}
// register secretary

function closeClassesModal3() {
    document.getElementById('classes-pop-screen1').style.display='none';
}

function openClassesModal3() {
    document.getElementById('classes-pop-screen1').style.display='block';
}

// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// Cours +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


function closecoursModal2() {
    document.getElementById('cours-pop-screen').style.display='none';
}

function opencoursModal2() {
    document.getElementById('cours-pop-screen').style.display='block';
}
// register secretary

function closecoursModal3() {
    document.getElementById('cours-pop-screen1').style.display='none';
}

function opencoursModal3() {
    document.getElementById('cours-pop-screen1').style.display='block';
}

function closecoursModal4() {
    document.getElementById('cours-pop-screen2').style.display='none';
}

function opencoursModal5() {
    document.getElementById('cours-pop-screen2').style.display='block';
}

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// Fees & Payment ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


function closefeesModal2() {
    document.getElementById('fees-pop-screen').style.display='none';
}

function openfeesModal2() {
    document.getElementById('fees-pop-screen').style.display='block';
}

// register secretary

function closefeesModal3() {
    document.getElementById('fees-pop-screen1').style.display='none';
}

function openfeesModal3() {
    document.getElementById('fees-pop-screen1').style.display='block';
}

function closefeesModal4() {
    document.getElementById('fees-pop-screen2').style.display='none';
}

function openfeesModal5() {
    document.getElementById('fees-pop-screen2').style.display='block';
}

// Periode ....

function openfeesModal6() {
    document.getElementById('fees-pop-screen4').style.display='block';
}

function closefeesModal6() {
    document.getElementById('fees-pop-screen4').style.display='none';
}

// Personnel....

function openpersonnelModal2() {
    document.getElementById('personnel-pop-screen4').style.display='block';
}

function closepersonnelModal() {
    document.getElementById('personnel-pop-screen4').style.display='none';
}


// Depense...............

function openDepenseModal() {
    document.getElementById('dps-pop-screen').style.display='block';
}

function closeDepenseModal() {
    document.getElementById('dps-pop-screen').style.display='none';
}


// Sell 

function openSellModal() {
    document.getElementById('sell-pop-screen').style.display='block';
}

function closeSellModal() {
    document.getElementById('sell-pop-screen').style.display='none';
}


// Personnel tbl extend fctns

function displayFuctiontbl() {
    document.getElementById('main_personnel_t').style.display = "block";
    document.getElementById('tbl-right').style.display = "none";
    document.getElementById('btnftn').style.visibility = "hidden";
}

// Remove employee &  edit 

function closeDltEmpModal() {
    document.getElementById('dlt-pop-screen').style.display = "none";
}

// Edit employee item

function closeEdtEmpModal() {
    document.getElementById('edt-pop-screen').style.display = "none";
}

