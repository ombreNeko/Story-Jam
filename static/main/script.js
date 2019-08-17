var plotbtn = $('.plot');
var plot1btn = $('.plot1')
var closebtn = $('.closed');


plotbtn.click(function(){
    $(this).parent().find('.summary').addClass('finalPos');
})

plot1btn.click(function(){
    $(this).parent().parent().find('.summary').addClass('finalPos');
})

closebtn.click(function(){
    $(this).parent().parent().removeClass('finalPos');
})
