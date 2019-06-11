import request from '@/utils/request'

// 获取工单列表。
export function getWorkList(params, token) {
  return request({
    url: '/workorder/workinfo/',
    method: 'get',
    params
  })
}

// 创建工单
export function createWork(data) {
  return request({
    url: '/workorder/workinfo/',
    method: 'post',
    data
  })
}

// 更新工单内容
export function updateWork(id, data) {
  return request({
    url: '/workorder/workinfo/' + id + '/',
    method: 'put',
    data
  })
}

// 根据work_id，获取任务执行结果。
export function getExecuteRes(params, token) {
  return request({
    url: '/workorder/executeres/',
    method: 'get',
    params
  })
}

// export function deleteAction(params) {
//   return request({
//     url: '/work_order/workinfo/' + params,
//     method: 'delete'
//   })
// }
