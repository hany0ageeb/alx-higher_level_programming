$(function(){
    function handleTranslate(languageCode){
        const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;
        $.get(url, function(data){
            $('DIV#hello').html(data.hello);
        });
    }
    $('INPUT#btn_translate').click(function(){
        const languageCode = $('INPUT#language_code').val();
        handleTranslate(languageCode);
    });
    $('INPUT#language_code').on('keypress', function(event){
        if(event.keyCode === 13) {
            const languageCode = $('INPUT#language_code').val();
            handleTranslate(languageCode);
        }
    });
});