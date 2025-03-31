function initializeStatisticsData(statsData) {
    statsData.forEach(stat => {
        createGenderChart(
            'chart-' + stat.id,
            stat.labels,
            stat.data,
            stat.title
        );
    });
} 