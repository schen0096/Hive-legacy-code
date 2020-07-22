let greeting = document.querySelector(".greetingFont");

// Get the current time
let today = new Date();
let currentHour = today.getHours();
console.log("hours", currentHour);

if (0 < currentHour && currentHour < 12) {
  greeting.textContent = "Good morning,";
}

else if (12 <= currentHour && currentHour < 17) {
  greeting.textContent = "Good afternoon,";
}

else if (17 <= currentHour && currentHour < 20) {
  greeting.textContent = "Good evening,";
}

else if (20 <= currentHour && currentHour < 24) {
  greeting.textContent = "Good night,";
}
