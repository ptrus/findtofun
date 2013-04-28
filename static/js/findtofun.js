if (window.location.hash == '#_=_') {
	window.location.hash = '';
}
/*BUTTON SHOW SOME DETAILS*/
//TO-DO one function for all buttons
$('#btnEvent_3').on('click', function (e) {
	$('#eventInfo_3').slideToggle("slow");
});

/*THREE WAY NAVIGATION*/
$('#top').on('click', function (e) {
	$('#topdiv').show();
	$('#locationDiv').show();
	$('#dateDiv').show();
	$('#mapsdiv').hide();
	$('#calendardiv').hide();
});
$('#maps').on('click', function (e) {
	$('#mapsdiv').show();
	$('#calendardiv').hide();
	$('#topdiv').hide();
	$('#dateDiv').show();
	$('#locationDiv').hide();
	initialize();
});
$('#calendar').on('click', function (e) {
	$('#calendardiv').show();
	$('#locationDiv').show();
	$('#topdiv').hide();
	$('#mapsdiv').hide();
	$('#dateDiv').hide();
    $('#datetimepicker').datetimepicker({
    format: 'dd/MM/yyyy hh:mm:ss'
    });

});
/*END THREE WAY NAVIGATION*/

/*DATE - TIME  FILTER*/
 $('#datetimepickerFrom').datetimepicker({
	language: 'en',
	pick12HourFormat: true
 });
 $('#datetimepickerTo').datetimepicker({
	language: 'en',
	pick12HourFormat: true
});
/*END DATE - TIME  FILTER*/
