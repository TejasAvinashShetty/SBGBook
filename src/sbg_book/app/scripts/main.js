require.config({
  paths: {
    'jquery': 'vendor/jquery/dist/jquery',
    'underscore': 'vendor/underscore/underscore',
    'backbone': 'vendor/backbone/backbone',
    'backbone.babysitter': 'vendor/backbone.babysitter/lib/backbone.babysitter',
    'backbone.wreqr': 'vendor/backbone.wreqr/lib/backbone.wreqr',
    'backbone.marionette': 'vendor/marionette/lib/backbone.marionette',
  },
  shim: {
    underscore: {
      exports: '_'
    },
    backbone: {
      exports: 'Backbone',
      deps: ['jquery', 'underscore']
    },
    marionette: {
      exports: 'Backbone.Marionette',
      deps: ['backbone']
    },
  },
  deps: ['jquery', 'underscore']
});
 
require(['jquery','underscore','backbone','backbone.babysitter','backbone.wreqr','backbone.marionette','views/app'], function($,_,Bb,Bbb,Bbw,Mnt,AppView) {
  new AppView; 
});
