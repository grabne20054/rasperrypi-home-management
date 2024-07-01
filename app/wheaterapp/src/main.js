import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-default.css';
import axios from 'axios';

const app = createApp(App);
app.use(router);
app.use(ToastPlugin);
app.use(axios);
app.mount('#app');
