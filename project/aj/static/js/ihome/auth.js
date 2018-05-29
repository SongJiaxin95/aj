function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$.get('/user/auths/',function (data) {
    if(data.code == '200'){
        $('#real-name').val(data.id_name);
        $('#id-card').val(data.id_card);
        $('.btn-success').hide()
        $('#real-name').prop('readonly',true)
        $('#id-card').prop('readonly',true)
    }
});

$('#form-auth').submit(function (e) {
    e.preventDefault();
    var real_name = $('#real-name').val();
    var id_card = $('#id-card').val();
    $.ajax({
        url: '/user/auths/',
        type:'PUT',
        datatype: 'json',
        data: {'real_name':real_name,'id_card':id_card},
        success:function (data) {
            if(data.code == '200'){
                $('.btn-success').hide()
                $('.error-msg').hide()
                $('#real-name').prop('readonly',true)
                $('#id-card').prop('readonly',true)
            }else{
                $('.error-msg').html('<i class="fa fa-exclamation-circle"></i>'+data.msg)
                $('.error-msg').show()
            }
        },
        error:function (msg) {
            alert('请求失败')
        }
    })
});

