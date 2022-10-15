const countEl = document.getElementById('count');

updateVisitCount();

// New and hot in-development API URL
function updateVisitCount() {
  fetch('https://76yyihxkq6.execute-api.us-east-1.amazonaws.com/dev2/count')
    .then(res => res.json())
    .then(res => {
        countEl.innerHTML = res;
  });
}

// // Old, known-good API URL
// function updateVisitCount() {
//   fetch('https://c4pnv7cd7a.execute-api.us-east-1.amazonaws.com/dev/count')
//     .then(res => res.json())
//     .then(res => {
//         countEl.innerHTML = res;
//   });
// }