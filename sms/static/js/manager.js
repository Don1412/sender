$(document).ready(function() {
    if($('#smsList').length) {
        $(this).on('click', 'tbody tr', function (e) {
            location.href = $(this).data('id');
        });
    }
});