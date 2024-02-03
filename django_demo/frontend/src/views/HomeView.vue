<script setup lang="ts">

import {onMounted, ref} from 'vue'
import {Configuration, UsersApi} from "@/api";

import {type AxiosRequestConfig} from "axios";


const token = '8336db255eacf69fcf62ac311f25c46b3231a6de'
// const axiosRequestConfig: AxiosRequestConfig = { headers: { Authorization: `Bearer ${token}` } }
// const axiosRequestConfig: AxiosRequestConfig = { headers: { Authorization: `Token ${token}`, 'Access-Control-Allow-Origin': 'http://localhost:8000/users/' } }
const axiosRequestConfig: AxiosRequestConfig = { headers: { Authorization: `Token ${token}` } }


const api = new UsersApi(new Configuration({basePath: 'http://localhost:8000'}))


  // constructor(basePath?: string) {
  //   super(new Configuration(), basePath)
  // }



const user = ref<string>('loading...')


onMounted(async () => {

  getUsers().then((response) => {
    console.log(response)
    user.value = JSON.stringify(response)
  }).catch(() => {
    user.value = 'error'
  })

})

async function getUsers(): Promise<string[]> {
  const response = (await api.listUsers(undefined, axiosRequestConfig)).data
  return response?.results ? response.results.map((user) => user.username) : []
}


</script>

<template>
  We in Vue now.<br>
  Here API response: {{ user }}
</template>
