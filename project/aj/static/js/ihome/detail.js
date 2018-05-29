function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}


$(document).ready(function(){

    var path = location.search
    id = path.split('=')[1]

    $.get('/house/detail/'+id+'/',function (data) {
        if(data.code == '200'){
            var detail_house = template('house_detail_list',{ohouse:data.house,facilitys:data.facility_list})
            $('.container').append(detail_house)

            var mySwiper = new Swiper ('.swiper-container', {
            loop: true,
            autoplay: 2000,
            autoplayDisableOnInteraction: false,
            pagination: '.swiper-pagination',
            paginationType: 'fraction'
            });
            var booking = data.booking;
            if (booking){
                $(".book-house").show();
                if (booking == '1'){
                    $('.book-house').attr('href','javascript:void(0)').click(function(){
                        $('.theme-popover-mask').fadeIn(100);
                        $('.theme-popover').slideDown(200);
                    })
                }
            }else{
                $(".book-house").hide();
            }
            $('.theme-poptit .close').click(function(){
                $('.theme-popover-mask').fadeOut(100);
                $('.theme-popover').slideUp(200);
            })

        }
    })


    $(".theme-signin").submit(function(e){
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
                    location.reload()
                }
            },
            error:function (msg) {
                console.log(msg)
            }
        });
    });

})

