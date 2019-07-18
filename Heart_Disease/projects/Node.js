
     // Create the XHR object.
function createCORSRequest(method, url) {
    var xhr = new XMLHttpRequest();
    if ("withCredentials" in xhr) {
      // XHR for Chrome/Firefox/Opera/Safari.
      xhr.open(method, url, true);
    } else if (typeof XDomainRequest != "undefined") {
      // XDomainRequest for IE.
      xhr = new XDomainRequest();
      xhr.open(method, url);
    } else {
      // CORS not supported.
      xhr = null;
    }
    return xhr;
  }
     
  // Make the actual CORS request.
  function makeCorsRequest(method, url, data, callback) {
    var xhr = createCORSRequest(method, url);
    if (!xhr) {
      alert('CORS not supported');
      return;
    }
    
    // Response handlers.
    xhr.onload = function() {      
      fetch(url, {
            method: method,
            body: data,
      })
      .then((res) => res.json())
      .then((resJSON) => {
          resJSON = JSON.parse(resJSON['body']);
          console.log('res JSON', resJSON);
          callback(resJSON);
       })
      .catch(err => console.log('err', err));
    };

    xhr.onerror = function() {
      callback(xhr.response);
    };
  
    xhr.send();
  }