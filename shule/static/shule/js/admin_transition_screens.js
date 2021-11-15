// admin-main-content-right
// classes-main-content-right
// cours-main-content-right
// fees-main-content-right
// welcom
// background-color: #ffffff;
// color: #333;


function switchToAdmin(){
    document.getElementById('welcom').style.display ='none';
    document.getElementById('admin-main-content-right').style.display ='block';
    document.getElementById('classes-main-content-right').style.display ='none';
    document.getElementById('personnel-main-content-right').style.display ='none';
    document.getElementById('fees-main-content-right').style.display ='none';

    document.getElementById('open1').style.background = 'rgba(30, 143, 255, 0.932)';
    document.getElementById('open1').style.color = 'white';

    document.getElementById('open2').style.background = '#ffffff';
    document.getElementById('open2').style.color = '#333';

    document.getElementById('open3').style.background = '#ffffff';
    document.getElementById('open3').style.color = '#333';

    document.getElementById('open4').style.background = '#ffffff';
    document.getElementById('open4').style.color = '#333';


   
}

function switchToClasse() {
    document.getElementById('welcom').style.display ='none';
    document.getElementById('admin-main-content-right').style.display ='none';
    document.getElementById('classes-main-content-right').style.display ='block';
    document.getElementById('personnel-main-content-right').style.display ='none';
    document.getElementById('fees-main-content-right').style.display ='none';

    document.getElementById('open2').style.background = 'rgba(30, 143, 255, 0.932)';
    document.getElementById('open2').style.color = 'white';

    document.getElementById('open1').style.background = '#ffffff';
    document.getElementById('open1').style.color = '#333';

    document.getElementById('open3').style.background = '#ffffff';
    document.getElementById('open3').style.color = '#333';

    document.getElementById('open4').style.background = '#ffffff';
    document.getElementById('open4').style.color = '#333';
}


function switchToPersonnel() {
   
    document.getElementById('welcom').style.display ='none';
    document.getElementById('admin-main-content-right').style.display ='none';
    document.getElementById('classes-main-content-right').style.display ='none';
    document.getElementById('personnel-main-content-right').style.display ='block';
    document.getElementById('fees-main-content-right').style.display ='none';

    document.getElementById('open3').style.background = 'rgba(30, 143, 255, 0.932)';
    document.getElementById('open3').style.color = 'white';

    document.getElementById('open1').style.background = '#ffffff';
    document.getElementById('open1').style.color = '#333';

    document.getElementById('open2').style.background = '#ffffff';
    document.getElementById('open2').style.color = '#333';

    document.getElementById('open4').style.background = '#ffffff';
    document.getElementById('open4').style.color = '#333';

}

function switchToFres() {
    document.getElementById('welcom').style.display ='none';
    document.getElementById('admin-main-content-right').style.display ='none';
    document.getElementById('classes-main-content-right').style.display ='none';
    document.getElementById('personnel-main-content-right').style.display ='none';
    document.getElementById('fees-main-content-right').style.display ='block';
    

    document.getElementById('open4').style.background = 'rgba(30, 143, 255, 0.932)';
    document.getElementById('open4').style.color = 'white';

    document.getElementById('open1').style.background = '#ffffff';
    document.getElementById('open1').style.color = '#333';

    document.getElementById('open2').style.background = '#ffffff';
    document.getElementById('open2').style.color = '#333';

    document.getElementById('open3').style.background = '#ffffff';
    document.getElementById('open3').style.color = '#333';

}



// function switchToCours() {
//     document.getElementById('welcom').style.display ='none';
//     document.getElementById('admin-main-content-right').style.display ='none';
//     document.getElementById('classes-main-content-right').style.display ='none';
//     document.getElementById('cours-main-content-right').style.display ='block';
//     document.getElementById('fees-main-content-right').style.display ='none';

//     document.getElementById('open3').style.background = 'rgba(30, 143, 255, 0.932)';
//     document.getElementById('open3').style.color = 'white';

//     document.getElementById('open1').style.background = '#ffffff';
//     document.getElementById('open1').style.color = '#333';

//     document.getElementById('open2').style.background = '#ffffff';
//     document.getElementById('open2').style.color = '#333';

//     document.getElementById('open4').style.background = '#ffffff';
//     document.getElementById('open4').style.color = '#333';

// }