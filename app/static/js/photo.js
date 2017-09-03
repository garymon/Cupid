
import $ from 'jquery';
import 'bootstrap';

$(document).ready(function() {
    $(function(){
        $(".img-click").click(function () {
            var date = $(this).parent("div").attr('data-date');
            $("#modal-date").text(date);
            console.log(date);

            var imgSrc = $(this).find("img").attr('src');
            $("#modal-img").attr('src', imgSrc);
            console.log(imgSrc);

        });
    });


    console.log("Photo.js");
//    $(function(){
//        $("#upload_link").on('click', function(e){
//            $("#upload").click();
//            e.preventDefault();
//            $("#upload:hidden").trigger('click');
//        });
//    });
//
    $("#upload_link").click(function(e) {
        document.getElementById('upload').click();
        e.preventDefault();
        return false;
    })

    $("#ascending_photo").click(function(e) {
        console.log("as");

    })


    $("#descending_photo").click(function(e) {
        console.log("de");
    })
})