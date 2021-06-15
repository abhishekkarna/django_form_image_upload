$(document).ready(() => {
  $("#spinner").hide();
  const payload = new FormData();
  $("#sourceImage").on("change", () => {
    payload.append("sourceImage", $("#sourceImage")[0].files[0]);
  });
  $("#checkprintImage").on("change", () => {
    payload.append("checkprintImage", $("#checkprintImage")[0].files[0]);
  });

  function openFile(blob, filename) {
    if (window.navigator.msSaveOrOpenBlob) {
      window.navigator.msSaveOrOpenBlob(blob, filename);
    } else {
      console.log("blob", blob);
      const a = document.createElement("a");
      document.body.appendChild(a);
      const url = window.URL.createObjectURL(blob);
      a.href = url;
      a.target = "_blank";
      a.click();
      setTimeout(() => {
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
      }, 0);
    }
  }

  $("#uploadImage").on("click", () => {
    $("#spinner").show();
    fetch("http://localhost:8000/image-upload", {
      method: "POST",
      body: payload,
    })
      .then((response) => {
        $("#spinner").hide();
        response.blob().then((blob) => {
          console.log("blob", blob);
          openFile(blob, "result");
        });
      })
      .catch((er) => $("#spinner").hide());
  });
});
