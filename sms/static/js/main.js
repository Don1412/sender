function select_name_template(name)
{
    $('#senderName').val(name);
}
function search_name_template()
{
    var nameValue = $('#senderName').val();
    $.get({
        url: '../name_template',
        data: {'name': nameValue},
        dataType: 'json',
        success: function(e)
        {
            alert(e);
        }
    });
}
function select_message_template(name)
{
    $.get({
        url: "../message_template",
        data: {'name':name},
        dataType: 'json',
        success: function(e)
        {
            var obj = jQuery.parseJSON(e);
            alert(obj);
            $('#message').val(obj.text);
            $('#type').val(obj.type)
        }
    });
}
var countNumbers = 0;
function count_numbers()
{
    var box = $("#numbers").val();//помещаем в var text содержимое текстареи
    var lines = box.split(/\r|\r\n|\n/);  //разбиваем это содержимое на фрагменты по переносам строк
    countNumbers = lines.length;
    for(var i = 0; i < lines.length; i++) if(lines[i].length < 1) countNumbers--;
    $('#numbers_to_send').html(countNumbers);
}