/**
 * Created by sehyeon on 2017-06-06.
 */

function edit_button(id) {

    var user_name = document.getElementById("my-page-user-name");
    var nickname = document.getElementById("my-page-nickname");

    var user_name_data = user_name.innerHTML;
    var nickname_data = nickname.innerHTML;

    user_name.innerHTML = "<input type='text' id='my-page-user-name-input' value='" + user_name_data + "'>";
    nickname.innerHTML = "<input type='text' id='my-page-nickname-input' value='" + nickname_data + "'>";

    document.getElementById("edit-button-" + id).style.display = "none";
    document.getElementById("save-button-" + id).style.display = "block";
}

function save_button(id) {
    var edited = get_edited_info();

    $.ajaxSetup({
        headers: {"X-CSRFToken": get_cookie("csrftoken")}
    });

    $.ajax({

        url: '/app/my_page/save/',
        type: 'POST',
        data: edited,
        success: function (result) {
            alert("저장되었습니다.");
            location.href = '/app/my_page/info/'
        },
        error: function (error) {
            alert("수정할 수 없습니다.");
        }
    });
}

function get_edited_info() {
    var user_name = document.getElementById("my-page-user-name-input");
    var nickname = document.getElementById("my-page-nickname-input");

    var edited_info = {
        'user_name': user_name.value,
        'nickname': nickname.value
    };
    return edited_info;
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

function search_friend(option, data) {
    $.ajaxSetup({
        headers: {"X-CSRFToken": get_cookie("csrftoken")}
    });

    var data_source = document.getElementById(data);

    $.ajax({
        url: '/app/my_page/friend/?action=search&option=findbyall&data=' + data_source.value + '/',
        type: 'POST',
        data: friends,
        success: function (result) {
            alert("저장되었습니다.");
            location.href = '/app/my_page/info/'
        },
        error: function (error) {
            alert("수정할 수 없습니다.");
        }
    });
}

function make_friend_relationship(id) {
    $.ajaxSetup({
        headers: {"X-CSRFToken": get_cookie("csrftoken")}
    });

    $.ajax({
        url: '/app/my_page/friend/?action=befriend&data=' + id + '/',
        type: 'POST',
        data: id,
        success: function (result) {
            alert(id + "에게 친구 신청을 마쳤습니다.");
            location.href = '/app/my_page/friend/'
        },
        error: function (error) {
            alert("친구로 신청할 수 없습니다.");
        }
    });

}