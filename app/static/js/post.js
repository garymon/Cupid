$("#post_btn").click(function(e) {
    onclick_post()
    e.preventDefault();
})

$('#textArea').keydown(function (e) {
    if (e.ctrlKey && e.keyCode == 13) {
        onclick_post()
    }
});

function onclick_post(e){
    var d = new Date();
    var min = d.getMinutes();
    var hour = d.getHours();
    var datee = d.getDate();
    var month = d.getMonth() + 1 ;
    var year = d.getFullYear();
    var sec = d.getSeconds();

    input_str = document.getElementById("textArea").value;
    json_obj = {
        name : "Jun Seo",
        date : year + "-" + month+ "-" + datee + " " + hour + ":" + min + ":"  + sec,
        content : input_str
    };

    sendServerJson(JSON.stringify(json_obj));
}

function sendServerJson(jsonData){
    $.ajax({
        type: "POST",
        url: "/api/posts",
        contentType: "application/json",
        data: jsonData,
        error: function(request,status,error){
            console.log("[post.html] : error");
        },
        success: function(result){
            console.log("[post.html] : success");
            window.location.reload();
            //$("#postContent").prepend(result)
            //$("#textArea").val("")
        }
    });
}

$(".update").click(function(e){
    var target = e.currentTarget
    e.preventDefault();
    var mostup = $(target).parents(".postTopClass");
    var updateWrite = $(mostup).find(".updateWrite");
    var updateDiv = $(mostup).find(".updateDiv");
    var postView = $(mostup).find(".postView");

    $(updateWrite).attr("style","display:visibility");
    $(updateDiv).attr("style","display:none");
})
$(".delete").click(function(e) {
    var target = e.currentTarget
    e.preventDefault();
    updateUUID = $(target).parents(".postTopClass").find(".updateUUID").text()
    uuidObj = {uuid : updateUUID}

    $.ajax({
        type: "DELETE",
        url: "/api/posts",
        contentType: "application/json",
        data: JSON.stringify(uuidObj),
        error: function(request,status,error){
            console.log("[post.html] : error");
        },
        success: function(result){
            console.log("[post.html] : success");
            window.location.reload();
        }
    });
})

$(".updateCompleteBtn").click(function(e) {
    var target = e.currentTarget
    e.preventDefault();

    var d = new Date();
    var min = d.getMinutes();
    var hour = d.getHours();
    var datee = d.getDate();
    var month = d.getMonth() + 1 ;
    var year = d.getFullYear();
    var sec = d.getSeconds();

    input_str = $(target).parents(".postTopClass").find(".updateTextArea").val()
    updateUUID = $(target).parents(".postTopClass").find(".updateUUID").text()

    $(target).parents(".postTopClass").find(".updateTextArea").val("")

    json_obj = {
        name : "Jun Seo",
        date : year + "/" + month+ "/" + datee + "/" + hour + ":" + min + ":"  + sec,
        content : input_str,
        uuid : updateUUID
    };

    $.ajax({
        type: "PUT",
        url: "/api/posts",
        contentType: "application/json",
        data: JSON.stringify(json_obj),
        error: function(request,status,error){
            console.log("[post.html] : error");
        },
        success: function(result){
            console.log("[post.html] : success");
            window.location.reload();
        }
    });
})