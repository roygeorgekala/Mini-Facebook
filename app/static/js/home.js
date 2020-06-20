
var profile = document.querySelector(".profile");
var menu = document.querySelector(".menu");

$(".profile").click(function(event){
  event.stopPropagation();
  menu.style.display = "block";
})

$(document).click(function(event){
  if(event.target==profile || event.target==menu){
  }
  else {
    menu.style.display="none";
  }
})

function addBio(){
  $(".name_bio form").css({"display":"block"});
  $(".add_bio").css({"display":"none"});
}
function noBio(){
  $(".name_bio form").css({"display":"none"});
  $(".add_bio").css({"display":"block"});
}
$("#cover_pic_sub").change(function(){
  //alert("input file selected");
  document.getElementById('cover_pic_form').submit();
})

$("#profile_img_sub").change(function(){
  document.getElementById('profile_img_form').submit();
})
