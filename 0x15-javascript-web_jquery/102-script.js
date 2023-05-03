$(document).ready(function () {
	$("INPUT#btn_translate").click(function () {
		const language_code = $("INPUT#language_code").val();
		$.getJSON(
			`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
			function (greeting) {
				$("#hello").text(greeting.hello);
			}
		);
	});
});
