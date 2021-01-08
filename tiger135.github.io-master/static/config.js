require.config({
    baseUrl: window.baseUrl ? window.baseUrl : '.',
    paths: {
        'rome': 'js/vendor/rome/dist/rome.min',
        'leafletdraw': 'js/vendor/leaflet-draw/dist/leaflet.draw',
        'tomtom.min': 'sdk/tomtom.min'
    },
    shim: {
        'rome': {
            exports: 'rome'
        },
        'leafletdraw': {
            deps: ['tomtom.min'],
            exports: 'leafletdraw'
        }
    }
});
