// navbar

var nav = gsap.timeline({defaults:{duration:0.5}});   
nav.fromTo("nav", { y:-80 , opacity: 0.2}, {y:0, opacity:1, ease: Circ.easeOut} )
    .fromTo(".navtitle", {y:-50 , opacity: 0.5}, {y:0 , opacity:1, ease: Circ.easeOut},'<.5')
    .fromTo(".navlinks", {y:-50 , opacity: 0.5}, {y:0 , opacity:1, ease: Circ.easeOut},'<')
;

// login page

  
nav.fromTo(".loginForm", {opacity: 0.0, scale:0.8}, {opacity:1, scale:1, ease: Circ.easeOut},"0.5" )
     .fromTo(".loginForm h2", {y:-80 , opacity: 0.0}, {y:0 , opacity:1, ease: Circ.easeOut},)
     .fromTo("form", {y:-40 , opacity: 0.0}, {y:0 , opacity:1, ease: Circ.easeOut},"<")
;