// フェードイン
function showElementAnimation() {
    var element = document.getElementsByClassName('fade-in');
    if (!element) return;
    var showTiming = window.innerHeight > 768 ? 200 : 60;
    var scrollY = window.pageYOffset;
    var windowH = window.innerHeight;
    for (var i = 0; i < element.length; i++) {
        var elemClientRect = element[i].getBoundingClientRect(); var elemY = scrollY + elemClientRect.top; if (scrollY + windowH - showTiming > elemY) {
            element[i].classList.add('show');
        } else if (scrollY + windowH < elemY) {
        }
    }
}
showElementAnimation();
window.addEventListener('scroll', showElementAnimation);


// グラフの作成
// 表示させる値の算出

// Boolean値をダミー変数にする関数を作る

function get_dummies(boolean_feature){
  if (boolean_feature == "True"){
      return 1
  } 
  else if(boolean_feature == "False"){
      return 0
  }}

// 正規表現で大学名を取得する関数を作る

function get_uni(former_university){
  const uni = former_university
  const re = uni.match(".{1,}大学")
  return re[0]}

// 東京芸術大学か桐朋学園大学かの判別を行う

function identify_the_uni(former_university){
  if (former_university == "東京芸術大学"){
    return 11.601225
  }else if (former_university == "桐朋学園大学"){
    return -0.535470
  }else {
    return 0
  }
}

const feature_values = document.getElementsByClassName("feature-values")
var coaching_history = Number(feature_values[0].textContent)
var t_childminder = get_dummies(feature_values[1].textContent)
var t_kindergarden_teacher = get_dummies(feature_values[2].textContent)
var t_vocal_music = get_dummies(feature_values[3].textContent)
var t_beginner = get_dummies(feature_values[4].textContent)
var t_contest = get_dummies(feature_values[5].textContent)
var former_university = feature_values[6].textContent
var composition = get_dummies(feature_values[7].textContent)
var study_abroad = get_dummies(feature_values[8].textContent)
former_university = identify_the_uni(former_university)

var intercept = 59.24843864264586
var forecast_price = (intercept +
  coaching_history*(-0.057814) +
  t_childminder*(-2.629911)+
  t_kindergarden_teacher*(-1.114511)+
  t_vocal_music*(-0.475124)+
  t_beginner*(2.028346)+
  t_contest*(2.835193)+
  former_university+
  composition*(4.651286)+
  study_abroad*(9.124657))

// 現状の教室の価格を表示させる

const current_price = document.getElementsByClassName("current-price")
var school_name = current_price[0].textContent
var price_minutes = current_price[1].textContent
var price_month = current_price[2].textContent
// var price_minutes = current_price[1].textContent
// var price_month = current_price[2].textContent



var ctx = document.getElementById("chart_cv");
var myBarChart = new Chart(ctx, {
  type: 'bar',
  data: {
   //凡例のラベル
    labels: [school_name],
    datasets: [
      {
        label: '現状の価格(分)', //データ項目のラベル
        data: [price_minutes], //グラフのデータ
        backgroundColor: "rgba(200,112,126,0.5)"
      },{
        label: '適正の価格(分)', //データ項目のラベル
        data: [forecast_price], //グラフのデータ
        backgroundColor: "rgba(80,126,164,0.5)"
      }
    ]
  },
  options: {
      legend: {
          labels: {
              fontColor: "white"
          },
      },
    title: {
      display: true,
    //   グラフタイトル
      text: '価格の診断',
      fontColor: "white",
      fontSize: 24
    },
    scales: {
        xAxes: [                           // Ｘ軸設定
            {
                scaleLabel: {                 // 軸ラベル
                    display: true,                // 表示設定
                    // labelString: 'XX教室',    // ラベル
                    fontColor: "white",             // 文字の色
                    fontSize: 20                  // フォントサイズ
                },
                gridLines: {                   // 補助線
                    // color: "rgba(255, 0, 0, 0.2)", // 補助線の色
                },
                ticks: {                      // 目盛り
                    fontColor: "white",             // 目盛りの色
                    fontSize: 14                  // フォントサイズ
                }
            }
        ],
      yAxes: [{
        ticks: {
          suggestedMax: 250, //最大値
          suggestedMin: 0, //最小値
          stepSize: 50, //縦ラベルの数値単位
          }
      }]
    },
  }
});

// http://www.kogures.com/hitoshi/javascript/chartjs/scale-label.html