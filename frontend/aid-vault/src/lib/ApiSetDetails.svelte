<script lang="ts" context="module">

  export async function apiSetDetails (api_token : string, tracking_id : string, front_regions, back_regions, intensity, diet) {
    const url = `http://localhost:3000/trackings/${tracking_id}/details`;

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
      const response = await fetch(url, options);
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
</script>