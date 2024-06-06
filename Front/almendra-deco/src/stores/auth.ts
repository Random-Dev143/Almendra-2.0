import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as { username: string } | null,
  }),
  actions: {
    login(user: { username: string }) {
      this.user = user;
    },
    logout() {
      this.user = null;
    },
  },
});
