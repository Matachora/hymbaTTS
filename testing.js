let cont;

function render() {
    cont = document.getElementById('cont');
    let plans = document.createElement('DIV');
    plans.innerHTML=`
    <div class="plan"> 
        <h1>free</h1>
        <h2>$0</h2>
    </div>
    <div class="plan">
        <h1>premium</h1>
        <h2>$100</h2>
    </div>
    `;
    cont.appendChild(plans);
}

function hide() {
    cont.style.display="none";
}