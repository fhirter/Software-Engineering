package cmd

import (
	"fmt"
	"github.com/fhirter/software-engineering/exercises/logic"
	"github.com/spf13/cobra"
	"strconv"
)

var meanCmd = &cobra.Command{
	Use:   "mean",
	Short: "Aggregate numbers with mean",
	Run: func(cmd *cobra.Command, args []string) {
		data, err := stringsToInts(args)
		if err != nil {
			fmt.Println(err)
			return
		}

		var result = logic.Mean(data, Window)

		fmt.Println(result)
	},
}

func stringsToInts(args []string) ([]int, error) {
	ints := make([]int, len(args))
	for i, arg := range args {
		num, err := strconv.Atoi(arg)
		if err != nil {
			return nil, fmt.Errorf("invalid number '%s': %w", arg, err)
		}
		ints[i] = num
	}
	return ints, nil
}
