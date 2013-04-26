'use strict';

/* Details */

$('#btnEvent').on('click', function (e) {
	$('#eventInfo').toggle("slow");
});

$('#btnEvent_2').on('click', function (e) {
	$('#eventInfo_2').toggle("slow");
});

$('#btnEvent_3').on('click', function (e) {
	$('#eventInfo_3').toggle("slow");
});

$('#top').on('click', function (e) {
	$('#topdiv').show();
	$('#mapsdiv').hide();
	$('#calendardiv').hide();
});

$('#maps').on('click', function (e) {
	$('#mapsdiv').show();
	$('#calendardiv').hide();
	$('#topdiv').hide();
	initialize();
});

$('#calendar').on('click', function (e) {
	$('#calendardiv').show();
	$('#topdiv').hide();
	$('#mapsdiv').hide();
	$(document).ready(function () {
          $("#jqxcalendar").jqxCalendar({ width: '100%', height: '350px', theme: 'bootstrap' });
          $('#jqxcalendar').bind('valuechanged', function (event) {
              var date = event.args.date;
              $("#log").text(date.toDateString());
          });
      });
});