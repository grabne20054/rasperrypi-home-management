<template>
    <div class="livestream-card">
      <div class="livestream-video">
        <iframe
          :src="livestreamUrl"
          frameborder="0"
          allowfullscreen
          title="Live Stream"
        ></iframe>
      </div>
    </div>
  </template>
  
<script>
export default {
  data() {
    return {
      token: '020202'
    };
  },
  computed: {
    livestreamUrl() {
      return `http://192.168.33.34:8081/stream/?access_token=${this.token}`;
    },
  },
};
</script>
  
  <style scoped>
  .livestream-card {
    width: 640px;
    height: 480px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    margin: 16px;
  }
  
  .livestream-video {
    width: 100%;
    height: 100%;
  }
  
  .livestream-video iframe {
    width: 100%;
    height: 100%;
  }

@media (max-width: 768px) {
  .live-stream-card {
    display: flex;
  }

}

  </style>
  