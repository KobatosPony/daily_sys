/**
 * Created by twilight on 2016/6/5.
 */
/// <reference path="/jquery-1.12.3.js"/>
$(document).bind("keydown",delYumemi);
$("#Yumemi").bind("click",modeltextdisplay);
$("#delmodel").bind("click",modeltextdel);

i = 0;
text_array  = new Array();
text_array[0] = "欢迎大家光临天象馆，<br>这里有不论何时永远<br>不会消失的繁星。";
text_array[1] = "我是星野梦美，戳我可<br>以向管理人员提供意见<br>哦。";
text_array[2] = "按F2隐藏本助手，按F4<br>恢复。";

function display_text(){
    if(i <= text_array.length){
        $("#text").html(text_array[i]);
        $("#textpad").fadeIn(1000).delay(4000).fadeOut(1000);
        i++;
    }
    else{
        i = 0;
    }
}
stop_interval = setInterval('display_text()',15000);
// 上为语言显示模块
////////////////////////////////////////////////////////////////////
function delYumemi(event){
    if(event.keyCode == 113){
        $("#text").css("display","none");
        $("#textpad").css("display","none");
        $("#Yumemi").css("display","none");
        clearInterval(stop_interval)
    }
    if(event.keyCode == 115){
        $("#text").css("display","");
        $("#textpad").css("display","");
        $("#Yumemi").css("display","");
        stop_interval = setInterval('display_text()',15000);
    }
}
//设置按键隐藏和恢复
//////////////////////////////////////////////////////////////////////
function modeltextdisplay(){
    $("#text").css("display","none");
    $("#textpad").css("display","none");
    $("#Yumemi").css("display","none");
    $("#flask").css("display","block");
    $("html").css("overflow","hidden");
    clearInterval(stop_interval);
}
function modeltextdel(){
    $("#text").css("display","");
    $("#textpad").css("display","");
    $("#Yumemi").css("display","");
    $("#flask").css("display","none");
    $("html").css("overflow","");
    stop_interval = setInterval('display_text()',15000);
}