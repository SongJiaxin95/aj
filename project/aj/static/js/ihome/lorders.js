//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);
    $(".order-accept").on("click", function(){
        var orderId = $(this).parents("li").attr("order-id");
        $(".modal-accept").attr("order-id", orderId);
    });
    $(".order-reject").on("click", function(){
        var orderId = $(this).parents("li").attr("order-id");
        $(".modal-reject").attr("order-id", orderId);
    });

    $.get('/order/mylorders/',function (data) {

        if(data.code == '200'){
            var lorders_html = template('lorders_list',{orders:data.orders});
            $('.orders-list').html(lorders_html);

            $('.order-accept').click(function () {
                var order_id = $(this).parents('li').attr('order-id');
                $('.modal-accept').attr('order-id',order_id)
            });

            $('.order-reject').click(function () {
                var order_id = $(this).parents('li').attr('order-id');
                $('.modal-reject').attr('order-id',order_id)
            });

            $('.modal-accept').click(function (data) {
                var order_id = $(this).attr('order-id');
                $.ajax({
                    url:'/order/order/'+order_id+'/',
                    type:'PATCH',
                    data:{'status':'WAIT_PAYMENT'},
                    dataType:'json',
                    success:function (data) {
                        if(data.code == '200'){
                            $('.order-operate_'+order_id).hide();
                            $('#accept-modal').modal('hide');
                            // $('#accept-modal').hide()
                            // $('.modal-backdrop').css({'display':'None'});

                            $('#'+order_id).html('待支付')
                        }
                    },
                    error:function (msg) {
                        alert('修改订单状态失败')
                    }
                })

            })
            $('.modal-reject').click(function (data) {
                var order_id = $(this).attr('order-id');
                var comment = $('#reject-reason').val();
                $.ajax({
                    url: '/order/order/' + order_id + '/',
                    type: 'PATCH',
                    data: {'status': 'REJECTED', 'comment': comment},
                    dataType: 'json',
                    success: function (data) {
                        if (data.code == '200') {
                            $('.order-operate_'+order_id).hide();
                            $('#reject-modal').modal('hide');
                            // $('#accept-modal').hide();
                            // $('.modal-backdrop').css({'display':'None'});
                            $('#' + order_id).html('已拒单')
                        }
                    },
                    error: function (msg) {
                        alert('修改订单状态失败')
                    }
                })
            })
        }
    })
});