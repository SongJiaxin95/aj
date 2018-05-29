function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$('#form-avatar').submit(function (e) {
    $(this).ajaxSubmit({
        url:'/user/user/',
        type:'PUT',
        dataType:'json',
        success:function (data) {
            if(data.code=='200'){
                $('#user-avatar').attr('src',data.url);
            }
        },
        error:function () {
          alert('上传头像失败!')
        }
    });
    return false
    // e.preventDefault();
    // var formFile = new FormData($('#form-avatar')[0]);
    // // formFile.append('file',$('#form-avatar>input')[0].files[0])
    // $.ajax({
    //     url: '/user/user/',
    //     type:'PUT',
    //     datatype: 'json',
    //     data: formFile,
    //     processData: false,
    //     cache: false,
    //     contentType: false,
    //     success:function (data) {
    //         $('#user-avatar').attr('src',data.url);
    //         alert('上传成功')
    //     },
    //     error:function (msg) {
    //         alert(msg)
    //     }
    // }
});


$('#form-name').submit(function (e) {
    e.preventDefault();
    var username = $('#user-name').val();
    $.ajax({
        url: '/user/user/',
        type:'PUT',
        datatype: 'json',
        data: {'name':username},
        success:function (data) {
            if(data.code == '200'){
                $('.error-msg').css('display','none')
                alert('保存成功')
            }else if(data.code == '1007'){
                $('.error-msg').css('display','block')
            }
        },
        error:function (msg) {
            alert('请求失败')
        }
    });
    return false
});

