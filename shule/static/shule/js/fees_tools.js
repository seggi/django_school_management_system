

function onpenForm1(){
    document.getElementById('1').style.color ="white";
    document.getElementById('2').style.color ="dodgerblue";
    document.getElementById('3').style.color ="dodgerblue";

    document.getElementById('1').style.background = "dodgerblue";
    document.getElementById('2').style.background = "none";
    document.getElementById('3').style.background = "none";

    document.getElementById('main_form_cachier1').style.display='block';
    document.getElementById('main_form_cachier2').style.display='none';
    document.getElementById('main_form_cachier3').style.display='none';
}

function onpenForm2(){
    document.getElementById('2').style.color ="white";
    document.getElementById('1').style.color ="dodgerblue";
    document.getElementById('3').style.color ="dodgerblue";

    document.getElementById('2').style.background = "dodgerblue";
    document.getElementById('1').style.background = "none";
    document.getElementById('3').style.background = "none";

    document.getElementById('main_form_cachier2').style.display='block';
    document.getElementById('main_form_cachier1').style.display='none';
    document.getElementById('main_form_cachier3').style.display='none';
}

function onpenForm3(){
    document.getElementById('3').style.color ="white";
    document.getElementById('1').style.color ="dodgerblue";
    document.getElementById('2').style.color ="dodgerblue";

    document.getElementById('1').style.background = "none";
    document.getElementById('2').style.background = "none";
    document.getElementById('3').style.background = "dodgerblue";
    document.getElementById('main_form_cachier3').style.display='block';
    document.getElementById('main_form_cachier2').style.display='none';
    document.getElementById('main_form_cachier1').style.display='none';
}