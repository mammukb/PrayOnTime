document.getElementById('prayerForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    function getPrayerStatus(prayerId) {
      const status = {
        ontime: 0,
        late: 0,
        missed: 0,
        withImam: 0
      };
  
      const select = document.getElementById(prayerId);
      const selectedValue = select.value;
      if (selectedValue) {
        status[selectedValue] = 1;
      }
  
      const withImamCheckbox = document.querySelector(`#${prayerId}imam`);
      if (withImamCheckbox.checked) {
          status.withImam = 1;
      }
      
  
      return status;
    }
  
    const prayers = {
      fajr: getPrayerStatus('fajr'),
      dhuhr: getPrayerStatus('dhuhr'),
      asr: getPrayerStatus('asr'),
      maghrib: getPrayerStatus('maghrib'),
      isha: getPrayerStatus('isha')
    };
  
    console.log(prayers);
    console.log(JSON.stringify(prayers));

    $.ajax({
        URL : 'http://127.0.0.1:8000/userhome',
        type: 'POST',
        contentType: 'application/json',
        data : JSON.stringify(prayers),
        success: function(responseData) {
            console.log('Response from Django backend:', responseData);
        },
        error: function(xhr, status, error) {
            console.error('AJAX request error:', error);
        }
    });




});

console.log("heloooo");

// function submitform() {

//     function getPrayerStatus(prayerId) {
//         const status = {
//           ontime: 0,
//           late: 0,
//           missed: 0,
//           withImam: 0
//         };
    
//         const select = document.getElementById(prayerId);
//         const selectedValue = select.value;
//         if (selectedValue) {
//           status[selectedValue] = 1;
//         }
    
//         const withImamCheckbox = document.getElementById(`${prayerId}_imam`);
//         if (withImamCheckbox.checked) {
//           status.withImam = 1;
//         }
    
//         return status;
//       }
    
//       const prayers = {
//         fajr: getPrayerStatus('fajr'),
//         dhuhr: getPrayerStatus('dhuhr'),
//         asr: getPrayerStatus('asr'),
//         maghrib: getPrayerStatus('maghrib'),
//         isha: getPrayerStatus('isha')
//       };
    
//       console.log(prayers);



// };