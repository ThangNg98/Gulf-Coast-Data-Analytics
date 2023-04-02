import { defineStore } from 'pinia';

export const useLoadingStore = defineStore('store', {
  state: () => ({
    isLoading: false
  }),
  actions: {
    setLoading(isLoading) {
      this.isLoading = isLoading;
    }
  }
});
