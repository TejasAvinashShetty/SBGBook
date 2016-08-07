//
// For toying around, just build everything here. 
// As the UI model becomes clearer we can modularize
//

define(['backbone',], function(Backbone) {
  var App = Backbone.View.extend({
    initialize: function() {
    }
  });
  
//
// first declare some backbone models
//

    Person = Backbone.Model.extend({
        defaults :{
            firstName : '',
            lastName : '',
            studentID : '',
            email: ''
        }
    });

    Class = Backbone.Model.extend({
        defaults :{
            name : '',
            startDate : '',
            endDate : ''
        }
    });

    Role = Backbone.Model.extend({
        defaults :{
            name : ''
        }
    });

    Section = Backbone.Model.extend({
        defaults :{
            name : '',
            classID : ''
        }
    });

    PersonCollection = Backbone.Collection.extend({
        model: Person,

	});
    



  return App;
});
