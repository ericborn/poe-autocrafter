//function status

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

function statusCheck(){
	//let num = 0;
	//eel.status_check()(function(ret) {console.log(ret)})
	let x = 0;
	let y = '';
	let d = 'dot';
	//changeColor(x, y)
	for (let i = 0; i < 3; i++){
		//console.log(i)
		//eel.status_check(i)(changeColor(ret) {console.log(ret)})
		//let y = ''
		x = eel.status_check(i)(function(ret) {console.log(ret)})
		y = d + String(i)
		//changeColor(x, string(y))
		console.log(x, String(y))
	}
}