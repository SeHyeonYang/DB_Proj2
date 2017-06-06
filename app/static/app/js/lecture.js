/**
 * Created by Yelim on 2017-05-31.
 */

function lecture_distinct_check(_lecture_input_id) {
    var lecture_input_id = document.getElementById("" + _lecture_input_id);
    var lecture_id = _lecture_input_id.value;

    $.ajaxSetup({
        headers: {"X-CSRFToken": get_cookie("csrftoken")}
    });

    $.ajax({
        url: '/app/lecture_check/?data=' + lecture_id + '/',
        type: 'POST',
        success: function (result) {
            var dict = JSON.parse(result);
            if (dict['distinct_check'] == 0) {
                alert("개설할 수 있는 강좌입니다.");
                $("#lecture_sign_up_button").attr('disabled', false);
            }
            else {
                alert("이미 개설된 강좌입니다.");
            }

        },
        fail: function (result) {
            alert("fail");
        }
    });

}

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