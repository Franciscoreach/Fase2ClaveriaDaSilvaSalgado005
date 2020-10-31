jQuery(function() {

  "use strict";

/* —-------------------------------------------------------------------------
* Abrir Menu (Hamburguesa)
* —-----------------------------------------------------------------------— */
jQuery(document).ready(function() {
jQuery('nav').on( 'click', 'li', function(){
  jQuery('.navbar-collapse').removeClass('open');
  jQuery('.navbar-toggler').removeClass('opened');
});
var toggle = document.querySelector('.nav-toggle');
var overlay = document.querySelector('#overlay');
  
  toggle.addEventListener('click', function(e) {
    this.classList.toggle('opened');
    this.classList.toggle('active');
    overlay.classList.toggle('open');
  });
});

/* —-------------------------------------------------------------------------
*  Sticky menu (Menu pegajoso)
* —-----------------------------------------------------------------------— */
var $header = jQuery('nav'),
    $headerHeight = 90;

var navScroll = {
    
  init:function(){
    jQuery(window).on('scroll',function(){
      navScroll.navDrop();
    })
  },
  
  navDrop:function(){
    var $scrollTop = jQuery(window).scrollTop();
    
    if($scrollTop > $headerHeight){
      $header.addClass('scrolled'); 
    }
    else if($scrollTop == 0) {
      $header.removeClass('scrolled');
    }
    
  }
}
navScroll.init();
});( jQuery )