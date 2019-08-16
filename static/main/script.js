var plotbtn = $('.plot')
var closebtn = $(".closed");


plotbtn.click(function(){
    $(this).parent().find('.summary').addClass('finalPos');
})

closebtn.click(function(){
    $(this).parent().parent().removeClass('finalPos');
})
