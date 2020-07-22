let dropdown = document.querySelectorAll("#dropdown-arrow");
let upArrow = `<i class="fas fa-angle-up"></i>`
let downArrow = `<i class="fas fa-angle-down"></i>`
let firstRow = document.querySelectorAll(".first-row")
let name = document.querySelector("#company-name-div");
let status = document.querySelector("#company-client-status");
let startDate = document.querySelector("#company-start-date");
let endDate = document.querySelector("#company-end-date");


dropdown.forEach(item => {
    let tr = item.parentNode.parentNode.parentNode;
    item.addEventListener("click", () => {
      //toggling between up and down arrows
      if (item.children[0].classList[1] === "fa-angle-down") {
        item.innerHTML = upArrow;
        let tds = tr.children;
        // tr.insertAdjacentHTML('afterend', `
        //             <tr class="extra-info-row">
        //               <td><strong>PoC:</strong> ${tr.classList[1]}</td>
        //               <td></td>
        //               <td><strong>Arcade Active Accounts: </strong> ${tr.classList[3]}</td>
        //               <td><strong>OrgID:</strong> ${tr.classList[2]}</td>
        //             </tr>`);
        tds[0].firstElementChild.insertAdjacentHTML('afterend', `
        <div id="poc">
          <strong>PoC:</strong> ${tr.classList[1]}
        </div>`)

        tds[1].firstElementChild.insertAdjacentHTML('afterend', `
        <div id="sub-active">
        </div>`)

        tds[2].firstElementChild.insertAdjacentHTML('afterend', `
        <div id="active-account">
          <strong>Arcade Accounts: </strong> ${tr.classList[3]}
        </div>`)

        tds[3].firstElementChild.insertAdjacentHTML('afterend', `
        <div id="org-id">
          <strong>OrgID:</strong> ${tr.classList[2]}
        </div>`)

      }
      else if (item.children[0].classList[1] === "fa-angle-up"){
        item.innerHTML = downArrow;
        tr.children[0].lastElementChild.remove();
        tr.children[1].lastElementChild.remove();
        tr.children[2].lastElementChild.remove();
        tr.children[3].lastElementChild.remove();
      }
    })

})
