
function validateTextbox(){

var box=document.getElementById("u");
var box2=document.getElementById("p");
if (box.value==""){
	alert("The field marked in red cannot be blank");
	box.focus();
	box.style.border="solid 3px red";
	return false;
}
else if (box2.value==""){
	alert("The field marked in red cannot be blank");
	box2.focus();
	box2.style.border="solid 3px red";
	return false;
}
else if(box2.value.length<5){
	alert("Plese enter at least 5 characters");
	box2.focus();
	box2.style.border="solid 3px red";
	return false;
}

}