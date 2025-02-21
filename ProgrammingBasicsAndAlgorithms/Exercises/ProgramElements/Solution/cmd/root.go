package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
	"os"
)

var rootCmd = &cobra.Command{
	Use:   "agg",
	Short: "Aggregate some numbers",
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("Aggregate command executed successfully!")
	},
}

var meanCmd = &cobra.Command{
	Use:   "mean",
	Short: "Aggregate numbers with mean",
	Run: func(cmd *cobra.Command, args []string) {
		mean()
	},
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
