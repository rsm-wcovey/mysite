async function hashPassword(password) {
    const encoder = new TextEncoder();
    const data = encoder.encode(password);
    const hashBuffer = await crypto.subtle.digest("SHA-256", data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, "0")).join("");
    return hashHex;
  }
  
  const correctHash = "f98f3d8cbcfa62aac83f1abb6411e40c5da9b2cf9ed67c0227b8675351a04500";
  
  window.onload = async () => {
    const password = prompt("Enter password:");
    const inputHash = await hashPassword(password);
  
    if (inputHash === correctHash) {
      document.getElementById("protected-content").style.display = "block";
    } else {
      document.body.innerHTML = "<h1>Access Denied</h1>";
    }
  };
  