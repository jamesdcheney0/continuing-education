return {
	{
		"echasnovski/snacks.nvim",
		event = "VeryLazy",
		config = true,
	},
	{
		"zbirenbaum/copilot.lua",
		cmd = "Copilot",
		event = "InsertEnter",
		config = function()
			require("copilot").setup({})
			local Snacks = require("snacks")
			local copilot_exists = pcall(require, "copilot")

			if copilot_exists then
				Snacks.toggle({
					name = "Copilot Completion",
					color = {
						enabled = "azure",
						disabled = "orange",
					},
					get = function()
						return not require("copilot.client").is_disabled()
					end,
					set = function(state)
						if state then
							require("copilot.command").enable()
						else
							require("copilot.command").disable()
						end
					end,
				}):map("<leader>at")
			end
		end,
	},
	{
		"CopilotC-Nvim/CopilotChat.nvim",
		event = "VeryLazy",
		dependencies = { "zbirenbaum/copilot.lua" },
		config = function()
			require("CopilotChat").setup({})
		end,
	},
}
