switchToPaiement = () => {
    document.getElementById("employee-main-content-right1").style.display ="block";
    document.getElementById("employee-main-content-right2").style.display ="none";
    document.getElementById("employee-main-content-right3").style.display ="none";
    document.getElementById("employee-main-content-right4").style.display ="none";

} 

switchToSalaire = () => {
    document.getElementById("employee-main-content-right1").style.display ="none";
    document.getElementById("employee-main-content-right2").style.display ="block";
    document.getElementById("employee-main-content-right3").style.display ="none";
    document.getElementById("employee-main-content-right4").style.display ="none";
}

switchToVente = () => {
    document.getElementById("employee-main-content-right1").style.display ="none";
    document.getElementById("employee-main-content-right2").style.display ="none";
    document.getElementById("employee-main-content-right3").style.display ="block";
    document.getElementById("employee-main-content-right4").style.display ="none";
}

switchToRapport = () => {
    document.getElementById("employee-main-content-right1").style.display ="none";
    document.getElementById("employee-main-content-right2").style.display ="none";
    document.getElementById("employee-main-content-right3").style.display ="none";
    document.getElementById("employee-main-content-right4").style.display ="block";
}