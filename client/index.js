const {app,BrowserWindow} = require('electron');

let mainWindow = null; 

// Emitted when the app "ready"
app.on('ready',startElectronApp);


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



