    function login() {
      // Get the phone number and password values from the input fields
      var phone = document.getElementById('phone').value;
      var password = document.getElementById('password').value;
      console.log(phone);
      console.log(password)

      // Create the request payload
      var data = {
        phone: phone,
        password: password
      };

      // Make the POST request using fetch
        fetch("http://127.0.0.1:8000/twillo/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}"
            },
            body: JSON.stringify(data)
        })
      .then(response => {
        if (response.ok) {
          // Successful login
          console.log('Login successful');
          // Perform any additional actions if needed
        } else {
          // Error occurred during login
          console.log('Login failed');
        }
      })
      .catch(error => {
        console.error('An error occurred:', error);
      });
    }