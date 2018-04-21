// AJAX for posting
function create_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "create_post/", // the endpoint
        type : "POST", // http method
        data : {
                 nom : $('#nom').val(),
                 date_depart : $('#date_depart').val(),
                 date_arriver : $('#date_arriver').val(),
                 telephone : $('#telephone').val(),
                 email : $('#email').val(),
                 message : $('#message').val(),
                 adultes : $('#adultes :selected').val(),
                 enfants : $('#enfants :selected').val(),
                 moyen : $('#moyen :selected').val(),
                 csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),}, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#nom').val(''); // remove the value from the input
            $('#date_depart').val(''); // remove the value from the input
            $('#date_arriver').val(''); // remove the value from the input
            $('#telephone').val(''); // remove the value from the input
            $('#email').val(''); // remove the value from the input
            $('#message').val(''); // remove the value from the input
            $('#adultes :selected').val()// remove the value from the input
            $('#enfants :selected').val()// remove the value from the input
            $('#moyen :selected').val()// remove the value from the input
            console.log(json); // log the returned json to the console
            $('#notif').html("<h4>Reservation enregistré, on reviendra vers vous au plus vite.</h4>"); // another sanity check
            $('#notif').show();
            $('#notif').animate({padding: 17, height:60},500);
            setTimeout(function(){ $('#notif').animate({padding:0, height:0},800); }, 2500);
            $('#hide').hide();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#notif').css("background-color","red");
            $('#notif').html("<h4>Quelque chose c'est mal passé.</h4>"); // another sanity check
            $('#notif').show();
            $('#notif').animate({padding: 17, height:60},500);
            setTimeout(function(){ $('#notif').animate({padding:0, height:0},800); }, 2500);
            $('#hide').hide();
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

// Submit post on submit

$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});