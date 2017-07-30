
import $ from 'jquery';
import 'bootstrap';


$(document).ready(function() {
    //Post text
    $("#postButton").click(function() {
        var getText = $("#postText").val();
        var postData = {content : getText, name : "JUN SEO", date : "", uuid : ""};

        $.ajax({
            type : "POST",
            url : "/post",
            contentType: "application/json",
            data : JSON.stringify(postData),
            success : function(args) {
                window.location.reload();
                console.log("post success", args);
            },
            error:function(e) {
                console.log("Post postText Error", e);
            }
        });
    })

    $(".postDelete").click(function() {
        console.log("delete");
        console.log($("this").parent("div"))
    })
})
