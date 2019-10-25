import axios from 'axios'

// export default() => {
//   return axios.create({
//     baseURL: `http://localhost:3000`
//   })
// }
export const Api = axios.create({baseURL: `http://localhost:3000`})