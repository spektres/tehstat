$(document).ready(function(){
	$('#id_mehanical_assembly').click(function(event){
		$('#div_id_mehanical_assembly_text').toggleClass('show');
		$('#id_mehanical_assembly_text').val('');
	});
});

$(document).ready(function(){
	$('#id_electrical_assembly').click(function(event){
		$('#div_id_electrical_assembly_text').toggleClass('show');
		$('#id_electrical_assembly_text').val('');
	});
});

$(document).ready(function(){
	$('#id_oil_assembly').click(function(event){
		$('#div_id_oil_assembly_text').toggleClass('show');
		$('#id_oil_assembly_text').val('');
	});
});

$(document).ready(function(){
	$('#id_air_assembly').click(function(event){
		$('#div_id_air_assembly_text').toggleClass('show');
		$('#id_air_assembly_text').val('');
	});
});

$(document).ready(function(){
	$('#id_another').click(function(event){
		$('#div_id_another_text').toggleClass('show');
		$('#id_another_text').val('');
	});
});