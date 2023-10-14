document.addEventListener('DOMContentLoaded', function() {
    // Get the slider container and individual items
    const sliderContainer = document.getElementById('slider-container');
    const sliderItems = sliderContainer.querySelectorAll('.slider-item');

    let currentIndex = 0; // Index of the currently displayed slide

    // Function to show a specific slide
    function showSlide(index) {
        // Hide all slides
        sliderItems.forEach(item => {
            item.style.display = 'none';
        });

        // Show the selected slide
        sliderItems[index].style.display = 'block';
    }

    // Initial slide display
    showSlide(currentIndex);

    // Function to display the next slide
    function nextSlide() {
        currentIndex = (currentIndex + 1) % sliderItems.length;
        showSlide(currentIndex);
    }

    // Function to display the previous slide
    function prevSlide() {
        currentIndex = (currentIndex - 1 + sliderItems.length) % sliderItems.length;
        showSlide(currentIndex);
    }

    // Optional: Auto-play the slider
    const autoPlayInterval = 5000; // 5 seconds
    setInterval(nextSlide, autoPlayInterval);

    // Optional: Add navigation buttons (e.g., Next and Previous)
    const nextButton = document.getElementById('next-button');
    const prevButton = document.getElementById('prev-button');

    if (nextButton && prevButton) {
        nextButton.addEventListener('click', nextSlide);
        prevButton.addEventListener('click', prevSlide);
    }
});
