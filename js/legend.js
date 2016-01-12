function makeLegend(){
	
	var legendbin= d3.select("#legend")
			.append("svg").attr("width","100%")
			.attr("height","100%")
			.attr("class","legendsvg")
			;
			
	var legendht = $(".legendsvg").height();
	
	legendbin.append("text")
		.text("Credit in each film:")
		.attr("y","25").attr("x","10")
		;
	
	var roles = ["Director","Writer","Editor","Producer","Actor"];
	
	var names = legendbin.selectAll("holders")
		.data(roles)
		.enter().append("g")
		//.attr("width","50").attr("height",20)
		.attr("transform",function(d,i){return "translate(30," + legendht*(i+1)/7.0;})
		;
		
	names.append("circle")
		.attr("cx","30")
		.attr("cy", function(d,i){return 25+legendht*(i+1)/7.0 ;})
		.attr("r", "6")
		.style("fill", function(d){return circleColor(d.toLowerCase());})
		;
	
	names.append("text")
		.text(function(d){return d;})
		.attr("x","50")
		.attr("y",function(d,i){return 30+legendht*(i+1)/7.0 ;})
		;	
}
