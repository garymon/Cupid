document.getElementById("increaseSort").onclick =  function() {
    console.log("increase");
};

document.getElementById("decreaseSort").onclick =  function() {
    console.log("decrease");
};

$("#photo_atag").click(function(e) {
    document.getElementById('upload').click();
    e.preventDefault();
    return false;
})
