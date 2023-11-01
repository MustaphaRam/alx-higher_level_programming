$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').empty();
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
