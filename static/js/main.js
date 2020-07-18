//function status
/*
Implement in html if js method doesnt work
<script type="text/javascript">
  eel.expose(webData);
    function webData(){
      var rolls = document.getElementById("rolls").value
      var mod = document.getElementById("desiredMod").value
      return [rolls, mod];
    }
</script>
*/ 

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

// runs a loop three times asking python to perform a check for the inventory/stash to be ready,
// item rarity to be magic and currecny being in the top left inventory slot
// calls the changeColor function with the result of those tests
// dot is the color dots indicating the status red/green for each item
async function rollStatusCheck(){
	var roll_d = 'dot';
	var y = ''
	//var data = 0;

	for (let i = 0; i < 3; i++){

		let data = await eel.roll_status_check(i, curr)() //(function(ret){console.log(ret)})
		//console.log(data)

		y = roll_d + String(i)
		//console.log(y)
		changeColor(data, y)
	}
}

// runs a loop three times asking python to perform a check for the inventory/stash to be ready,
// item rarity to be magic and currecny being in the top left inventory slot
// calls the changeColor function with the result of those tests
async function sortStatusCheck(){
  var sort_d = 'dot';
  var x = ''
  //var data = 0;

  let data = await eel.sort_status_check(1)() //(function(ret){console.log(ret)})
    console.log(data)

    x = sort_d + String(1)
    //console.log(y)
    changeColor(data, x)
}
  
// used to change the dot color next to each item in the status check
// 1 means passed (green), -1 means failed (red)
// automatically fired from the status check function based upon the return
// value from python
function changeColor(status, id){
      if (status == 1) {
      	document.getElementById(id).style.backgroundColor = "green";
      } else if (status == -1) {
      	document.getElementById(id).style.backgroundColor = "red";
      }
}

function sortInventory(){

}

// Used to report the desired number of rolls and mod back to python
async function webData(){
	var rolls = document.getElementById("rolls").value
  var curr = document.getElementById("desiredCurr").value
	var mod = document.getElementById("desiredMod").value
	await eel.roll_function(rolls, curr, mod)() //(function(ret) {console.log(ret)})
  await eel.sort_inventory():
	//return[rolls, mod];
} 