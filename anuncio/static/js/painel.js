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
    $('button[name="delete"]').click(function(){
        anuncioId = $(this).attr('data-id');
        $.get('/delete/', {id: anuncioId}, function(data){
            location.reload();
        });
    });
    $('button[name="aceitar"]').click(function(){
        anuncioId = $(this).attr('data-id');
        $.get('/aprovar/', {id: anuncioId}, function(data){
            location.reload();
        });
    });
});
