$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    translate();
  });

  function translate () {
    $('DIV#hello').empty();
    const len = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + len,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  }

  $('INPUT#language_code').keypress(function (e) {
    const key = e.which;
    if (key === 13) {
      translate();
    }
  });
});
