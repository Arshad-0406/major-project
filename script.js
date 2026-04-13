function generateImage() {
  const prompt = document.getElementById("prompt").value;
  const loader = document.getElementById("loader");
  const img = document.getElementById("output");
  const downloadBtn = document.getElementById("downloadBtn");

  if (!prompt) {
    alert("Please enter a description!");
    return;
  }

  loader.style.display = "block";
  img.style.display = "none";
  downloadBtn.style.display = "none";

  fetch("http://localhost:5000/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt })
  })
  .then(res => res.json())
  .then(data => {
    loader.style.display = "none";

    img.src = data.image;
    img.style.display = "block";

    // Update download button
    downloadBtn.href = data.image;
    downloadBtn.style.display = "inline-block";

    // Add result to gallery
    addToGallery(data.image);
  })
  .catch((err) => {
    loader.style.display = "none";
    console.error(err);
    alert("Error generating image. Check if your server is running.");
  });
}


document.getElementById("prompt").addEventListener("keydown", function(e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    generateImage();
  }
});