const raindrop = document.querySelector(".raindrop");

function randRange(minNum, maxNum) {
  return Math.floor(Math.random() * (maxNum - minNum)) + minNum;
}

const rain = setInterval(function() {
  const randLeft = randRange(0, 1600);
  const randHeight = randRange(10, 15);
  const randWidth = randRange(0.3, 3);
  const newRaindrop = document.createElement("div");

  newRaindrop.className = "raindrop";
  newRaindrop.style.left = `${randLeft}px`;
  newRaindrop.style.height = `${randHeight}px`;
  newRaindrop.style.width = `${randWidth}px`;

  if (parseFloat(newRaindrop.style.width) < 1.5) {
    newRaindrop.style.animationDuration = "2s";
  }

  document.querySelector(".background").appendChild(newRaindrop);
}, 100);

setTimeout(function() {
  clearInterval(rain);
}, 13000);
