//jQuery('body').append('<a href="https://google.com">Перейти в гугл!</a>');

jQuery('document').ready(function(){
    jQuery('body').append('<a href="https://google.com">Перейти в гугл!</a>');
    jQuery('div').remove();
    var name_;
    name_ = jQuery('p').clone();
    jQuery('body').append(name_);
    var kat1, kat2;
    kat1 = 3
    kat2 = 4
//    alert((kat1 ** 2 + kat2 ** 2 ) ** 0.5)
    alert(Math.sqrt(kat1 ** 2 + kat2 ** 2 ))
});