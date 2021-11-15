

function switchToStudent(){
    
    document.getElementById('welcom1').style.display ='none';
    document.getElementById('employee-main-content-right').style.display ='block';
    document.getElementById('student-main-content-right').style.display ='none';
    document.getElementById('product-main-content-right').style.display ='none';
    

    document.getElementById('open2').style.background = 'rgba(30, 143, 255, 0.932)';
    document.getElementById('open2').style.color = 'white';

    document.getElementById('open3').style.background = '#ffffff';
    document.getElementById('open3').style.color = '#333';

    document.getElementById('open4').style.background = '#ffffff';
    document.getElementById('open4').style.color = '#333';
   
}

function switchToEmployee() {
    document.getElementById('welcom1').style.display ='none';
    document.getElementById('employee-main-content-right').style.display ='none';
    document.getElementById('student-main-content-right').style.display ='block';
    document.getElementById('product-main-content-right').style.display ='none';
    

    document.getElementById('open3').style.background = 'rgba(30, 143, 255, 0.932)';
    document.getElementById('open3').style.color = 'white';

    document.getElementById('open2').style.background = '#ffffff';
    document.getElementById('open2').style.color = '#333';

    document.getElementById('open4').style.background = '#ffffff';
    document.getElementById('open4').style.color = '#333';
}


function switchToProducts() {
   
    document.getElementById('welcom1').style.display ='none';
    document.getElementById('employee-main-content-right').style.display ='none';
    document.getElementById('student-main-content-right').style.display ='none';
    document.getElementById('product-main-content-right').style.display ='block';
    

    document.getElementById('open4').style.background = 'rgba(30, 143, 255, 0.932)';
    document.getElementById('open4').style.color = 'white';

    document.getElementById('open2').style.background = '#ffffff';
    document.getElementById('open2').style.color = '#333';

    document.getElementById('open3').style.background = '#ffffff';
    document.getElementById('open3').style.color = '#333';

}


