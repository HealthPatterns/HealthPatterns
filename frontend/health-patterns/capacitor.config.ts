import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.example.healthpatterns',
  appName: 'HealthPatterns',
  webDir: 'dist',
  server: {
    androidScheme: 'https'
  }
};

export default config;
