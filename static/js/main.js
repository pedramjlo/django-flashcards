document.addEventListener('DOMContentLoaded', function() {
    var categories = document.querySelectorAll(".category-color-square");

    categories.forEach(function(category) {
        var color = category.getAttribute('data-color') || 'white';  // Default to white if color is not provided
        console.log(category, color); // Logging element and color
        category.style.backgroundColor = color;
    });

    const flashcards = document.querySelectorAll('.flashcard');
    flashcards.forEach(flashcard => {
        flashcard.addEventListener('click', () => {
            flashcard.classList.toggle('flipped'); // Toggle flip on card click
        });
    });

    const pinButtons = document.querySelectorAll('.pin-btn');
    pinButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            event.stopPropagation(); // Prevent card flip on pin button click

            // Toggle is_pinned state and update UI
            const isPinned = button.getAttribute('data-pinned') === 'true';
            button.setAttribute('data-pinned', !isPinned);

            // Toggle icon based on the new state
            const svgElement = button.querySelector('svg');
            if (isPinned) {
                svgElement.innerHTML = `<path fill="#797979" d="M22.05 20.212a1.556 1.556 0 0 1-1.713-.363l-1.282-1.282-6.76-.02-1.324 1.325a1.56 1.56 0 0 1-2.541-.504 1.534 1.534 0 0 1-.117-.596v-3.894l-7.269.001a.736.736 0 1 1 0-1.474l7.27-.002.026-3.868a1.557 1.557 0 0 1 2.633-1.086l1.318 1.319 6.745-.038 1.314-1.314a1.55 1.55 0 0 1 2.653 1.095l-.002 9.253a1.55 1.55 0 0 1-.95 1.448Z"/>`;
            } else {
                svgElement.innerHTML = `<path fill="red" d="M20.212 6.234a1.556 1.556 0 0 1-.363 1.713l-1.282 1.282-.02 6.76 1.325 1.325a1.558 1.558 0 0 1-1.1 2.658l-3.894-.001.001 7.269a.736.736 0 1 1-1.474 0l-.002-7.27-3.868-.026a1.557 1.557 0 0 1-1.086-2.633l1.319-1.318-.038-6.745-1.314-1.314a1.55 1.55 0 0 1 1.095-2.653l9.253.002a1.55 1.55 0 0 1 1.448.95Z"/>`;
            }

            // Handle your AJAX request here to change the `is_pinned` state
        });
    });

    const selectElements = document.querySelectorAll('.card-options select');
    selectElements.forEach(select => {
        select.addEventListener('change', function() {
            const flashcardId = select.closest('.flashcard-container').dataset.flashcardId;
            const isLearned = select.id === 'is_learned' ? select.value === 'Yes' : undefined;
            const isPinned = select.id === 'is_pinned' ? select.value === 'Yes' : undefined;

            // AJAX request to update is_learned and is_pinned states
            fetch('/update-flashcard/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken // Ensure CSRF token is included
                },
                body: JSON.stringify({ flashcardId, isLearned, isPinned })
            }).then(response => response.json())
              .then(data => {
                  // Handle the response, update UI if needed
              });
        });
    });
});
