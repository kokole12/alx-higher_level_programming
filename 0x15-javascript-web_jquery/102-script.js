$(document).ready(function () {
<<<<<<< HEAD
  $('INPUT#btn_translate').click(function () {
    const language_code = $('INPUT#language_code').val();
    $.getJSON(
	`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
	function (greeting) {
	  $('#hello').text(greeting.hello);
	});
  });
=======
	$("INPUT#btn_translate").click(function () {
		const language_code = $("INPUT#language_code").val();
		$.getJSON(
			`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
			function (greeting) {
				$("#hello").text(greeting.hello);
			}
		);
	});
>>>>>>> 23edbe07405b7c9d1883dbf7b85853105aa15d6a
});
