const {execFile} = require('child_process');
const config = require('../config');
const chooseFileBtn = document.querySelector('.choose-file');


chooseFileBtn.addEventListener('click', callJupyterCell);

async function callJupyterCell(e) {
    /** First Approach */
    /*
    const response = await fetch(`${config.jupyterURL}/${config.jupyterRoute}?${config.jupyterQuery}=true`);
    console.log({response})
    if(response.status !== 200) {
        alert('Check the JupyterURL link, the jupyter kernel gateway is running')
    } */
    execFile('../../backend/webcam.pyc',['--version'],(error,stdout)=>{
        if(error) throw error;
    })
    
}