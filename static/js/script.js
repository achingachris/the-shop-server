$( document ).ready(function() {
  $(".wrap-fade").hover(
    function () {
      $(this).find("img").addClass("fading");
    },
    function () {
      $(this).find("img").removeClass("fading");
    }
  );
});
var windowWidth = $(window).width();
var yourNavigation = $("#navbar");
    yourHeader = $('.upperHeader').height();

$(window).scroll(function() {
  if(windowWidth > 768){
    if( $(this).scrollTop() > yourHeader ) {
      yourNavigation.addClass('sticky');
      $('#logoSm').fadeIn("slow");
    } else {
      yourNavigation.removeClass('sticky');
      $('#logoSm').fadeOut();
    }
  }

});
