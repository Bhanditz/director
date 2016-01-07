function draw(){
var canvas = d3.select("#main")

d3.json("data/data.json", function(error, newdata){
	
var bins = canvas.selectAll(".directorbin")
			.data(newdata)
			.enter().append("svg")
			.attr("class", "directorbin")
			;

var binheight = $(".directorbin").height()
	binwidth =	$(".directorbin").width()
	;
	
var roles = ["Director", "Writer", "Producer", "Editor", "Actor"];
	
	bins.selectAll("lines")
		.data(roles)
		.enter().append("line")
		.attr("x1",0).attr("x2",binwidth)
		.attr("y1", function(d,i){return binheight*(i+1)/6.0 ;})
		.attr("y2", function(d,i){return binheight*(i+1)/6.0 ;})
		;
		
var groups =bins.selectAll("svg")
				.data(function(d){return d.films;})
				.enter().append("g")
				.attr("transform", function(d,i){
					var len = d3.select(this.parentNode).data()[0].nofilms;
					return "translate(" + scaleMaker(i,binwidth,len)+",0)";
				});
				
groups.selectAll("circ")
	.data(function(d){return d.credits;})
	.enter().append("circle")
	.attr("r",5).attr("cx",0)
	.attr("cy", function(d){return separateCircles(d, binheight);})
	.attr("class", function(d){return d;})
	.style("fill",function(d){return circleColor(d);})
	;
});
}

function separateCircles(d, h){
	var pos = h/6.0;
	if ( d == "director"){ 
		return pos;
	} else if ( d == "writer"){
		return pos*2;
	} else if (d == "editor"){
		return pos*3;
	} else if (d == "producer"){
		return pos *4;
	} else if ( d == "actor"){
		return pos*5;
	}
}

function circleColor(d){
	if (d == 'director'){
		return "blue";
	} else if ( d == "writer"){
		return "green" ;
	} else if ( d == "editor"){
		return "yellow";
	} else if (d == "producer"){
		return "orange";
	} else if (d == "actor"){
		return "red";
	}
}

function scaleMaker(i,w,l){
	var scale = d3.scale.linear()
					.domain([0,l])
					.range([0,w])
					;
	return scale(i);
}
	


