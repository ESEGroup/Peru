$(document).ready( function() {
    $('button[data-type]').click(function(){
        type = $(this).attr('data-type');
        anuncioId = $(this).attr('data-id');
        switch(type) {
            case "amar":
                badgeID = "#acounter";
                break;
            case "curtir":
                badgeID = "#ccounter";
                break;
            default:
                badgeID = "#ocounter";
        }
        $.get('/reacao/', {id: anuncioId, reacao: type}, function(data){
            $('*[data-id="'+anuncioId+'"]').children(badgeID).html(data);
        });
    });
});
