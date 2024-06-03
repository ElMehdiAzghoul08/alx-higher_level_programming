$(document).ready(function() {
    $('#btn_translate').click(function() {
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: $('#language_code').val() }, function(data) {
            $('#hello').text(data.hello);
        });
    });

    $('#language_code').keypress(function(prcs_) {
        if (prcs_.which === 13) {
            $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: $('#language_code').val() }, function(data) {
                $('#hello').text(data.hello);
            });
        }
    });
});
