import { defineStore } from "pinia";

export const useUser = defineStore("user", { 
  state: () => {
    return {
      userName: null,
      userId: null,
    }
  },
  actions: {
    setUserName(userName){
      this.userName = userName
    },
    setUserId(userId){
      this.userId = userId
    }
  }
})