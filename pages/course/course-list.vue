<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="header-title">{{departmentInfo.name}}</text>
		</view>
		
		<!-- 课程列表 -->
		<view class="content">
			<view class="search-box">
				<input type="text" placeholder="搜索课程..." v-model="searchText" @input="filterCourses" />
				<text class="search-icon">🔍</text>
			</view>
			
			<view class="course-list">
				<view class="course-item" v-for="(item, index) in filteredCourses" :key="index" 
					  @click="navigateToCourseDetail(item.id)">
					<view class="course-info">
						<view class="course-header">
							<text class="course-name">{{item.name}}</text>
							<view class="rating">
								<text class="rating-score">{{item.rating.toFixed(1)}}</text>
								<view class="stars">
									<text v-for="n in 5" :key="n" class="star" 
										  :class="{ 'filled': n <= Math.round(item.rating) }">★</text>
								</view>
							</view>
						</view>
						<view class="course-code">{{item.code}}</view>
						<view class="course-meta">
							<text class="credits">{{item.credits}}学分</text>
							<text class="review-count">{{item.reviewCount}}条评价</text>
						</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			deptId: null,
			searchText: '',
			departmentInfo: {},
			allCourses: [],
			filteredCourses: []
		}
	},
	onLoad(options) {
		// 获取传递过来的学院ID
		this.deptId = parseInt(options.deptId) || 1;
		
		// 获取学院信息
		this.getDepartmentInfo();
		
		// 获取该学院的课程列表
		this.getCoursesByDepartment();
	},
	methods: {
		goBack() {
			uni.navigateBack();
		},
		getDepartmentInfo() {
			// 模拟从API获取学院信息
			const departments = [
				{
					id: 1,
					name: '创新工程学院',
					shortName: '工程',
					color: '#3498db',
					courseCount: 45,
					reviewCount: 328
				},
				{
					id: 2,
					name: '商学院',
					shortName: '商学',
					color: '#e74c3c',
					courseCount: 38,
					reviewCount: 256
				},
				{
					id: 3,
					name: '人文艺术学院',
					shortName: '人文',
					color: '#9b59b6',
					courseCount: 42,
					reviewCount: 187
				},
				{
					id: 4,
					name: '通识教育学院',
					shortName: '通识',
					color: '#f39c12',
					courseCount: 25,
					reviewCount: 142
				},
				{
					id: 5,
					name: '旅游与酒店学院',
					shortName: '旅游',
					color: '#27ae60',
					courseCount: 32,
					reviewCount: 165
				},
				{
					id: 6,
					name: '法学院',
					shortName: '法学',
					color: '#16a085',
					courseCount: 28,
					reviewCount: 120
				},
				{
					id: 7,
					name: '医学院',
					shortName: '医学',
					color: '#d35400',
					courseCount: 36,
					reviewCount: 210
				}
			];
			
			this.departmentInfo = departments.find(dept => dept.id === this.deptId) || departments[0];
		},
		getCoursesByDepartment() {
			// 模拟从API获取课程数据
			// 根据不同学院ID返回不同的课程列表
			const coursesByDept = {
				// 创新工程学院
				1: [
					{ id: 101, code: 'CS460', name: '计算机视觉', credits: 3, rating: 4.8, reviewCount: 56 },
					{ id: 102, code: 'CS462', name: '机器学习', credits: 3, rating: 4.9, reviewCount: 78 },
					{ id: 103, code: 'CS463', name: '深度学习', credits: 3, rating: 4.7, reviewCount: 63 },
					{ id: 104, code: 'CS464', name: '数据挖掘', credits: 3, rating: 4.5, reviewCount: 47 }
				],
				// 商学院
				2: [
					{ id: 201, code: 'BBAZ16001', name: '管理导论', credits: 3, rating: 4.5, reviewCount: 48 },
					{ id: 202, code: 'BBAZ16002', name: '微观经济学', credits: 3, rating: 4.3, reviewCount: 39 },
					{ id: 203, code: 'BBAZ16015', name: '市场营销', credits: 3, rating: 4.8, reviewCount: 63 }
				],
				// 人文艺术学院
				3: [
					{ id: 301, code: 'BAFZ02', name: '影视摄像基础', credits: 3, rating: 4.6, reviewCount: 45 },
					{ id: 302, code: 'BJ19001', name: '大众传播基础', credits: 3, rating: 4.7, reviewCount: 53 },
					{ id: 303, code: 'BJ19003', name: '数码摄影', credits: 3, rating: 4.8, reviewCount: 59 }
				],
				// 通识教育学院
				4: [
					{ id: 401, code: 'ENG001', name: '大学英语', credits: 20, rating: 4.2, reviewCount: 87 },
					{ id: 402, code: 'GCLBL001', name: '宪法与基本法概论', credits: 1, rating: 4.0, reviewCount: 65 },
					{ id: 403, code: 'CHNRW001', name: '中文阅读与写作', credits: 3, rating: 4.3, reviewCount: 78 }
				],
				// 旅游与酒店学院
				5: [
					{ id: 501, code: 'BITM1301', name: '旅游及酒店业概论', credits: 3, rating: 4.7, reviewCount: 58 },
					{ id: 502, code: 'BHM1901', name: '综合渡假村管理', credits: 3, rating: 4.5, reviewCount: 46 },
					{ id: 503, code: 'BHM1258', name: '消费者行为学', credits: 3, rating: 4.6, reviewCount: 52 },
					{ id: 504, code: 'BHM1222', name: '餐饮运作', credits: 3, rating: 4.4, reviewCount: 41 }
				],
				// 法学院
				6: [
					{ id: 601, code: 'BL19001', name: '法学导论', credits: 3, rating: 4.6, reviewCount: 52 },
					{ id: 602, code: 'BL19027-001', name: '法律基础与理论专题：法律电影赏析', credits: 3, rating: 4.8, reviewCount: 63 },
					{ id: 603, code: 'BL19027-002', name: '法律基础与理论专题：澳门法概论', credits: 3, rating: 4.5, reviewCount: 48 }
				],
				// 医学院
				7: [
					{ id: 701, code: 'BC1015', name: '组织胚胎学', credits: 3, rating: 4.5, reviewCount: 47 },
					{ id: 702, code: 'BC1004', name: '中医基础理论', credits: 6, rating: 4.6, reviewCount: 53 },
					{ id: 703, code: 'BC2043', name: '细胞生物学', credits: 3, rating: 4.8, reviewCount: 62 }
				]
			};
			
			// 获取当前学院的课程
			this.allCourses = coursesByDept[this.deptId] || [];
			this.filteredCourses = [...this.allCourses];
		},
		filterCourses() {
			if (!this.searchText) {
				this.filteredCourses = [...this.allCourses];
				return;
			}
			
			const searchLower = this.searchText.toLowerCase();
			this.filteredCourses = this.allCourses.filter(course => {
				return course.name.toLowerCase().includes(searchLower) || 
					   course.code.toLowerCase().includes(searchLower);
			});
		},
		navigateToCourseDetail(courseId) {
			console.log('跳转到课程详情，课程ID:', courseId);
			// 使用相对路径
			const url = './course-detail?courseId=' + courseId;
			console.log('跳转URL:', url);
			
			uni.navigateTo({
				url: url,
				success: function() {
					console.log('跳转成功');
				},
				fail: function(err) {
					console.error('跳转失败:', err);
					// 显示错误提示
					uni.showToast({
						title: '跳转失败，请稍后再试',
						icon: 'none',
						duration: 2000
					});
				}
			});
		}
	}
}
</script>

