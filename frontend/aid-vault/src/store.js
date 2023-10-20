import { writable } from 'svelte/store';

export const loginData = writable({
    username: "",
    accessToken: "",
});

export const trackingData = writable({
    unixtime: 0,
    isTracking: false,
    tracking_id: "",
    count: 0,
    front_regions: [false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false],
    back_regions: [false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false],
    intensity: 0,
    diet: {
        "Obst": false,
        "Gemüse": false,
        "Milchprodukte": false,
        "Fleisch": false,
        "Fisch": false,
        "Eier": false,
        "Weißmehl": false,
        "Vollkorn": false,
        "Soja": false
    },
  });