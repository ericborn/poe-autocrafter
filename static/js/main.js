function statusCheck(){
	var status = (0,0);
	for (let i = 0; i < 3; i++){
		status = eel.status_check(i)changeColor(ret) {console.log(ret)}
	}
}

function webData(){
	var rolls = document.getElementById("rolls").value
	var mod = document.getElementById("desiredMod").value
	eel.roll_function(rolls, mod)(function(ret) {console.log(ret)})
}

function changeColor(status, id){
      if (status == 1) {
      	document.getElementById(id).style.backgroundColor = "green";
      } else if (status == -1) {
      	document.getElementById(id).style.backgroundColor = "red";
      }
}