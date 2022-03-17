var nav = gsap.timeline({defaults:{duration:0.5}});   
nav.fromTo("nav", { y:-80 , opacity: 0.2}, {y:0, opacity:1, ease: Circ.easeOut} )
    .fromTo(".navtitle", {y:-50 , opacity: 0.5}, {y:0 , opacity:1, ease: Circ.easeOut},'<.5')
    .fromTo(".navlinks", {y:-50 , opacity: 0.5}, {y:0 , opacity:1, ease: Circ.easeOut},'<')
;



