# SwapContext

- RVA: `0x006B9820`–`0x006B9EB4` (길이 `1,684` bytes)
- VA: `0x00000001406B9820`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2398`
- 디코드: `391`개 명령, `1,684/1,684` bytes 표시
- 미해석 바이트: `2` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **46**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x006B9866` → [KiStartThreadCycleAccumulationContextSwap](../30/KiStartThreadCycleAccumulationContextSwap_function_00309C10.md) (function, `0x00309C10`)
- `0x006B988E` → [KiCheckAndApplyCacheIsolation](../5C/KiCheckAndApplyCacheIsolation_function_005C3FF0.md) (function, `0x005C3FF0`)
- `0x006B98B5` → [KeCheckAndApplyBamQos](../39/KeCheckAndApplyBamQos_function_00391910.md) (function, `0x00391910`)
- `0x006B990E` → [KiSaveThreadIptState](../5B/KiSaveThreadIptState_function_005BA120.md) (function, `0x005BA120`)
- `0x006B99B7` → [KiUpdateSpeculationControl](../3E/KiUpdateSpeculationControl_function_003E63E0.md) (function, `0x003E63E0`)
- `0x006B9A33` → [SwapContext + 0x326](SwapContext_function_006B9820.md) (inside-function, `0x006B9B46`)
- `0x006B9A3C` → [SwapContext + 0x32F](SwapContext_function_006B9820.md) (inside-function, `0x006B9B4F`)
- `0x006B9A45` → [SwapContext + 0x218](SwapContext_function_006B9820.md) (inside-function, `0x006B9A38`)
- `0x006B9A4E` → [SwapContext + 0x221](SwapContext_function_006B9820.md) (inside-function, `0x006B9A41`)
- `0x006B9A57` → [SwapContext + 0x22A](SwapContext_function_006B9820.md) (inside-function, `0x006B9A4A`)
- `0x006B9A60` → [SwapContext + 0x233](SwapContext_function_006B9820.md) (inside-function, `0x006B9A53`)
- `0x006B9A69` → [SwapContext + 0x23C](SwapContext_function_006B9820.md) (inside-function, `0x006B9A5C`)
- `0x006B9A72` → [SwapContext + 0x245](SwapContext_function_006B9820.md) (inside-function, `0x006B9A65`)
- `0x006B9A7B` → [SwapContext + 0x24E](SwapContext_function_006B9820.md) (inside-function, `0x006B9A6E`)
- `0x006B9A84` → [SwapContext + 0x257](SwapContext_function_006B9820.md) (inside-function, `0x006B9A77`)
- `0x006B9A8D` → [SwapContext + 0x260](SwapContext_function_006B9820.md) (inside-function, `0x006B9A80`)
- `0x006B9A96` → [SwapContext + 0x269](SwapContext_function_006B9820.md) (inside-function, `0x006B9A89`)
- `0x006B9A9F` → [SwapContext + 0x272](SwapContext_function_006B9820.md) (inside-function, `0x006B9A92`)
- `0x006B9AA8` → [SwapContext + 0x27B](SwapContext_function_006B9820.md) (inside-function, `0x006B9A9B`)
- `0x006B9AB1` → [SwapContext + 0x284](SwapContext_function_006B9820.md) (inside-function, `0x006B9AA4`)
- `0x006B9ABA` → [SwapContext + 0x28D](SwapContext_function_006B9820.md) (inside-function, `0x006B9AAD`)
- `0x006B9AC3` → [SwapContext + 0x296](SwapContext_function_006B9820.md) (inside-function, `0x006B9AB6`)
- `0x006B9ACC` → [SwapContext + 0x29F](SwapContext_function_006B9820.md) (inside-function, `0x006B9ABF`)
- `0x006B9AD5` → [SwapContext + 0x2A8](SwapContext_function_006B9820.md) (inside-function, `0x006B9AC8`)
- `0x006B9ADE` → [SwapContext + 0x2B1](SwapContext_function_006B9820.md) (inside-function, `0x006B9AD1`)
- `0x006B9AE7` → [SwapContext + 0x2BA](SwapContext_function_006B9820.md) (inside-function, `0x006B9ADA`)
- `0x006B9AF0` → [SwapContext + 0x2C3](SwapContext_function_006B9820.md) (inside-function, `0x006B9AE3`)
- `0x006B9AF9` → [SwapContext + 0x2CC](SwapContext_function_006B9820.md) (inside-function, `0x006B9AEC`)
- `0x006B9B02` → [SwapContext + 0x2D5](SwapContext_function_006B9820.md) (inside-function, `0x006B9AF5`)
- `0x006B9B0B` → [SwapContext + 0x2DE](SwapContext_function_006B9820.md) (inside-function, `0x006B9AFE`)
- `0x006B9B14` → [SwapContext + 0x2E7](SwapContext_function_006B9820.md) (inside-function, `0x006B9B07`)
- `0x006B9B1D` → [SwapContext + 0x2F0](SwapContext_function_006B9820.md) (inside-function, `0x006B9B10`)
- `0x006B9B26` → [SwapContext + 0x2F9](SwapContext_function_006B9820.md) (inside-function, `0x006B9B19`)
- `0x006B9B2F` → [SwapContext + 0x302](SwapContext_function_006B9820.md) (inside-function, `0x006B9B22`)
- `0x006B9B38` → [SwapContext + 0x30B](SwapContext_function_006B9820.md) (inside-function, `0x006B9B2B`)
- `0x006B9B41` → [SwapContext + 0x314](SwapContext_function_006B9820.md) (inside-function, `0x006B9B34`)
- `0x006B9B4A` → [SwapContext + 0x31D](SwapContext_function_006B9820.md) (inside-function, `0x006B9B3D`)
- `0x006B9BF9` → [HvlSwitchVirtualAddressSpace](../3C/HvlSwitchVirtualAddressSpace_function_003C7C60.md) (function, `0x003C7C60`)
- `0x006B9D1F` → [KiRestoreThreadIptState](../5B/KiRestoreThreadIptState_function_005BA0F0.md) (function, `0x005BA0F0`)
- `0x006B9DFE` → [HalRequestSoftwareInterrupt](../3F/HalRequestSoftwareInterrupt_function_003FADA0.md) (function, `0x003FADA0`)
- `0x006B9E21` → [EtwTraceContextSwap](../41/EtwTraceContextSwap_function_004174A0.md) (function, `0x004174A0`)
- `0x006B9E32` → [KiClearLastBranchRecordStack](../41/KiClearLastBranchRecordStack_function_0041CAB0.md) (function, `0x0041CAB0`)
- `0x006B9E43` → [KiResetProcessorTraceBuffer](../5B/KiResetProcessorTraceBuffer_function_005B21B0.md) (function, `0x005B21B0`)
- `0x006B9E60` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x006B9E79` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x006B9E96` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x006B9EA1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- [KiIdleLoop](KiIdleLoop_function_006B2910.md) at `0x006B2A32`
- [KiSwapContext](KiSwapContext_function_006B9740.md) at `0x006B97B1`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A33`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A3C`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A45`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A4E`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A57`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A60`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A69`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A72`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A7B`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A84`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A8D`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A96`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9A9F`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9AA8`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9AB1`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9ABA`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9AC3`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9ACC`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9AD5`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9ADE`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9AE7`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9AF0`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9AF9`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9B02`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9B0B`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9B14`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9B1D`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9B26`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9B2F`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9B38`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9B41`
- [SwapContext](SwapContext_function_006B9820.md) at `0x006B9B4A`

### Static image references
- `0x006B983C` → RVA `0x00FC6CE8` (`ALMOSTRO`; read)
- `0x006B9871` → RVA `0x00FC6B30` (`ALMOSTRO`; read)
- `0x006B9878` → RVA `0x00FC6E84` (`ALMOSTRO`; read)
- `0x006B9902` → RVA `0x00FC6B94` (`ALMOSTRO`; read)
- `0x006B991B` → RVA `0x01201841` (`CFGRO`; read)
- `0x006B9BAB` → RVA `0x01201840` (`CFGRO`; read)
- `0x006B9BED` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x006B9C78` → RVA `0x00F475C0` (`.data`; read)
- `0x006B9CBC` → RVA `0x00FC6C60` (`ALMOSTRO`; read)
- `0x006B9E0F` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x006B9E82` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006B9820  48 55                           push rbp
006B9822  48 83 EC 30                     sub rsp, 0x30
006B9826  0F 0D 4E 71                     prefetchw byte ptr [rsi + 0x71]
006B982A  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
006B982E  80 7E 71 00                     cmp byte ptr [rsi + 0x71], 0
006B9832  0F 85 46 06 00 00               jne 0x1406b9e7e
006B9838  C6 46 71 01                     mov byte ptr [rsi + 0x71], 1
006B983C  8B 05 A6 D4 90 00               mov eax, dword ptr [rip + 0x90d4a6]
006B9842  85 C0                           test eax, eax
006B9844  74 06                           je 0x1406b984c
006B9846  F3                              .byte 0xf3
006B9847  0F                              .byte 0x0f
006B9848  3A F0                           cmp dh, al
006B984A  C0 00 8B                        rol byte ptr [rax], 0x8b
006B984D  05 3E D6 90 00                  add eax, 0x90d63e
006B9852  85 C0                           test eax, eax
006B9854  74 09                           je 0x1406b985f
006B9856  33 D2                           xor edx, edx
006B9858  B9 02 05 00 C0                  mov ecx, 0xc0000502
006B985D  0F 30                           wrmsr
006B985F  FA                              cli
006B9860  48 8B CB                        mov rcx, rbx
006B9863  48 8B D6                        mov rdx, rsi
006B9866  E8 A5 03 C5 FF                  call 0x140309c10
006B986B  FF 83 3C 2D 00 00               inc dword ptr [rbx + 0x2d3c]
006B9871  48 8B 2D B8 D2 90 00            mov rbp, qword ptr [rip + 0x90d2b8]
006B9878  83 3D 05 D6 90 00 00            cmp dword ptr [rip + 0x90d605], 0
006B987F  74 12                           je 0x1406b9893
006B9881  48 0F BA E5 2C                  bt rbp, 0x2c
006B9886  73 0B                           jae 0x1406b9893
006B9888  48 8B CB                        mov rcx, rbx
006B988B  48 8B D6                        mov rdx, rsi
006B988E  E8 5D A7 F0 FF                  call 0x1405c3ff0
006B9893  48 39 73 18                     cmp qword ptr [rbx + 0x18], rsi
006B9897  74 21                           je 0x1406b98ba
006B9899  0F B6 8E 04 02 00 00            movzx ecx, byte ptr [rsi + 0x204]
006B98A0  8B 83 EC 00 00 00               mov eax, dword ptr [rbx + 0xec]
006B98A6  33 C1                           xor eax, ecx
006B98A8  A9 0F 00 00 00                  test eax, 0xf
006B98AD  74 0B                           je 0x1406b98ba
006B98AF  48 8B CB                        mov rcx, rbx
006B98B2  48 8B D6                        mov rdx, rsi
006B98B5  E8 56 80 CD FF                  call 0x140391910
006B98BA  48 8B 97 50 02 00 00            mov rdx, qword ptr [rdi + 0x250]
006B98C1  48 8B 4F 60                     mov rcx, qword ptr [rdi + 0x60]
006B98C5  48 83 E2 FD                     and rdx, 0xfffffffffffffffd
006B98C9  8B C2                           mov eax, edx
006B98CB  74 2A                           je 0x1406b98f7
006B98CD  48 C1 EA 20                     shr rdx, 0x20
006B98D1  48 0F BA E5 26                  bt rbp, 0x26
006B98D6  72 17                           jb 0x1406b98ef
006B98D8  48 0F BA E5 0F                  bt rbp, 0xf
006B98DD  72 15                           jb 0x1406b98f4
006B98DF  0F BA E5 17                     bt ebp, 0x17
006B98E3  73 05                           jae 0x1406b98ea
006B98E5  0F AE 21                        xsave ptr [rcx]
006B98E8  EB 0D                           jmp 0x1406b98f7
006B98EA  0F AE 01                        fxsave [rcx]
006B98ED  EB 08                           jmp 0x1406b98f7
006B98EF  0F C7 29                        xsaves ptr [rcx]
006B98F2  EB 03                           jmp 0x1406b98f7
006B98F4  0F AE 31                        xsaveopt ptr [rcx]
006B98F7  0F AE 59 18                     stmxcsr dword ptr [rcx + 0x18]
006B98FB  A9 00 01 00 00                  test eax, 0x100
006B9900  74 11                           je 0x1406b9913
006B9902  83 3D 8B D2 90 00 00            cmp dword ptr [rip + 0x90d28b], 0
006B9909  74 08                           je 0x1406b9913
006B990B  48 8B CF                        mov rcx, rdi
006B990E  E8 0D 08 F0 FF                  call 0x1405ba120
006B9913  48 89 67 58                     mov qword ptr [rdi + 0x58], rsp
006B9917  48 8B 66 58                     mov rsp, qword ptr [rsi + 0x58]
006B991B  F6 05 1F 7F B4 00 01            test byte ptr [rip + 0xb47f1f], 1
006B9922  74 2D                           je 0x1406b9951
006B9924  48 8B 8E 10 04 00 00            mov rcx, qword ptr [rsi + 0x410]
006B992B  48 89 8B A8 9B 00 00            mov qword ptr [rbx + 0x9ba8], rcx
006B9932  F3 48 0F 1E CA                  rdsspq rdx
006B9937  48 8B 8E 08 04 00 00            mov rcx, qword ptr [rsi + 0x408]
006B993E  F3 0F 01 29                     rstorssp dword ptr [rcx]
006B9942  F3 0F 01 EA                     saveprevssp
006B9946  48 83 EA 08                     sub rdx, 8
006B994A  48 89 97 08 04 00 00            mov qword ptr [rdi + 0x408], rdx
006B9951  48 8B 87 20 02 00 00            mov rax, qword ptr [rdi + 0x220]
006B9958  48 83 B8 10 03 00 00 00         cmp qword ptr [rax + 0x310], 0
006B9960  74 13                           je 0x1406b9975
006B9962  B9 00 01 00 C0                  mov ecx, 0xc0000100
006B9967  0F 32                           rdmsr
006B9969  89 87 78 06 00 00               mov dword ptr [rdi + 0x678], eax
006B996F  89 97 7C 06 00 00               mov dword ptr [rdi + 0x67c], edx
006B9975  66 65 0F BA 34 25 5E 08 00 00 00  btr word ptr gs:[0x85e], 0
006B9980  73 04                           jae 0x1406b9986
006B9982  80 4F 7E 01                     or byte ptr [rdi + 0x7e], 1
006B9986  66 0F BA 66 7E 00               bt word ptr [rsi + 0x7e], 0
006B998C  73 09                           jae 0x1406b9997
006B998E  65 80 0C 25 5E 08 00 00 01      or byte ptr gs:[0x85e], 1
006B9997  80 66 7E FE                     and byte ptr [rsi + 0x7e], 0xfe
006B999B  48 8B 8E 20 02 00 00            mov rcx, qword ptr [rsi + 0x220]
006B99A2  0A 8B E0 06 00 00               or cl, byte ptr [rbx + 0x6e0]
006B99A8  80 E1 C2                        and cl, 0xc2
006B99AB  48 3B 8F 20 02 00 00            cmp rcx, qword ptr [rdi + 0x220]
006B99B2  74 0D                           je 0x1406b99c1
006B99B4  80 E1 C0                        and cl, 0xc0
006B99B7  E8 24 CA D2 FF                  call 0x1403e63e0
006B99BC  E9 B6 01 00 00                  jmp 0x1406b9b77
006B99C1  65 0F B6 0C 25 5E 08 00 00      movzx ecx, byte ptr gs:[0x85e]
006B99CA  66 83 E1 03                     and cx, 3
006B99CE  66 83 F9 01                     cmp cx, 1
006B99D2  0F 85 9F 01 00 00               jne 0x1406b9b77
006B99D8  FA                              cli
006B99D9  65 0F B7 04 25 64 08 00 00      movzx eax, word ptr gs:[0x864]
006B99E2  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006B99EB  74 12                           je 0x1406b99ff
006B99ED  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006B99F6  B9 48 00 00 00                  mov ecx, 0x48
006B99FB  33 D2                           xor edx, edx
006B99FD  0F 30                           wrmsr
006B99FF  65 0F B6 14 25 5A 08 00 00      movzx edx, byte ptr gs:[0x85a]
006B9A08  F7 C2 10 00 00 00               test edx, 0x10
006B9A0E  74 17                           je 0x1406b9a27
006B9A10  B8 01 00 00 00                  mov eax, 1
006B9A15  33 D2                           xor edx, edx
006B9A17  B9 49 00 00 00                  mov ecx, 0x49
006B9A1C  0F 30                           wrmsr
006B9A1E  65 0F B6 14 25 5A 08 00 00      movzx edx, byte ptr gs:[0x85a]
006B9A27  F7 C2 40 00 00 00               test edx, 0x40
006B9A2D  0F 84 37 01 00 00               je 0x1406b9b6a
006B9A33  E8 0E 01 00 00                  call 0x1406b9b46
006B9A38  48 83 C4 08                     add rsp, 8
006B9A3C  E8 0E 01 00 00                  call 0x1406b9b4f
006B9A41  48 83 C4 08                     add rsp, 8
006B9A45  E8 EE FF FF FF                  call 0x1406b9a38
006B9A4A  48 83 C4 08                     add rsp, 8
006B9A4E  E8 EE FF FF FF                  call 0x1406b9a41
006B9A53  48 83 C4 08                     add rsp, 8
006B9A57  E8 EE FF FF FF                  call 0x1406b9a4a
006B9A5C  48 83 C4 08                     add rsp, 8
006B9A60  E8 EE FF FF FF                  call 0x1406b9a53
006B9A65  48 83 C4 08                     add rsp, 8
006B9A69  E8 EE FF FF FF                  call 0x1406b9a5c
006B9A6E  48 83 C4 08                     add rsp, 8
006B9A72  E8 EE FF FF FF                  call 0x1406b9a65
006B9A77  48 83 C4 08                     add rsp, 8
006B9A7B  E8 EE FF FF FF                  call 0x1406b9a6e
006B9A80  48 83 C4 08                     add rsp, 8
006B9A84  E8 EE FF FF FF                  call 0x1406b9a77
006B9A89  48 83 C4 08                     add rsp, 8
006B9A8D  E8 EE FF FF FF                  call 0x1406b9a80
006B9A92  48 83 C4 08                     add rsp, 8
006B9A96  E8 EE FF FF FF                  call 0x1406b9a89
006B9A9B  48 83 C4 08                     add rsp, 8
006B9A9F  E8 EE FF FF FF                  call 0x1406b9a92
006B9AA4  48 83 C4 08                     add rsp, 8
006B9AA8  E8 EE FF FF FF                  call 0x1406b9a9b
006B9AAD  48 83 C4 08                     add rsp, 8
006B9AB1  E8 EE FF FF FF                  call 0x1406b9aa4
006B9AB6  48 83 C4 08                     add rsp, 8
006B9ABA  E8 EE FF FF FF                  call 0x1406b9aad
006B9ABF  48 83 C4 08                     add rsp, 8
006B9AC3  E8 EE FF FF FF                  call 0x1406b9ab6
006B9AC8  48 83 C4 08                     add rsp, 8
006B9ACC  E8 EE FF FF FF                  call 0x1406b9abf
006B9AD1  48 83 C4 08                     add rsp, 8
006B9AD5  E8 EE FF FF FF                  call 0x1406b9ac8
006B9ADA  48 83 C4 08                     add rsp, 8
006B9ADE  E8 EE FF FF FF                  call 0x1406b9ad1
006B9AE3  48 83 C4 08                     add rsp, 8
006B9AE7  E8 EE FF FF FF                  call 0x1406b9ada
006B9AEC  48 83 C4 08                     add rsp, 8
006B9AF0  E8 EE FF FF FF                  call 0x1406b9ae3
006B9AF5  48 83 C4 08                     add rsp, 8
006B9AF9  E8 EE FF FF FF                  call 0x1406b9aec
006B9AFE  48 83 C4 08                     add rsp, 8
006B9B02  E8 EE FF FF FF                  call 0x1406b9af5
006B9B07  48 83 C4 08                     add rsp, 8
006B9B0B  E8 EE FF FF FF                  call 0x1406b9afe
006B9B10  48 83 C4 08                     add rsp, 8
006B9B14  E8 EE FF FF FF                  call 0x1406b9b07
006B9B19  48 83 C4 08                     add rsp, 8
006B9B1D  E8 EE FF FF FF                  call 0x1406b9b10
006B9B22  48 83 C4 08                     add rsp, 8
006B9B26  E8 EE FF FF FF                  call 0x1406b9b19
006B9B2B  48 83 C4 08                     add rsp, 8
006B9B2F  E8 EE FF FF FF                  call 0x1406b9b22
006B9B34  48 83 C4 08                     add rsp, 8
006B9B38  E8 EE FF FF FF                  call 0x1406b9b2b
006B9B3D  48 83 C4 08                     add rsp, 8
006B9B41  E8 EE FF FF FF                  call 0x1406b9b34
006B9B46  48 83 C4 08                     add rsp, 8
006B9B4A  E8 EE FF FF FF                  call 0x1406b9b3d
006B9B4F  48 83 C4 08                     add rsp, 8
006B9B53  B8 DA DA 00 00                  mov eax, 0xdada
006B9B58  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006B9B61  74 07                           je 0x1406b9b6a
006B9B63  B0 20                           mov al, 0x20
006B9B65  F3 48 0F AE E8                  incsspq rax
006B9B6A  0F AE E8                        lfence
006B9B6D  65 80 0C 25 5E 08 00 00 02      or byte ptr gs:[0x85e], 2
006B9B76  FB                              sti
006B9B77  4C 8B B6 B8 00 00 00            mov r14, qword ptr [rsi + 0xb8]
006B9B7E  4C 3B B7 B8 00 00 00            cmp r14, qword ptr [rdi + 0xb8]
006B9B85  0F 84 BF 00 00 00               je 0x1406b9c4a
006B9B8B  0F B6 8B D1 00 00 00            movzx ecx, byte ptr [rbx + 0xd1]
006B9B92  0F B6 83 D0 00 00 00            movzx eax, byte ptr [rbx + 0xd0]
006B9B99  49 8B 96 80 00 00 00            mov rdx, qword ptr [r14 + 0x80]
006B9BA0  F0 48 0F AB 4C C2 08            lock bts qword ptr [rdx + rax*8 + 8], rcx
006B9BA7  49 8B 4E 28                     mov rcx, qword ptr [r14 + 0x28]
006B9BAB  F6 05 8E 7C B4 00 01            test byte ptr [rip + 0xb47c8e], 1
006B9BB2  74 39                           je 0x1406b9bed
006B9BB4  FA                              cli
006B9BB5  0F BA E1 01                     bt ecx, 1
006B9BB9  73 0C                           jae 0x1406b9bc7
006B9BBB  48 0F BA E9 3F                  bts rcx, 0x3f
006B9BC0  83 8B 98 AE 00 00 01            or dword ptr [rbx + 0xae98], 1
006B9BC7  48 89 8B 80 AE 00 00            mov qword ptr [rbx + 0xae80], rcx
006B9BCE  48 0F BA F1 3F                  btr rcx, 0x3f
006B9BD3  83 A3 98 AE 00 00 FD            and dword ptr [rbx + 0xae98], 0xfffffffd
006B9BDA  41 0F BA A6 60 01 00 00 00      bt dword ptr [r14 + 0x160], 0
006B9BE3  73 07                           jae 0x1406b9bec
006B9BE5  83 B3 98 AE 00 00 03            xor dword ptr [rbx + 0xae98], 3
006B9BEC  FB                              sti
006B9BED  F7 05 C1 CE 90 00 01 00 00 00   test dword ptr [rip + 0x90cec1], 1
006B9BF7  74 07                           je 0x1406b9c00
006B9BF9  E8 62 E0 D0 FF                  call 0x1403c7c60
006B9BFE  EB 27                           jmp 0x1406b9c27
006B9C00  0F 22 D9                        mov cr3, rcx
006B9C03  F6 05 36 7C B4 00 01            test byte ptr [rip + 0xb47c36], 1
006B9C0A  74 1B                           je 0x1406b9c27
006B9C0C  0F BA E1 01                     bt ecx, 1
006B9C10  72 15                           jb 0x1406b9c27
006B9C12  0F 20 E0                        mov rax, cr4
006B9C15  48 35 80 00 00 00               xor rax, 0x80
006B9C1B  0F 22 E0                        mov cr4, rax
006B9C1E  48 35 80 00 00 00               xor rax, 0x80
006B9C24  0F 22 E0                        mov cr4, rax
006B9C27  0F B6 8B D1 00 00 00            movzx ecx, byte ptr [rbx + 0xd1]
006B9C2E  0F B6 83 D0 00 00 00            movzx eax, byte ptr [rbx + 0xd0]
006B9C35  48 8B 97 B8 00 00 00            mov rdx, qword ptr [rdi + 0xb8]
006B9C3C  48 8B 92 80 00 00 00            mov rdx, qword ptr [rdx + 0x80]
006B9C43  F0 48 0F B3 4C C2 08            lock btr qword ptr [rdx + rax*8 + 8], rcx
006B9C4A  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
006B9C4E  F6 05 EB 7B B4 00 01            test byte ptr [rip + 0xb47beb], 1
006B9C55  75 0D                           jne 0x1406b9c64
006B9C57  4C 8B BB 88 FE FF FF            mov r15, qword ptr [rbx - 0x178]
006B9C5E  49 89 47 04                     mov qword ptr [r15 + 4], rax
006B9C62  EB 07                           jmp 0x1406b9c6b
006B9C64  48 89 83 88 AE 00 00            mov qword ptr [rbx + 0xae88], rax
006B9C6B  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
006B9C6F  48 85 C0                        test rax, rax
006B9C72  0F 8D EE 01 00 00               jge 0x1406b9e66
006B9C78  83 3D 41 D9 88 00 00            cmp dword ptr [rip + 0x88d941], 0
006B9C7F  0F 85 8A 01 00 00               jne 0x1406b9e0f
006B9C85  48 0F BA E5 37                  bt rbp, 0x37
006B9C8A  73 20                           jae 0x1406b9cac
006B9C8C  B9 C4 01 00 00                  mov ecx, 0x1c4
006B9C91  48 8B 87 28 04 00 00            mov rax, qword ptr [rdi + 0x428]
006B9C98  48 8B 96 28 04 00 00            mov rdx, qword ptr [rsi + 0x428]
006B9C9F  48 3B C2                        cmp rax, rdx
006B9CA2  74 08                           je 0x1406b9cac
006B9CA4  8B C2                           mov eax, edx
006B9CA6  48 C1 EA 20                     shr rdx, 0x20
006B9CAA  0F 30                           wrmsr
006B9CAC  48 8B 97 50 02 00 00            mov rdx, qword ptr [rdi + 0x250]
006B9CB3  48 8B C2                        mov rax, rdx
006B9CB6  48 25 00 00 04 00               and rax, 0x40000
006B9CBC  48 23 15 9D CF 90 00            and rdx, qword ptr [rip + 0x90cf9d]
006B9CC3  48 0B D0                        or rdx, rax
006B9CC6  48 0B 96 50 02 00 00            or rdx, qword ptr [rsi + 0x250]
006B9CCD  C6 47 71 00                     mov byte ptr [rdi + 0x71], 0
006B9CD1  48 8B 4E 60                     mov rcx, qword ptr [rsi + 0x60]
006B9CD5  48 83 E2 FD                     and rdx, 0xfffffffffffffffd
006B9CD9  8B C2                           mov eax, edx
006B9CDB  74 2B                           je 0x1406b9d08
006B9CDD  48 C1 EA 20                     shr rdx, 0x20
006B9CE1  48 0F BA E5 29                  bt rbp, 0x29
006B9CE6  73 06                           jae 0x1406b9cee
006B9CE8  A8 01                           test al, 1
006B9CEA  74 02                           je 0x1406b9cee
006B9CEC  DB E3                           fninit
006B9CEE  48 0F BA E5 26                  bt rbp, 0x26
006B9CF3  72 0B                           jb 0x1406b9d00
006B9CF5  0F BA E5 17                     bt ebp, 0x17
006B9CF9  72 0A                           jb 0x1406b9d05
006B9CFB  0F AE 09                        fxrstor [rcx]
006B9CFE  EB 08                           jmp 0x1406b9d08
006B9D00  0F C7 19                        xrstors ptr [rcx]
006B9D03  EB 03                           jmp 0x1406b9d08
006B9D05  0F AE 29                        xrstor ptr [rcx]
006B9D08  0F AE 51 18                     ldmxcsr dword ptr [rcx + 0x18]
006B9D0C  A9 00 01 00 00                  test eax, 0x100
006B9D11  74 11                           je 0x1406b9d24
006B9D13  83 3D 7A CE 90 00 00            cmp dword ptr [rip + 0x90ce7a], 0
006B9D1A  74 08                           je 0x1406b9d24
006B9D1C  48 8B CE                        mov rcx, rsi
006B9D1F  E8 CC 03 F0 FF                  call 0x1405ba0f0
006B9D24  0F BA 66 74 0A                  bt dword ptr [rsi + 0x74], 0xa
006B9D29  0F 82 A0 00 00 00               jb 0x1406b9dcf
006B9D2F  48 8B 86 20 02 00 00            mov rax, qword ptr [rsi + 0x220]
006B9D36  48 83 B8 10 03 00 00 00         cmp qword ptr [rax + 0x310], 0
006B9D3E  8B 86 78 06 00 00               mov eax, dword ptr [rsi + 0x678]
006B9D44  74 0B                           je 0x1406b9d51
006B9D46  8B 86 F0 00 00 00               mov eax, dword ptr [rsi + 0xf0]
006B9D4C  05 00 20 00 00                  add eax, 0x2000
006B9D51  48 8B 8B 80 FE FF FF            mov rcx, qword ptr [rbx - 0x180]
006B9D58  66 89 41 52                     mov word ptr [rcx + 0x52], ax
006B9D5C  C1 E8 10                        shr eax, 0x10
006B9D5F  88 41 54                        mov byte ptr [rcx + 0x54], al
006B9D62  88 61 57                        mov byte ptr [rcx + 0x57], ah
006B9D65  B8 53 00 00 00                  mov eax, 0x53
006B9D6A  8E E0                           mov fs, eax
006B9D6C  8B 86 78 06 00 00               mov eax, dword ptr [rsi + 0x678]
006B9D72  8B 96 7C 06 00 00               mov edx, dword ptr [rsi + 0x67c]
006B9D78  B9 00 01 00 C0                  mov ecx, 0xc0000100
006B9D7D  0F 30                           wrmsr
006B9D7F  8C D8                           mov eax, ds
006B9D81  8C C2                           mov edx, es
006B9D83  23 C2                           and eax, edx
006B9D85  8C EA                           mov edx, gs
006B9D87  23 C2                           and eax, edx
006B9D89  66 83 F8 2B                     cmp ax, 0x2b
006B9D8D  74 13                           je 0x1406b9da2
006B9D8F  BA 2B 00 00 00                  mov edx, 0x2b
006B9D94  8E DA                           mov ds, edx
006B9D96  8E C2                           mov es, edx
006B9D98  FA                              cli
006B9D99  0F 01 F8                        swapgs
006B9D9C  8E EA                           mov gs, edx
006B9D9E  0F 01 F8                        swapgs
006B9DA1  FB                              sti
006B9DA2  48 8B 86 F0 00 00 00            mov rax, qword ptr [rsi + 0xf0]
006B9DA9  8B 96 F4 00 00 00               mov edx, dword ptr [rsi + 0xf4]
006B9DAF  48 89 83 B0 FE FF FF            mov qword ptr [rbx - 0x150], rax
006B9DB6  F6 46 03 04                     test byte ptr [rsi + 3], 4
006B9DBA  74 0C                           je 0x1406b9dc8
006B9DBC  8B 86 80 06 00 00               mov eax, dword ptr [rsi + 0x680]
006B9DC2  8B 96 84 06 00 00               mov edx, dword ptr [rsi + 0x684]
006B9DC8  B9 02 01 00 C0                  mov ecx, 0xc0000102
006B9DCD  0F 30                           wrmsr
006B9DCF  F7 83 BC 38 00 00 01 00 01 00   test dword ptr [rbx + 0x38bc], 0x10001
006B9DD9  75 72                           jne 0x1406b9e4d
006B9DDB  FF 86 54 01 00 00               inc dword ptr [rsi + 0x154]
006B9DE1  80 BE C1 00 00 00 01            cmp byte ptr [rsi + 0xc1], 1
006B9DE8  75 1C                           jne 0x1406b9e06
006B9DEA  66 0F B6 44 24 28               movzx ax, byte ptr [rsp + 0x28]
006B9DF0  66 0B 86 E6 01 00 00            or ax, word ptr [rsi + 0x1e6]
006B9DF7  74 0D                           je 0x1406b9e06
006B9DF9  B9 01 00 00 00                  mov ecx, 1
006B9DFE  E8 9D 0F D4 FF                  call 0x1403fada0
006B9E03  48 0B CC                        or rcx, rsp
006B9E06  0F 94 C0                        sete al
006B9E09  48 83 C4 30                     add rsp, 0x30
006B9E0D  5D                              pop rbp
006B9E0E  C3                              ret
006B9E0F  F7 05 EB CC 90 00 04 00 00 00   test dword ptr [rip + 0x90cceb], 4
006B9E19  74 0B                           je 0x1406b9e26
006B9E1B  48 8B CF                        mov rcx, rdi
006B9E1E  48 8B D6                        mov rdx, rsi
006B9E21  E8 7A D6 D5 FF                  call 0x1404174a0
006B9E26  F7 05 90 D7 88 00 02 00 00 00   test dword ptr [rip + 0x88d790], 2
006B9E30  74 05                           je 0x1406b9e37
006B9E32  E8 79 2C D6 FF                  call 0x14041cab0
006B9E37  F7 05 7F D7 88 00 04 00 00 00   test dword ptr [rip + 0x88d77f], 4
006B9E41  74 05                           je 0x1406b9e48
006B9E43  E8 68 83 EF FF                  call 0x1405b21b0
006B9E48  E9 38 FE FF FF                  jmp 0x1406b9c85
006B9E4D  4D 33 C9                        xor r9, r9
006B9E50  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
006B9E55  4C 8B C6                        mov r8, rsi
006B9E58  48 8B D7                        mov rdx, rdi
006B9E5B  B9 B8 00 00 00                  mov ecx, 0xb8
006B9E60  E8 FB 37 E4 FF                  call 0x1404fd660
006B9E65  CC                              int3
006B9E66  4D 33 C9                        xor r9, r9
006B9E69  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
006B9E6E  4C 8B C6                        mov r8, rsi
006B9E71  48 8B D7                        mov rdx, rdi
006B9E74  B9 CE 01 00 00                  mov ecx, 0x1ce
006B9E79  E8 E2 37 E4 FF                  call 0x1404fd660
006B9E7E  33 ED                           xor ebp, ebp
006B9E80  FF C5                           inc ebp
006B9E82  85 2D 24 B4 90 00               test dword ptr [rip + 0x90b424], ebp
006B9E88  75 1C                           jne 0x1406b9ea6
006B9E8A  F7 05 24 CC 90 00 40 00 00 00   test dword ptr [rip + 0x90cc24], 0x40
006B9E94  74 10                           je 0x1406b9ea6
006B9E96  E8 F5 55 C5 FF                  call 0x14030f490
006B9E9B  84 C0                           test al, al
006B9E9D  74 07                           je 0x1406b9ea6
006B9E9F  8B CD                           mov ecx, ebp
006B9EA1  E8 BA 55 C5 FF                  call 0x14030f460
006B9EA6  F3 90                           pause
006B9EA8  80 7E 71 00                     cmp byte ptr [rsi + 0x71], 0
006B9EAC  0F 84 86 F9 FF FF               je 0x1406b9838
006B9EB2  EB CC                           jmp 0x1406b9e80
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SwapContext(unsigned __int8 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_cr4;
    __int64 v_ds;
    __int64 v_es;
    __int64 v_gs;
    __int64 v_rbp;
    __int64 v_rsp;
    unsigned __int8 v_stack_m10;
    unsigned __int64 v_stack_p120;
    unsigned __int8 v_stack_pF0;

    v_rsp = (v_rsp) - (48);
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rsi + 113)) != 0) goto loc_006B9E7E;
loc_006B9838:
    *(unsigned __int8 *)(v_rsi + 113) = 1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9491622))) + (0x90D63EULL));
    if ((unsigned int)(result) != 0) {
        a2 = 0;
        a1 = 0xC0000502ULL;
    }
    result = KiStartThreadCycleAccumulationContextSwap(v_rbx, v_rsi, a3, a4);
    if ((*(unsigned int *)(v_rip + 9491973)) == 0) goto loc_006B9893;
    if ((*(unsigned int *)(v_rip + 9491973)) < 0) {
        a1 = v_rbx;
        a2 = v_rsi;
        result = KiCheckAndApplyCacheIsolation(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(v_rbx + 24)) == v_rsi) goto loc_006B98BA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 236))) ^ ((unsigned int)(*(unsigned __int8 *)(v_rsi + 516))));
    if ((((unsigned int)(result)) & (15)) != 0) {
        a1 = v_rbx;
        a2 = v_rsi;
        result = KeCheckAndApplyBamQos(a1, a2, a3, a4);
    }
    a2 = (*(unsigned __int64 *)(v_rdi + 592)) & (-3);
    if (condition_is_equal) goto loc_006B98F7;
    a2 = (a2) >> (32);
    if (condition_is_below) goto loc_006B98EF;
    if (condition_is_below) goto loc_006B98F4;
    if (condition_is_above_or_equal) goto loc_006B98EA;
    goto loc_006B98F7;
loc_006B98EA:
    goto loc_006B98F7;
loc_006B98EF:
    goto loc_006B98F7;
loc_006B98F4:
loc_006B98F7:
    if ((((unsigned int)((unsigned int)(a2))) & (256)) == 0) goto loc_006B9913;
    result = (unsigned int)(a2);
    if ((*(unsigned int *)(v_rip + 9491083)) != 0) {
        a1 = v_rdi;
        result = KiSaveThreadIptState(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rdi + 88) = v_rsp;
    if (((*(unsigned __int8 *)(v_rip + 11829023)) & (1)) != 0) {
        a1 = *(unsigned __int64 *)(v_rsi + 1040);
        *(unsigned __int64 *)(v_rbx + 39848) = a1;
        a1 = *(unsigned __int64 *)(v_rsi + 1032);
        a2 = (a2) - (8);
        *(unsigned __int64 *)(v_rdi + 1032) = a2;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 544) + 784)) != 0) {
        a1 = 0xC0000100ULL;
        *(unsigned int *)(v_rdi + 1656) = (unsigned int)(*(unsigned __int64 *)(v_rdi + 544));
        *(unsigned int *)(v_rdi + 1660) = a2;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 544) + 784)) < 0) {
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 544) + 784)) < 0) {
    }
    a1 = (unsigned __int8)((*(unsigned __int64 *)(v_rsi + 544)) | (*(unsigned __int8 *)(v_rbx + 1760)));
    a1 = (unsigned __int8)((a1) & (194));
    if (a1 == (*(unsigned __int64 *)(v_rdi + 544))) goto loc_006B99C1;
    a1 = (unsigned __int8)((a1) & (192));
    result = KiUpdateSpeculationControl(a1, a2, a3, a4);
    goto loc_006B9B77;
loc_006B99C1:
    a1 = (unsigned __int16)((*(unsigned __int8 *)(gs_base + (0 + 2142))) & (3));
    if (a1 != 1) goto loc_006B9B77;
    if ((*(unsigned __int16 *)(gs_base + (0 + 2150))) != ((unsigned __int16)(*(unsigned __int16 *)(gs_base + (0 + 2148))))) {
        *(unsigned __int16 *)(gs_base + (0 + 2150)) = (unsigned __int16)(*(unsigned __int16 *)(gs_base + (0 + 2148)));
        a1 = 72;
        a2 = 0;
    }
    result = *(unsigned __int16 *)(gs_base + (0 + 2148));
    if ((((unsigned int)(*(unsigned __int8 *)(gs_base + (0 + 2138)))) & (16)) != 0) {
        result = 1;
        a2 = 0;
        a1 = 73;
        a2 = *(unsigned __int8 *)(gs_base + (0 + 2138));
    }
    if (((a2) & (64)) == 0) goto loc_006B9B6A;
    result = SwapContext___0x326(a1, a2, a3, a4);
    v_rsp = (*(unsigned __int64 *)(v_rsi + 88)) + (8);
    result = SwapContext___0x32F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x218(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x221(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x22A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x233(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x23C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x245(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x24E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x257(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x260(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x269(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x272(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x27B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x284(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x28D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x296(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x29F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x2A8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x2B1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x2BA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x2C3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x2CC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x2D5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x2DE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x2E7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x2F0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x2F9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x302(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x30B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x314(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = SwapContext___0x31D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
loc_006B9B77:
    if ((*(unsigned __int64 *)(v_rsi + 184)) == (*(unsigned __int64 *)(v_rdi + 184))) goto loc_006B9C4A;
    if (((*(unsigned __int8 *)(v_rip + 11828366)) & (1)) == 0) goto loc_006B9BED;
    if (!(condition_is_above_or_equal)) {
    }
    *(unsigned __int64 *)(v_rbx + 44672) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 184) + 40);
    if (!(condition_is_above_or_equal)) {
    }
loc_006B9BED:
    if (((*(unsigned int *)(v_rip + 9490113)) & (1)) == 0) goto loc_006B9C00;
    result = HvlSwitchVirtualAddressSpace(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 184) + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 184) + 128), a3, a4);
    goto loc_006B9C27;
loc_006B9C00:
    if (((*(unsigned __int8 *)(v_rip + 11828278)) & (1)) == 0) goto loc_006B9C27;
    if (!(condition_is_below)) {
        result = v_cr4;
        result = (result) ^ (128);
        v_cr4 = result;
        result = (result) ^ (128);
        v_cr4 = result;
    }
loc_006B9C4A:
    if (((*(unsigned __int8 *)(v_rip + 11828203)) & (1)) != 0) goto loc_006B9C64;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx - 376) + 4) = *(unsigned __int64 *)(v_rsi + 40);
    goto loc_006B9C6B;
loc_006B9C64:
    *(unsigned __int64 *)(v_rbx + 44680) = *(unsigned __int64 *)(v_rsi + 40);
loc_006B9C6B:
    *(unsigned __int64 *)(v_rbx + 40) = *(unsigned __int64 *)(v_rsi + 40);
    if (condition_is_greater_or_equal) goto loc_006B9E66;
    if ((*(unsigned int *)(v_rip + 8968513)) != 0) goto loc_006B9E0F;
loc_006B9C85:
    if ((*(unsigned int *)(v_rip + 8968513)) >= 0) goto loc_006B9CAC;
    result = *(unsigned __int64 *)(v_rdi + 1064);
    if ((*(unsigned __int64 *)(v_rdi + 1064)) != (*(unsigned __int64 *)(v_rsi + 1064))) {
        result = (unsigned int)(*(unsigned __int64 *)(v_rsi + 1064));
        a2 = (*(unsigned __int64 *)(v_rsi + 1064)) >> (32);
    }
    result = (*(unsigned __int64 *)(v_rdi + 592)) & (0x40000ULL);
    a2 = (*(unsigned __int64 *)(v_rdi + 592)) & (*(unsigned __int64 *)(v_rip + 9490333));
    a2 = (a2) | (result);
    a2 = (a2) | (*(unsigned __int64 *)(v_rsi + 592));
    *(unsigned __int8 *)(v_rdi + 113) = 0;
    a2 = (a2) & (-3);
    if (condition_is_equal) goto loc_006B9D08;
    a2 = (a2) >> (32);
    if (condition_is_above_or_equal) goto loc_006B9CEE;
    if ((((unsigned __int8)((unsigned int)(a2))) & (1)) != 0) {
    }
    if (condition_is_below) goto loc_006B9D00;
    if (condition_is_below) goto loc_006B9D05;
    goto loc_006B9D08;
loc_006B9D00:
    goto loc_006B9D08;
loc_006B9D05:
loc_006B9D08:
    if ((((unsigned int)((unsigned int)(a2))) & (256)) == 0) goto loc_006B9D24;
    result = (unsigned int)(a2);
    if ((*(unsigned int *)(v_rip + 9490042)) != 0) {
        a1 = v_rsi;
        result = KiRestoreThreadIptState(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 9490042)) < 0) goto loc_006B9DCF;
    result = (unsigned int)(*(unsigned int *)(v_rsi + 1656));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 544) + 784)) != 0) {
        result = *(unsigned int *)(v_rsi + 240);
        result = (unsigned int)((result) + (0x2000ULL));
    }
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx - 384) + 82) = (unsigned __int16)(result);
    result = (unsigned int)((result) >> (16));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx - 384) + 84) = (unsigned __int8)(result);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx - 384) + 87) = (unsigned __int8)(result);
    result = (unsigned int)(((unsigned int)(v_ds)) & ((unsigned int)((unsigned int)(v_es))));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(v_gs))));
    if (((unsigned __int16)(result)) != 43) {
        a2 = 43;
        v_ds = a2;
        v_es = a2;
        v_gs = a2;
    }
    *(unsigned __int64 *)(v_rbx - 336) = *(unsigned __int64 *)(v_rsi + 240);
    result = *(unsigned __int64 *)(v_rsi + 240);
    if (((*(unsigned __int8 *)(v_rsi + 3)) & (4)) != 0) {
        result = *(unsigned int *)(v_rsi + 1664);
        a2 = *(unsigned int *)(v_rsi + 1668);
    }
loc_006B9DCF:
    if (((*(unsigned int *)(v_rbx + 14524)) & (0x10001ULL)) != 0) goto loc_006B9E4D;
    if ((*(unsigned __int8 *)(v_rsi + 193)) != 1) goto loc_006B9E06;
    result = (unsigned __int16)((v_stack_pF0) | (*(unsigned __int16 *)(v_rsi + 486)));
    if (!(condition_is_equal)) {
        a1 = 1;
        result = HalRequestSoftwareInterrupt(a1, a2, a3, a4);
        a1 = (a1) | (v_rsp);
    }
    result = (condition_is_equal) ? 1 : 0;
    v_rsp = (v_rsp) + (48);
    return result;
loc_006B9E0F:
    if (((*(unsigned int *)(v_rip + 9489643)) & (4)) != 0) {
        a1 = v_rdi;
        a2 = v_rsi;
        result = EtwTraceContextSwap(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(v_rip + 8968080)) & (2)) != 0) {
        result = KiClearLastBranchRecordStack(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(v_rip + 8968063)) & (4)) != 0) {
        result = KiResetProcessorTraceBuffer(a1, a2, a3, a4);
    }
    goto loc_006B9C85;
loc_006B9E4D:
    a4 = 0;
    v_stack_p120 = 0;
    result = KeBugCheckEx(184, v_rdi, v_rsi, a4);
loc_006B9E66:
    a4 = 0;
    v_stack_p120 = 0;
    result = KeBugCheckEx(462, v_rdi, v_rsi, a4);
loc_006B9E7E:
    v_rbp = 0;
loc_006B9E80:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 9483300)) & ((unsigned int)(v_rbp))) != 0) goto loc_006B9EA6;
    if (((*(unsigned int *)(v_rip + 9489444)) & (64)) == 0) goto loc_006B9EA6;
    result = KiCheckVpBackingLongSpinWaitHypercall(462, v_rdi, v_rsi, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = (unsigned int)(v_rbp);
        result = HvlNotifyLongSpinWait(a1, v_rdi, v_rsi, a4);
    }
    if ((*(unsigned __int8 *)(v_rsi + 113)) == 0) goto loc_006B9838;
    goto loc_006B9E80;
}
```

