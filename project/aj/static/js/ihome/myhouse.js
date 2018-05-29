$(document).ready(function(){
    $(".auth-warn").show();
    $.get('/house/auth_myhouse/',function (data) {
        if(data.code == '200'){
            $('.auth-warn').hide();
            var house_list_html = '';
            for(var i=0;i<data.hlist_list.length;i++){
                var house_html = '<li>';
                house_html += '<a href="/house/detail/?id='+data.hlist_list[i].id+'">';
                house_html += '<div class="house-title">';
                house_html += '<h3>房屋ID:'+data.hlist_list[i].id +'—— 房屋标题:'+data.hlist_list[i].title+'</h3>';
                house_html += '</div>';
                house_html += '<div class="house-content">';
                house_html += '<img src="'+data.hlist_list[i].image+'">';
                house_html += '<div class="house-text">';
                house_html += '<ul>';
                house_html += '<li>位于：'+data.hlist_list[i].area+'</li>';
                house_html += '<li>价格：￥'+data.hlist_list[i].price+'/晚</li>';
                house_html += '<li>发布时间：'+data.hlist_list[i].create_time+'</li>';
                house_html += '</ul></div></div></a></li>';
                house_list_html += house_html
            }
            $('#houses-list').append(house_list_html)
        }else{
            $('#houses-list').hide()
        }
    })


})