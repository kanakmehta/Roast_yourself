const video = document.getElementById("video");

// start webcam
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        alert("Camera access denied");
    });

async function scan() {
    const line = document.getElementById("line");
    const img = document.getElementById("img");

    line.innerText = "Scanning... 👀";
    img.src = "";

    // capture frame
    const canvas = document.createElement("canvas");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const imageData = canvas.toDataURL("image/jpeg");

    // send to backend
    let res = await fetch('/scan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: imageData })
    });

    let data = await res.json();

    setTimeout(() => {
        img.src = "/static/images/" + data.image;
        line.innerText = data.line;
    }, 1000);
}
async function scan() {
    const line = document.getElementById("line");
    const img = document.getElementById("img");

    line.innerText = "Scanning...";

    let res = await fetch('/get_character');
    let data = await res.json();

    img.src = "/static/images/" + data.image;
    line.innerText = data.line;
}