$(function(){
    $('INPUT#btn_translate').click(function(){
        const languageCode = $('INPUT#language_code').val();
        let url = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;
        $.get(url, function(data){
            $('DIV#hello').html(data.hello);
        });
    });
});