var share_post_params = {"effect":"1","opacity":"0","top_distance":"220","opacity_intensity":"0.7"};
var adsense_position = 0;

window.onscroll = function scrollFunction() {
    var scrollPos = window.scrollY;

    var share_box = document.getElementById("share_post-box");


    if (scrollPos > share_post_params.top_distance-20) {
        share_box.style.position = "fixed";
        share_box.style.top = "20px";
    } else {
        share_box.style.position = "absolute";
        share_box.style.top = share_post_params.top_distance+"px";
    }

    //last adsense banner
    var last_adsense_banner = document.getElementById("text-14");

    if (window.pageYOffset+20 > last_adsense_banner.offsetTop) {
        if(adsense_position == 0)
            adsense_position = last_adsense_banner.offsetTop;
        last_adsense_banner.classList.add("fix-banner");
    }
    if (window.pageYOffset+20 < adsense_position) {
        adsense_position = 0;
        last_adsense_banner.classList.remove("fix-banner");
    }

}
