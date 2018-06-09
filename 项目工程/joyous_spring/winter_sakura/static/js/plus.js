/**
 * Created by twilight on 2016/6/6.
 */
$("#returnTop").bind("click",r_top);
$("#second_model,#third_model,#forth_model,#fifth_model,.story_model").bind("mouseover",trans_border);
$("#second_model,#third_model,#forth_model,#fifth_model,.story_model").bind("mouseout",trans_border_e);
$("#rollpad,#news_pad").bind("mouseover",trans_border2);
$("#rollpad,#news_pad").bind("mouseout",trans_border_e2);
$("div[class^='roll_point']").bind("click",choice_roll);
//绑定
$(window).scroll(function()
{
    var height = $(window).scrollTop();
    if(height>10)   //显示返回顶部
    {
        $("#returnTop").removeClass("hide");
    }
    else    //隐藏返回顶部
    {
        $("#returnTop").addClass("hide");
    }
});
//监听
function r_top(){
    $("body,html").animate({scrollTop:"0px"},300)
}
//返回顶部插件
///////////////////////////////////////////////////////////////////////////////
function toPoint(percent){
    var str=percent.replace("%","");
    str= str/100;
    return str;
}


function rollpad(){
    var roll = document.getElementById("roll_ul").style.marginLeft;
    roll = parseFloat(roll);
    if(parseFloat(roll)/100 >= -2){
        roll  = roll/100 - 1;
        roll_pic = (roll*100).toString() + "%";
        $("#roll_ul").animate({marginLeft:roll_pic},500);
    }
    else{
        $("#roll_ul").animate({marginLeft:"0%"},500);
    }
}

time = setInterval('rollpad()',3500);

function choice_roll(){
    if($(this).attr("class") == "roll_point_1")
    {
        $("#roll_ul").animate({marginLeft:"0%"},500);
        clearInterval(time);
        time = setInterval('rollpad()',3500);
    }
    if($(this).attr("class") == "roll_point_2")
    {
        $("#roll_ul").animate({marginLeft:"-100%"},500);
        clearInterval(time);
        time = setInterval('rollpad()',3500);
    }
    if($(this).attr("class") == "roll_point_3")
    {
        $("#roll_ul").animate({marginLeft:"-200%"},500);
        clearInterval(time);
        time = setInterval('rollpad()',3500);
    }
    if($(this).attr("class") == "roll_point_4")
    {
        $("#roll_ul").animate({marginLeft:"-300%"},500);
        clearInterval(time);
        time = setInterval('rollpad()',3500);
    }
}
//滚动广告
////////////////////////////////////////////////////////////////////////////////////
function trans_border(){
    $(this).css('border', '2px solid white');
    $(this).css('border-bottom', '1px solid white');
    $(this).css('border-top', '1px solid white');
}

function trans_border_e(){
    $(this).css('border', '2px rgba(255,255,255,0.7) solid');
    $(this).css('border-bottom', '1px rgba(255,255,255,0.7) solid');
    $(this).css('border-top', '1px rgba(255,255,255,0.7) solid');
}

function trans_border2(){
    $(this).css('border', '2px solid white');
}

function trans_border_e2(){
    $(this).css('border', '2px rgba(255,255,255,0.7) solid');
}
//div的鼠标指向边框高亮
url = "http://fanyi.youdao.com/openapi.do?keyfrom=abc1243&key=1207861310&type=data&doctype=json&version=1.1&q=good";
//(未完成)
//调用有道翻译api
//////////////////////////////////////////////////////////////////////////////////
i = 0;
function titledisplay()
{
    if(i<11)
    {
        $("#span>li").eq(i).animate({opacity:1},500);
        i++;
    }
    else
    {
        clearInterval(title_show);
    }
}
$(document).ready(function(){
    title_show = setInterval('titledisplay()',100);
});


