<template>
	<view class="container">
		<view class="intro">本项目已包含uni ui组件，无需import和注册，可直接使用。在代码区键入字母u，即可通过代码助手列出所有可用组件。光标置于组件名称处按F1，即可查看组件文档。</view>
		<text class="intro">详见：</text>
		<uni-link :href="href" :text="href"></uni-link>
		<view>{{word_from_backend}}</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				href: 'https://uniapp.dcloud.io/component/README?id=uniui',
				word_from_backend: ''
			}
		},
		methods: {

		},
		onShow() {
			// send data to backend
			uni.request({
				url: 'http://127.0.0.1:8081/request',
				data: {
				    inputstr: '这是一条由前端发给后端，再有后端发给前端的信息，看看能不能显示在前端'
				},
				header: {
					'custom-type': 'application/json'
				},
				success: (res) => {
					console.log(res.data);
					this.word_from_backend = res.data;
				}
			})
		}
	}
</script>

<style>
	.container {
		padding: 20px;
		font-size: 14px;
		line-height: 24px;
	}
</style>
