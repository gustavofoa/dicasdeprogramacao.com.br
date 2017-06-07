var share_post_params = {"effect":"1","opacity":"0","top_distance":"220","opacity_intensity":"0.7"};

window.onscroll = function scrollFunction() {
    var scrollPos = document.body.scrollTop;

    if (scrollPos > share_post_params.top_distance-20) {
        document.getElementById("share_post-box").style.position = "fixed";
        document.getElementById("share_post-box").style.top = "20px";
    } else {
        document.getElementById("share_post-box").style.position = "absolute";
        document.getElementById("share_post-box").style.top = share_post_params.top_distance+"px";
    }
}
