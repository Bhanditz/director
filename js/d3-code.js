function draw(){
var vis =	d3.select("#main")
var canvas = vis.select("#vis")

d3.json("data/data.json", function(error, newdata){
	
//Make svg element for each director
var bins = canvas.selectAll(".directorbin")
			.data(newdata)
			//.enter().append("svg")
			.enter().append("div")
			.attr("class", "directorbin")
			;
var dirheight = $(".directorbin").height();

	bins.style("top",function(d,i){return dirheight*i+"px";});
			

	
	
	bins.append("text").text(function(d){return d.name;})
		.attr("text-anchor","middle")
		.attr("class","dirname")
		;
		
var directors = bins.append("svg").attr("class","directorsvg");
	
//Gets height and width of each director svg
var binheight = $(".directorsvg").height()
	binwidth =	$(".directorsvg").width()
	;			
	
var roles = ["Director", "Writer", "Producer", "Editor", "Actor"];

//Add lines to each bin
//	Currently not in use, but they're there
	directors.selectAll("lines")
		.data(roles)
		.enter().append("line")
		.attr("x1",0).attr("x2",binwidth)
		.attr("y1", function(d,i){return binheight*(i+1)/6.0 ;})
		.attr("y2", function(d,i){return binheight*(i+1)/6.0 ;})
		;
		
//Make group for each film
//Director --> [film1, film2, ... ]
//scaleMaker makes a scale for each bin
//Note that len goes up a level with select(this.parentNode)
var groups =directors.selectAll("svg")
				.data(function(d){return d.films;})
				.enter().append("g")
				.attr("transform", function(d,i){
					var len = d3.select(this.parentNode).data()[0].nofilms;
					return "translate(" + scaleMaker(i,binwidth,len)+",0)";
				})
				.on("mouseover", function(d){
					
					var infohold = d3.select("#credit")
					var texthold = infohold.append("svg")
									.attr("width","100%").attr("height","100%")
									.attr("class","detail")
									.append("text").attr("x",10).attr("y",10);
					
					var dirname = d3.select(this.parentNode).data()[0].name;
					
					texthold.append("tspan").text(dirname).attr("x",10).attr("dy",20);				
					texthold.append("tspan").text(d.title).attr("x",10).attr("dy",30);
					texthold.append("tspan").text(d.year).attr("x",10).attr("dy",20);
					texthold.append("tspan").text(d.credits).attr("x",10).attr("dy",20);
					
					
				})
				.on("mouseout", function(d){
					d3.selectAll(".detail").remove();
				})
				;
				

				
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
		return "#1BCCF8";//"#0074E8";1D50CE
	} else if ( d == "writer"){
		return "#FFAD07" ;
	} else if ( d == "editor"){
		return "#F5F756";
	} else if (d == "producer"){
		return "#19D425";
	} else if (d == "actor"){
		return "#FC0066";
	}
}

function scaleMaker(i,w,l){
	var scale = d3.scale.linear()
					.domain([0,l-1])
					.range([.05*w,.95*w])
					;
	return scale(i);
}
	


