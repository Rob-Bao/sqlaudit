import request from '@/utils/request'

export function getDList(params) {
  return request({
    url: '/instance/tableinfo/',
    method: 'get',
    params

  })
}
