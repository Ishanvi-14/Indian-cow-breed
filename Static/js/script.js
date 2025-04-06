document.addEventListener("DOMContentLoaded", function () {
    const imageInput = document.getElementById("image");
    const previewContainer = document.getElementById("image-preview");
    const previewImage = previewContainer.querySelector("img");
  
    imageInput.addEventListener("change", function () {
      const file = this.files[0];
      if (file) {
        const reader = new FileReader();
  
        reader.addEventListener("load", function () {
          previewImage.setAttribute("src", this.result);
          previewContainer.style.display = "block";
        });
  
        reader.readAsDataURL(file);
      } else {
        previewImage.setAttribute("src", "");
        previewContainer.style.display = "none";
      }
    });
  
    // ✅ Language dropdown with persistent default
    const languages = [
      { code: "en", name: "English" },
      { code: "hi", name: "Hindi" },
      { code: "mr", name: "Marathi" },
      { code: "ta", name: "Tamil" },
      { code: "te", name: "Telugu" },
      { code: "kn", name: "Kannada" }
    ];
    const select = document.getElementById("language-select");
    select.innerHTML = "";
    languages.forEach((lang) => {
      const option = document.createElement("option");
      option.value = lang.code;
      option.textContent = lang.name;
      if (lang.code === select.dataset.selected) option.selected = true;
      select.appendChild(option);
    });
  });
  
  // ✅ Map and vet listing
  function initMap() {
    if (!navigator.geolocation) {
      alert("Geolocation is not supported by your browser.");
      return;
    }
  
    navigator.geolocation.getCurrentPosition(position => {
      const userLocation = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
      };
  
      const map = new google.maps.Map(document.getElementById("map"), {
        center: userLocation,
        zoom: 12,
      });
  
      new google.maps.Marker({
        position: userLocation,
        map: map,
        title: "You are here",
        icon: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
      });
  
      const service = new google.maps.places.PlacesService(map);
      service.nearbySearch({
        location: userLocation,
        radius: 10000,
        keyword: "veterinary doctor"
      }, (results, status) => {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
          const vetList = document.getElementById("vet-list");
          vetList.innerHTML = "";
          results.forEach(place => {
            new google.maps.Marker({
              map: map,
              position: place.geometry.location,
              title: place.name
            });
  
            // 🩺 Add to vet list below map
            const listItem = document.createElement("li");
            const phone = place.formatted_phone_number || "Phone not available";
            const link = `https://www.google.com/maps/place/?q=place_id:${place.place_id}`;
  
            listItem.innerHTML = `
              <strong>${place.name}</strong><br>
              📍 <a href="${link}" target="_blank">View on Maps</a><br>
              📞 ${phone}<br><br>
            `;
            vetList.appendChild(listItem);
          });
        }
      });
    }, () => {
      alert("Unable to retrieve your location.");
    });
  }
  