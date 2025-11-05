import pandas as pd
import numpy as np
from scipy.stats import ks_2samp
import streamlit as st
import plotly.graph_objects as go


class DataValidator:
    def __init__(self):
        pass
    
    def validate_synthetic_data(self, original_df: pd.DataFrame, synthetic_df: pd.DataFrame, alpha: float = 0.05):
        st.subheader("Validation and Quality Metrics")
        
        validation_results = {
            'columns': [],
            'ks_statistic': [],
            'ks_pvalue': [],
            'ks_significant': [],
            'mean_original': [],
            'mean_synthetic': [],
            'mean_diff': [],
            'mean_diff_percent': []
        }
        
        common_columns = set(original_df.columns) & set(synthetic_df.columns)
        
        for col in common_columns:
            if not pd.api.types.is_numeric_dtype(original_df[col]) or not pd.api.types.is_numeric_dtype(synthetic_df[col]):
                continue
                
            orig_data = original_df[col].dropna()
            synth_data = synthetic_df[col].dropna()
            
            if len(orig_data) == 0 or len(synth_data) == 0:
                continue
            
            ks_stat, ks_pvalue = ks_2samp(orig_data, synth_data)
            
            mean_orig = orig_data.mean()
            mean_synth = synth_data.mean()
            mean_diff = abs(mean_orig - mean_synth)
            mean_diff_percent = (mean_diff / abs(mean_orig)) * 100 if mean_orig != 0 else 0
            
            validation_results['columns'].append(col)
            validation_results['ks_statistic'].append(ks_stat)
            validation_results['ks_pvalue'].append(ks_pvalue)
            validation_results['ks_significant'].append(ks_pvalue < alpha)
            validation_results['mean_original'].append(mean_orig)
            validation_results['mean_synthetic'].append(mean_synth)
            validation_results['mean_diff'].append(mean_diff)
            validation_results['mean_diff_percent'].append(mean_diff_percent)
        
        validation_df = pd.DataFrame(validation_results)
        
        if len(validation_df) > 0:
            col1, col2, col3 = st.columns(3)
            
            significant_cols = validation_df['ks_significant'].sum()
            total_cols = len(validation_df)
            quality_score = self.calculate_quality_score(validation_df)
            
            with col1:
                st.metric("Quality Score", f"{quality_score:.1f}/100")
            
            with col2:
                st.metric("Distribution Match", f"{(total_cols - significant_cols)}/{total_cols}")
            
            with col3:
                st.metric("Avg Mean Difference", f"{validation_df['mean_diff_percent'].mean():.2f}%")
            
            if quality_score >= 80:
                st.success("EXCELLENT: Synthetic data closely matches original distribution")
            elif quality_score >= 60:
                st.warning("GOOD: Synthetic data reasonably matches original distribution")
            elif quality_score >= 40:
                st.info("FAIR: Some differences detected in synthetic data")
            else:
                st.error("POOR: Significant differences in synthetic data")
            
            st.subheader("Detailed Column Analysis")
            display_df = validation_df.copy()
            display_df['ks_significant'] = display_df['ks_significant'].map({True: '❌', False: '✅'})
            display_df = display_df.round(4)
            st.dataframe(display_df, use_container_width=True)
            
            self._plot_distributions(original_df, synthetic_df, common_columns)
            
        else:
            st.warning("No numeric columns available for validation.")
        
        return validation_df

    def _plot_distributions(self, original_df: pd.DataFrame, synthetic_df: pd.DataFrame, common_columns: set):
        st.subheader("Distribution Comparison")
        for col in common_columns:
            if pd.api.types.is_numeric_dtype(original_df[col]):
                fig = go.Figure()
                fig.add_trace(go.Histogram(
                    x=original_df[col].dropna(), 
                    name='Original', 
                    opacity=0.7, 
                    nbinsx=20
                ))
                fig.add_trace(go.Histogram(
                    x=synthetic_df[col].dropna(), 
                    name='Synthetic', 
                    opacity=0.7, 
                    nbinsx=20
                ))
                fig.update_layout(
                    title=f'Distribution of {col}',
                    xaxis_title=col,
                    yaxis_title='Frequency',
                    barmode='overlay'
                )
                st.plotly_chart(fig, use_container_width=True)

    def calculate_quality_score(self, validation_df: pd.DataFrame) -> float:
        if len(validation_df) == 0:
            return 0
            
        ks_penalty = validation_df['ks_significant'].mean() * 40
        mean_diff_penalty = min(30, validation_df['mean_diff_percent'].mean() / 2)
        base_score = 100
        quality_score = base_score - ks_penalty - mean_diff_penalty
        
        return max(0, quality_score)