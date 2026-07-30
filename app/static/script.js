const soundButton = document.getElementById("sound-button");
const buttonCount = document.getElementById("button-count");

async function loadCount() {
  const response = await fetch("/api/count");
  const data = await response.json();

  buttonCount.textContent = data.count;
}

loadCount();

soundButton.addEventListener("click", async () => {
  const sound = new Audio("/api/audio");

  sound.play().catch((error) => {
    console.error("音声を再生できませんでした。", error);
  });

  const response = await fetch("/api/count", {
    method: "POST",
  });

  const data = await response.json();
  buttonCount.textContent = data.count;
});