<style>
.container {
	padding-bottom: 30rpx;
}

.header {
	display: flex;
	align-items: center;
	padding: 20rpx 30rpx;
	background-color: #ffffff;
	border-bottom: 1px solid #f0f0f0;
}

.back-btn {
	width: 60rpx;
	height: 60rpx;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 40rpx;
}

.header-title {
	flex: 1;
	text-align: center;
	font-size: 36rpx;
	font-weight: bold;
	margin-right: 60rpx;
}

.content {
	padding: 30rpx;
}

.search-box {
	position: relative;
	margin-bottom: 30rpx;
}

.search-box input {
	width: 100%;
	height: 80rpx;
	background-color: #f5f5f5;
	border-radius: 40rpx;
	padding: 0 80rpx 0 30rpx;
	font-size: 28rpx;
}

.search-icon {
	position: absolute;
	right: 30rpx;
	top: 50%;
	transform: translateY(-50%);
	font-size: 32rpx;
}

.course-list {
	display: flex;
	flex-direction: column;
	gap: 30rpx;
}

.course-item {
	background-color: #ffffff;
	border-radius: 20rpx;
	padding: 30rpx;
	box-shadow: 0 2rpx 10rpx rgba(0, 0, 0, 0.05);
}

.course-header {
	display: flex;
	justify-content: space-between;
	align-items: flex-start;
	margin-bottom: 20rpx;
}

.course-name {
	font-size: 32rpx;
	font-weight: bold;
	flex: 1;
}

.rating {
	display: flex;
	flex-direction: column;
	align-items: flex-end;
}

.rating-score {
	font-size: 36rpx;
	font-weight: bold;
	color: #f39c12;
}

.stars {
	display: flex;
	margin-top: 6rpx;
}

.star {
	font-size: 24rpx;
	color: #ddd;
	margin-left: 4rpx;
}

.star.filled {
	color: #f39c12;
}

.course-code {
	font-size: 28rpx;
	color: #666;
	margin-bottom: 20rpx;
}

.course-meta {
	display: flex;
	justify-content: space-between;
	font-size: 26rpx;
	color: #888;
}

.credits, .review-count {
	background-color: #f5f5f5;
	padding: 6rpx 16rpx;
	border-radius: 20rpx;
}
</style>