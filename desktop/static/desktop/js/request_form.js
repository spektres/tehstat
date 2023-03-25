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

$(document).ready(function(){
	$('#button_clearly_form').click(function(event){
		document.getElementById('button_clearly_form').classList.add('hidden');
		document.getElementById('button_form').classList.remove('hidden');

		document.getElementById('div_id_room').classList.add('show');
		document.getElementById('div_id_compressor').classList.add('show');
		document.getElementById('div_id_mehanical_assembly').classList.add('show');
		document.getElementById('div_id_electrical_assembly').classList.add('show');
		document.getElementById('div_id_oil_assembly').classList.add('show');
		document.getElementById('div_id_air_assembly').classList.add('show');
		document.getElementById('div_id_another').classList.add('show');
		document.getElementById('div_id_text_open').classList.remove('show');

		document.getElementById('div_id_mehanical_assembly_text').classList.remove('show');
		document.getElementById('div_id_electrical_assembly_text').classList.remove('show');
		document.getElementById('div_id_oil_assembly_text').classList.remove('show');
		document.getElementById('div_id_air_assembly_text').classList.remove('show');
		document.getElementById('div_id_another_text').classList.remove('show');

		document.getElementById('push').classList.add('show');

		document.getElementById('alert_form').classList.add('hidden');
		document.getElementById('alert_clearly_form').classList.remove('hidden');

		$('#id_text_open').val('');
	});
});

$(document).ready(function(){
	$('#button_form').click(function(event){
		document.getElementById('button_clearly_form').classList.remove('hidden');
		document.getElementById('button_form').classList.add('hidden');

		document.getElementById('div_id_room').classList.add('show');
		document.getElementById('div_id_compressor').classList.add('show');
		document.getElementById('div_id_mehanical_assembly').classList.remove('show');
		document.getElementById('div_id_electrical_assembly').classList.remove('show');
		document.getElementById('div_id_oil_assembly').classList.remove('show');
		document.getElementById('div_id_air_assembly').classList.remove('show');
		document.getElementById('div_id_another').classList.remove('show');
		document.getElementById('div_id_text_open').classList.add('show');

		document.getElementById('div_id_mehanical_assembly_text').classList.remove('show');
		document.getElementById('div_id_electrical_assembly_text').classList.remove('show');
		document.getElementById('div_id_oil_assembly_text').classList.remove('show');
		document.getElementById('div_id_air_assembly_text').classList.remove('show');
		document.getElementById('div_id_another_text').classList.remove('show');

		document.getElementById('push').classList.add('show');

		document.getElementById('alert_form').classList.remove('hidden');
		document.getElementById('alert_clearly_form').classList.add('hidden');

		$('input:checkbox').prop('checked', false);
	});
});
