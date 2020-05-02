const {execFile} = require('child_process');
const open = require('open')
const config = require('../config');
const chooseFileBtn = document.querySelector('.choose-file');


chooseFileBtn.addEventListener('click', callJupyterCell);

async function callJupyterCell(e) {
   try {
    await open(__dirname + '\\' + 'webcam.pyc',{wait:true})
   }catch(e) {
       console.error(e)
   }

}