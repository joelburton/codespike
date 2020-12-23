// Based on https://jsfiddle.net/developit/bwgkr6uq/ which just works but is based on unpkg.com.
// Provided by loader.min.js.
require.config({paths: {'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs'}});
window.MonacoEnvironment = {getWorkerUrl: () => proxy};
let proxy = URL.createObjectURL(new Blob([`
    self.MonacoEnvironment = {
        baseUrl: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min'
    };
    importScripts('https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs/base/worker/workerMain.min.js');
`], {type: 'text/javascript'}));
require(["vs/editor/editor.main"], function () {
    let editor = monaco.editor.create(document.getElementById('container'), {
        value: problemCode,
        language: 'javascript',
        theme: 'vs-dark'
    });
    editor.addAction({
        // An unique identifier of the contributed action.
        id: 'test-code',

        // A label of the action that will be presented to the user.
        label: 'Test My Code',

        // An optional array of keybindings for the action.
        keybindings: [
            monaco.KeyMod.CtrlCmd | monaco.KeyCode.F10,
            // chord
            monaco.KeyMod.chord(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KEY_K, monaco.KeyMod.CtrlCmd | monaco.KeyCode.KEY_M)
        ],

        // A precondition for this action.
        precondition: null,

        // A rule to evaluate on top of the precondition in order to dispatch the keybindings.
        keybindingContext: null,

        contextMenuGroupId: 'navigation',

        contextMenuOrder: 1.5,

        // Method that will be executed when the action is triggered.
        // @param editor The editor instance is passed in as a convinience
        run: function (ed) {
            let text = ed.getValue();
            eval(`func = ${text}`);
            x = eval(text);
            output = func();
            eval(onlyTestCode);
        }


    });
});