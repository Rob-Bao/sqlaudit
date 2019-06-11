import request from '@/utils/request'

export function getUList(params) {
  return request({
    url: '/user/userinfo/',
    method: 'get',
    params
  })
}

export function changeURoles(data) {
  return request({
    url: '/perms/roleinfo/0/',
    method: 'put',
    data
  })
}
