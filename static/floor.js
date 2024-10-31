document.addEventListener("DOMContentLoaded", () => {
    const floorImage = document.getElementById("floor-image");
    let scale = 1;
    let isDragging = false;
    let startX, startY;

    // Zoom with the mouse wheel
    floorImage.addEventListener("wheel", (event) => {
        event.preventDefault();
        scale += event.deltaY * -0.001;  // Adjust the zoom sensitivity
        scale = Math.min(Math.max(0.5, scale), 3);  // Limit the zoom level
        floorImage.style.transform = `scale(${scale})`;
    });

    // Drag to move the image
    floorImage.addEventListener("mousedown", (event) => {
        isDragging = true;
        startX = event.pageX - floorImage.offsetLeft;
        startY = event.pageY - floorImage.offsetTop;
        floorImage.style.cursor = "grabbing";
    });

    floorImage.addEventListener("mousemove", (event) => {
        if (isDragging) {
            const x = event.pageX - startX;
            const y = event.pageY - startY;
            floorImage.style.left = `${x}px`;
            floorImage.style.top = `${y}px`;
        }
    });

    floorImage.addEventListener("mouseup", () => {
        isDragging = false;
        floorImage.style.cursor = "grab";
    });

    floorImage.addEventListener("mouseleave", () => {
        isDragging = false;
        floorImage.style.cursor = "grab";
    });
});
