var plotbtn = document.querySelector(".plot");
var closebtn = document.querySelector(".closed");

var content = document.querySelector(".summary");
plotbtn.addEventListener("click",function(){
    content.classList.add("finalPos");
    closebtn.addEventListener("click",function(){
    content.classList.remove("finalPos");
    })
})


