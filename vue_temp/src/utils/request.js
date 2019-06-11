import axios from 'axios'
import { Message } from 'element-ui'
import store from '../store'
import { getToken } from '@/utils/auth'
import router from '../router'

// 创建axios实例
const service = axios.create({
  baseURL: process.env.BASE_API, // api的base_url
  timeout: 5000 // 请求超时时间
})

// request拦截器
service.interceptors.request.use(config => {
  if (store.getters.token) {
    // 在config中，添加token信息
    config.headers['Authorization'] = 'JWT ' + getToken() // 符合后端自定义的格式要求修改
  }
  return config // 返回request信息
}, error => {
  // 当报错的时候，做些什么
  console.log(error) // for debug
  Promise.reject(error)
})

// respone拦截器
service.interceptors.response.use(
  response => {
  /**
  * code为非200是抛错 可结合自己业务进行修改
  */
    return response.data // 返回token信息
  },
  error => {
    if (error.response.status === 401) { // 401处理
      store.dispatch('FedLogOut').then(() => {
        router.push({ path: '/login' }) // 登录超时，重新登录
        Message({
          message: '登陆超时',
          type: 'error',
          duration: 5 * 1000
        })
      })
    } else if (error.response.status === 403) { // 403处理
      Message({
        message: '权限拒绝',
        type: 'error'
      })
    } else if (error.response.status === 400) { // 403处理
      Message({
        message: '无效的请求 message:' + error.response.data.non_field_errors,
        type: 'error'
      })
    } else if (error.response.status === 404) { // 404处理
      Message({
        message: '用户名或者密码错误',
        type: 'error'
      })
    } else if (error.response.status === 500) { // 500处理
      Message({
        type: 'error',
        message: '服务器内部错误'
      })
    }
    console.log(error.response.data)// for debug
    return Promise.reject(error)
  }
)

export default service
