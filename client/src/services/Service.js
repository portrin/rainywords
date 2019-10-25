/* eslint-disable no-console */
import {Api} from './Api'

export default {
  login(params) {
    console.log(params)
    return Api.post('admin-callback/', params)
  },
  confirmReset(params) {
    return Api.post('confirm-reset/', params)
  },
  logout() {
    return Api.get('logout/')
  }
}