//视频推荐
//var url_video_recommend = "http://192.168.0.19:80/tcm-live-rest/api/v1/video/recommendation"
var url_video_recommend = "https://api.lb.jiankanghao.net/api/v1/video/recommendation";
//视频详情
//var url_video_info1 = "http://192.168.0.19:80/tcm-live-rest/api/v1/video/info_h5";
var url_video_info = "https://api.lb.jiankanghao.net/api/v1/video/info_h5";
//商城首页
var url_shop_h5 = 'https://m.jiankanghao.net/wx_index.html';

/*rem计算适配*/
(function(doc, win) {
	var docEl = doc.documentElement,
		resizeEvt = 'orientationchange' in window ? 'orientationchange' : 'resize',
		recalc = function() {
			var clientWidth = docEl.clientWidth;
			if(!clientWidth) return;
			docEl.style.fontSize = 100 * (clientWidth / 750) + 'px'; //以750px（即iPhone6）的标准，设置font-size：100px；
		};
	if(!doc.addEventListener) return;
	win.addEventListener(resizeEvt, recalc, false);
	doc.addEventListener('DOMContentLoaded', recalc, false);
})(document, window);
/**
 * 获取get参数
 */
function GetRequest() {
	var url = location.search; //获取url中"?"符后的字串
	var theRequest = new Object();
	if(url.indexOf("?") != -1) {
		var str = url.substr(1);
		strs = str.split("&");
		for(var i = 0; i < strs.length; i++) {
			theRequest[strs[i].split("=")[0]] = unescape(strs[i].split("=")[1]);
		}
	}
	return theRequest;
}
