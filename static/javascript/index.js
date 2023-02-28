console.log('Welcome to DiabetesX!!!');

// why [0] even if only one element
// link: https://stackoverflow.com/a/32027957
const copyBtn = document.getElementsByClassName('ui-copy-btn')[0];

const onURLBtnClicked = (event) => {
  const api_url = copyBtn.getAttribute('data-api');

  // copy to clipboard
  navigator.clipboard.writeText(api_url);
  copyBtn.textContent = 'Api Copied!!';
  setTimeout(() => {
    copyBtn.textContent = 'diabetesx-api';
  }, 1200);
};

copyBtn.addEventListener('click', onURLBtnClicked);
