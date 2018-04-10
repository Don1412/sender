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
            console.log(e.template.name);
        }
    });
}
function select_message_template(name)
{
    console.log('message');
    $.get({
        url: "../message_template",
        data: {'name':name},
        dataType: 'json',
        success: function(e)
        {
            $('#message').html(e.template.text);
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