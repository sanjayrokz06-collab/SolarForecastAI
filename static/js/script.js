function updateClock(){

    let now = new Date();

    document.getElementById("clock").innerHTML =
    "Last Updated : " + now.toLocaleString();

}

setInterval(updateClock,1000);

updateClock();

// Refresh prediction every 5 minutes
setInterval(function(){

    location.reload();

},300000);