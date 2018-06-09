/**
 * Created by twilight on 2018/1/5.
 */
//绑定函数
$('#submit_btn').on('click',check_register_info);


var info_ul = $("#info_ul");
info_ul.css('display','none');

function check_register_info()
{
    var username_value = $('#username').val();
    var password_value = $('#password').val();
    var nickname_value = $('#nickname').val();
    var true_name_value = $('#true_name').val();
    var tel_value = $('#tel').val();
    var address_value = $('#address').val();
    var info = $('#register_info');


    //定义正则表达式
    var username_pattern = /^[a-zA-Z0-9_-]{4,16}$/;
    var password_pattern = /^[a-zA-Z0-9_-]{6,18}$/;
    var nickname_pattern = /^[A-Za-z\u4e00-\u9fa5]{2,10}$/;
    var true_name_pattern = /^[\u4e00-\u9fa5]{2,5}$/;
    var tel_pattern = /^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$/;
    var address_pattern = /^[\u4e00-\u9fa5A-Za-z]{3,25}$/;


    if(!username_pattern.test(username_value))
    {
        info_ul.css('display','block');
        info.text('用户名格式错误!');
    }
    else if(!password_pattern.test(password_value))
    {
        info_ul.css('display','block');
        info.text('密码格式错误!');
    }
    else  if(!nickname_pattern.test(nickname_value))
    {
        info_ul.css('display','block');
        info.text('昵称格式错误!');
    }
    else if(!true_name_pattern.test(true_name_value))
    {
        info_ul.css('display','block');
        info.text('请填写正确的真实姓名!');
    }
    else if(!tel_pattern.test(tel_value))
    {
        info_ul.css('display','block');
        info.text('请填写正确的联系方式!');
    }
    else if(!address_pattern.test(address_value))
    {
        info_ul.css('display','block');
        info.text('请填写正确的地址!');
    }
    else
    {
        $('#register_form').submit();
    }
}