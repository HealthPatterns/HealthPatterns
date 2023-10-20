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
  });