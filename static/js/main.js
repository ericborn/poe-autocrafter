//function status

function webData(){
	var rolls = document.getElementById("rolls").value
	var mod = document.getElementById("desiredMod").value
	eel.roll_function(rolls, mod)(function(ret) {console.log(ret)})
}

// Inside a function marked 'async' we can use the 'await' keyword.
async function run() {

  // The first call returns the function and the second actually execute it
  let data = await eel.status_check(1);
  // Must prefix call with 'await', otherwise it's the same syntax

  console.log("Got this from Python: " + data);
}

run();

/*
function statusCheck(){

	//running manally with these values works
	
	//let x = 1;
	//let num = 0;
	var d = 'dot';
	//y = d + String(num)
	//changeColor(x, y)

	var y = ''
	var data = 0;
	//var num = 0;
	for (let i = 0; i < 3; i++){
		//console.log(i)
		//eel.status_check(i)(changeColor(ret) {console.log(ret)})
		//let y = ''

		//console.log(i)
		
		data = eel.status_check(i) //(function(ret){console.log(ret)})
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
*/
function changeColor(status, id){
      if (status == 1) {
      	document.getElementById(id).style.backgroundColor = "green";
      } else if (status == -1) {
      	document.getElementById(id).style.backgroundColor = "red";
      }
}