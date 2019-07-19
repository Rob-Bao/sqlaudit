import request from '@/utils/request'

// 实例相关
export function getList(params, token) {
  return request({
    url: '/instance/instanceinfo/',
    method: 'get',
    params
  })
}

export function createAction(data) {
  return request({
    url: '/instance/instanceinfo/',
    method: 'post',
    data
  })
}

export function deleteAction(params) {
  return request({
    url: '/instance/instanceinfo/' + params,
    method: 'delete'
  })
}

// 数据库相关
export function getDBList(params) {
  return request({
    url: '/instance/databaseinfo/',
    method: 'get',
    params
  })
}

// inception 相关
export function CheckMysql(params) {
  return request({
    url: '/instance/checkmysql/',
    method: 'get',
    params
  })
}
