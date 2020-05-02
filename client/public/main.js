const {execFile} = require('child_process');
const open = require('open')
const config = require('../config');
const path =require('path')
const chooseFileBtn = document.querySelector('.choose-file');


chooseFileBtn.addEventListener('click', callJupyterCell);

async function callJupyterCell(e) {
   try {
    await open(path.join(__dirname ,'..' ,'..', 'backend\\', 'webcam.pyc'),{wait:true})
   }catch(e) {
       console.error(e)
   }

}