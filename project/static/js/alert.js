$('.alert-error').removeClass("hide");
$('.alert-error').addClass("show");
$('.alert-error').addClass("showalert");
setTimeout(function(){
    $('.alert-error').addClass("hide");
    $('.alert-error').removeClass("show");
},5000);

$('.close-btn-error').click(function(){
    $('.alert-error').addClass("hide");
    $('.alert-error').removeClass("show");
});


$('.alert-success').removeClass("hide");
$('.alert-success').addClass("show");
$('.alert-success').addClass("showalert");
    setTimeout(function(){
        $('.alert-success').addClass("hide");
        $('.alert-success').removeClass("show");
    },5000);

$('.close-btn-success').click(function(){
    $('.alert-success').addClass("hide");
    $('.alert-success').removeClass("show");
});
