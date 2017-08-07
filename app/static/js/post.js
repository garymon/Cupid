
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
        var postData = {uuid : $(this).parents(".postUuid").data('uuid')};

        $.ajax({
            type : "DELETE",
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

    $(".postUpdate").click(function() {
        $(this).parents(".panel").find(".postContent").hide();
        $(this).parents(".panel").find(".updateTextBox").show();
    });

    $(".updateButton").click(function() {
        var updateText = $(this).parents(".updateTextBox").find(".updateText").val();
        console.log(updateText);
        var updateData = {content : updateText, name : "JUN SEO", date : "", uuid : $(this).parents(".postUuid").data('uuid')};

        $.ajax({
            type : "PUT",
            url : "/post",
            contentType: "application/json",
            data : JSON.stringify(updateData),
            success : function(args) {
                window.location.reload();
                console.log("update success", args);
            },
            error:function(e) {
                console.log("update updateText Error", e);
            }
        });
    })

    $(".updateCancelButton").click(function() {
        $(this).parents(".panel-body").find(".postContent").show();
        $(this).parents(".panel-body").find(".updateTextBox").hide();

        var originContent = $(this).parents(".updateTextBox").find(".updateText").data('content');
        $(this).parents(".updateTextBox").find(".updateText").val(originContent);
    })
})
