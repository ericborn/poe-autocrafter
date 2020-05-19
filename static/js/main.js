function statusCheck(){
	eel.status_check()
}

function webData(){
	var rolls = document.getElementById("rolls").value
	var mod = document.getElementById("desiredMod").value
	eel.roll_function(rolls, mod)(function(ret) {console.log(ret)})
}