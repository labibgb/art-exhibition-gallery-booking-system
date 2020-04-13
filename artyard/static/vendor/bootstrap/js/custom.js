setTimeout( function(){
    $("#message").fadeOut('slow');
}, 3000);
$("#custom-checkbox").on('click', function() {
    // in the handler, 'this' refers to the box clicked on
    var $box = $(this);
    console.log( $box )
    if ($box.is(":checked")) {
      // the name of the box is retrieved using the .attr() method
      // as it is assumed and expected to be immutable
      //var group = "#custom-checkbox[name='" + $box.attr("name") + "']";
      // the checked state of the group/box on the other hand will change
      // and the current value is retrieved using .prop() method
      //$(group).prop("checked", false);
      $box.prop("checked", true);
    } else {
      $box.prop("checked", false);
    }
});
$(document).ready(function() {
  $('.mdb-select').materialSelect();
});