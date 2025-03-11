package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
	"os"
)

var Window int

var rootCmd = &cobra.Command{
	Use:   "agg",
	Short: "Aggregate numbers using different aggregators",
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

func init() {
	cobra.OnInitialize()
	rootCmd.PersistentFlags().IntVarP(&Window, "window", "w", 2, "window size")

	rootCmd.AddCommand(meanCmd)
}
