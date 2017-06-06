/**
 * Created by sehyeon on 2017-05-30.
 */

function distinct_check(_user_input_id) {
    var user_input_id = document.getElementById("" + _user_input_id);
    var user_id = user_input_id.value;

    $.ajaxSetup({
        headers: {"X-CSRFToken": get_cookie("csrftoken")}
    });

    $.ajax({
        url: '/app/id_check/?data=' + user_id + '/',
        type: 'POST',
        success: function (result) {
            var dict = JSON.parse(result);
            if (dict['distinct_check'] == 0) {
                alert("사용할 수 있는 아이디입니다.");
                $("#sign-up-button").attr('disabled', false);
            }
            else {
                alert("이미 사용중인아이디입니다.");
            }

        },
        fail: function (result) {
            alert("fail");
        }
    });

}

// using jQuery
function get_cookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
