$(document).foundation();
$("#portal-globalnav").tinyNav({
    active: 'selected', // String: Set the "active" class
    header: 'Navigation', // String: Specify text for "header" and show header instead of the active item
    indent: '- ', // String: Specify text for indenting sub-items
    label: '' // String: Sets the 
});

    $( "#button-search" ).click(function() {
      $( "#effect" ).removeClass( "show-for-large" );
    });
    function callback() {
      setTimeout(function() {
        $( "#effect" ).addClass( "newClass" );
      }, 1500 );
    }