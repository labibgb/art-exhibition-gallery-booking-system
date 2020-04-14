setTimeout( function(){
    $("#message").fadeOut('slow');
}, 3000);
$(".custom-control-input").on('click', function() {
    // in the handler, 'this' refers to the box clicked on
    var $box = $(this);
    if ($box.is(":checked")) {
      console.log("click");
      // the name of the box is retrieved using the .attr() method
      // as it is assumed and expected to be immutable
      var group = ".custom-control-input[name='" + $box.attr("name") + "']";
      // the checked state of the group/box on the other hand will change
      // and the current value is retrieved using .prop() method
      console.log( group );
      $(group).prop("checked", false);
      $box.prop("checked", true);
    } else {
      console.log("click1");
      $box.prop("checked", false);
    }
});
function intcon( x )
{
  var res = 0;
  for( var i = 0 ; i < x.length ; i++ )
  {
    if( x[ i ] >= '0' && x[ i ] <= '9' )
    {
      res *= 10;
      res += (x[ i ]-'0');
      
    }
  }
  return res;
}
function dateConverter( date )
{
  var arr = new Array();
  var c = 0;
  var cal = 0;
  for( var i = 0 ; i < date.length ; i++ )
  {
    //console.log( date[ i ] );
    if( date[ i ] =='-')
    {
      console.log( date[ i ] );
      arr.push(cal);
      cal = 0; 
    }
    else if( date[ i ] >= '0' && date[ i ] <= '9' )
    {
      cal *= 10;
      console.log( date[ i ] );
      cal += date[ i ]-'0';
      
    }
  }
  arr.push( cal );
  return arr;
}
var month = [ 0 , 31 , 28 , 31 , 30 , 31 , 30, 31 , 31 , 30 , 31 ,30 , 31 ];
console.log( month );

var stday = document.querySelector("#stday").textContent;
var edday = document.querySelector("#edday").textContent;
var conestday = dateConverter( stday );
var coneedday = dateConverter( edday );
console.log( conestday );
console.log( coneedday );

var day = coneedday[ 2 ]-conestday[ 2 ]+1;
if( day < 0 ){
    day += month[ conestday[ 1 ] ];
    conestday[ 1 ] = conestday[ 1 ] +1;
}
  var mn = coneedday[ 1 ]-conestday[ 1 ];
  if( mn < 0 )
  {
    mn += 12;
    conestday[ 0 ] = conestday[ 0 ] + 1;
  }
  year = coneedday[ 0 ]-conestday[ 0 ];
  year *= 365;
  for( var i = conestday[ i ]; i <= coneedday[ 1 ]; i++  )
  {
    day += month[ i ];
  }
  day += year;
  if( day < 0 ){
    day = 1;
  }

  var val = document.querySelector("#galleryAmount").textContent;
  var total = 0;
  total = intcon( val );
  total = total * day;

  document.querySelector("#pay").textContent = 'Pay '+ total +'৳';
  var cost = document.querySelector("#cost");
  cost.setAttribute('value', total);
  $(function() {
    $('[data-toggle="tooltip"]').tooltip()
  })
