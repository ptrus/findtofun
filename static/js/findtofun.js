if (window.location.hash == '#_=_') {
	window.location.hash = '';
}

$('#top').on('click', function(e) {
	$('#topdiv').show();
	$('#mapsdiv').hide();
	$('#calendardiv').hide();
});

$('#maps').on('click', function(e) {
	$('#mapsdiv').show();
	$('#calendardiv').hide();
	$('#topdiv').hide();
	initialize();
});

$('#calendar').on('click', function(e) {
	$('#datetimepicker').show();
	$('#topdiv').hide();
	$('#mapsdiv').hide();
	$('#datetimepicker').datetimepicker({
		format: 'dd/MM/yyyy hh:mm:ss',
	});
});

$('#sign-in').on('click', function (e) {
	$('#odjavljen').toggle("slow");
	$('#prijavljen').toggle("slow");
});

$('#logout').on('click', function (e) {
	$('#prijavljen').toggle("slow");
	$('#odjavljen').toggle("slow");
});