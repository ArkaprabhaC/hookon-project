$(function(){  //document ready function
    $("load", function(){
        console.log("Loaded");
        $(".splash").fadeOut();
    });


    $("#popular-internships .owl-carousel").owlCarousel({  //calling the owl carousel plugin
        items: 2.5,
        loop: true,
        
        responsive:{
            0:{
                items:2.5,
                reset: false,
                margin: 10,
            },
            800:{
                items:3.5,
                margin: 16,
            },
            1000:{
                items:4.5,
                margin: 16,
            },
            1400:{
                items: 6,
                nav:false,
                loop:false,
                margin: 20,
            }
        }
    }); 

    $("#sponsor .owl-carousel").owlCarousel({
        items: 1,
        autoplay: true,
        margin: 10,
        responsive:{
            0:{
                items: 1
            },
            400:{
                items: 2
            },
            1000:{
                items: 3
            },
            1400:{
                items: 4
            }
        }
    });
    $("#company-list .owl-carousel").owlCarousel({
        items: 4.5,
        loop: true,
        responsive:{
            0:{
                items: 4.5
            },
            400:{
                items: 4.5
            },
            1000:{
                items: 6.5
            },
            1400:{
                items: 8
            }
        }
    });








// modal

var loginModal = document.getElementById('modal');
$(".modal-btn").on('click', function(e){
    e.preventDefault();
    $('.login-modal').show();
});
$(".login-modal .close").on('click', function(){
    $(".login-modal").hide();
});
$(window).on('click', function(event) {
    if (event.target == loginModal) {
        $('.login-modal').hide();
    }
    
});
$(".input-password input").focus(
    function(){
        $(this).parent('div').addClass("focused")}).blur(
            function(){
            $(this).parent('div').removeClass("focused");
});
// modal end


//password visible or hide 
$('.eye').on("click", function() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
        $(".eye-slash").show();
        $(".eye-open").hide();
    
    } else {
        x.type = "password";
        
        $(".eye-slash").hide();
        $(".eye-open").show();
    }
});

//password function end

//Display user avatar and first name when user registers or logins


//When User is logged in login is 1 when logged out login is 0 /****/ THIS IS JUST FOR FRONT END TEST
checkLogin(0);
$("#log-in-btn").on('click', function(){
    checkLogin(1);
});
function checkLogin(val){
    if (val == 0) {
        $(".user-avatar").hide();
        $(".modal-btn").show();
    } else if (val == 1){
        $(".modal-btn").hide();
        $(".user-avatar").show();
        
    }
}
//End of login test





});