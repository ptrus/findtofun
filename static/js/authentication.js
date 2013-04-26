
$('#sign-in').on('click', function (e) {
	$('#odjavljen').toggle("slow");
	$('#prijavljen').toggle("slow");
});

$('#logout').on('click', function (e) {
	$('#prijavljen').toggle("slow");
	$('#odjavljen').toggle("slow");
});