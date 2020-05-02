const {app,BrowserWindow,ipcMain,dialog} = require('electron');

let mainWindow = null; 

// Emitted when the app "ready"
app.on('ready',startElectronApp);


ipcMain.on('get-file-from-user',getFileFromUser);



function startElectronApp () {
    mainWindow = new BrowserWindow({
        darkTheme       :       true,
        show            :       false,
        webPreferences  :       {
            nodeIntegration: true
        },
        width           :       955
    })

    mainWindow.loadFile('./public/index.html');
    
    // Emitted when file loaded successfully 
    mainWindow.on('ready-to-show', () => {
        mainWindow.show();
    })
}


function getFileFromUser () {
    const files = dialog.showOpenDialogSync({
        properties      :   ['openFile'],
        title           :   'Choose The Image for Processing it'
    })

    if(!files) return ;
    const file = files[0]; // first file 
    mainWindow.webContents.send('file-already-chosen',file);
}



