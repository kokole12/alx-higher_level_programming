$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('ul').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('ul li:last').remove();
  });
  $('DIV#clear_list').click(function () {
    $('li').remove();
  });
});
