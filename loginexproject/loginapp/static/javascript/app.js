window.onload = () => {
    const loadAnimation = document.getElementById("loader");
    const loginWord = document.getElementById("btn-login");

    console.log(loadAnimation);
    turnToLoading();
    function turnToLoading() {
            loginWord.addEventListener("click", () => {
                if(loginWord.value != ''){
                   loginWord.value = ''
                   loadAnimation.style.display = 'inline-block'
                }
            });
    }
};
