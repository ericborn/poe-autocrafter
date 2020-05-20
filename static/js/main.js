//function status

function webData(){
	var rolls = document.getElementById("rolls").value
	var mod = document.getElementById("desiredMod").value
	eel.roll_function(rolls, mod)(function(ret) {console.log(ret)})
}

function statusCheck(){

	//running manally with these values works
	
	//let x = 1;
	//let num = 0;
	let d = 'dot';
	//y = d + String(num)
	//changeColor(x, y)

	let y = ''
	let data = 0;
	//var num = 0;
	for (let i = 0; i < 3; i++){
		//console.log(i)
		//eel.status_check(i)(changeColor(ret) {console.log(ret)})
		//let y = ''

		//console.log(i)
		
		data = eel.status_check(i)(function(ret){console.log(ret)})
		console.log(data)
		//x = eel.status_check(i)(function(ret){console.log(ret)}) //working but passes undefined to console
		//y = 'dot' + String(i)
		//console.log(x)
		//console.log(y)
		y = d + String(i)
		console.log(y)
		//changeColor(data, y)
	}
}

function changeColor(status, id){
      if (status == 1) {
      	document.getElementById(id).style.backgroundColor = "green";
      } else if (status == -1) {
      	document.getElementById(id).style.backgroundColor = "red";
      }
}