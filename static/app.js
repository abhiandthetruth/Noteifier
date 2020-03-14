const previewBtn = document.getElementById('preview-btn');
    textArea = document.getElementById('text-area');
    previewArea = document.getElementById('preview-area');
    xhr = new XMLHttpRequest();
xhr.onreadystatechange = function()
{
    if(xhr.readyState == 4 && xhr.status == 200) {
        previewArea.innerHTML = xhr.responseText
    }
}
previewBtn.addEventListener('click',handlePreview);

function handlePreview(e){
    console.log(textArea.value)
    xhr.open('POST', 'https://api.github.com/markdown', true);
    data = { "text": textArea.value, "mode": "markdown"}
    xhr.send(JSON.stringify(data));
}