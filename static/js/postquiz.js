$(document).ready(function() {
    function genlist(){
	$.getJSON("/generatedlist/" + $("#loc").text() + "/" + $("#pop").text() + "/" + $("#spec").text(), function(data){
	    console.log("pls");
	    //console.log(data);
	    for (i in data){
		college = data[i];
		console.log(college);
		colstr = "";
		colstr += ("<tr>"
			      + "<td>" + college.name + "</td>"
			      + "<td>" + college.location + "</td>"
			      + "<td>" + college.pop + "</td>"
			      + "<td>"); 
		for (a in college.specialization){
		    specs = college.specialization
		    colstr += (specs[a] + ", ");
		}
		
		colstr += ("</td>" + "<td>");
		
		for (j in college.matched){
		    reasons =  college.matched
		    colstr += ( reasons[j]+ ", ");
		}
		
		colstr += ("</td>"
			      +"<td>" + college.info + "</td>" + "</tr>");
		console.log(colstr);
		$("#colleges").append(colstr);
	    }
	}
		 )};
    genlist();
});