## 5. (Beta) C Style

```c
int64_t SwapContext(uint8_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t v_cr4;
    int64_t v_ds;
    int64_t v_es;
    int64_t v_gs;
    int64_t local_rbp;
    int64_t local_rsp;
    uint8_t v_stack_m10;
    uint64_t v_stack_p120;
    uint8_t v_stack_pF0;

    local_rsp = (local_rsp) - (48);
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(local_rsi + 0x71)) != 0) goto loc_006B9E7E;
loc_006B9838:
    *(uint8_t *)(local_rsi + 0x71) = 1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x90D4A6))) + (0x90D63EULL));
    if ((uint32_t)(result) != 0) {
        Arg2 = 0;
        Arg1 = 0xC0000502ULL;
    }
    result = KiStartThreadCycleAccumulationContextSwap(local_rbx, local_rsi, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x90D605)) == 0) goto loc_006B9893;
    if ((*(uint32_t *)(v_rip + 0x90D605)) < 0) {
        Arg1 = local_rbx;
        Arg2 = local_rsi;
        result = KiCheckAndApplyCacheIsolation(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint64_t *)(local_rbx + 0x18)) == local_rsi) goto loc_006B98BA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0xEC))) ^ ((uint32_t)(*(uint8_t *)(local_rsi + 0x204))));
    if ((((uint32_t)(result)) & (15)) != 0) {
        Arg1 = local_rbx;
        Arg2 = local_rsi;
        result = KeCheckAndApplyBamQos(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = (*(uint64_t *)(local_rdi + 0x250)) & (-3);
    if (condition_is_equal) goto loc_006B98F7;
    Arg2 = (Arg2) >> (32);
    if (condition_is_below) goto loc_006B98EF;
    if (condition_is_below) goto loc_006B98F4;
    if (condition_is_above_or_equal) goto loc_006B98EA;
    goto loc_006B98F7;
loc_006B98EA:
    goto loc_006B98F7;
loc_006B98EF:
    goto loc_006B98F7;
loc_006B98F4:
loc_006B98F7:
    if ((((uint32_t)((uint32_t)(Arg2))) & (256)) == 0) goto loc_006B9913;
    result = (uint32_t)(Arg2);
    if ((*(uint32_t *)(v_rip + 0x90D28B)) != 0) {
        Arg1 = local_rdi;
        result = KiSaveThreadIptState(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(local_rdi + 0x58) = local_rsp;
    if (((*(uint8_t *)(v_rip + 0xB47F1F)) & (1)) != 0) {
        Arg1 = *(uint64_t *)(local_rsi + 0x410);
        *(uint64_t *)(local_rbx + 0x9BA8) = Arg1;
        Arg1 = *(uint64_t *)(local_rsi + 0x408);
        Arg2 = (Arg2) - (8);
        *(uint64_t *)(local_rdi + 0x408) = Arg2;
    }
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x220) + 0x310)) != 0) {
        Arg1 = 0xC0000100ULL;
        *(uint32_t *)(local_rdi + 0x678) = (uint32_t)(*(uint64_t *)(local_rdi + 0x220));
        *(uint32_t *)(local_rdi + 0x67C) = Arg2;
    }
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x220) + 0x310)) < 0) {
    }
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x220) + 0x310)) < 0) {
    }
    Arg1 = (uint8_t)((*(uint64_t *)(local_rsi + 0x220)) | (*(uint8_t *)(local_rbx + 0x6E0)));
    Arg1 = (uint8_t)((Arg1) & (194));
    if (Arg1 == (*(uint64_t *)(local_rdi + 0x220))) goto loc_006B99C1;
    Arg1 = (uint8_t)((Arg1) & (192));
    result = KiUpdateSpeculationControl(Arg1, Arg2, Arg3, Arg4);
    goto loc_006B9B77;
loc_006B99C1:
    Arg1 = (uint16_t)((*(uint8_t *)(gs_base + (0 + 0x85E))) & (3));
    if (Arg1 != 1) goto loc_006B9B77;
    if ((*(uint16_t *)(gs_base + (0 + 0x866))) != ((uint16_t)(*(uint16_t *)(gs_base + (0 + 0x864))))) {
        *(uint16_t *)(gs_base + (0 + 0x866)) = (uint16_t)(*(uint16_t *)(gs_base + (0 + 0x864)));
        Arg1 = 72;
        Arg2 = 0;
    }
    result = *(uint16_t *)(gs_base + (0 + 0x864));
    if ((((uint32_t)(*(uint8_t *)(gs_base + (0 + 0x85A)))) & (16)) != 0) {
        result = 1;
        Arg2 = 0;
        Arg1 = 73;
        Arg2 = *(uint8_t *)(gs_base + (0 + 0x85A));
    }
    if (((Arg2) & (64)) == 0) goto loc_006B9B6A;
    result = SwapContext___0x326(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (*(uint64_t *)(local_rsi + 0x58)) + (8);
    result = SwapContext___0x32F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x218(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x221(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x22A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x233(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x23C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x245(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x24E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x257(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x260(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x269(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x272(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x27B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x284(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x28D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x296(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x29F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x2A8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x2B1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x2BA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x2C3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x2CC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x2D5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x2DE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x2E7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x2F0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x2F9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x302(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x30B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x314(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = SwapContext___0x31D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
loc_006B9B77:
    if ((*(uint64_t *)(local_rsi + 0xB8)) == (*(uint64_t *)(local_rdi + 0xB8))) goto loc_006B9C4A;
    if (((*(uint8_t *)(v_rip + 0xB47C8E)) & (1)) == 0) goto loc_006B9BED;
    if (!(condition_is_above_or_equal)) {
    }
    *(uint64_t *)(local_rbx + 0xAE80) = *(uint64_t *)(*(uint64_t *)(local_rsi + 0xB8) + 0x28);
    if (!(condition_is_above_or_equal)) {
    }
loc_006B9BED:
    if (((*(uint32_t *)(v_rip + 0x90CEC1)) & (1)) == 0) goto loc_006B9C00;
    result = HvlSwitchVirtualAddressSpace(*(uint64_t *)(*(uint64_t *)(local_rsi + 0xB8) + 0x28), *(uint64_t *)(*(uint64_t *)(local_rsi + 0xB8) + 0x80), Arg3, Arg4);
    goto loc_006B9C27;
loc_006B9C00:
    if (((*(uint8_t *)(v_rip + 0xB47C36)) & (1)) == 0) goto loc_006B9C27;
    if (!(condition_is_below)) {
        result = v_cr4;
        result = (result) ^ (128);
        v_cr4 = result;
        result = (result) ^ (128);
        v_cr4 = result;
    }
loc_006B9C4A:
    if (((*(uint8_t *)(v_rip + 0xB47BEB)) & (1)) != 0) goto loc_006B9C64;
    *(uint64_t *)(*(uint64_t *)(local_rbx - 0x178) + 0x4) = *(uint64_t *)(local_rsi + 0x28);
    goto loc_006B9C6B;
loc_006B9C64:
    *(uint64_t *)(local_rbx + 0xAE88) = *(uint64_t *)(local_rsi + 0x28);
loc_006B9C6B:
    *(uint64_t *)(local_rbx + 0x28) = *(uint64_t *)(local_rsi + 0x28);
    if (condition_is_greater_or_equal) goto loc_006B9E66;
    if ((*(uint32_t *)(v_rip + 0x88D941)) != 0) goto loc_006B9E0F;
loc_006B9C85:
    if ((*(uint32_t *)(v_rip + 0x88D941)) >= 0) goto loc_006B9CAC;
    result = *(uint64_t *)(local_rdi + 0x428);
    if ((*(uint64_t *)(local_rdi + 0x428)) != (*(uint64_t *)(local_rsi + 0x428))) {
        result = (uint32_t)(*(uint64_t *)(local_rsi + 0x428));
        Arg2 = (*(uint64_t *)(local_rsi + 0x428)) >> (32);
    }
    result = (*(uint64_t *)(local_rdi + 0x250)) & (0x40000ULL);
    Arg2 = (*(uint64_t *)(local_rdi + 0x250)) & (*(uint64_t *)(v_rip + 0x90CF9D));
    Arg2 = (Arg2) | (result);
    Arg2 = (Arg2) | (*(uint64_t *)(local_rsi + 0x250));
    *(uint8_t *)(local_rdi + 0x71) = 0;
    Arg2 = (Arg2) & (-3);
    if (condition_is_equal) goto loc_006B9D08;
    Arg2 = (Arg2) >> (32);
    if (condition_is_above_or_equal) goto loc_006B9CEE;
    if ((((uint8_t)((uint32_t)(Arg2))) & (1)) != 0) {
    }
    if (condition_is_below) goto loc_006B9D00;
    if (condition_is_below) goto loc_006B9D05;
    goto loc_006B9D08;
loc_006B9D00:
    goto loc_006B9D08;
loc_006B9D05:
loc_006B9D08:
    if ((((uint32_t)((uint32_t)(Arg2))) & (256)) == 0) goto loc_006B9D24;
    result = (uint32_t)(Arg2);
    if ((*(uint32_t *)(v_rip + 0x90CE7A)) != 0) {
        Arg1 = local_rsi;
        result = KiRestoreThreadIptState(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0x90CE7A)) < 0) goto loc_006B9DCF;
    result = (uint32_t)(*(uint32_t *)(local_rsi + 0x678));
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x220) + 0x310)) != 0) {
        result = *(uint32_t *)(local_rsi + 0xF0);
        result = (uint32_t)((result) + (0x2000ULL));
    }
    *(uint16_t *)(*(uint64_t *)(local_rbx - 0x180) + 0x52) = (uint16_t)(result);
    result = (uint32_t)((result) >> (16));
    *(uint8_t *)(*(uint64_t *)(local_rbx - 0x180) + 0x54) = (uint8_t)(result);
    *(uint8_t *)(*(uint64_t *)(local_rbx - 0x180) + 0x57) = (uint8_t)(result);
    result = (uint32_t)(((uint32_t)(v_ds)) & ((uint32_t)((uint32_t)(v_es))));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(v_gs))));
    if (((uint16_t)(result)) != 43) {
        Arg2 = 43;
        v_ds = Arg2;
        v_es = Arg2;
        v_gs = Arg2;
    }
    *(uint64_t *)(local_rbx - 0x150) = *(uint64_t *)(local_rsi + 0xF0);
    result = *(uint64_t *)(local_rsi + 0xF0);
    if (((*(uint8_t *)(local_rsi + 0x3)) & (4)) != 0) {
        result = *(uint32_t *)(local_rsi + 0x680);
        Arg2 = *(uint32_t *)(local_rsi + 0x684);
    }
loc_006B9DCF:
    if (((*(uint32_t *)(local_rbx + 0x38BC)) & (0x10001ULL)) != 0) goto loc_006B9E4D;
    if ((*(uint8_t *)(local_rsi + 0xC1)) != 1) goto loc_006B9E06;
    result = (uint16_t)((v_stack_pF0) | (*(uint16_t *)(local_rsi + 0x1E6)));
    if (!(condition_is_equal)) {
        Arg1 = 1;
        result = HalRequestSoftwareInterrupt(Arg1, Arg2, Arg3, Arg4);
        Arg1 = (Arg1) | (local_rsp);
    }
    result = (condition_is_equal) ? 1 : 0;
    local_rsp = (local_rsp) + (48);
    return result;
loc_006B9E0F:
    if (((*(uint32_t *)(v_rip + 0x90CCEB)) & (4)) != 0) {
        Arg1 = local_rdi;
        Arg2 = local_rsi;
        result = EtwTraceContextSwap(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(v_rip + 0x88D790)) & (2)) != 0) {
        result = KiClearLastBranchRecordStack(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(v_rip + 0x88D77F)) & (4)) != 0) {
        result = KiResetProcessorTraceBuffer(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_006B9C85;
loc_006B9E4D:
    Arg4 = 0;
    v_stack_p120 = 0;
    result = KeBugCheckEx(184, local_rdi, local_rsi, Arg4);
loc_006B9E66:
    Arg4 = 0;
    v_stack_p120 = 0;
    result = KeBugCheckEx(462, local_rdi, local_rsi, Arg4);
loc_006B9E7E:
    local_rbp = 0;
loc_006B9E80:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0x90B424)) & ((uint32_t)(local_rbp))) != 0) goto loc_006B9EA6;
    if (((*(uint32_t *)(v_rip + 0x90CC24)) & (64)) == 0) goto loc_006B9EA6;
    result = KiCheckVpBackingLongSpinWaitHypercall(462, local_rdi, local_rsi, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = (uint32_t)(local_rbp);
        result = HvlNotifyLongSpinWait(Arg1, local_rdi, local_rsi, Arg4);
    }
    if ((*(uint8_t *)(local_rsi + 0x71)) == 0) goto loc_006B9838;
    goto loc_006B9E80;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B9820&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
