function validateTextbox2(){

var box=document.getElementById("name");
var box2=document.getElementById("branch");
var box3=document.getElementById("hname");
var box4=document.getElementById("room");
var box5=document.getElementById("contect");
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
else if (box3.value==""){
	alert("The field marked in red cannot be blank");
	box3.focus();
	box3.style.border="solid 3px red";
	return false;
}
else if (box4.value==""){
	alert("The field marked in red cannot be blank");
	box4.focus();
	box4.style.border="solid 3px red";
	return false;
}
else if (box5.value==""){
	alert("The field marked in red cannot be blank");
	box5.focus();
	box5.style.border="solid 3px red";
	return false;
}

}