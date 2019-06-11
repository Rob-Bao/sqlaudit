import Vue from 'vue'
import Router from 'vue-router'

// in development-env not use lazy-loading, because lazy-loading too many pages will cause webpack hot update too slow. so only in production use lazy-loading;
// detail: https://panjiachen.github.io/vue-element-admin-site/#/lazy-loading

Vue.use(Router)

/* Layout */
import Layout from '../views/layout/Layout'

/**
* hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
* alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
*                                if not set alwaysShow, only more than one route under the children
*                                it will becomes nested mode, otherwise not show the root menu
* redirect: noredirect           if `redirect:noredirect` will no redirect in the breadcrumb
* name:'router-name'             the name is used by <keep-alive> (must set!!!)
* meta : {
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
  }
**/
export const constantRouterMap = [
  { path: '/login', component: () => import('@/views/login/index'), hidden: true },
  { path: '/404', component: () => import('@/views/404'), hidden: true },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    name: 'Dashboard',
    hidden: true,
    meta: { title: 'Dashboard', icon: 'example' },
    children: [{
      path: 'dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: 'Dashboard', icon: 'dashboard' }
    }]
  },
  // {
  //   path: '/sqlaction',
  //   component: Layout,
  //   name: 'SqlAction',
  //   meta: { title: '库表操作 ', icon: 'table' },
  //   children: [
  //     {
  //       path: 'createtable',
  //       component: () => import('@/views/sqlaction/createtable/index'),
  //       name: 'CreateTable',
  //       meta: { title: '申请创建表' }
  //     },
  //     {
  //       path: 'altertable',
  //       name: 'AlterTable',
  //       component: () => import('@/views/sqlaction/altertable/index'),
  //       meta: { title: '表结构修改' }
  //     }
  //   ]
  // },
  {
    path: '/task',
    component: Layout,
    name: 'Task',
    meta: { title: '工单相关 ', icon: 'edit' },
    children: [
      {
        path: 'mytask',
        name: 'Mytask',
        component: () => import('@/views/task/mytask/tasklist'),
        meta: { title: '我的工单', icon: 'clipboard' }
      },
      {
        // path: 'create/:id(\\d+)',
        path: 'create',
        component: () => import('@/views/task/mytask/create'),
        name: 'CreateTask',
        meta: { title: 'CreateTask', noCache: true },
        hidden: true
      },
      {
        path: 'myapproval',
        name: 'Myapproval',
        perms: 'app.change_worksheet',
        component: () => import('@/views/task/myapproval/auditlist'),
        meta: { title: '我的审批', icon: 'message' }
      }
    ]
  },
  {
    path: '/document',
    component: Layout,
    name: 'Document',
    meta: { title: ' 库表信息 ', icon: 'documentation' },
    children: [
      {
        path: 'https://www.tapd.cn/50533802/markdown_wikis/view/#1150533802001002966',
        meta: { title: 'SQL规范', icon: 'link' }
      },
      {
        path: 'tructure',
        name: 'Tructure',
        component: () => import('@/views/document/tructure/dbtableinfo'),
        meta: { title: '库表结构', icon: 'table' }
      },
      {
        path: 'slow',
        name: 'Slow',
        hidden: true,
        component: () => import('@/views/document/slow/index'),
        meta: { title: 'SQL慢查浏览', icon: '' }
      }
    ]
  },
  {
    path: '/settings',
    component: Layout,
    name: 'Settings',
    meta: { title: '系统设置', icon: 'drag' },
    children: [
      {
        path: 'people',
        perms: 'auth.change_user',
        component: () => import('@/views/settings/people/index'),
        name: 'People',
        meta: { title: '人员管理', icon: 'user' }
      },
      {
        path: 'databases',
        perms: 'app.change_instanceinfo',
        component: () => import('@/views/settings/databases/index'),
        name: 'Databases',
        meta: { title: '数据库管理', icon: 'database' }
      }
    ]
  },

  { path: '*', redirect: '/404', hidden: true }
]

export default new Router({
  // mode: 'history', //后端支持可开
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

// export const asyncRouterMap = [
//   {
//     path: '/permission',
//     component: Layout,
//     redirect: '/permission/index',
//     alwaysShow: true, // will always show the root menu
//     meta: {
//       title: 'permission',
//       icon: 'lock',
//       roles: ['admin', 'editor'] // you can set roles in root nav
//     },
//     children: [
//       {
//         path: 'page',
//         component: () => import('@/views/permission/page'),
//         name: 'PagePermission',
//         meta: {
//           title: 'pagePermission',
//           roles: ['admin'] // or you can only set roles in sub nav
//         }
//       },
//       {
//         path: 'directive',
//         component: () => import('@/views/permission/directive'),
//         name: 'DirectivePermission',
//         meta: {
//           title: 'directivePermission'
//           // if do not set roles, means: this page does not require permission
//         }
//       }
//     ]
//   },
//
//   { path: '*', redirect: '/404', hidden: true }
// ]
