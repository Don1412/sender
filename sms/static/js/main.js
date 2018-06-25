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
            $('#name_template_select').append('' +
                '<a id="name_template_'+nameValue+'" class="dropdown-item" onclick="select_name_template(\''+nameValue+'\')">'+nameValue+'' +
                    '<i class="fa-btn fa fa-1x fa-trash" onclick="delete_name_template(\''+nameValue+'\')"></i>' +
                '</a>');
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
            $('#message_template_input').val(e.template.text);
        }
    });
}

function search_message_template() {
    var message = $('#message_template_input').val();
    var nameValue = $('#message_template_name').val();
    var btn = '' +
        '<a class="btn dropdown-toggle" id="message_template_btn" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">' +
            '<i class="fa fa-1x fa-file-text"></i>' +
        '</a>';
    var btn_add = '' +
        '<div class="form-group" id="message-btn-group">' +
            '<input type="text" class="form-control col-2 d-inline" id="message_template_name">' +
            '<a class="btn toggle_arrow" role="button" id="message_template_btn" onclick="add_message_template()">\n' +
                '<i class="fa fa-2x fa-plus"></i>\n' +
            '</a>' +
        '</div>';
    var a = document.getElementById('message_template_btn');
    if(message.length <= 0 || $('#message-btn-group').length) {
        a = document.getElementById('message-btn-group');
        a.outerHTML = btn;
    }
    else {
        $.get({
            url: '../message_template',
            data: {'name': nameValue},
            dataType: 'json',
            success: function(e) {
                $('#message-btn-group').remove();
                a.outerHTML = btn;
            },
            error: function (e) {
                a.outerHTML = btn_add;
            }
        });
    }
}

function add_message_template() {
    var nameValue = $('#message_template_name').val();
    var text = $('#message_template_input').val();
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
            search_message_template();
            $('#message_template_select').append('' +
                '<a id="message_template_'+nameValue+'" class="dropdown-item" onclick="select_message_template(\''+nameValue+'\')">'+nameValue+'' +
                    '<i class="fa-btn fa fa-1x fa-trash" onclick="delete_message_template(\''+nameValue+'\')"></i>' +
                '</a>');
        }
    });
}
function delete_message_template(name) {
    event.stopPropagation();
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
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