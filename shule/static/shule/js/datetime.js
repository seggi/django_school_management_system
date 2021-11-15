// var dt = new Date()
// document.getElementById("datetime").innerHTML = (( "0"+dt.getDate()).slice(-2)) +"."+ (("0"+(dt.getMonth()+1)).slice(-2))
//     +"."+ (dt.getFullYear()) +" "+ (("0"+dt.getHours()).slice(-2)) +":"+ (("0"+dt.getMinutes()).slice(-2));


function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();

    m = chechTime(m);
    s = chechTime(s);
    document.getElementById('datetime').innerHTML = h + ":" + m + ":" + s;
    document.getElementById('datetime1').innerHTML = h + ":" + m + ":" + s;
    var  t = setTimeout(startTime, 500);
}

function chechTime(i) {
    if (i < 10) {i ="0" + i};
        return i;
}








// function searchOpen() {
//     var search = $('#searchinput').val()
//     var data = {
//         search: search
//     };
//     $.ajax({
//         url: '/shule/cachier/search/',
//         data: data,
//         dataType: 'jsonp',
//         jsonpCallback: 'searchResult'
//     });
// }


// function searchResult(data) {
    
//     $( "#searchinput" ).autocomplete ({
//         source: data,
//     });
   
// }

