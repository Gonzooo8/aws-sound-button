const soundButton = document.getElementById("sound-button");

soundButton.addEventListener("click", () => {
  const sound = new Audio("/static/audio/duck-toy-sound.mp3");
  sound.play().catch((error) => {
    console.error("音声を再生できませんでした。", error);
  });
});
