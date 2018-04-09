function select_name_template(name)
{
    $('#senderName').val(name);
}
function select_message_template(name)
{
    var type = $('#type').val();
    $.get({
        url: "../message_template",
        success: function(e)
        {
            alert(e);
            $('#senderName').val(e.text);
            $('#type').val(e.type)
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