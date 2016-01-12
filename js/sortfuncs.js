function sorterFilm(){
	var sortbins = d3.selectAll(".directorbin")
		.sort(function(a,b){
			return d3.ascending(b.nofilms,a.nofilms)
			;})
		.transition().duration("3000")
		.style("top", function(d,i){
			return 140*i +"px";
		})
		;
}

function sorterDir(){
	var sortbins = d3.selectAll(".directorbin")
		.sort(function(a,b){
			return d3.ascending(b.dirno,a.dirno)
			;})
		.transition().duration("3000")
		.style("top", function(d,i){
			return 140*i +"px";
		})
		;
}

function sorterWri(){
	var sortbins = d3.selectAll(".directorbin")
		.sort(function(a,b){
			return d3.ascending(b.wrino,a.wrino)
			;})
		.transition().duration("3000")
		.style("top", function(d,i){
			return 140*i +"px";
		})
		;
}

function sorterEdi(){
	var sortbins = d3.selectAll(".directorbin")
		.sort(function(a,b){
			return d3.ascending(b.edino,a.edino)
			;})
		.transition().duration("3000")
		.style("top", function(d,i){
			return 140*i +"px";
		})
		;
}

function sorterPro(){
	var sortbins = d3.selectAll(".directorbin")
		.sort(function(a,b){
			return d3.ascending(b.prono,a.prono)
			;})
		.transition().duration("3000")
		.style("top", function(d,i){
			return 140*i +"px";
		})
		;
}

function sorterAct(){
	var sortbins = d3.selectAll(".directorbin")
		.sort(function(a,b){
			return d3.ascending(b.actno,a.actno)
			;})
		.transition().duration("3000")
		.style("top", function(d,i){
			return 140*i +"px";
		})
		;
}





