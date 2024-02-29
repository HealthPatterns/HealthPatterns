import { loginData, trackingData } from "../store.js";
import { get } from "svelte/store";

const url = "https://localhost/api";

export async function fetchData() {
  try {
    await apiGetUsername(get(loginData).accessToken);
    await apiGetActiveTracking(get(loginData).accessToken);
    if (get(trackingData).isTracking){
      apiGetDetails (get(loginData).accessToken, get(trackingData).tracking_id)
    }
  } catch (error) {
    console.error("Error fetchData:", error);
  }
}

export async function apiLogin(username : string, password : string) {
const api_url = `${url}/auth/login`;

const formData = new URLSearchParams();
formData.append('username', username);
formData.append('password', password);

const options = {
method: 'POST',
headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'accept': 'application/json'
},
body: formData
};

try {
const response = await fetch(api_url, options);
const statusCode = response.status;
if (statusCode === 200) {
    const data = await response.json();
    get(loginData).accessToken = data.access_token;
    fetchData();
    console.log("API call 'Login' successful.");
    return true;
} else {
    console.log("Error during API call 'Login'.");
    return "Login failed. Please check your credentials";
}
} catch (error) {
console.error("Error:", error);
}
}

export async function apiRegister(username : string, password : string) {
const api_url = `${url}/user/register`;

const data = {
  nickname: username,
  password: password
};

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'accept': 'application/json'
  },
  body: JSON.stringify(data)
};

try {
const response = await fetch(api_url, options);
const statusCode = response.status;
if (statusCode === 201) {
    const data = await response.json();
    console.log(data);
    //TODO: Login after successful registration
    console.log("API call 'Register' successful.");
} else {
    console.log("Error during API call 'Register'.");
    return "Registration failed. Please check your credentials";
}
} catch (error) {
console.error("Error:", error);
}
}

export async function apiGetUsername(api_token: string) {
const api_url = `${url}/user/name`;

const options = {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
    accept: "application/json",
    Authorization: "Bearer " + api_token,
  },
};

try {
  const response = await fetch(api_url, options);
  const statusCode = response.status;
  if (statusCode === 200) {
    console.log("API call 'GetUsername' successful.");
    const data = await response.json();
    loginData.update((ld) => {
      ld.username = data.display_name;
      return ld;
    });
  } else {
    console.log("Error during API call 'GetUsername'.");
  }
} catch (error) {
  console.error("Error:", error);
}
}

export async function apiStartTracking(api_token: string) {
  const current_time = Math.floor(Date.now() / 1000);
  const api_url = `${url}/trackings`;

  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'accept': 'application/json',
      'Authorization': 'Bearer ' + api_token,
    },
    body: JSON.stringify({
      'time_start': current_time
    })
  };

  try {
    const response = await fetch(api_url, options);
    const statusCode = response.status;
    if (statusCode === 201) {
      console.log("API call 'StartTracking' successful.");
      const data = await response.json();
      trackingData.update((td) => {
        td.tracking_id = data.id;
        return td;
      });
    } else {
      console.log("Error during API call 'StartTracking'.");
    }
  } catch (error) {
    console.error("Error:", error);
  }
}

export async function apiStopTracking(api_token: string, tracking_id: string) {
  const current_time = Math.floor(Date.now() / 1000);
  const api_url = `${url}/trackings/${tracking_id}`;

  const options = {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'accept': 'application/json',
      'Authorization': 'Bearer ' + api_token,
    },
    body: JSON.stringify({
      'time_end': current_time
    })
  };

  try {
    const response = await fetch(api_url, options);
    const statusCode = response.status;
    if (statusCode === 200) {
      console.log("API call 'StopTracking' successful.");
    } else {
      console.log("Error during API call 'StopTracking'.");
    }
  } catch (error) {
    console.error("Error:", error);
  }
}

export async function apiGetActiveTracking(api_token: string) {
const api_url = `${url}/trackings/active`;

const options = {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
    accept: "application/json",
    Authorization: "Bearer " + api_token,
  },
};

try {
  const response = await fetch(api_url, options);
  const statusCode = response.status;
  if (statusCode === 200) {
    console.log("API call 'GetActiveTracking' successful.");
    const data = await response.json();
    if (data && data.length > 0) {
      trackingData.update((td) => {
        td.tracking_id = data[0].id;
        td.unixtime = data[0].time_start;
        td.isTracking = true;
        return td;
      });
    }
  } else {
    console.log("Error during API call 'GetActiveTracking'.");
  }
} catch (error) {
  console.error("Error:", error);
}
}

export async function apiGetDetails(api_token: string, tracking_id: string) {
const api_url = `${url}/trackings/${tracking_id}/details`;

const options = {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
    accept: "application/json",
    Authorization: "Bearer " + api_token,
  },
};

try {
  const response = await fetch(api_url, options);
  const statusCode = response.status;
  if (statusCode === 200) {
    console.log("API call 'GetDetails' successful.");
    const data = await response.json();
    if (data && data.front_regions !== null) {
      trackingData.update((td) => {
        td.front_regions = data.front_regions;
        td.back_regions = data.back_regions;
        td.intensity = data.intensity;
        td.diet = data.diet;
        return td;
      });
    }
  } else {
    console.log("Error during API call 'GetDetails'.");
  }
} catch (error) {
  console.error("Error:", error);
}
}

export async function apiSetDetails (api_token : string, tracking_id : string, front_regions : boolean[], back_regions : boolean[], intensity : number, diet : Object) {
const api_url = `${url}/trackings/${tracking_id}/details`;

const options = {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json',
    'accept': 'application/json',
    'Authorization': 'Bearer ' + api_token,
  },
  body: JSON.stringify({
    'front_regions': front_regions,
    'back_regions': back_regions,
    'intensity': intensity,
    'diet': diet
  })
};

try {
  const response = await fetch(api_url, options);
  const statusCode = response.status;
  if (statusCode === 200) {
    console.log("API call 'SetDetails' successful.");
  } else {
    console.log("Error during API call 'SetDetails'.");
  }
} catch (error) {
  console.error("Error:", error);
}
}
