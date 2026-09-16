import pandas as pd
import pytest
from corsair_lab.evaluation import forecast_records, score_forecasts, load_yields


def test_future_changes_cannot_change_earlier_predictions():
    series = pd.Series([1., 2., 3., 4., 5., 6., 7., 8.],
                       index=pd.date_range("2024-01-01", periods=8), name="fixture")
    original = forecast_records(series, window=2)
    changed = series.copy()
    changed.iloc[5:] = 1000.
    rerun = forecast_records(changed, window=2)
    before = original.origin_date < series.index[5]
    pd.testing.assert_series_equal(original.loc[before, "prediction_pct"], rerun.loc[before, "prediction_pct"])


def test_metrics_convert_percentage_points_to_basis_points():
    fixture = pd.DataFrame({"series": ["x", "x"], "model": ["m", "m"],
                            "prediction_pct": [4.1, 4.0], "actual_pct": [4., 4.2]})
    scores = score_forecasts(fixture).iloc[0]
    assert scores["MAE (bp)"] == pytest.approx(15.)
    assert scores["RMSE (bp)"] == pytest.approx(250 ** .5)


def test_horizon_uses_observed_sessions_not_calendar_days():
    series = pd.Series([1., 2., 3., 4., 5.], name="fixture",
                       index=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-05", "2024-01-08", "2024-01-09"]))
    rows = forecast_records(series, horizon=2, window=2)
    assert rows.iloc[0].origin_date == pd.Timestamp("2024-01-05")
    assert rows.iloc[0].target_date == pd.Timestamp("2024-01-09")
    assert rows.iloc[0].actual_pct == 5.


def test_input_guards():
    series = pd.Series([1., 2., 3., 4.], index=pd.date_range("2024-01-01", periods=4))
    with pytest.raises(ValueError, match="positive integer"):
        forecast_records(series, horizon=0)
    with pytest.raises(ValueError, match="Insufficient"):
        forecast_records(series, window=20)
    with pytest.raises(ValueError, match="empty"):
        score_forecasts(pd.DataFrame())
    with pytest.raises(ValueError, match="unique"):
        forecast_records(pd.concat([series, series]), window=2)


def test_snapshot_is_bounded_and_missing_values_are_not_filled():
    frame, _ = load_yields()
    assert frame.observation_date.min() >= pd.Timestamp("2020-01-01")
    assert frame.observation_date.max() <= pd.Timestamp("2024-12-31")
    assert frame[["DGS2", "DGS10"]].isna().any().all()
