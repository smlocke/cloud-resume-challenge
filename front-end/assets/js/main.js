const countEl = document.getElementById('count');

updateVisitCount();

function updateVisitCount() {
  fetch('https://c4pnv7cd7a.execute-api.us-east-1.amazonaws.com/dev/count')
    .then(res => res.json())
    .then(res => {
        countEl.innerHTML = res;
  });
}



//     .then((data) => {
//         document.getElementById('count').innerText = data.count
//          })
// }



// function updateVisitCount() {
//   fetch('https://u9ef363qq1.execute-api.us-east-1.amazonaws.com/Prod/visitor/')
//   .then(res => res.json())
//   .then(res => {
//     countEl.innerHTML = res;
//   });
// }