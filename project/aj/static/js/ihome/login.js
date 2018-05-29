function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function() {
    $("#mobile").focus(function(){
        $("#mobile-err").hide();
    });
    $("#password").focus(function(){
        $("#password-err").hide();
    });
    $(".form-login").submit(function(e){
        e.preventDefault();
        mobile = $("#mobile").val();
        passwd = $("#password").val();
        $.ajax({
            url: '/user/login/',
            type:'POST',
            datatype: 'json',
            data: {'mobile':mobile,'password':passwd,},
            success:function (data) {
                if(data.code == '200'){
                    var path = document.referrer
                    if(path.indexOf('/user/register/') != -1 | path=='' | path.indexOf('http://127.0.0.1:8000') == -1){
                        location.href = '/'
                    }
                    else{
                        location.href = path
                    }
                }
            },
            error:function (msg) {
                alert(msg)
            }
        });
    });
})