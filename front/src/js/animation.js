export const initAnimation = () => {
    /* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
    particlesJS.load('particles-js', 'static/build/js/plugins/particles.json', function() {
      console.log('callback - particles.js config loaded');
    });

    particlesJS.load('particles-js2', 'static/build/js/plugins/particles.json', function() {
      console.log('callback - particles.js config loaded');
    });
}


