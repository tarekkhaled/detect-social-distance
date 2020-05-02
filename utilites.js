// TODO::LATER

const fs = require('fs');
(function createEnviormentPaths () {
    let envs = getEachPathAlone(process.env.path);
    let pythonPath = getPythonScriptsPath(envs);
    fs.writeFile('./.env',`pythonPath=${pythonPath}`,(err) => {
        if(err) console.error(err)
    });
}())

function getEachPathAlone(string) {
    const paths = [];
    let path = ''
   for (let i = 0; i < string.length ; i++) {
       if (string[i] === ';') {
           paths.push(path)
           path = ''
       } 
       string[i] != ';' && (path = path + (string[i]));
   }
   return paths;
}

function getPythonScriptsPath(envs) {
    let regex = /C:.*\python[1-9]{2}\\+Scripts/g
    let path = envs.find( path => regex.test(path) ); 
    if (!path) throw new Error('Python Scripts is missing from Enviorments !');
    return path;
}


