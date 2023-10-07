(function ($) {
  "use strict";

  // PRE LOADER
  $(window).load(function(){
    $('.preloader').fadeOut(1000);
  });

  // MENU
  $('.navbar-collapse a').on('click',function(){
    $(".navbar-collapse").collapse('hide');
  });

  $(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
      $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
      $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
  });

  // SLIDER
  $('.owl-carousel').owlCarousel({
    animateOut: 'fadeOut',
    items:1,
    loop:true,
    autoplayHoverPause: false,
    autoplay: true,
    smartSpeed: 1000,
  });

  // PARALLAX EFFECT
  $.stellar({
    horizontalScrolling: false,
  });

  // MAGNIFIC POPUP
  $('.image-popup').magnificPopup({
      type: 'image',
      removalDelay: 300,
      mainClass: 'mfp-with-zoom',
      gallery:{
        enabled:true
      },
      zoom: {
        enabled: true,
        duration: 300,
        easing: 'ease-in-out',
        opener: function(openerElement) {
          return openerElement.is('img') ? openerElement : openerElement.find('img');
        }
      }
  });

  // SMOOTHSCROLL
  $(function() {
    $('.custom-navbar a, #home a').on('click', function(event) {
      var $anchor = $(this);
      $('html, body').stop().animate({
        scrollTop: $($anchor.attr('href')).offset().top - 49
      }, 1000);
      event.preventDefault();
    });
  });

  // WOW ANIMATION
  new WOW({ mobile: false }).init();

})(jQuery);

//card
$(document).ready(function() {
  $('.card').delay(1800).queue(function(next) {
    $(this).removeClass('hover');
    $('a.hover').removeClass('hover');
    next();
  });
});

// Add any additional JavaScript code here
