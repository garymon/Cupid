
import $ from 'jquery';
import 'bootstrap';

$(document).ready(function() {

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
})