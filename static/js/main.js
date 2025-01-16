document.addEventListener('DOMContentLoaded', function() {
    var categories = document.querySelectorAll(".category-color-square");

    categories.forEach(function(category) {
        var color = category.getAttribute('data-color') || 'white';  // Default to white if color is not provided

        console.log(category, color);  // Logging element and color

        category.style.backgroundColor = color;  
        var colorSquares = category.querySelectorAll('.category-color-square');
        
        colorSquares.forEach(function(square) {
            square.style.backgroundColor = color;
        });
    });
});
