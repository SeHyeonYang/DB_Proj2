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

function join_group(group_id) {
    $.ajaxSetup({
        headers: {"X-CSRFToken": get_cookie("csrftoken")}
    });

    $.ajax({
        url: '/app/group_home/?option=join&data=' + group_id + '/',
        type: 'POST',
        data: group_id,
        success: function (result) {
            alert("가입했습니다.");
            location.href = '/app/group_home/'
        },
        error: function (error) {
            alert("가입할 수 없습니다.");
        }
    });

}

function friend_approve(friend_id) {
    $.ajaxSetup({
        headers: {"X-CSRFToken": get_cookie("csrftoken")}
    });

    alert("OK");
    $.ajax({
        url: '/app/my_page/friend/?action=approve&data=' + friend_id + '/',
        type: 'POST',
        success: function (result) {
            alert("수락했습니다.");
            location.href = '/app/my_page/friend/'
        },
        error: function (error) {
            alert("실패했습니다.");
        }
    });
}

function delete_article(user_id, article_id) {
    $.ajaxSetup({
        headers: {"X-CSRFToken": get_cookie("csrftoken")}
    });

    $.ajax({
        url: '/app/article/delete/?user=' + user_id + '&article='+article_id+'/',
        type: 'POST',
        success: function (result) {
            alert("게시물을 삭제합니다.");
            location.href = '/app/article/total/'
        },
        error: function (error) {
            alert("권한이 없어 지울 수 없습니다.");
        }
    });
}

function delete_section(username, section_id) {
    $.ajaxSetup({
        headers: {"X-CSRFToken": get_cookie("csrftoken")}
    });

    $.ajax({
        url: '/app/lecture/delete/?user=' + username + '&section='+section_id+'/',
        type: 'POST',
        success: function (result) {
            alert("분기강좌를 개설취소합니다.");
            location.href = '/app/my_page/ongoing/'
        },
        error: function (error) {
            alert("권한이 없어 취소할 수 없습니다.");
        }
    });
}