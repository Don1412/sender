function select_name_template(name) {
    $('#senderName').val(name);
}
function search_name_template() {
    var nameValue = $('#senderName').val();
    var btn = '<a class="btn toggle_arrow dropdown-toggle" role="button" id="name_template_btn" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n' +
            '<i class="fa fa-2x fa-address-card"></i>\n' +
            '</a>';
    var btn_add = '<a class="btn toggle_arrow" role="button" id="name_template_btn" onclick="add_name_template()">\n' +
                    '<i class="fa fa-2x fa-plus"></i>\n' +
                    '</a>';
    var a = document.getElementById('name_template_btn');
    if(nameValue.length <= 0) {
        a.outerHTML = btn;
    }
    else {
        $.get({
            url: '../name_template',
            data: {'name': nameValue},
            dataType: 'json',
            success: function(e) {
                a.outerHTML = btn;
            },
            error: function (e) {
                a.outerHTML = btn_add;
            }
        });
    }
}
function add_name_template() {
    var nameValue = $('#senderName').val();
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.post({
        url: "../name_template/",
        dataType: 'json',
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        data: {'name': nameValue},
        success: function(e)
        {
            search_name_template();
            $('#name_template_select').append('<a id="name_template_'+nameValue+'" class="dropdown-item" onclick="select_name_template(\''+nameValue+'\')">'+nameValue+'</a>');
        }
    });
}
function delete_name_template(name) {
    event.stopPropagation();
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.post({
        url: "../delete_name_template/",
        dataType: 'json',
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        data: {'name': name},
        success: function(e)
        {
            $('#name_template_'+name).remove();
        }
    });
}
function select_message_template(name) {
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
function add_message_template() {
    var nameValue = $('#senderName').val();
    var text = $('#message').val();
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.post({
        url: "../message_template/",
        dataType: 'json',
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        data: {'name': nameValue, 'text': text},
        success: function(e)
        {
            $('#message_template_select').append('<a id="message_template_'+nameValue+'" class="dropdown-item" onclick="select_message_template(\''+nameValue+'\')">'+nameValue+'</a>');
        }
    });
}
function delete_message_template(name) {
    event.stopPropagation();
    $.post({
        url: "../delete_message_template/",
        dataType: 'json',
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        data: {'name': name},
        success: function(e)
        {
            $('#message_template_'+name).remove();
        }
    });
}
var countNumbers = 0;
function count_numbers() {
    var box = $("#numbers").val();//помещаем в var text содержимое текстареи
    var lines = box.split(/\r|\r\n|\n/);  //разбиваем это содержимое на фрагменты по переносам строк
    countNumbers = lines.length;
    for(var i = 0; i < lines.length; i++) if(lines[i].length < 1) countNumbers--;
    $('#numbers_to_send').html(countNumbers);
}