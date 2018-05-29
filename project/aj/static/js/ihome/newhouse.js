function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $.get('/house/area_facility/',function (data) {
        var area_html_list = '';
        for(var i=0;i<data.area_list.length;i++){
            var area_html = '<option value="'+data.area_list[i].id+'">'+data.area_list[i].name+'</option>';
            area_html_list += area_html
        }
        $('#area-id').html(area_html_list)

        var facility_html_list = '';
        for(var i=0;i<data.facility_list.length;i++){
            var facility_list = '<li><div class="checkbox">'
            facility_list += '<label><input type="checkbox" name="facility" value="'+data.facility_list[i].id+'">'+data.facility_list[i].name
            facility_list += '</label></div></li>'
            facility_html_list += facility_list
        }
        $('.house-facility-list').html(facility_html_list)
    })

    $('#form-house-info').submit(function (e) {
        e.preventDefault()
        // $(this).ajax({
        //     url: '/house/newhouse/',
        //     type:'POST',
        //     datatype: 'json',
        //     data:$(this).serialize(),
        //     success:function (data) {
        //         if(data.code == '200'){
        //             $('#form-house-info').hide();
        //             $('#form-house-image').show();
        //             $('#house-id').val(data.house_id)
        //         }
        //     },
        //     error:function (msg) {
        //         alert('请求错误')
        //     }
        // });
        //
        //
        $.post('/house/newhouse/',$(this).serialize(),function (data) {
            if(data.code == '200'){
                    $('#form-house-info').hide();
                    $('#form-house-image').show();
                    $('#house-id').val(data.house_id)
                }
        });
        return false
    });


    $('#form-house-image').submit(function (e) {
        $(this).ajaxSubmit({
            url:'/house/newhouse_img/',
            type:'POST',
            dataType:'json',
            success:function (data) {
                if(data.code=='200'){
                    $('.house-image-cons').append('<img src="'+data.url+'">')
                }
            },
            error:function () {
              alert('上传头像失败!')
            }
        });
        return false
    });

});
