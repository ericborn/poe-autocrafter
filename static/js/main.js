//function status

function webData(){
	var rolls = document.getElementById("rolls").value
	var mod = document.getElementById("desiredMod").value
	eel.roll_function(rolls, mod)(function(ret) {console.log(ret)})
}
/*
// Inside a function marked 'async' we can use the 'await' keyword.
async function statusCheck() {

  // The first call returns the function and the second actually execute it
  let data = await eel.status_check()();
  // Must prefix call with 'await', otherwise it's the same syntax

  console.log("Got this from Python: " + data);
}

//statusCheck();

*/

async function statusCheck(){
	var d = 'dot';
	var y = ''
	//var data = 0;

	for (let i = 0; i < 3; i++){

		let data = await eel.status_check(i)() //(function(ret){console.log(ret)})
		//console.log(data)

		y = d + String(i)
		//console.log(y)
		changeColor(data, y)
	}
}


function changeColor(status, id){
      if (status == 1) {
      	document.getElementById(id).style.backgroundColor = "green";
      } else if (status == -1) {
      	document.getElementById(id).style.backgroundColor = "red";
      }
}