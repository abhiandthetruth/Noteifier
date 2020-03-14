const textAreas = document.getElementsByClassName("text-area");
let i = 0;
let xhr = new XMLHttpRequest();
xhr.open('POST', 'https://api.github.com/markdown', true);
data = { "text": textAreas[0].innerHTML, "mode": "markdown"};
xhr.onreadystatechange = function()
{
    if (xhr.readyState == 4 && xhr.status == 200)
    {
        textAreas[i].innerHTML = xhr.responseText;
        i = i+1;
        if (i == textAreas.length) return;
        data = { "text": textAreas[i].innerHTML, "mode": "markdown"}
        xhr.open('POST', 'https://api.github.com/markdown', true);
        xhr.send(JSON.stringify(data));
    }
};
xhr.send(JSON.stringify(data));
