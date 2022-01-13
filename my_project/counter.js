jQuery('document').ready(function(){
    jQuery('button').on('click', function(){    //jQuery('input').on('keyup', function() - меняет значение life
//        alert('Вы нажали кнопку!!');

        var value1, value2, value3, res;
        value1 = parseInt(jQuery('#val1').val());  //parseInt() переводит из str в int
        value2 = parseInt(jQuery('#val2').val());  //parseInt() переводит из str в int
        value3 = jQuery('#val3').val();
        if (value3 == '+') {
            res = value1 + value2;
        } else if (value3 == '-') {
            res = value1 - value2;
        } else if (value3 == '*') {
            res = value1 * value2;
        } else {
            res = value1 / value2;
        }
        alert(res);
        jQuery('#result_life').html(res)  //для тегов html
});