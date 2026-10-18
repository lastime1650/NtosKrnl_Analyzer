# sub_00C7EB3D

- RVA: `0x00C7EB3D`–`0x00C7F7B0` (길이 `3,187` bytes)
- VA: `0x0000000140C7EB3D`
- 실행 섹션: `INIT`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2DB4`
- 디코드: `808`개 명령, `3,187/3,187` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x00C7EBA9` → [MmMapIoSpaceEx](../../text/32/MmMapIoSpaceEx_function_00327830.md) (function, `0x00327830`)
- `0x00C7EBD4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C7EBF0` → [KiSwInterruptPresent](../BE/KiSwInterruptPresent_function_00BEF1F4.md) (function, `0x00BEF1F4`)
- `0x00C7EC4D` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting](../../text/22/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting_function_00222FE0.md) (function, `0x00222FE0`)
- `0x00C7EC5D` → [MmStrongCodeGuaranteesEnforced](../C6/MmStrongCodeGuaranteesEnforced_function_00C6C980.md) (function, `0x00C6C980`)
- `0x00C7EC81` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x00C7EC9E` → [RtlCaptureImageExceptionValues](../../text/43/RtlCaptureImageExceptionValues_function_00432890.md) (function, `0x00432890`)
- `0x00C7F161` → [RtlSectionTableFromVirtualAddress](../../text/43/RtlSectionTableFromVirtualAddress_function_00432CF0.md) (function, `0x00432CF0`)
- `0x00C7F17C` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x00C7F195` → [RtlCaptureImageExceptionValues](../../text/43/RtlCaptureImageExceptionValues_function_00432890.md) (function, `0x00432890`)
- `0x00C7F660` → [RtlSectionTableFromVirtualAddress](../../text/43/RtlSectionTableFromVirtualAddress_function_00432CF0.md) (function, `0x00432CF0`)
- `0x00C7F781` → [KdDisableDebugger](../../text/5B/KdDisableDebugger_function_005B0900.md) (function, `0x005B0900`)
- `0x00C7F79A` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (function, `0x004FFB40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C7EB58` → RVA `0x01008620` (`INITDATA`; read)
- `0x00C7EB60` → RVA `0x01008620` (`INITDATA`; write)
- `0x00C7EBDA` → RVA `0x01008090` (`INITDATA`; write)
- `0x00C7EC43` → RVA `0x01008088` (`INITDATA`; write)
- `0x00C7EC56` → RVA `0x01008088` (`INITDATA`; read/write)
- `0x00C7EC6D` → RVA `0x01008088` (`INITDATA`; read)
- `0x00C7EC7A` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00C7ED66` → RVA `0x00E0A0C8` (`.data`; read)
- `0x00C7ED71` → RVA `0x00E0A0D8` (`.data`; read)
- `0x00C7F172` → RVA `0x00FC6B98` (`ALMOSTRO`; read)
- `0x00C7F671` → RVA `0x0100864C` (`INITDATA`; write)
- `0x00C7F6C5` → RVA `0x01008648` (`INITDATA`; read/write)
- `0x00C7F743` → RVA `0x00F475DC` (`.data`; read)
- `0x00C7F74B` → RVA `0x00E0AA1C` (`.data`; read)
- `0x00C7F78C` → RVA `0x00BEF284` (`INIT`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x00C7EBA9` → [MmMapIoSpaceEx](../../text/32/MmMapIoSpaceEx_function_00327830.md) (`INIT` → `.text`)
  - `0x00C7EBD4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C7EC4D` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting](../../text/22/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting_function_00222FE0.md) (`INIT` → `.text`)
  - `0x00C7EC81` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`INIT` → `.text`)
  - `0x00C7EC9E` → [RtlCaptureImageExceptionValues](../../text/43/RtlCaptureImageExceptionValues_function_00432890.md) (`INIT` → `.text`)
  - `0x00C7F161` → [RtlSectionTableFromVirtualAddress](../../text/43/RtlSectionTableFromVirtualAddress_function_00432CF0.md) (`INIT` → `.text`)
  - `0x00C7F17C` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`INIT` → `.text`)
  - `0x00C7F195` → [RtlCaptureImageExceptionValues](../../text/43/RtlCaptureImageExceptionValues_function_00432890.md) (`INIT` → `.text`)
  - `0x00C7F660` → [RtlSectionTableFromVirtualAddress](../../text/43/RtlSectionTableFromVirtualAddress_function_00432CF0.md) (`INIT` → `.text`)
  - `0x00C7F781` → [KdDisableDebugger](../../text/5B/KdDisableDebugger_function_005B0900.md) (`INIT` → `.text`)
  - `0x00C7F79A` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C7EB3D  40 53                           push rbx
00C7EB3F  55                              push rbp
00C7EB40  56                              push rsi
00C7EB41  57                              push rdi
00C7EB42  41 54                           push r12
00C7EB44  41 56                           push r14
00C7EB46  41 57                           push r15
00C7EB48  48 83 EC 30                     sub rsp, 0x30
00C7EB4C  48 8B EA                        mov rbp, rdx
00C7EB4F  48 8B 6D 48                     mov rbp, qword ptr [rbp + 0x48]
00C7EB53  48 89 6C 24 78                  mov qword ptr [rsp + 0x78], rbp
00C7EB58  8B 05 C2 9A 38 00               mov eax, dword ptr [rip + 0x389ac2]
00C7EB5E  FF C8                           dec eax
00C7EB60  89 05 BA 9A 38 00               mov dword ptr [rip + 0x389aba], eax
00C7EB66  8B 05 B4 9A 38 00               mov eax, dword ptr [rip + 0x389ab4]
00C7EB6C  85 C0                           test eax, eax
00C7EB6E  0F 85 2C 0C 00 00               jne 0x140c7f7a0
00C7EB74  8D 48 1B                        lea ecx, [rax + 0x1b]
00C7EB77  0F 32                           rdmsr
00C7EB79  48 C1 E2 20                     shl rdx, 0x20
00C7EB7D  48 0B C2                        or rax, rdx
00C7EB80  48 8B D8                        mov rbx, rax
00C7EB83  48 0F BA E0 0A                  bt rax, 0xa
00C7EB88  73 04                           jae 0x140c7eb8e
00C7EB8A  33 C0                           xor eax, eax
00C7EB8C  EB 4C                           jmp 0x140c7ebda
00C7EB8E  48 B8 00 F0 FF FF 0F 00 00 00   movabs rax, 0xffffff000
00C7EB98  48 23 D8                        and rbx, rax
00C7EB9B  BA 00 10 00 00                  mov edx, 0x1000
00C7EBA0  41 B8 04 02 00 00               mov r8d, 0x204
00C7EBA6  48 8B CB                        mov rcx, rbx
00C7EBA9  E8 82 8C 6A FF                  call 0x140327830
00C7EBAE  48 85 C0                        test rax, rax
00C7EBB1  75 27                           jne 0x140c7ebda
00C7EBB3  C7 85 78 01 00 00 09 00 00 E8   mov dword ptr [rbp + 0x178], 0xe8000009
00C7EBBD  8B 8D 78 01 00 00               mov ecx, dword ptr [rbp + 0x178]
00C7EBC3  C1 C1 65                        rol ecx, 0x65
00C7EBC6  48 21 44 24 20                  and qword ptr [rsp + 0x20], rax
00C7EBCB  45 33 C9                        xor r9d, r9d
00C7EBCE  4C 8B C3                        mov r8, rbx
00C7EBD1  8D 50 08                        lea edx, [rax + 8]
00C7EBD4  E8 87 EA 87 FF                  call 0x1404fd660
00C7EBD9  90                              nop
00C7EBDA  48 89 05 AF 94 38 00            mov qword ptr [rip + 0x3894af], rax
00C7EBE1  48 B8 89 02 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000289
00C7EBEB  80 38 00                        cmp byte ptr [rax], 0
00C7EBEE  74 5D                           je 0x140c7ec4d
00C7EBF0  E8 FF 05 F7 FF                  call 0x140bef1f4
00C7EBF5  85 C0                           test eax, eax
00C7EBF7  79 54                           jns 0x140c7ec4d
00C7EBF9  0F 31                           rdtsc
00C7EBFB  48 C1 E2 20                     shl rdx, 0x20
00C7EBFF  48 0B C2                        or rax, rdx
00C7EC02  48 8B D0                        mov rdx, rax
00C7EC05  48 8B C8                        mov rcx, rax
00C7EC08  48 C1 C9 03                     ror rcx, 3
00C7EC0C  48 33 D1                        xor rdx, rcx
00C7EC0F  48 B8 01 20 00 04 80 00 10 70   movabs rax, 0x7010008004002001
00C7EC19  48 F7 E2                        mul rdx
00C7EC1C  48 8B CA                        mov rcx, rdx
00C7EC1F  48 33 C8                        xor rcx, rax
00C7EC22  48 B8 CD CC CC CC CC CC CC CC   movabs rax, 0xcccccccccccccccd
00C7EC2C  48 F7 E1                        mul rcx
00C7EC2F  48 C1 EA 03                     shr rdx, 3
00C7EC33  48 8D 04 92                     lea rax, [rdx + rdx*4]
00C7EC37  48 03 C0                        add rax, rax
00C7EC3A  48 2B C8                        sub rcx, rax
00C7EC3D  48 83 F9 01                     cmp rcx, 1
00C7EC41  73 0A                           jae 0x140c7ec4d
00C7EC43  C7 05 3B 94 38 00 01 00 00 00   mov dword ptr [rip + 0x38943b], 1
00C7EC4D  E8 8E 43 5A FF                  call 0x140222fe0
00C7EC52  85 C0                           test eax, eax
00C7EC54  74 07                           je 0x140c7ec5d
00C7EC56  83 25 2B 94 38 00 00            and dword ptr [rip + 0x38942b], 0
00C7EC5D  E8 1E DD FE FF                  call 0x140c6c980
00C7EC62  85 C0                           test eax, eax
00C7EC64  74 07                           je 0x140c7ec6d
00C7EC66  83 25 1B 94 38 00 00            and dword ptr [rip + 0x38941b], 0
00C7EC6D  83 3D 14 94 38 00 00            cmp dword ptr [rip + 0x389414], 0
00C7EC74  0F 84 01 0A 00 00               je 0x140c7f67b
00C7EC7A  48 8D 0D 7F 13 38 FF            lea rcx, [rip - 0xc7ec81]
00C7EC81  E8 DA 4E 7C FF                  call 0x140443b60
00C7EC86  4C 8B F0                        mov r14, rax
00C7EC89  4C 8D 85 68 01 00 00            lea r8, [rbp + 0x168]
00C7EC90  48 8D 95 78 01 00 00            lea rdx, [rbp + 0x178]
00C7EC97  48 8D 0D 62 13 38 FF            lea rcx, [rip - 0xc7ec9e]
00C7EC9E  E8 ED 3B 7B FF                  call 0x140432890
00C7ECA3  8B 8D 68 01 00 00               mov ecx, dword ptr [rbp + 0x168]
00C7ECA9  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00C7ECB3  48 F7 E1                        mul rcx
00C7ECB6  48 C1 EA 03                     shr rdx, 3
00C7ECBA  89 95 68 01 00 00               mov dword ptr [rbp + 0x168], edx
00C7ECC0  85 D2                           test edx, edx
00C7ECC2  0F 84 AA 04 00 00               je 0x140c7f172
00C7ECC8  48 8B 9D 78 01 00 00            mov rbx, qword ptr [rbp + 0x178]
00C7ECCF  48 89 9D 00 01 00 00            mov qword ptr [rbp + 0x100], rbx
00C7ECD6  8B C2                           mov eax, edx
00C7ECD8  48 8D 0C 40                     lea rcx, [rax + rax*2]
00C7ECDC  4C 8D 3C 8B                     lea r15, [rbx + rcx*4]
00C7ECE0  33 FF                           xor edi, edi
00C7ECE2  89 BD 80 00 00 00               mov dword ptr [rbp + 0x80], edi
00C7ECE8  E9 67 04 00 00                  jmp 0x140c7f154
00C7ECED  33 F6                           xor esi, esi
00C7ECEF  41 F7 40 24 00 00 00 02         test dword ptr [r8 + 0x24], 0x2000000
00C7ECF7  0F 85 EC 01 00 00               jne 0x140c7eee9
00C7ECFD  41 81 38 49 4E 49 54            cmp dword ptr [r8], 0x54494e49
00C7ED04  75 0E                           jne 0x140c7ed14
00C7ED06  41 81 78 04 4B 44 42 47         cmp dword ptr [r8 + 4], 0x4742444b
00C7ED0E  0F 84 D5 01 00 00               je 0x140c7eee9
00C7ED14  41 81 38 50 41 47 45            cmp dword ptr [r8], 0x45474150
00C7ED1B  75 30                           jne 0x140c7ed4d
00C7ED1D  B8 77 78 00 00                  mov eax, 0x7877
00C7ED22  66 41 39 40 04                  cmp word ptr [r8 + 4], ax
00C7ED27  0F 84 BC 01 00 00               je 0x140c7eee9
00C7ED2D  B8 77 72 00 00                  mov eax, 0x7277
00C7ED32  66 41 39 40 04                  cmp word ptr [r8 + 4], ax
00C7ED37  0F 84 AC 01 00 00               je 0x140c7eee9
00C7ED3D  B8 77 77 00 00                  mov eax, 0x7777
00C7ED42  66 41 39 40 04                  cmp word ptr [r8 + 4], ax
00C7ED47  0F 84 9C 01 00 00               je 0x140c7eee9
00C7ED4D  41 81 38 45 52 52 41            cmp dword ptr [r8], 0x41525245
00C7ED54  75 10                           jne 0x140c7ed66
00C7ED56  B8 54 41 00 00                  mov eax, 0x4154
00C7ED5B  66 41 39 40 04                  cmp word ptr [r8 + 4], ax
00C7ED60  0F 84 83 01 00 00               je 0x140c7eee9
00C7ED66  0F 10 0D 5B B3 18 00            movups xmm1, xmmword ptr [rip + 0x18b35b]
00C7ED6D  0F 11 4D 48                     movups xmmword ptr [rbp + 0x48], xmm1
00C7ED71  0F 10 05 60 B3 18 00            movups xmm0, xmmword ptr [rip + 0x18b360]
00C7ED78  0F 11 45 58                     movups xmmword ptr [rbp + 0x58], xmm0
00C7ED7C  41 BB 07 00 00 00               mov r11d, 7
00C7ED82  44 89 5D 68                     mov dword ptr [rbp + 0x68], r11d
00C7ED86  66 49 0F 7E C9                  movq r9, xmm1
00C7ED8B  4C 89 8D D8 00 00 00            mov qword ptr [rbp + 0xd8], r9
00C7ED92  4D 8B D0                        mov r10, r8
00C7ED95  4C 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], r8
00C7ED9C  41 0F B6 12                     movzx edx, byte ptr [r10]
00C7EDA0  49 FF C2                        inc r10
00C7EDA3  4C 89 95 D0 00 00 00            mov qword ptr [rbp + 0xd0], r10
00C7EDAA  41 0F B6 01                     movzx eax, byte ptr [r9]
00C7EDAE  49 FF C1                        inc r9
00C7EDB1  4C 89 8D D8 00 00 00            mov qword ptr [rbp + 0xd8], r9
00C7EDB8  48 3B D0                        cmp rdx, rax
00C7EDBB  75 0F                           jne 0x140c7edcc
00C7EDBD  41 83 C3 FF                     add r11d, -1
00C7EDC1  44 89 5D 68                     mov dword ptr [rbp + 0x68], r11d
00C7EDC5  75 D5                           jne 0x140c7ed9c
00C7EDC7  E9 1D 01 00 00                  jmp 0x140c7eee9
00C7EDCC  41 B9 08 00 00 00               mov r9d, 8
00C7EDD2  44 89 4D 38                     mov dword ptr [rbp + 0x38], r9d
00C7EDD6  4C 8B 55 50                     mov r10, qword ptr [rbp + 0x50]
00C7EDDA  4C 89 95 B0 00 00 00            mov qword ptr [rbp + 0xb0], r10
00C7EDE1  4D 8B D8                        mov r11, r8
00C7EDE4  4C 89 85 A8 00 00 00            mov qword ptr [rbp + 0xa8], r8
00C7EDEB  49 8B 0B                        mov rcx, qword ptr [r11]
00C7EDEE  49 83 C3 08                     add r11, 8
00C7EDF2  4C 89 9D A8 00 00 00            mov qword ptr [rbp + 0xa8], r11
00C7EDF9  49 8B 02                        mov rax, qword ptr [r10]
00C7EDFC  49 83 C2 08                     add r10, 8
00C7EE00  4C 89 95 B0 00 00 00            mov qword ptr [rbp + 0xb0], r10
00C7EE07  48 3B C8                        cmp rcx, rax
00C7EE0A  75 47                           jne 0x140c7ee53
00C7EE0C  41 83 C1 F8                     add r9d, -8
00C7EE10  44 89 4D 38                     mov dword ptr [rbp + 0x38], r9d
00C7EE14  41 83 F9 08                     cmp r9d, 8
00C7EE18  73 D1                           jae 0x140c7edeb
00C7EE1A  45 85 C9                        test r9d, r9d
00C7EE1D  0F 84 C6 00 00 00               je 0x140c7eee9
00C7EE23  41 0F B6 13                     movzx edx, byte ptr [r11]
00C7EE27  49 FF C3                        inc r11
00C7EE2A  4C 89 9D A8 00 00 00            mov qword ptr [rbp + 0xa8], r11
00C7EE31  41 0F B6 02                     movzx eax, byte ptr [r10]
00C7EE35  49 FF C2                        inc r10
00C7EE38  4C 89 95 B0 00 00 00            mov qword ptr [rbp + 0xb0], r10
00C7EE3F  48 3B D0                        cmp rdx, rax
00C7EE42  75 0F                           jne 0x140c7ee53
00C7EE44  41 83 C1 FF                     add r9d, -1
00C7EE48  44 89 4D 38                     mov dword ptr [rbp + 0x38], r9d
00C7EE4C  75 D5                           jne 0x140c7ee23
00C7EE4E  E9 96 00 00 00                  jmp 0x140c7eee9
00C7EE53  41 BB 04 00 00 00               mov r11d, 4
00C7EE59  44 89 5D 70                     mov dword ptr [rbp + 0x70], r11d
00C7EE5D  4C 8B 4D 58                     mov r9, qword ptr [rbp + 0x58]
00C7EE61  4C 89 8D E8 00 00 00            mov qword ptr [rbp + 0xe8], r9
00C7EE68  4D 8B D0                        mov r10, r8
00C7EE6B  4C 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], r8
00C7EE72  41 0F B6 12                     movzx edx, byte ptr [r10]
00C7EE76  49 FF C2                        inc r10
00C7EE79  4C 89 95 E0 00 00 00            mov qword ptr [rbp + 0xe0], r10
00C7EE80  41 0F B6 01                     movzx eax, byte ptr [r9]
00C7EE84  49 FF C1                        inc r9
00C7EE87  4C 89 8D E8 00 00 00            mov qword ptr [rbp + 0xe8], r9
00C7EE8E  48 3B D0                        cmp rdx, rax
00C7EE91  75 0C                           jne 0x140c7ee9f
00C7EE93  41 83 C3 FF                     add r11d, -1
00C7EE97  44 89 5D 70                     mov dword ptr [rbp + 0x70], r11d
00C7EE9B  75 D5                           jne 0x140c7ee72
00C7EE9D  EB 4A                           jmp 0x140c7eee9
00C7EE9F  41 BB 06 00 00 00               mov r11d, 6
00C7EEA5  44 89 5D 78                     mov dword ptr [rbp + 0x78], r11d
00C7EEA9  4C 8B 4D 60                     mov r9, qword ptr [rbp + 0x60]
00C7EEAD  4C 89 8D F8 00 00 00            mov qword ptr [rbp + 0xf8], r9
00C7EEB4  4D 8B D0                        mov r10, r8
00C7EEB7  4C 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], r8
00C7EEBE  41 0F B6 12                     movzx edx, byte ptr [r10]
00C7EEC2  49 FF C2                        inc r10
00C7EEC5  4C 89 95 F0 00 00 00            mov qword ptr [rbp + 0xf0], r10
00C7EECC  41 0F B6 01                     movzx eax, byte ptr [r9]
00C7EED0  49 FF C1                        inc r9
00C7EED3  4C 89 8D F8 00 00 00            mov qword ptr [rbp + 0xf8], r9
00C7EEDA  48 3B D0                        cmp rdx, rax
00C7EEDD  75 0F                           jne 0x140c7eeee
00C7EEDF  41 83 C3 FF                     add r11d, -1
00C7EEE3  44 89 5D 78                     mov dword ptr [rbp + 0x78], r11d
00C7EEE7  75 D5                           jne 0x140c7eebe
00C7EEE9  BE 01 00 00 00                  mov esi, 1
00C7EEEE  41 8B 40 24                     mov eax, dword ptr [r8 + 0x24]
00C7EEF2  85 C0                           test eax, eax
00C7EEF4  79 07                           jns 0x140c7eefd
00C7EEF6  BE 01 00 00 00                  mov esi, 1
00C7EEFB  EB 0C                           jmp 0x140c7ef09
00C7EEFD  0F BA E0 1D                     bt eax, 0x1d
00C7EF01  B8 01 00 00 00                  mov eax, 1
00C7EF06  0F 43 F0                        cmovae esi, eax
00C7EF09  41 8B 40 08                     mov eax, dword ptr [r8 + 8]
00C7EF0D  41 39 40 10                     cmp dword ptr [r8 + 0x10], eax
00C7EF11  76 06                           jbe 0x140c7ef19
00C7EF13  41 8B 48 10                     mov ecx, dword ptr [r8 + 0x10]
00C7EF17  EB 02                           jmp 0x140c7ef1b
00C7EF19  8B C8                           mov ecx, eax
00C7EF1B  45 8B 50 0C                     mov r10d, dword ptr [r8 + 0xc]
00C7EF1F  44 03 D1                        add r10d, ecx
00C7EF22  8B 13                           mov edx, dword ptr [rbx]
00C7EF24  48 8D 0D D5 10 38 FF            lea rcx, [rip - 0xc7ef2b]
00C7EF2B  48 03 CA                        add rcx, rdx
00C7EF2E  41 B9 01 00 00 00               mov r9d, 1
00C7EF34  44 89 4D 30                     mov dword ptr [rbp + 0x30], r9d
00C7EF38  85 F6                           test esi, esi
00C7EF3A  0F 85 D7 01 00 00               jne 0x140c7f117
00C7EF40  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
00C7EF44  2B C2                           sub eax, edx
00C7EF46  83 F8 06                        cmp eax, 6
00C7EF49  0F 82 C8 01 00 00               jb 0x140c7f117
00C7EF4F  2B D7                           sub edx, edi
00C7EF51  83 FA 06                        cmp edx, 6
00C7EF54  0F 82 BD 01 00 00               jb 0x140c7f117
00C7EF5A  40 38 71 FA                     cmp byte ptr [rcx - 6], sil
00C7EF5E  75 27                           jne 0x140c7ef87
00C7EF60  40 38 71 FB                     cmp byte ptr [rcx - 5], sil
00C7EF64  75 21                           jne 0x140c7ef87
00C7EF66  40 38 71 FC                     cmp byte ptr [rcx - 4], sil
00C7EF6A  75 1B                           jne 0x140c7ef87
00C7EF6C  40 38 71 FD                     cmp byte ptr [rcx - 3], sil
00C7EF70  75 15                           jne 0x140c7ef87
00C7EF72  40 38 71 FE                     cmp byte ptr [rcx - 2], sil
00C7EF76  75 0F                           jne 0x140c7ef87
00C7EF78  40 38 71 FF                     cmp byte ptr [rcx - 1], sil
00C7EF7C  75 09                           jne 0x140c7ef87
00C7EF7E  83 65 30 00                     and dword ptr [rbp + 0x30], 0
00C7EF82  E9 95 01 00 00                  jmp 0x140c7f11c
00C7EF87  80 79 FA 84                     cmp byte ptr [rcx - 6], 0x84
00C7EF8B  75 1E                           jne 0x140c7efab
00C7EF8D  80 79 FB 00                     cmp byte ptr [rcx - 5], 0
00C7EF91  75 18                           jne 0x140c7efab
00C7EF93  80 79 FC 00                     cmp byte ptr [rcx - 4], 0
00C7EF97  75 12                           jne 0x140c7efab
00C7EF99  80 79 FD 00                     cmp byte ptr [rcx - 3], 0
00C7EF9D  75 0C                           jne 0x140c7efab
00C7EF9F  80 79 FE 00                     cmp byte ptr [rcx - 2], 0
00C7EFA3  75 06                           jne 0x140c7efab
00C7EFA5  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7EFA9  74 D3                           je 0x140c7ef7e
00C7EFAB  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7EFAF  75 1E                           jne 0x140c7efcf
00C7EFB1  80 79 FB CC                     cmp byte ptr [rcx - 5], 0xcc
00C7EFB5  75 18                           jne 0x140c7efcf
00C7EFB7  80 79 FC CC                     cmp byte ptr [rcx - 4], 0xcc
00C7EFBB  75 12                           jne 0x140c7efcf
00C7EFBD  80 79 FD CC                     cmp byte ptr [rcx - 3], 0xcc
00C7EFC1  75 0C                           jne 0x140c7efcf
00C7EFC3  80 79 FE CC                     cmp byte ptr [rcx - 2], 0xcc
00C7EFC7  75 06                           jne 0x140c7efcf
00C7EFC9  80 79 FF CC                     cmp byte ptr [rcx - 1], 0xcc
00C7EFCD  74 AF                           je 0x140c7ef7e
00C7EFCF  80 79 FA 1F                     cmp byte ptr [rcx - 6], 0x1f
00C7EFD3  75 46                           jne 0x140c7f01b
00C7EFD5  80 79 FB 84                     cmp byte ptr [rcx - 5], 0x84
00C7EFD9  75 18                           jne 0x140c7eff3
00C7EFDB  80 79 FC 00                     cmp byte ptr [rcx - 4], 0
00C7EFDF  75 12                           jne 0x140c7eff3
00C7EFE1  80 79 FD 00                     cmp byte ptr [rcx - 3], 0
00C7EFE5  75 0C                           jne 0x140c7eff3
00C7EFE7  80 79 FE 00                     cmp byte ptr [rcx - 2], 0
00C7EFEB  75 06                           jne 0x140c7eff3
00C7EFED  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7EFF1  74 8B                           je 0x140c7ef7e
00C7EFF3  80 79 FA 1F                     cmp byte ptr [rcx - 6], 0x1f
00C7EFF7  75 22                           jne 0x140c7f01b
00C7EFF9  80 79 FB 80                     cmp byte ptr [rcx - 5], 0x80
00C7EFFD  75 1C                           jne 0x140c7f01b
00C7EFFF  80 79 FC 00                     cmp byte ptr [rcx - 4], 0
00C7F003  75 16                           jne 0x140c7f01b
00C7F005  80 79 FD 00                     cmp byte ptr [rcx - 3], 0
00C7F009  75 10                           jne 0x140c7f01b
00C7F00B  80 79 FE 00                     cmp byte ptr [rcx - 2], 0
00C7F00F  75 0A                           jne 0x140c7f01b
00C7F011  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F015  0F 84 63 FF FF FF               je 0x140c7ef7e
00C7F01B  80 79 FA 66                     cmp byte ptr [rcx - 6], 0x66
00C7F01F  75 22                           jne 0x140c7f043
00C7F021  80 79 FB 0F                     cmp byte ptr [rcx - 5], 0xf
00C7F025  75 1C                           jne 0x140c7f043
00C7F027  80 79 FC 1F                     cmp byte ptr [rcx - 4], 0x1f
00C7F02B  75 16                           jne 0x140c7f043
00C7F02D  80 79 FD 44                     cmp byte ptr [rcx - 3], 0x44
00C7F031  75 10                           jne 0x140c7f043
00C7F033  80 79 FE 00                     cmp byte ptr [rcx - 2], 0
00C7F037  75 0A                           jne 0x140c7f043
00C7F039  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F03D  0F 84 3B FF FF FF               je 0x140c7ef7e
00C7F043  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7F047  0F 85 CA 00 00 00               jne 0x140c7f117
00C7F04D  80 79 FB 0F                     cmp byte ptr [rcx - 5], 0xf
00C7F051  75 1C                           jne 0x140c7f06f
00C7F053  80 79 FC 1F                     cmp byte ptr [rcx - 4], 0x1f
00C7F057  75 16                           jne 0x140c7f06f
00C7F059  80 79 FD 44                     cmp byte ptr [rcx - 3], 0x44
00C7F05D  75 10                           jne 0x140c7f06f
00C7F05F  80 79 FE 00                     cmp byte ptr [rcx - 2], 0
00C7F063  75 0A                           jne 0x140c7f06f
00C7F065  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F069  0F 84 0F FF FF FF               je 0x140c7ef7e
00C7F06F  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7F073  0F 85 9E 00 00 00               jne 0x140c7f117
00C7F079  80 79 FB CC                     cmp byte ptr [rcx - 5], 0xcc
00C7F07D  75 1C                           jne 0x140c7f09b
00C7F07F  80 79 FC 0F                     cmp byte ptr [rcx - 4], 0xf
00C7F083  75 16                           jne 0x140c7f09b
00C7F085  80 79 FD 1F                     cmp byte ptr [rcx - 3], 0x1f
00C7F089  75 10                           jne 0x140c7f09b
00C7F08B  80 79 FE 40                     cmp byte ptr [rcx - 2], 0x40
00C7F08F  75 0A                           jne 0x140c7f09b
00C7F091  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F095  0F 84 E3 FE FF FF               je 0x140c7ef7e
00C7F09B  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7F09F  75 76                           jne 0x140c7f117
00C7F0A1  80 79 FB CC                     cmp byte ptr [rcx - 5], 0xcc
00C7F0A5  75 1C                           jne 0x140c7f0c3
00C7F0A7  80 79 FC CC                     cmp byte ptr [rcx - 4], 0xcc
00C7F0AB  75 16                           jne 0x140c7f0c3
00C7F0AD  80 79 FD 0F                     cmp byte ptr [rcx - 3], 0xf
00C7F0B1  75 10                           jne 0x140c7f0c3
00C7F0B3  80 79 FE 1F                     cmp byte ptr [rcx - 2], 0x1f
00C7F0B7  75 0A                           jne 0x140c7f0c3
00C7F0B9  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F0BD  0F 84 BB FE FF FF               je 0x140c7ef7e
00C7F0C3  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7F0C7  75 4E                           jne 0x140c7f117
00C7F0C9  80 79 FB CC                     cmp byte ptr [rcx - 5], 0xcc
00C7F0CD  75 1C                           jne 0x140c7f0eb
00C7F0CF  80 79 FC CC                     cmp byte ptr [rcx - 4], 0xcc
00C7F0D3  75 16                           jne 0x140c7f0eb
00C7F0D5  80 79 FD CC                     cmp byte ptr [rcx - 3], 0xcc
00C7F0D9  75 10                           jne 0x140c7f0eb
00C7F0DB  80 79 FE 66                     cmp byte ptr [rcx - 2], 0x66
00C7F0DF  75 0A                           jne 0x140c7f0eb
00C7F0E1  80 79 FF 90                     cmp byte ptr [rcx - 1], 0x90
00C7F0E5  0F 84 93 FE FF FF               je 0x140c7ef7e
00C7F0EB  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7F0EF  75 26                           jne 0x140c7f117
00C7F0F1  80 79 FB CC                     cmp byte ptr [rcx - 5], 0xcc
00C7F0F5  75 20                           jne 0x140c7f117
00C7F0F7  80 79 FC CC                     cmp byte ptr [rcx - 4], 0xcc
00C7F0FB  75 1A                           jne 0x140c7f117
00C7F0FD  80 79 FD CC                     cmp byte ptr [rcx - 3], 0xcc
00C7F101  75 14                           jne 0x140c7f117
00C7F103  80 79 FE CC                     cmp byte ptr [rcx - 2], 0xcc
00C7F107  75 0E                           jne 0x140c7f117
00C7F109  33 C0                           xor eax, eax
00C7F10B  80 79 FF 90                     cmp byte ptr [rcx - 1], 0x90
00C7F10F  44 0F 44 C8                     cmove r9d, eax
00C7F113  44 89 4D 30                     mov dword ptr [rbp + 0x30], r9d
00C7F117  45 85 C9                        test r9d, r9d
00C7F11A  75 0D                           jne 0x140c7f129
00C7F11C  C7 41 FA 4C 87 00 98            mov dword ptr [rcx - 6], 0x9800874c
00C7F123  66 C7 41 FE C3 90               mov word ptr [rcx - 2], 0x90c3
00C7F129  8B 7B 04                        mov edi, dword ptr [rbx + 4]
00C7F12C  89 BD 80 00 00 00               mov dword ptr [rbp + 0x80], edi
00C7F132  48 83 C3 0C                     add rbx, 0xc
00C7F136  48 89 9D 00 01 00 00            mov qword ptr [rbp + 0x100], rbx
00C7F13D  49 3B DF                        cmp rbx, r15
00C7F140  74 30                           je 0x140c7f172
00C7F142  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
00C7F146  39 03                           cmp dword ptr [rbx], eax
00C7F148  72 0A                           jb 0x140c7f154
00C7F14A  44 39 53 04                     cmp dword ptr [rbx + 4], r10d
00C7F14E  0F 86 CE FD FF FF               jbe 0x140c7ef22
00C7F154  44 8B 03                        mov r8d, dword ptr [rbx]
00C7F157  48 8D 15 A2 0E 38 FF            lea rdx, [rip - 0xc7f15e]
00C7F15E  49 8B CE                        mov rcx, r14
00C7F161  E8 8A 3B 7B FF                  call 0x140432cf0
00C7F166  48 85 C0                        test rax, rax
00C7F169  4C 8B C0                        mov r8, rax
00C7F16C  0F 85 7B FB FF FF               jne 0x140c7eced
00C7F172  4C 8B 35 1F 7A 34 00            mov r14, qword ptr [rip + 0x347a1f]
00C7F179  49 8B CE                        mov rcx, r14
00C7F17C  E8 DF 49 7C FF                  call 0x140443b60
00C7F181  4C 8B F8                        mov r15, rax
00C7F184  4C 8D 85 70 01 00 00            lea r8, [rbp + 0x170]
00C7F18B  48 8D 95 08 01 00 00            lea rdx, [rbp + 0x108]
00C7F192  49 8B CE                        mov rcx, r14
00C7F195  E8 F6 36 7B FF                  call 0x140432890
00C7F19A  8B 8D 70 01 00 00               mov ecx, dword ptr [rbp + 0x170]
00C7F1A0  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00C7F1AA  48 F7 E1                        mul rcx
00C7F1AD  48 C1 EA 03                     shr rdx, 3
00C7F1B1  89 95 70 01 00 00               mov dword ptr [rbp + 0x170], edx
00C7F1B7  85 D2                           test edx, edx
00C7F1B9  0F 84 B2 04 00 00               je 0x140c7f671
00C7F1BF  48 8B 9D 08 01 00 00            mov rbx, qword ptr [rbp + 0x108]
00C7F1C6  48 89 9D 40 01 00 00            mov qword ptr [rbp + 0x140], rbx
00C7F1CD  8B C2                           mov eax, edx
00C7F1CF  48 8D 0C 40                     lea rcx, [rax + rax*2]
00C7F1D3  4C 8D 24 8B                     lea r12, [rbx + rcx*4]
00C7F1D7  33 FF                           xor edi, edi
00C7F1D9  89 BD A0 00 00 00               mov dword ptr [rbp + 0xa0], edi
00C7F1DF  E9 73 04 00 00                  jmp 0x140c7f657
00C7F1E4  33 F6                           xor esi, esi
00C7F1E6  41 F7 40 24 00 00 00 02         test dword ptr [r8 + 0x24], 0x2000000
00C7F1EE  0F 85 FE 01 00 00               jne 0x140c7f3f2
00C7F1F4  41 81 38 49 4E 49 54            cmp dword ptr [r8], 0x54494e49
00C7F1FB  75 0E                           jne 0x140c7f20b
00C7F1FD  41 81 78 04 4B 44 42 47         cmp dword ptr [r8 + 4], 0x4742444b
00C7F205  0F 84 E7 01 00 00               je 0x140c7f3f2
00C7F20B  41 81 38 50 41 47 45            cmp dword ptr [r8], 0x45474150
00C7F212  75 30                           jne 0x140c7f244
00C7F214  B8 77 78 00 00                  mov eax, 0x7877
00C7F219  66 41 39 40 04                  cmp word ptr [r8 + 4], ax
00C7F21E  0F 84 CE 01 00 00               je 0x140c7f3f2
00C7F224  B8 77 72 00 00                  mov eax, 0x7277
00C7F229  66 41 39 40 04                  cmp word ptr [r8 + 4], ax
00C7F22E  0F 84 BE 01 00 00               je 0x140c7f3f2
00C7F234  B8 77 77 00 00                  mov eax, 0x7777
00C7F239  66 41 39 40 04                  cmp word ptr [r8 + 4], ax
00C7F23E  0F 84 AE 01 00 00               je 0x140c7f3f2
00C7F244  41 81 38 45 52 52 41            cmp dword ptr [r8], 0x41525245
00C7F24B  75 10                           jne 0x140c7f25d
00C7F24D  B8 54 41 00 00                  mov eax, 0x4154
00C7F252  66 41 39 40 04                  cmp word ptr [r8 + 4], ax
00C7F257  0F 84 95 01 00 00               je 0x140c7f3f2
00C7F25D  0F 10 0D 64 AE 18 00            movups xmm1, xmmword ptr [rip + 0x18ae64]
00C7F264  0F 11 4D 48                     movups xmmword ptr [rbp + 0x48], xmm1
00C7F268  0F 10 05 69 AE 18 00            movups xmm0, xmmword ptr [rip + 0x18ae69]
00C7F26F  0F 11 45 58                     movups xmmword ptr [rbp + 0x58], xmm0
00C7F273  41 BB 07 00 00 00               mov r11d, 7
00C7F279  44 89 9D 88 00 00 00            mov dword ptr [rbp + 0x88], r11d
00C7F280  66 49 0F 7E C9                  movq r9, xmm1
00C7F285  4C 89 8D 18 01 00 00            mov qword ptr [rbp + 0x118], r9
00C7F28C  4D 8B D0                        mov r10, r8
00C7F28F  4C 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], r8
00C7F296  41 0F B6 12                     movzx edx, byte ptr [r10]
00C7F29A  49 FF C2                        inc r10
00C7F29D  4C 89 95 10 01 00 00            mov qword ptr [rbp + 0x110], r10
00C7F2A4  41 0F B6 01                     movzx eax, byte ptr [r9]
00C7F2A8  49 FF C1                        inc r9
00C7F2AB  4C 89 8D 18 01 00 00            mov qword ptr [rbp + 0x118], r9
00C7F2B2  48 3B D0                        cmp rdx, rax
00C7F2B5  75 12                           jne 0x140c7f2c9
00C7F2B7  41 83 C3 FF                     add r11d, -1
00C7F2BB  44 89 9D 88 00 00 00            mov dword ptr [rbp + 0x88], r11d
00C7F2C2  75 D2                           jne 0x140c7f296
00C7F2C4  E9 29 01 00 00                  jmp 0x140c7f3f2
00C7F2C9  41 B9 08 00 00 00               mov r9d, 8
00C7F2CF  44 89 4D 40                     mov dword ptr [rbp + 0x40], r9d
00C7F2D3  4C 8B 55 50                     mov r10, qword ptr [rbp + 0x50]
00C7F2D7  4C 89 95 C0 00 00 00            mov qword ptr [rbp + 0xc0], r10
00C7F2DE  4D 8B D8                        mov r11, r8
00C7F2E1  4C 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], r8
00C7F2E8  49 8B 0B                        mov rcx, qword ptr [r11]
00C7F2EB  49 83 C3 08                     add r11, 8
00C7F2EF  4C 89 9D B8 00 00 00            mov qword ptr [rbp + 0xb8], r11
00C7F2F6  49 8B 02                        mov rax, qword ptr [r10]
00C7F2F9  49 83 C2 08                     add r10, 8
00C7F2FD  4C 89 95 C0 00 00 00            mov qword ptr [rbp + 0xc0], r10
00C7F304  48 3B C8                        cmp rcx, rax
00C7F307  75 47                           jne 0x140c7f350
00C7F309  41 83 C1 F8                     add r9d, -8
00C7F30D  44 89 4D 40                     mov dword ptr [rbp + 0x40], r9d
00C7F311  41 83 F9 08                     cmp r9d, 8
00C7F315  73 D1                           jae 0x140c7f2e8
00C7F317  45 85 C9                        test r9d, r9d
00C7F31A  0F 84 D2 00 00 00               je 0x140c7f3f2
00C7F320  41 0F B6 13                     movzx edx, byte ptr [r11]
00C7F324  49 FF C3                        inc r11
00C7F327  4C 89 9D B8 00 00 00            mov qword ptr [rbp + 0xb8], r11
00C7F32E  41 0F B6 02                     movzx eax, byte ptr [r10]
00C7F332  49 FF C2                        inc r10
00C7F335  4C 89 95 C0 00 00 00            mov qword ptr [rbp + 0xc0], r10
00C7F33C  48 3B D0                        cmp rdx, rax
00C7F33F  75 0F                           jne 0x140c7f350
00C7F341  41 83 C1 FF                     add r9d, -1
00C7F345  44 89 4D 40                     mov dword ptr [rbp + 0x40], r9d
00C7F349  75 D5                           jne 0x140c7f320
00C7F34B  E9 A2 00 00 00                  jmp 0x140c7f3f2
00C7F350  41 BB 04 00 00 00               mov r11d, 4
00C7F356  44 89 9D 90 00 00 00            mov dword ptr [rbp + 0x90], r11d
00C7F35D  4C 8B 4D 58                     mov r9, qword ptr [rbp + 0x58]
00C7F361  4C 89 8D 28 01 00 00            mov qword ptr [rbp + 0x128], r9
00C7F368  4D 8B D0                        mov r10, r8
00C7F36B  4C 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], r8
00C7F372  41 0F B6 12                     movzx edx, byte ptr [r10]
00C7F376  49 FF C2                        inc r10
00C7F379  4C 89 95 20 01 00 00            mov qword ptr [rbp + 0x120], r10
00C7F380  41 0F B6 01                     movzx eax, byte ptr [r9]
00C7F384  49 FF C1                        inc r9
00C7F387  4C 89 8D 28 01 00 00            mov qword ptr [rbp + 0x128], r9
00C7F38E  48 3B D0                        cmp rdx, rax
00C7F391  75 0F                           jne 0x140c7f3a2
00C7F393  41 83 C3 FF                     add r11d, -1
00C7F397  44 89 9D 90 00 00 00            mov dword ptr [rbp + 0x90], r11d
00C7F39E  75 D2                           jne 0x140c7f372
00C7F3A0  EB 50                           jmp 0x140c7f3f2
00C7F3A2  41 BB 06 00 00 00               mov r11d, 6
00C7F3A8  44 89 9D 98 00 00 00            mov dword ptr [rbp + 0x98], r11d
00C7F3AF  4C 8B 4D 60                     mov r9, qword ptr [rbp + 0x60]
00C7F3B3  4C 89 8D 38 01 00 00            mov qword ptr [rbp + 0x138], r9
00C7F3BA  4D 8B D0                        mov r10, r8
00C7F3BD  4C 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], r8
00C7F3C4  41 0F B6 12                     movzx edx, byte ptr [r10]
00C7F3C8  49 FF C2                        inc r10
00C7F3CB  4C 89 95 30 01 00 00            mov qword ptr [rbp + 0x130], r10
00C7F3D2  41 0F B6 01                     movzx eax, byte ptr [r9]
00C7F3D6  49 FF C1                        inc r9
00C7F3D9  4C 89 8D 38 01 00 00            mov qword ptr [rbp + 0x138], r9
00C7F3E0  48 3B D0                        cmp rdx, rax
00C7F3E3  75 12                           jne 0x140c7f3f7
00C7F3E5  41 83 C3 FF                     add r11d, -1
00C7F3E9  44 89 9D 98 00 00 00            mov dword ptr [rbp + 0x98], r11d
00C7F3F0  75 D2                           jne 0x140c7f3c4
00C7F3F2  BE 01 00 00 00                  mov esi, 1
00C7F3F7  41 8B 40 24                     mov eax, dword ptr [r8 + 0x24]
00C7F3FB  85 C0                           test eax, eax
00C7F3FD  79 07                           jns 0x140c7f406
00C7F3FF  BE 01 00 00 00                  mov esi, 1
00C7F404  EB 0C                           jmp 0x140c7f412
00C7F406  0F BA E0 1D                     bt eax, 0x1d
00C7F40A  B8 01 00 00 00                  mov eax, 1
00C7F40F  0F 43 F0                        cmovae esi, eax
00C7F412  41 8B 40 08                     mov eax, dword ptr [r8 + 8]
00C7F416  41 39 40 10                     cmp dword ptr [r8 + 0x10], eax
00C7F41A  76 06                           jbe 0x140c7f422
00C7F41C  41 8B 48 10                     mov ecx, dword ptr [r8 + 0x10]
00C7F420  EB 02                           jmp 0x140c7f424
00C7F422  8B C8                           mov ecx, eax
00C7F424  45 8B 50 0C                     mov r10d, dword ptr [r8 + 0xc]
00C7F428  44 03 D1                        add r10d, ecx
00C7F42B  8B 13                           mov edx, dword ptr [rbx]
00C7F42D  49 8D 0C 16                     lea rcx, [r14 + rdx]
00C7F431  41 B9 01 00 00 00               mov r9d, 1
00C7F437  44 89 4D 34                     mov dword ptr [rbp + 0x34], r9d
00C7F43B  85 F6                           test esi, esi
00C7F43D  0F 85 D7 01 00 00               jne 0x140c7f61a
00C7F443  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
00C7F447  2B C2                           sub eax, edx
00C7F449  83 F8 06                        cmp eax, 6
00C7F44C  0F 82 C8 01 00 00               jb 0x140c7f61a
00C7F452  2B D7                           sub edx, edi
00C7F454  83 FA 06                        cmp edx, 6
00C7F457  0F 82 BD 01 00 00               jb 0x140c7f61a
00C7F45D  40 38 71 FA                     cmp byte ptr [rcx - 6], sil
00C7F461  75 27                           jne 0x140c7f48a
00C7F463  40 38 71 FB                     cmp byte ptr [rcx - 5], sil
00C7F467  75 21                           jne 0x140c7f48a
00C7F469  40 38 71 FC                     cmp byte ptr [rcx - 4], sil
00C7F46D  75 1B                           jne 0x140c7f48a
00C7F46F  40 38 71 FD                     cmp byte ptr [rcx - 3], sil
00C7F473  75 15                           jne 0x140c7f48a
00C7F475  40 38 71 FE                     cmp byte ptr [rcx - 2], sil
00C7F479  75 0F                           jne 0x140c7f48a
00C7F47B  40 38 71 FF                     cmp byte ptr [rcx - 1], sil
00C7F47F  75 09                           jne 0x140c7f48a
00C7F481  83 65 34 00                     and dword ptr [rbp + 0x34], 0
00C7F485  E9 95 01 00 00                  jmp 0x140c7f61f
00C7F48A  80 79 FA 84                     cmp byte ptr [rcx - 6], 0x84
00C7F48E  75 1E                           jne 0x140c7f4ae
00C7F490  80 79 FB 00                     cmp byte ptr [rcx - 5], 0
00C7F494  75 18                           jne 0x140c7f4ae
00C7F496  80 79 FC 00                     cmp byte ptr [rcx - 4], 0
00C7F49A  75 12                           jne 0x140c7f4ae
00C7F49C  80 79 FD 00                     cmp byte ptr [rcx - 3], 0
00C7F4A0  75 0C                           jne 0x140c7f4ae
00C7F4A2  80 79 FE 00                     cmp byte ptr [rcx - 2], 0
00C7F4A6  75 06                           jne 0x140c7f4ae
00C7F4A8  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F4AC  74 D3                           je 0x140c7f481
00C7F4AE  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7F4B2  75 1E                           jne 0x140c7f4d2
00C7F4B4  80 79 FB CC                     cmp byte ptr [rcx - 5], 0xcc
00C7F4B8  75 18                           jne 0x140c7f4d2
00C7F4BA  80 79 FC CC                     cmp byte ptr [rcx - 4], 0xcc
00C7F4BE  75 12                           jne 0x140c7f4d2
00C7F4C0  80 79 FD CC                     cmp byte ptr [rcx - 3], 0xcc
00C7F4C4  75 0C                           jne 0x140c7f4d2
00C7F4C6  80 79 FE CC                     cmp byte ptr [rcx - 2], 0xcc
00C7F4CA  75 06                           jne 0x140c7f4d2
00C7F4CC  80 79 FF CC                     cmp byte ptr [rcx - 1], 0xcc
00C7F4D0  74 AF                           je 0x140c7f481
00C7F4D2  80 79 FA 1F                     cmp byte ptr [rcx - 6], 0x1f
00C7F4D6  75 46                           jne 0x140c7f51e
00C7F4D8  80 79 FB 84                     cmp byte ptr [rcx - 5], 0x84
00C7F4DC  75 18                           jne 0x140c7f4f6
00C7F4DE  80 79 FC 00                     cmp byte ptr [rcx - 4], 0
00C7F4E2  75 12                           jne 0x140c7f4f6
00C7F4E4  80 79 FD 00                     cmp byte ptr [rcx - 3], 0
00C7F4E8  75 0C                           jne 0x140c7f4f6
00C7F4EA  80 79 FE 00                     cmp byte ptr [rcx - 2], 0
00C7F4EE  75 06                           jne 0x140c7f4f6
00C7F4F0  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F4F4  74 8B                           je 0x140c7f481
00C7F4F6  80 79 FA 1F                     cmp byte ptr [rcx - 6], 0x1f
00C7F4FA  75 22                           jne 0x140c7f51e
00C7F4FC  80 79 FB 80                     cmp byte ptr [rcx - 5], 0x80
00C7F500  75 1C                           jne 0x140c7f51e
00C7F502  80 79 FC 00                     cmp byte ptr [rcx - 4], 0
00C7F506  75 16                           jne 0x140c7f51e
00C7F508  80 79 FD 00                     cmp byte ptr [rcx - 3], 0
00C7F50C  75 10                           jne 0x140c7f51e
00C7F50E  80 79 FE 00                     cmp byte ptr [rcx - 2], 0
00C7F512  75 0A                           jne 0x140c7f51e
00C7F514  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F518  0F 84 63 FF FF FF               je 0x140c7f481
00C7F51E  80 79 FA 66                     cmp byte ptr [rcx - 6], 0x66
00C7F522  75 22                           jne 0x140c7f546
00C7F524  80 79 FB 0F                     cmp byte ptr [rcx - 5], 0xf
00C7F528  75 1C                           jne 0x140c7f546
00C7F52A  80 79 FC 1F                     cmp byte ptr [rcx - 4], 0x1f
00C7F52E  75 16                           jne 0x140c7f546
00C7F530  80 79 FD 44                     cmp byte ptr [rcx - 3], 0x44
00C7F534  75 10                           jne 0x140c7f546
00C7F536  80 79 FE 00                     cmp byte ptr [rcx - 2], 0
00C7F53A  75 0A                           jne 0x140c7f546
00C7F53C  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F540  0F 84 3B FF FF FF               je 0x140c7f481
00C7F546  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7F54A  0F 85 CA 00 00 00               jne 0x140c7f61a
00C7F550  80 79 FB 0F                     cmp byte ptr [rcx - 5], 0xf
00C7F554  75 1C                           jne 0x140c7f572
00C7F556  80 79 FC 1F                     cmp byte ptr [rcx - 4], 0x1f
00C7F55A  75 16                           jne 0x140c7f572
00C7F55C  80 79 FD 44                     cmp byte ptr [rcx - 3], 0x44
00C7F560  75 10                           jne 0x140c7f572
00C7F562  80 79 FE 00                     cmp byte ptr [rcx - 2], 0
00C7F566  75 0A                           jne 0x140c7f572
00C7F568  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F56C  0F 84 0F FF FF FF               je 0x140c7f481
00C7F572  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7F576  0F 85 9E 00 00 00               jne 0x140c7f61a
00C7F57C  80 79 FB CC                     cmp byte ptr [rcx - 5], 0xcc
00C7F580  75 1C                           jne 0x140c7f59e
00C7F582  80 79 FC 0F                     cmp byte ptr [rcx - 4], 0xf
00C7F586  75 16                           jne 0x140c7f59e
00C7F588  80 79 FD 1F                     cmp byte ptr [rcx - 3], 0x1f
00C7F58C  75 10                           jne 0x140c7f59e
00C7F58E  80 79 FE 40                     cmp byte ptr [rcx - 2], 0x40
00C7F592  75 0A                           jne 0x140c7f59e
00C7F594  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F598  0F 84 E3 FE FF FF               je 0x140c7f481
00C7F59E  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7F5A2  75 76                           jne 0x140c7f61a
00C7F5A4  80 79 FB CC                     cmp byte ptr [rcx - 5], 0xcc
00C7F5A8  75 1C                           jne 0x140c7f5c6
00C7F5AA  80 79 FC CC                     cmp byte ptr [rcx - 4], 0xcc
00C7F5AE  75 16                           jne 0x140c7f5c6
00C7F5B0  80 79 FD 0F                     cmp byte ptr [rcx - 3], 0xf
00C7F5B4  75 10                           jne 0x140c7f5c6
00C7F5B6  80 79 FE 1F                     cmp byte ptr [rcx - 2], 0x1f
00C7F5BA  75 0A                           jne 0x140c7f5c6
00C7F5BC  80 79 FF 00                     cmp byte ptr [rcx - 1], 0
00C7F5C0  0F 84 BB FE FF FF               je 0x140c7f481
00C7F5C6  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7F5CA  75 4E                           jne 0x140c7f61a
00C7F5CC  80 79 FB CC                     cmp byte ptr [rcx - 5], 0xcc
00C7F5D0  75 1C                           jne 0x140c7f5ee
00C7F5D2  80 79 FC CC                     cmp byte ptr [rcx - 4], 0xcc
00C7F5D6  75 16                           jne 0x140c7f5ee
00C7F5D8  80 79 FD CC                     cmp byte ptr [rcx - 3], 0xcc
00C7F5DC  75 10                           jne 0x140c7f5ee
00C7F5DE  80 79 FE 66                     cmp byte ptr [rcx - 2], 0x66
00C7F5E2  75 0A                           jne 0x140c7f5ee
00C7F5E4  80 79 FF 90                     cmp byte ptr [rcx - 1], 0x90
00C7F5E8  0F 84 93 FE FF FF               je 0x140c7f481
00C7F5EE  80 79 FA CC                     cmp byte ptr [rcx - 6], 0xcc
00C7F5F2  75 26                           jne 0x140c7f61a
00C7F5F4  80 79 FB CC                     cmp byte ptr [rcx - 5], 0xcc
00C7F5F8  75 20                           jne 0x140c7f61a
00C7F5FA  80 79 FC CC                     cmp byte ptr [rcx - 4], 0xcc
00C7F5FE  75 1A                           jne 0x140c7f61a
00C7F600  80 79 FD CC                     cmp byte ptr [rcx - 3], 0xcc
00C7F604  75 14                           jne 0x140c7f61a
00C7F606  80 79 FE CC                     cmp byte ptr [rcx - 2], 0xcc
00C7F60A  75 0E                           jne 0x140c7f61a
00C7F60C  33 C0                           xor eax, eax
00C7F60E  80 79 FF 90                     cmp byte ptr [rcx - 1], 0x90
00C7F612  44 0F 44 C8                     cmove r9d, eax
00C7F616  44 89 4D 34                     mov dword ptr [rbp + 0x34], r9d
00C7F61A  45 85 C9                        test r9d, r9d
00C7F61D  75 0D                           jne 0x140c7f62c
00C7F61F  C7 41 FA 4C 87 00 98            mov dword ptr [rcx - 6], 0x9800874c
00C7F626  66 C7 41 FE C3 90               mov word ptr [rcx - 2], 0x90c3
00C7F62C  8B 7B 04                        mov edi, dword ptr [rbx + 4]
00C7F62F  89 BD A0 00 00 00               mov dword ptr [rbp + 0xa0], edi
00C7F635  48 83 C3 0C                     add rbx, 0xc
00C7F639  48 89 9D 40 01 00 00            mov qword ptr [rbp + 0x140], rbx
00C7F640  49 3B DC                        cmp rbx, r12
00C7F643  74 2C                           je 0x140c7f671
00C7F645  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
00C7F649  39 03                           cmp dword ptr [rbx], eax
00C7F64B  72 0A                           jb 0x140c7f657
00C7F64D  44 39 53 04                     cmp dword ptr [rbx + 4], r10d
00C7F651  0F 86 D4 FD FF FF               jbe 0x140c7f42b
00C7F657  44 8B 03                        mov r8d, dword ptr [rbx]
00C7F65A  49 8B D6                        mov rdx, r14
00C7F65D  49 8B CF                        mov rcx, r15
00C7F660  E8 8B 36 7B FF                  call 0x140432cf0
00C7F665  48 85 C0                        test rax, rax
00C7F668  4C 8B C0                        mov r8, rax
00C7F66B  0F 85 73 FB FF FF               jne 0x140c7f1e4
00C7F671  C7 05 D1 8F 38 00 01 00 00 00   mov dword ptr [rip + 0x388fd1], 1
00C7F67B  0F 31                           rdtsc
00C7F67D  48 C1 E2 20                     shl rdx, 0x20
00C7F681  48 0B C2                        or rax, rdx
00C7F684  48 8B D0                        mov rdx, rax
00C7F687  48 8B C8                        mov rcx, rax
00C7F68A  48 C1 C9 03                     ror rcx, 3
00C7F68E  48 33 D1                        xor rdx, rcx
00C7F691  48 B8 01 20 00 04 80 00 10 70   movabs rax, 0x7010008004002001
00C7F69B  48 F7 E2                        mul rdx
00C7F69E  48 8B CA                        mov rcx, rdx
00C7F6A1  48 33 C8                        xor rcx, rax
00C7F6A4  48 B8 CD CC CC CC CC CC CC CC   movabs rax, 0xcccccccccccccccd
00C7F6AE  48 F7 E1                        mul rcx
00C7F6B1  48 C1 EA 03                     shr rdx, 3
00C7F6B5  48 8D 04 92                     lea rax, [rdx + rdx*4]
00C7F6B9  48 03 C0                        add rax, rax
00C7F6BC  48 2B C8                        sub rcx, rax
00C7F6BF  48 83 F9 01                     cmp rcx, 1
00C7F6C3  73 07                           jae 0x140c7f6cc
00C7F6C5  83 0D 7C 8F 38 00 02            or dword ptr [rip + 0x388f7c], 2
00C7F6CC  0F 31                           rdtsc
00C7F6CE  48 C1 E2 20                     shl rdx, 0x20
00C7F6D2  48 0B C2                        or rax, rdx
00C7F6D5  48 8B D0                        mov rdx, rax
00C7F6D8  48 8B C8                        mov rcx, rax
00C7F6DB  48 C1 C9 03                     ror rcx, 3
00C7F6DF  48 33 D1                        xor rdx, rcx
00C7F6E2  48 B8 01 20 00 04 80 00 10 70   movabs rax, 0x7010008004002001
00C7F6EC  48 F7 E2                        mul rdx
00C7F6EF  48 8B CA                        mov rcx, rdx
00C7F6F2  48 33 C8                        xor rcx, rax
00C7F6F5  48 B8 CD CC CC CC CC CC CC CC   movabs rax, 0xcccccccccccccccd
00C7F6FF  48 F7 E1                        mul rcx
00C7F702  48 C1 EA 03                     shr rdx, 3
00C7F706  48 8D 04 92                     lea rax, [rdx + rdx*4]
00C7F70A  48 03 C0                        add rax, rax
00C7F70D  48 2B C8                        sub rcx, rax
00C7F710  48 83 F9 01                     cmp rcx, 1
00C7F714  73 07                           jae 0x140c7f71d
00C7F716  83 0D 2B 8F 38 00 04            or dword ptr [rip + 0x388f2b], 4
00C7F71D  0F 31                           rdtsc
00C7F71F  48 C1 E2 20                     shl rdx, 0x20
00C7F723  48 0B C2                        or rax, rdx
00C7F726  48 8B D0                        mov rdx, rax
00C7F729  48 8B C8                        mov rcx, rax
00C7F72C  48 C1 C9 03                     ror rcx, 3
00C7F730  48 33 D1                        xor rdx, rcx
00C7F733  48 B8 01 20 00 04 80 00 10 70   movabs rax, 0x7010008004002001
00C7F73D  48 F7 E2                        mul rdx
00C7F740  4C 8B D2                        mov r10, rdx
00C7F743  44 0F B6 0D 91 7E 2C 00         movzx r9d, byte ptr [rip + 0x2c7e91]
00C7F74B  0F B6 0D CA B2 18 00            movzx ecx, byte ptr [rip + 0x18b2ca]
00C7F752  4C 0B C9                        or r9, rcx
00C7F755  4C 33 D0                        xor r10, rax
00C7F758  48 B8 15 AE 47 E1 7A 14 AE 47   movabs rax, 0x47ae147ae147ae15
00C7F762  49 F7 E2                        mul r10
00C7F765  49 8B C2                        mov rax, r10
00C7F768  48 2B C2                        sub rax, rdx
00C7F76B  48 D1 E8                        shr rax, 1
00C7F76E  48 03 C2                        add rax, rdx
00C7F771  48 C1 E8 06                     shr rax, 6
00C7F775  48 6B C0 64                     imul rax, rax, 0x64
00C7F779  4C 2B D0                        sub r10, rax
00C7F77C  4D 3B D1                        cmp r10, r9
00C7F77F  73 1F                           jae 0x140c7f7a0
00C7F781  E8 7A 11 93 FF                  call 0x1405b0900
00C7F786  89 85 A4 00 00 00               mov dword ptr [rbp + 0xa4], eax
00C7F78C  48 8D 15 F1 FA F6 FF            lea rdx, [rip - 0x9050f]
00C7F793  48 8B 8D C8 00 00 00            mov rcx, qword ptr [rbp + 0xc8]
00C7F79A  E8 A1 03 88 FF                  call 0x1404ffb40
00C7F79F  90                              nop
00C7F7A0  48 83 C4 30                     add rsp, 0x30
00C7F7A4  41 5F                           pop r15
00C7F7A6  41 5E                           pop r14
00C7F7A8  41 5C                           pop r12
00C7F7AA  5F                              pop rdi
00C7F7AB  5E                              pop rsi
00C7F7AC  5D                              pop rbp
00C7F7AD  5B                              pop rbx
00C7F7AE  C3                              ret
00C7F7AF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00C7EB3D(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (48);
    v_stack_p10 = *(unsigned __int64 *)(a2 + 72);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3709634))) - 1);
    *(unsigned int *)(v_rip + 3709626) = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3709620))) != 0) goto loc_00C7F7A0;
    a2 = (a2) << (32);
    result = ((unsigned int)(*(unsigned int *)(v_rip + 3709620))) | (a2);
    if (condition_is_above_or_equal) goto loc_00C7EB8E;
    result = 0;
    goto loc_00C7EBDA;
loc_00C7EB8E:
    v_rbx = (result) & (0);
    result = MmMapIoSpaceEx(v_rbx, (unsigned int)(0x1000ULL), 516, a4);
    if (result == 0) {
        *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 376) = 0xE8000009ULL;
        a1 = *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 376);
        a4 = 0;
        a3 = v_rbx;
        a2 = result + 8;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rip + 3708079) = result;
    if ((*(unsigned __int8 *)(result)) == 0) goto loc_00C7EC4D;
    result = KiSwInterruptPresent(a1, a2, a3, a4);
    if (!sign_flag) goto loc_00C7EC4D;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    a1 = (a2) ^ (result);
    a2 = (a2) >> (3);
    result = (a2 + a2 * 4) + (a2 + a2 * 4);
    a1 = (a1) - (result);
    if (a1 < 1) {
        *(unsigned int *)(v_rip + 3707963) = 1;
    }
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
    }
    result = MmStrongCodeGuaranteesEnforced(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
    }
    if ((*(unsigned int *)(v_rip + 3707924)) == 0) goto loc_00C7F67B;
    result = RtlImageNtHeader(v_rip - 13102209, a2, a3, a4);
    result = RtlCaptureImageExceptionValues(v_rip - 13102238, *(unsigned __int64 *)(a2 + 72) + 376, *(unsigned __int64 *)(a2 + 72) + 360, a4);
    a2 = (*(unsigned __int64 *)(a2 + 72) + 376) >> (3);
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360) = (unsigned int)(a2);
    if ((unsigned int)(a2) == 0) goto loc_00C7F172;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 256) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 376);
    v_rdi = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 128) = 0;
    goto loc_00C7F154;
loc_00C7ECED:
    v_rsi = 0;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360 + 36)) & (0x2000000ULL)) != 0) goto loc_00C7EEE9;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360)) != 0x54494E49ULL) goto loc_00C7ED14;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360 + 4)) == 0x4742444BULL) goto loc_00C7EEE9;
loc_00C7ED14:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360)) != 0x45474150ULL) goto loc_00C7ED4D;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 72) + 360 + 4)) == ((unsigned __int16)((unsigned int)(0x7877ULL)))) goto loc_00C7EEE9;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 72) + 360 + 4)) == ((unsigned __int16)((unsigned int)(0x7277ULL)))) goto loc_00C7EEE9;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 72) + 360 + 4)) == ((unsigned __int16)((unsigned int)(0x7777ULL)))) goto loc_00C7EEE9;
loc_00C7ED4D:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360)) != 0x41525245ULL) goto loc_00C7ED66;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 72) + 360 + 4)) == ((unsigned __int16)((unsigned int)(0x4154ULL)))) goto loc_00C7EEE9;
loc_00C7ED66:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 72) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 88) = v_xmm0;
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 104) = 7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 216) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 208) = *(unsigned __int64 *)(a2 + 72) + 360;
loc_00C7ED9C:
    v_r10 = (*(unsigned __int64 *)(a2 + 72) + 360) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 208) = v_r10;
    a4 = (a4) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 216) = a4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 72) + 360)) != (*(unsigned __int8 *)(a4))) goto loc_00C7EDCC;
    v_r11 = (unsigned int)((7) + (-1));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 104) = (unsigned int)(v_r11);
    if (condition_is_not_equal) goto loc_00C7ED9C;
    goto loc_00C7EEE9;
loc_00C7EDCC:
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 56) = 8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 176) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 80);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 168) = *(unsigned __int64 *)(a2 + 72) + 360;
loc_00C7EDEB:
    v_r11 = (*(unsigned __int64 *)(a2 + 72) + 360) + (8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 168) = v_r11;
    v_r10 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 80)) + (8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 176) = v_r10;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 360)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 80)))) goto loc_00C7EE53;
    a4 = (unsigned int)((8) + (-8));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 56) = a4;
    if (a4 >= 8) goto loc_00C7EDEB;
    if (a4 == 0) goto loc_00C7EEE9;
loc_00C7EE23:
    v_r11 = (v_r11) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 168) = v_r11;
    v_r10 = (v_r10) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 176) = v_r10;
    if ((*(unsigned __int8 *)(v_r11)) != (*(unsigned __int8 *)(v_r10))) goto loc_00C7EE53;
    a4 = (unsigned int)((a4) + (-1));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 56) = a4;
    if (condition_is_not_equal) goto loc_00C7EE23;
    goto loc_00C7EEE9;
loc_00C7EE53:
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 112) = 4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 232) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 88);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 224) = *(unsigned __int64 *)(a2 + 72) + 360;
loc_00C7EE72:
    v_r10 = (*(unsigned __int64 *)(a2 + 72) + 360) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 224) = v_r10;
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 88)) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 232) = a4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 72) + 360)) != (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 88)))) goto loc_00C7EE9F;
    v_r11 = (unsigned int)((4) + (-1));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 112) = (unsigned int)(v_r11);
    if (condition_is_not_equal) goto loc_00C7EE72;
    goto loc_00C7EEE9;
loc_00C7EE9F:
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 120) = 6;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 248) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 96);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 240) = *(unsigned __int64 *)(a2 + 72) + 360;
loc_00C7EEBE:
    v_r10 = (*(unsigned __int64 *)(a2 + 72) + 360) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 240) = v_r10;
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 96)) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 248) = a4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 72) + 360)) != (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 96)))) goto loc_00C7EEEE;
    v_r11 = (unsigned int)((6) + (-1));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 120) = (unsigned int)(v_r11);
    if (condition_is_not_equal) goto loc_00C7EEBE;
loc_00C7EEE9:
loc_00C7EEEE:
    if (!sign_flag) goto loc_00C7EEFD;
    goto loc_00C7EF09;
loc_00C7EEFD:
    v_rsi = 1;
    if (condition_is_above_or_equal) { v_rsi = 1; }
loc_00C7EF09:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360 + 16)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360 + 8))))) goto loc_00C7EF19;
    goto loc_00C7EF1B;
loc_00C7EF19:
loc_00C7EF1B:
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360 + 12))) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360 + 8)))))));
loc_00C7EF22:
    a1 = (v_rip - 13102891) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 376))));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 48) = 1;
    if ((unsigned int)(v_rsi) != 0) goto loc_00C7F117;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360 + 12))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 376))))));
    if (((unsigned int)(result)) < 6) goto loc_00C7F117;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 376)))) - (0));
    if (((unsigned int)(a2)) < 6) goto loc_00C7F117;
    if ((*(unsigned __int8 *)(a1 - 6)) != ((unsigned __int8)(v_rsi))) goto loc_00C7EF87;
    if ((*(unsigned __int8 *)(a1 - 5)) != ((unsigned __int8)(v_rsi))) goto loc_00C7EF87;
    if ((*(unsigned __int8 *)(a1 - 4)) != ((unsigned __int8)(v_rsi))) goto loc_00C7EF87;
    if ((*(unsigned __int8 *)(a1 - 3)) != ((unsigned __int8)(v_rsi))) goto loc_00C7EF87;
    if ((*(unsigned __int8 *)(a1 - 2)) != ((unsigned __int8)(v_rsi))) goto loc_00C7EF87;
    if ((*(unsigned __int8 *)(a1 - 1)) != ((unsigned __int8)(v_rsi))) goto loc_00C7EF87;
loc_00C7EF7E:
    goto loc_00C7F11C;
loc_00C7EF87:
    if ((*(unsigned __int8 *)(a1 - 6)) != 132) goto loc_00C7EFAB;
    if ((*(unsigned __int8 *)(a1 - 5)) != 0) goto loc_00C7EFAB;
    if ((*(unsigned __int8 *)(a1 - 4)) != 0) goto loc_00C7EFAB;
    if ((*(unsigned __int8 *)(a1 - 3)) != 0) goto loc_00C7EFAB;
    if ((*(unsigned __int8 *)(a1 - 2)) != 0) goto loc_00C7EFAB;
    if ((*(unsigned __int8 *)(a1 - 1)) == 0) goto loc_00C7EF7E;
loc_00C7EFAB:
    if ((*(unsigned __int8 *)(a1 - 6)) != 204) goto loc_00C7EFCF;
    if ((*(unsigned __int8 *)(a1 - 5)) != 204) goto loc_00C7EFCF;
    if ((*(unsigned __int8 *)(a1 - 4)) != 204) goto loc_00C7EFCF;
    if ((*(unsigned __int8 *)(a1 - 3)) != 204) goto loc_00C7EFCF;
    if ((*(unsigned __int8 *)(a1 - 2)) != 204) goto loc_00C7EFCF;
    if ((*(unsigned __int8 *)(a1 - 1)) == 204) goto loc_00C7EF7E;
loc_00C7EFCF:
    if ((*(unsigned __int8 *)(a1 - 6)) != 31) goto loc_00C7F01B;
    if ((*(unsigned __int8 *)(a1 - 5)) != 132) goto loc_00C7EFF3;
    if ((*(unsigned __int8 *)(a1 - 4)) != 0) goto loc_00C7EFF3;
    if ((*(unsigned __int8 *)(a1 - 3)) != 0) goto loc_00C7EFF3;
    if ((*(unsigned __int8 *)(a1 - 2)) != 0) goto loc_00C7EFF3;
    if ((*(unsigned __int8 *)(a1 - 1)) == 0) goto loc_00C7EF7E;
loc_00C7EFF3:
    if ((*(unsigned __int8 *)(a1 - 6)) != 31) goto loc_00C7F01B;
    if ((*(unsigned __int8 *)(a1 - 5)) != 128) goto loc_00C7F01B;
    if ((*(unsigned __int8 *)(a1 - 4)) != 0) goto loc_00C7F01B;
    if ((*(unsigned __int8 *)(a1 - 3)) != 0) goto loc_00C7F01B;
    if ((*(unsigned __int8 *)(a1 - 2)) != 0) goto loc_00C7F01B;
    if ((*(unsigned __int8 *)(a1 - 1)) == 0) goto loc_00C7EF7E;
loc_00C7F01B:
    if ((*(unsigned __int8 *)(a1 - 6)) != 102) goto loc_00C7F043;
    if ((*(unsigned __int8 *)(a1 - 5)) != 15) goto loc_00C7F043;
    if ((*(unsigned __int8 *)(a1 - 4)) != 31) goto loc_00C7F043;
    if ((*(unsigned __int8 *)(a1 - 3)) != 68) goto loc_00C7F043;
    if ((*(unsigned __int8 *)(a1 - 2)) != 0) goto loc_00C7F043;
    if ((*(unsigned __int8 *)(a1 - 1)) == 0) goto loc_00C7EF7E;
loc_00C7F043:
    if ((*(unsigned __int8 *)(a1 - 6)) != 204) goto loc_00C7F117;
    if ((*(unsigned __int8 *)(a1 - 5)) != 15) goto loc_00C7F06F;
    if ((*(unsigned __int8 *)(a1 - 4)) != 31) goto loc_00C7F06F;
    if ((*(unsigned __int8 *)(a1 - 3)) != 68) goto loc_00C7F06F;
    if ((*(unsigned __int8 *)(a1 - 2)) != 0) goto loc_00C7F06F;
    if ((*(unsigned __int8 *)(a1 - 1)) == 0) goto loc_00C7EF7E;
loc_00C7F06F:
    if ((*(unsigned __int8 *)(a1 - 6)) != 204) goto loc_00C7F117;
    if ((*(unsigned __int8 *)(a1 - 5)) != 204) goto loc_00C7F09B;
    if ((*(unsigned __int8 *)(a1 - 4)) != 15) goto loc_00C7F09B;
    if ((*(unsigned __int8 *)(a1 - 3)) != 31) goto loc_00C7F09B;
    if ((*(unsigned __int8 *)(a1 - 2)) != 64) goto loc_00C7F09B;
    if ((*(unsigned __int8 *)(a1 - 1)) == 0) goto loc_00C7EF7E;
loc_00C7F09B:
    if ((*(unsigned __int8 *)(a1 - 6)) != 204) goto loc_00C7F117;
    if ((*(unsigned __int8 *)(a1 - 5)) != 204) goto loc_00C7F0C3;
    if ((*(unsigned __int8 *)(a1 - 4)) != 204) goto loc_00C7F0C3;
    if ((*(unsigned __int8 *)(a1 - 3)) != 15) goto loc_00C7F0C3;
    if ((*(unsigned __int8 *)(a1 - 2)) != 31) goto loc_00C7F0C3;
    if ((*(unsigned __int8 *)(a1 - 1)) == 0) goto loc_00C7EF7E;
loc_00C7F0C3:
    if ((*(unsigned __int8 *)(a1 - 6)) != 204) goto loc_00C7F117;
    if ((*(unsigned __int8 *)(a1 - 5)) != 204) goto loc_00C7F0EB;
    if ((*(unsigned __int8 *)(a1 - 4)) != 204) goto loc_00C7F0EB;
    if ((*(unsigned __int8 *)(a1 - 3)) != 204) goto loc_00C7F0EB;
    if ((*(unsigned __int8 *)(a1 - 2)) != 102) goto loc_00C7F0EB;
    if ((*(unsigned __int8 *)(a1 - 1)) == 144) goto loc_00C7EF7E;
loc_00C7F0EB:
    if ((*(unsigned __int8 *)(a1 - 6)) != 204) goto loc_00C7F117;
    if ((*(unsigned __int8 *)(a1 - 5)) != 204) goto loc_00C7F117;
    if ((*(unsigned __int8 *)(a1 - 4)) != 204) goto loc_00C7F117;
    if ((*(unsigned __int8 *)(a1 - 3)) != 204) goto loc_00C7F117;
    if ((*(unsigned __int8 *)(a1 - 2)) == 204) {
        result = 0;
        a4 = 1;
        if ((*(unsigned __int8 *)(a1 - 1)) == 144) { a4 = 0; }
        *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 48) = a4;
    }
    if (a4 == 0) {
        *(unsigned int *)(a1 - 6) = 0x9800874CULL;
        *(unsigned __int16 *)(a1 - 2) = 0x90C3ULL;
    }
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 128) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 376) + 4)));
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 376)) + (12);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 256) = v_rbx;
    if (v_rbx == (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 376) + (unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 2 * 4)) goto loc_00C7F172;
    if ((*(unsigned int *)(v_rbx)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 360 + 12))))) goto loc_00C7F154;
    if ((*(unsigned int *)(v_rbx + 4)) <= ((unsigned int)(v_r10))) goto loc_00C7EF22;
loc_00C7F154:
    result = RtlSectionTableFromVirtualAddress(0, v_rip - 13103454, (unsigned int)(*(unsigned int *)(v_rbx)), a4);
    if (result != 0) goto loc_00C7ECED;
loc_00C7F172:
    result = RtlImageNtHeader(*(unsigned __int64 *)(v_rip + 3439135), v_rip - 13103454, result, a4);
    result = RtlCaptureImageExceptionValues(*(unsigned __int64 *)(v_rip + 3439135), *(unsigned __int64 *)(a2 + 72) + 264, *(unsigned __int64 *)(a2 + 72) + 368, a4);
    a2 = (*(unsigned __int64 *)(a2 + 72) + 264) >> (3);
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368) = (unsigned int)(a2);
    if ((unsigned int)(a2) == 0) goto loc_00C7F671;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 320) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264);
    v_rdi = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 160) = 0;
    goto loc_00C7F657;
loc_00C7F1E4:
    v_rsi = 0;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368 + 36)) & (0x2000000ULL)) != 0) goto loc_00C7F3F2;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368)) != 0x54494E49ULL) goto loc_00C7F20B;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368 + 4)) == 0x4742444BULL) goto loc_00C7F3F2;
loc_00C7F20B:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368)) != 0x45474150ULL) goto loc_00C7F244;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 72) + 368 + 4)) == ((unsigned __int16)((unsigned int)(0x7877ULL)))) goto loc_00C7F3F2;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 72) + 368 + 4)) == ((unsigned __int16)((unsigned int)(0x7277ULL)))) goto loc_00C7F3F2;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 72) + 368 + 4)) == ((unsigned __int16)((unsigned int)(0x7777ULL)))) goto loc_00C7F3F2;
loc_00C7F244:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368)) != 0x41525245ULL) goto loc_00C7F25D;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 72) + 368 + 4)) == ((unsigned __int16)((unsigned int)(0x4154ULL)))) goto loc_00C7F3F2;
loc_00C7F25D:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 72) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 88) = v_xmm0;
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 136) = 7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 280) = a4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 272) = *(unsigned __int64 *)(a2 + 72) + 368;
loc_00C7F296:
    v_r10 = (*(unsigned __int64 *)(a2 + 72) + 368) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 272) = v_r10;
    a4 = (a4) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 280) = a4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 72) + 368)) != (*(unsigned __int8 *)(a4))) goto loc_00C7F2C9;
    v_r11 = (unsigned int)((7) + (-1));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 136) = (unsigned int)(v_r11);
    if (condition_is_not_equal) goto loc_00C7F296;
    goto loc_00C7F3F2;
loc_00C7F2C9:
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 64) = 8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 192) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 80);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 184) = *(unsigned __int64 *)(a2 + 72) + 368;
loc_00C7F2E8:
    v_r11 = (*(unsigned __int64 *)(a2 + 72) + 368) + (8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 184) = v_r11;
    v_r10 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 80)) + (8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 192) = v_r10;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 368)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 80)))) goto loc_00C7F350;
    a4 = (unsigned int)((8) + (-8));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 64) = a4;
    if (a4 >= 8) goto loc_00C7F2E8;
    if (a4 == 0) goto loc_00C7F3F2;
loc_00C7F320:
    v_r11 = (v_r11) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 184) = v_r11;
    v_r10 = (v_r10) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 192) = v_r10;
    if ((*(unsigned __int8 *)(v_r11)) != (*(unsigned __int8 *)(v_r10))) goto loc_00C7F350;
    a4 = (unsigned int)((a4) + (-1));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 64) = a4;
    if (condition_is_not_equal) goto loc_00C7F320;
    goto loc_00C7F3F2;
loc_00C7F350:
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 144) = 4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 296) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 88);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 288) = *(unsigned __int64 *)(a2 + 72) + 368;
loc_00C7F372:
    v_r10 = (*(unsigned __int64 *)(a2 + 72) + 368) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 288) = v_r10;
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 88)) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 296) = a4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 72) + 368)) != (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 88)))) goto loc_00C7F3A2;
    v_r11 = (unsigned int)((4) + (-1));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 144) = (unsigned int)(v_r11);
    if (condition_is_not_equal) goto loc_00C7F372;
    goto loc_00C7F3F2;
loc_00C7F3A2:
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 152) = 6;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 312) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 96);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 304) = *(unsigned __int64 *)(a2 + 72) + 368;
loc_00C7F3C4:
    v_r10 = (*(unsigned __int64 *)(a2 + 72) + 368) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 304) = v_r10;
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 96)) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 312) = a4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 72) + 368)) != (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 96)))) goto loc_00C7F3F7;
    v_r11 = (unsigned int)((6) + (-1));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 152) = (unsigned int)(v_r11);
    if (condition_is_not_equal) goto loc_00C7F3C4;
loc_00C7F3F2:
loc_00C7F3F7:
    if (!sign_flag) goto loc_00C7F406;
    goto loc_00C7F412;
loc_00C7F406:
    v_rsi = 1;
    if (condition_is_above_or_equal) { v_rsi = 1; }
loc_00C7F412:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368 + 16)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368 + 8))))) goto loc_00C7F422;
    goto loc_00C7F424;
loc_00C7F422:
loc_00C7F424:
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368 + 12))) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368 + 8)))))));
loc_00C7F42B:
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 52) = 1;
    if ((unsigned int)(v_rsi) != 0) goto loc_00C7F61A;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368 + 12))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))))));
    if (((unsigned int)(result)) < 6) goto loc_00C7F61A;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264)))) - (0));
    if (((unsigned int)(a2)) < 6) goto loc_00C7F61A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6)) != ((unsigned __int8)(v_rsi))) goto loc_00C7F48A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 5)) != ((unsigned __int8)(v_rsi))) goto loc_00C7F48A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 4)) != ((unsigned __int8)(v_rsi))) goto loc_00C7F48A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 3)) != ((unsigned __int8)(v_rsi))) goto loc_00C7F48A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2)) != ((unsigned __int8)(v_rsi))) goto loc_00C7F48A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 1)) != ((unsigned __int8)(v_rsi))) goto loc_00C7F48A;
loc_00C7F481:
    goto loc_00C7F61F;
loc_00C7F48A:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6)) != 132) goto loc_00C7F4AE;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 5)) != 0) goto loc_00C7F4AE;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 4)) != 0) goto loc_00C7F4AE;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 3)) != 0) goto loc_00C7F4AE;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2)) != 0) goto loc_00C7F4AE;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 1)) == 0) goto loc_00C7F481;
loc_00C7F4AE:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6)) != 204) goto loc_00C7F4D2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 5)) != 204) goto loc_00C7F4D2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 4)) != 204) goto loc_00C7F4D2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 3)) != 204) goto loc_00C7F4D2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2)) != 204) goto loc_00C7F4D2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 1)) == 204) goto loc_00C7F481;
loc_00C7F4D2:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6)) != 31) goto loc_00C7F51E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 5)) != 132) goto loc_00C7F4F6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 4)) != 0) goto loc_00C7F4F6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 3)) != 0) goto loc_00C7F4F6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2)) != 0) goto loc_00C7F4F6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 1)) == 0) goto loc_00C7F481;
loc_00C7F4F6:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6)) != 31) goto loc_00C7F51E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 5)) != 128) goto loc_00C7F51E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 4)) != 0) goto loc_00C7F51E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 3)) != 0) goto loc_00C7F51E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2)) != 0) goto loc_00C7F51E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 1)) == 0) goto loc_00C7F481;
loc_00C7F51E:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6)) != 102) goto loc_00C7F546;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 5)) != 15) goto loc_00C7F546;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 4)) != 31) goto loc_00C7F546;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 3)) != 68) goto loc_00C7F546;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2)) != 0) goto loc_00C7F546;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 1)) == 0) goto loc_00C7F481;
loc_00C7F546:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6)) != 204) goto loc_00C7F61A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 5)) != 15) goto loc_00C7F572;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 4)) != 31) goto loc_00C7F572;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 3)) != 68) goto loc_00C7F572;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2)) != 0) goto loc_00C7F572;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 1)) == 0) goto loc_00C7F481;
loc_00C7F572:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6)) != 204) goto loc_00C7F61A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 5)) != 204) goto loc_00C7F59E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 4)) != 15) goto loc_00C7F59E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 3)) != 31) goto loc_00C7F59E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2)) != 64) goto loc_00C7F59E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 1)) == 0) goto loc_00C7F481;
loc_00C7F59E:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6)) != 204) goto loc_00C7F61A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 5)) != 204) goto loc_00C7F5C6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 4)) != 204) goto loc_00C7F5C6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 3)) != 15) goto loc_00C7F5C6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2)) != 31) goto loc_00C7F5C6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 1)) == 0) goto loc_00C7F481;
loc_00C7F5C6:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6)) != 204) goto loc_00C7F61A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 5)) != 204) goto loc_00C7F5EE;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 4)) != 204) goto loc_00C7F5EE;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 3)) != 204) goto loc_00C7F5EE;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2)) != 102) goto loc_00C7F5EE;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 1)) == 144) goto loc_00C7F481;
loc_00C7F5EE:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6)) != 204) goto loc_00C7F61A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 5)) != 204) goto loc_00C7F61A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 4)) != 204) goto loc_00C7F61A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 3)) != 204) goto loc_00C7F61A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2)) == 204) {
        result = 0;
        a4 = 1;
        if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 1)) == 144) { a4 = 0; }
        *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 52) = a4;
    }
    if (a4 == 0) {
        *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 6) = 0x9800874CULL;
        *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3439135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264))) * 1 - 2) = 0x90C3ULL;
    }
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 160) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264) + 4)));
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264)) + (12);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 320) = v_rbx;
    if (v_rbx == (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 264) + (unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 2 * 4)) goto loc_00C7F671;
    if ((*(unsigned int *)(v_rbx)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 368 + 12))))) goto loc_00C7F657;
    if ((*(unsigned int *)(v_rbx + 4)) <= ((unsigned int)(v_r10))) goto loc_00C7F42B;
loc_00C7F657:
    result = RtlSectionTableFromVirtualAddress(0, *(unsigned __int64 *)(v_rip + 3439135), (unsigned int)(*(unsigned int *)(v_rbx)), a4);
    if (result != 0) goto loc_00C7F1E4;
loc_00C7F671:
    *(unsigned int *)(v_rip + 3706833) = 1;
loc_00C7F67B:
    a2 = (*(unsigned __int64 *)(v_rip + 3439135)) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    a1 = (a2) ^ (result);
    a2 = (a2) >> (3);
    result = (a2 + a2 * 4) + (a2 + a2 * 4);
    a1 = (a1) - (result);
    if (a1 < 1) {
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    a1 = (a2) ^ (result);
    a2 = (a2) >> (3);
    result = (a2 + a2 * 4) + (a2 + a2 * 4);
    a1 = (a1) - (result);
    if (a1 < 1) {
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    a4 = (*(unsigned __int8 *)(v_rip + 2915985)) | (*(unsigned __int8 *)(v_rip + 1618634));
    v_r10 = (a2) ^ (result);
    result = (v_r10) - (a2);
    result = (result) >> (1);
    result = (result) + (a2);
    result = (result) >> (6);
    result = (result) * (result);
    v_r10 = (v_r10) - (result);
    if (v_r10 < a4) {
        result = KdDisableDebugger(*(unsigned __int8 *)(v_rip + 1618634), a2, result, a4);
        *(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 164) = (unsigned int)(result);
        a2 = v_rip - 591119;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 200);
        result = local_unwind(a1, a2, result, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00C7EB3D(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (48);
    v_stack_p10 = *(uint64_t *)(arg2 + 0x48);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x389AC2))) - 1);
    *(uint32_t *)(v_rip + 0x389ABA) = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x389AB4))) != 0) goto loc_00C7F7A0;
    Arg2 = (Arg2) << (32);
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x389AB4))) | (Arg2);
    if (condition_is_above_or_equal) goto loc_00C7EB8E;
    result = 0;
    goto loc_00C7EBDA;
loc_00C7EB8E:
    local_rbx = (result) & (0);
    result = MmMapIoSpaceEx(local_rbx, (uint32_t)(0x1000ULL), 516, Arg4);
    if (result == 0) {
        *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x178) = 0xE8000009ULL;
        Arg1 = *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x178);
        Arg4 = 0;
        Arg3 = local_rbx;
        Arg2 = result + 8;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(v_rip + 0x3894AF) = result;
    if ((*(uint8_t *)(result)) == 0) goto loc_00C7EC4D;
    result = KiSwInterruptPresent(Arg1, Arg2, Arg3, Arg4);
    if (!sign_flag) goto loc_00C7EC4D;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    Arg1 = (Arg2) ^ (result);
    Arg2 = (Arg2) >> (3);
    result = (Arg2 + Arg2 * 4) + (Arg2 + Arg2 * 4);
    Arg1 = (Arg1) - (result);
    if (Arg1 < 1) {
        *(uint32_t *)(v_rip + 0x38943B) = 1;
    }
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) {
    }
    result = MmStrongCodeGuaranteesEnforced(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) {
    }
    if ((*(uint32_t *)(v_rip + 0x389414)) == 0) goto loc_00C7F67B;
    result = RtlImageNtHeader(v_rip - 13102209, Arg2, Arg3, Arg4);
    result = RtlCaptureImageExceptionValues(v_rip - 13102238, *(uint64_t *)(arg2 + 0x48) + 376, *(uint64_t *)(arg2 + 0x48) + 360, Arg4);
    Arg2 = (*(uint64_t *)(arg2 + 0x48) + 376) >> (3);
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168) = (uint32_t)(Arg2);
    if ((uint32_t)(Arg2) == 0) goto loc_00C7F172;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x100) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x178);
    local_rdi = 0;
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x80) = 0;
    goto loc_00C7F154;
loc_00C7ECED:
    local_rsi = 0;
    if (((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0x24)) & (0x2000000ULL)) != 0) goto loc_00C7EEE9;
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168)) != 0x54494E49ULL) goto loc_00C7ED14;
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0x4)) == 0x4742444BULL) goto loc_00C7EEE9;
loc_00C7ED14:
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168)) != 0x45474150ULL) goto loc_00C7ED4D;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0x4)) == ((uint16_t)((uint32_t)(0x7877ULL)))) goto loc_00C7EEE9;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0x4)) == ((uint16_t)((uint32_t)(0x7277ULL)))) goto loc_00C7EEE9;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0x4)) == ((uint16_t)((uint32_t)(0x7777ULL)))) goto loc_00C7EEE9;
loc_00C7ED4D:
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168)) != 0x41525245ULL) goto loc_00C7ED66;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0x4)) == ((uint16_t)((uint32_t)(0x4154ULL)))) goto loc_00C7EEE9;
loc_00C7ED66:
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x48) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x58) = v_xmm0;
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x68) = 7;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xD8) = 0;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xD0) = *(uint64_t *)(arg2 + 0x48) + 360;
loc_00C7ED9C:
    local_r10 = (*(uint64_t *)(arg2 + 0x48) + 360) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xD0) = local_r10;
    Arg4 = (Arg4) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xD8) = Arg4;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168)) != (*(uint8_t *)(Arg4))) goto loc_00C7EDCC;
    local_r11 = (uint32_t)((7) + (-1));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x68) = (uint32_t)(local_r11);
    if (condition_is_not_equal) goto loc_00C7ED9C;
    goto loc_00C7EEE9;
loc_00C7EDCC:
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x38) = 8;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xB0) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x50);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xA8) = *(uint64_t *)(arg2 + 0x48) + 360;
loc_00C7EDEB:
    local_r11 = (*(uint64_t *)(arg2 + 0x48) + 360) + (8);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xA8) = local_r11;
    local_r10 = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x50)) + (8);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xB0) = local_r10;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x50)))) goto loc_00C7EE53;
    Arg4 = (uint32_t)((8) + (-8));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x38) = Arg4;
    if (Arg4 >= 8) goto loc_00C7EDEB;
    if (Arg4 == 0) goto loc_00C7EEE9;
loc_00C7EE23:
    local_r11 = (local_r11) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xA8) = local_r11;
    local_r10 = (local_r10) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xB0) = local_r10;
    if ((*(uint8_t *)(local_r11)) != (*(uint8_t *)(local_r10))) goto loc_00C7EE53;
    Arg4 = (uint32_t)((Arg4) + (-1));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x38) = Arg4;
    if (condition_is_not_equal) goto loc_00C7EE23;
    goto loc_00C7EEE9;
loc_00C7EE53:
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x70) = 4;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xE8) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x58);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xE0) = *(uint64_t *)(arg2 + 0x48) + 360;
loc_00C7EE72:
    local_r10 = (*(uint64_t *)(arg2 + 0x48) + 360) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xE0) = local_r10;
    Arg4 = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x58)) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xE8) = Arg4;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168)) != (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x58)))) goto loc_00C7EE9F;
    local_r11 = (uint32_t)((4) + (-1));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x70) = (uint32_t)(local_r11);
    if (condition_is_not_equal) goto loc_00C7EE72;
    goto loc_00C7EEE9;
loc_00C7EE9F:
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x78) = 6;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xF8) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x60);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xF0) = *(uint64_t *)(arg2 + 0x48) + 360;
loc_00C7EEBE:
    local_r10 = (*(uint64_t *)(arg2 + 0x48) + 360) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xF0) = local_r10;
    Arg4 = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x60)) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xF8) = Arg4;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168)) != (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x60)))) goto loc_00C7EEEE;
    local_r11 = (uint32_t)((6) + (-1));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x78) = (uint32_t)(local_r11);
    if (condition_is_not_equal) goto loc_00C7EEBE;
loc_00C7EEE9:
loc_00C7EEEE:
    if (!sign_flag) goto loc_00C7EEFD;
    goto loc_00C7EF09;
loc_00C7EEFD:
    local_rsi = 1;
    if (condition_is_above_or_equal) { local_rsi = 1; }
loc_00C7EF09:
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0x10)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0x8))))) goto loc_00C7EF19;
    goto loc_00C7EF1B;
loc_00C7EF19:
loc_00C7EF1B:
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0xC))) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0x8)))))));
loc_00C7EF22:
    Arg1 = (v_rip - 13102891) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x178))));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x30) = 1;
    if ((uint32_t)(local_rsi) != 0) goto loc_00C7F117;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0xC))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x178))))));
    if (((uint32_t)(result)) < 6) goto loc_00C7F117;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x178)))) - (0));
    if (((uint32_t)(Arg2)) < 6) goto loc_00C7F117;
    if ((*(uint8_t *)(Arg1 - 0x6)) != ((uint8_t)(local_rsi))) goto loc_00C7EF87;
    if ((*(uint8_t *)(Arg1 - 0x5)) != ((uint8_t)(local_rsi))) goto loc_00C7EF87;
    if ((*(uint8_t *)(Arg1 - 0x4)) != ((uint8_t)(local_rsi))) goto loc_00C7EF87;
    if ((*(uint8_t *)(Arg1 - 0x3)) != ((uint8_t)(local_rsi))) goto loc_00C7EF87;
    if ((*(uint8_t *)(Arg1 - 0x2)) != ((uint8_t)(local_rsi))) goto loc_00C7EF87;
    if ((*(uint8_t *)(Arg1 - 0x1)) != ((uint8_t)(local_rsi))) goto loc_00C7EF87;
loc_00C7EF7E:
    goto loc_00C7F11C;
loc_00C7EF87:
    if ((*(uint8_t *)(Arg1 - 0x6)) != 132) goto loc_00C7EFAB;
    if ((*(uint8_t *)(Arg1 - 0x5)) != 0) goto loc_00C7EFAB;
    if ((*(uint8_t *)(Arg1 - 0x4)) != 0) goto loc_00C7EFAB;
    if ((*(uint8_t *)(Arg1 - 0x3)) != 0) goto loc_00C7EFAB;
    if ((*(uint8_t *)(Arg1 - 0x2)) != 0) goto loc_00C7EFAB;
    if ((*(uint8_t *)(Arg1 - 0x1)) == 0) goto loc_00C7EF7E;
loc_00C7EFAB:
    if ((*(uint8_t *)(Arg1 - 0x6)) != 204) goto loc_00C7EFCF;
    if ((*(uint8_t *)(Arg1 - 0x5)) != 204) goto loc_00C7EFCF;
    if ((*(uint8_t *)(Arg1 - 0x4)) != 204) goto loc_00C7EFCF;
    if ((*(uint8_t *)(Arg1 - 0x3)) != 204) goto loc_00C7EFCF;
    if ((*(uint8_t *)(Arg1 - 0x2)) != 204) goto loc_00C7EFCF;
    if ((*(uint8_t *)(Arg1 - 0x1)) == 204) goto loc_00C7EF7E;
loc_00C7EFCF:
    if ((*(uint8_t *)(Arg1 - 0x6)) != 31) goto loc_00C7F01B;
    if ((*(uint8_t *)(Arg1 - 0x5)) != 132) goto loc_00C7EFF3;
    if ((*(uint8_t *)(Arg1 - 0x4)) != 0) goto loc_00C7EFF3;
    if ((*(uint8_t *)(Arg1 - 0x3)) != 0) goto loc_00C7EFF3;
    if ((*(uint8_t *)(Arg1 - 0x2)) != 0) goto loc_00C7EFF3;
    if ((*(uint8_t *)(Arg1 - 0x1)) == 0) goto loc_00C7EF7E;
loc_00C7EFF3:
    if ((*(uint8_t *)(Arg1 - 0x6)) != 31) goto loc_00C7F01B;
    if ((*(uint8_t *)(Arg1 - 0x5)) != 128) goto loc_00C7F01B;
    if ((*(uint8_t *)(Arg1 - 0x4)) != 0) goto loc_00C7F01B;
    if ((*(uint8_t *)(Arg1 - 0x3)) != 0) goto loc_00C7F01B;
    if ((*(uint8_t *)(Arg1 - 0x2)) != 0) goto loc_00C7F01B;
    if ((*(uint8_t *)(Arg1 - 0x1)) == 0) goto loc_00C7EF7E;
loc_00C7F01B:
    if ((*(uint8_t *)(Arg1 - 0x6)) != 102) goto loc_00C7F043;
    if ((*(uint8_t *)(Arg1 - 0x5)) != 15) goto loc_00C7F043;
    if ((*(uint8_t *)(Arg1 - 0x4)) != 31) goto loc_00C7F043;
    if ((*(uint8_t *)(Arg1 - 0x3)) != 68) goto loc_00C7F043;
    if ((*(uint8_t *)(Arg1 - 0x2)) != 0) goto loc_00C7F043;
    if ((*(uint8_t *)(Arg1 - 0x1)) == 0) goto loc_00C7EF7E;
loc_00C7F043:
    if ((*(uint8_t *)(Arg1 - 0x6)) != 204) goto loc_00C7F117;
    if ((*(uint8_t *)(Arg1 - 0x5)) != 15) goto loc_00C7F06F;
    if ((*(uint8_t *)(Arg1 - 0x4)) != 31) goto loc_00C7F06F;
    if ((*(uint8_t *)(Arg1 - 0x3)) != 68) goto loc_00C7F06F;
    if ((*(uint8_t *)(Arg1 - 0x2)) != 0) goto loc_00C7F06F;
    if ((*(uint8_t *)(Arg1 - 0x1)) == 0) goto loc_00C7EF7E;
loc_00C7F06F:
    if ((*(uint8_t *)(Arg1 - 0x6)) != 204) goto loc_00C7F117;
    if ((*(uint8_t *)(Arg1 - 0x5)) != 204) goto loc_00C7F09B;
    if ((*(uint8_t *)(Arg1 - 0x4)) != 15) goto loc_00C7F09B;
    if ((*(uint8_t *)(Arg1 - 0x3)) != 31) goto loc_00C7F09B;
    if ((*(uint8_t *)(Arg1 - 0x2)) != 64) goto loc_00C7F09B;
    if ((*(uint8_t *)(Arg1 - 0x1)) == 0) goto loc_00C7EF7E;
loc_00C7F09B:
    if ((*(uint8_t *)(Arg1 - 0x6)) != 204) goto loc_00C7F117;
    if ((*(uint8_t *)(Arg1 - 0x5)) != 204) goto loc_00C7F0C3;
    if ((*(uint8_t *)(Arg1 - 0x4)) != 204) goto loc_00C7F0C3;
    if ((*(uint8_t *)(Arg1 - 0x3)) != 15) goto loc_00C7F0C3;
    if ((*(uint8_t *)(Arg1 - 0x2)) != 31) goto loc_00C7F0C3;
    if ((*(uint8_t *)(Arg1 - 0x1)) == 0) goto loc_00C7EF7E;
loc_00C7F0C3:
    if ((*(uint8_t *)(Arg1 - 0x6)) != 204) goto loc_00C7F117;
    if ((*(uint8_t *)(Arg1 - 0x5)) != 204) goto loc_00C7F0EB;
    if ((*(uint8_t *)(Arg1 - 0x4)) != 204) goto loc_00C7F0EB;
    if ((*(uint8_t *)(Arg1 - 0x3)) != 204) goto loc_00C7F0EB;
    if ((*(uint8_t *)(Arg1 - 0x2)) != 102) goto loc_00C7F0EB;
    if ((*(uint8_t *)(Arg1 - 0x1)) == 144) goto loc_00C7EF7E;
loc_00C7F0EB:
    if ((*(uint8_t *)(Arg1 - 0x6)) != 204) goto loc_00C7F117;
    if ((*(uint8_t *)(Arg1 - 0x5)) != 204) goto loc_00C7F117;
    if ((*(uint8_t *)(Arg1 - 0x4)) != 204) goto loc_00C7F117;
    if ((*(uint8_t *)(Arg1 - 0x3)) != 204) goto loc_00C7F117;
    if ((*(uint8_t *)(Arg1 - 0x2)) == 204) {
        result = 0;
        Arg4 = 1;
        if ((*(uint8_t *)(Arg1 - 0x1)) == 144) { Arg4 = 0; }
        *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x30) = Arg4;
    }
    if (Arg4 == 0) {
        *(uint32_t *)(Arg1 - 0x6) = 0x9800874CULL;
        *(uint16_t *)(Arg1 - 0x2) = 0x90C3ULL;
    }
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x80) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x178) + 0x4)));
    local_rbx = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x178)) + (12);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x100) = local_rbx;
    if (local_rbx == (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x178) + (uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 2 * 4)) goto loc_00C7F172;
    if ((*(uint32_t *)(local_rbx)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x168 + 0xC))))) goto loc_00C7F154;
    if ((*(uint32_t *)(local_rbx + 0x4)) <= ((uint32_t)(local_r10))) goto loc_00C7EF22;
loc_00C7F154:
    result = RtlSectionTableFromVirtualAddress(0, v_rip - 13103454, (uint32_t)(*(uint32_t *)(local_rbx)), Arg4);
    if (result != 0) goto loc_00C7ECED;
loc_00C7F172:
    result = RtlImageNtHeader(*(uint64_t *)(v_rip + 0x347A1F), v_rip - 13103454, result, Arg4);
    result = RtlCaptureImageExceptionValues(*(uint64_t *)(v_rip + 0x347A1F), *(uint64_t *)(arg2 + 0x48) + 264, *(uint64_t *)(arg2 + 0x48) + 368, Arg4);
    Arg2 = (*(uint64_t *)(arg2 + 0x48) + 264) >> (3);
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170) = (uint32_t)(Arg2);
    if ((uint32_t)(Arg2) == 0) goto loc_00C7F671;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x140) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108);
    local_rdi = 0;
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0xA0) = 0;
    goto loc_00C7F657;
loc_00C7F1E4:
    local_rsi = 0;
    if (((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0x24)) & (0x2000000ULL)) != 0) goto loc_00C7F3F2;
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170)) != 0x54494E49ULL) goto loc_00C7F20B;
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0x4)) == 0x4742444BULL) goto loc_00C7F3F2;
loc_00C7F20B:
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170)) != 0x45474150ULL) goto loc_00C7F244;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0x4)) == ((uint16_t)((uint32_t)(0x7877ULL)))) goto loc_00C7F3F2;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0x4)) == ((uint16_t)((uint32_t)(0x7277ULL)))) goto loc_00C7F3F2;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0x4)) == ((uint16_t)((uint32_t)(0x7777ULL)))) goto loc_00C7F3F2;
loc_00C7F244:
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170)) != 0x41525245ULL) goto loc_00C7F25D;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0x4)) == ((uint16_t)((uint32_t)(0x4154ULL)))) goto loc_00C7F3F2;
loc_00C7F25D:
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x48) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x58) = v_xmm0;
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x88) = 7;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x118) = Arg4;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x110) = *(uint64_t *)(arg2 + 0x48) + 368;
loc_00C7F296:
    local_r10 = (*(uint64_t *)(arg2 + 0x48) + 368) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x110) = local_r10;
    Arg4 = (Arg4) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x118) = Arg4;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170)) != (*(uint8_t *)(Arg4))) goto loc_00C7F2C9;
    local_r11 = (uint32_t)((7) + (-1));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x88) = (uint32_t)(local_r11);
    if (condition_is_not_equal) goto loc_00C7F296;
    goto loc_00C7F3F2;
loc_00C7F2C9:
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x40) = 8;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xC0) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x50);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xB8) = *(uint64_t *)(arg2 + 0x48) + 368;
loc_00C7F2E8:
    local_r11 = (*(uint64_t *)(arg2 + 0x48) + 368) + (8);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xB8) = local_r11;
    local_r10 = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x50)) + (8);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xC0) = local_r10;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x50)))) goto loc_00C7F350;
    Arg4 = (uint32_t)((8) + (-8));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x40) = Arg4;
    if (Arg4 >= 8) goto loc_00C7F2E8;
    if (Arg4 == 0) goto loc_00C7F3F2;
loc_00C7F320:
    local_r11 = (local_r11) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xB8) = local_r11;
    local_r10 = (local_r10) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xC0) = local_r10;
    if ((*(uint8_t *)(local_r11)) != (*(uint8_t *)(local_r10))) goto loc_00C7F350;
    Arg4 = (uint32_t)((Arg4) + (-1));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x40) = Arg4;
    if (condition_is_not_equal) goto loc_00C7F320;
    goto loc_00C7F3F2;
loc_00C7F350:
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x90) = 4;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x128) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x58);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x120) = *(uint64_t *)(arg2 + 0x48) + 368;
loc_00C7F372:
    local_r10 = (*(uint64_t *)(arg2 + 0x48) + 368) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x120) = local_r10;
    Arg4 = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x58)) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x128) = Arg4;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170)) != (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x58)))) goto loc_00C7F3A2;
    local_r11 = (uint32_t)((4) + (-1));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x90) = (uint32_t)(local_r11);
    if (condition_is_not_equal) goto loc_00C7F372;
    goto loc_00C7F3F2;
loc_00C7F3A2:
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x98) = 6;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x138) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x60);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x130) = *(uint64_t *)(arg2 + 0x48) + 368;
loc_00C7F3C4:
    local_r10 = (*(uint64_t *)(arg2 + 0x48) + 368) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x130) = local_r10;
    Arg4 = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x60)) + 1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x138) = Arg4;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170)) != (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x60)))) goto loc_00C7F3F7;
    local_r11 = (uint32_t)((6) + (-1));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x98) = (uint32_t)(local_r11);
    if (condition_is_not_equal) goto loc_00C7F3C4;
loc_00C7F3F2:
loc_00C7F3F7:
    if (!sign_flag) goto loc_00C7F406;
    goto loc_00C7F412;
loc_00C7F406:
    local_rsi = 1;
    if (condition_is_above_or_equal) { local_rsi = 1; }
loc_00C7F412:
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0x10)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0x8))))) goto loc_00C7F422;
    goto loc_00C7F424;
loc_00C7F422:
loc_00C7F424:
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0xC))) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0x8)))))));
loc_00C7F42B:
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x34) = 1;
    if ((uint32_t)(local_rsi) != 0) goto loc_00C7F61A;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0xC))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))))));
    if (((uint32_t)(result)) < 6) goto loc_00C7F61A;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108)))) - (0));
    if (((uint32_t)(Arg2)) < 6) goto loc_00C7F61A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6)) != ((uint8_t)(local_rsi))) goto loc_00C7F48A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x5)) != ((uint8_t)(local_rsi))) goto loc_00C7F48A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x4)) != ((uint8_t)(local_rsi))) goto loc_00C7F48A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x3)) != ((uint8_t)(local_rsi))) goto loc_00C7F48A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2)) != ((uint8_t)(local_rsi))) goto loc_00C7F48A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x1)) != ((uint8_t)(local_rsi))) goto loc_00C7F48A;
loc_00C7F481:
    goto loc_00C7F61F;
loc_00C7F48A:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6)) != 132) goto loc_00C7F4AE;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x5)) != 0) goto loc_00C7F4AE;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x4)) != 0) goto loc_00C7F4AE;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x3)) != 0) goto loc_00C7F4AE;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2)) != 0) goto loc_00C7F4AE;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x1)) == 0) goto loc_00C7F481;
loc_00C7F4AE:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6)) != 204) goto loc_00C7F4D2;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x5)) != 204) goto loc_00C7F4D2;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x4)) != 204) goto loc_00C7F4D2;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x3)) != 204) goto loc_00C7F4D2;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2)) != 204) goto loc_00C7F4D2;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x1)) == 204) goto loc_00C7F481;
loc_00C7F4D2:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6)) != 31) goto loc_00C7F51E;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x5)) != 132) goto loc_00C7F4F6;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x4)) != 0) goto loc_00C7F4F6;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x3)) != 0) goto loc_00C7F4F6;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2)) != 0) goto loc_00C7F4F6;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x1)) == 0) goto loc_00C7F481;
loc_00C7F4F6:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6)) != 31) goto loc_00C7F51E;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x5)) != 128) goto loc_00C7F51E;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x4)) != 0) goto loc_00C7F51E;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x3)) != 0) goto loc_00C7F51E;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2)) != 0) goto loc_00C7F51E;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x1)) == 0) goto loc_00C7F481;
loc_00C7F51E:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6)) != 102) goto loc_00C7F546;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x5)) != 15) goto loc_00C7F546;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x4)) != 31) goto loc_00C7F546;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x3)) != 68) goto loc_00C7F546;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2)) != 0) goto loc_00C7F546;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x1)) == 0) goto loc_00C7F481;
loc_00C7F546:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6)) != 204) goto loc_00C7F61A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x5)) != 15) goto loc_00C7F572;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x4)) != 31) goto loc_00C7F572;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x3)) != 68) goto loc_00C7F572;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2)) != 0) goto loc_00C7F572;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x1)) == 0) goto loc_00C7F481;
loc_00C7F572:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6)) != 204) goto loc_00C7F61A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x5)) != 204) goto loc_00C7F59E;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x4)) != 15) goto loc_00C7F59E;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x3)) != 31) goto loc_00C7F59E;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2)) != 64) goto loc_00C7F59E;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x1)) == 0) goto loc_00C7F481;
loc_00C7F59E:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6)) != 204) goto loc_00C7F61A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x5)) != 204) goto loc_00C7F5C6;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x4)) != 204) goto loc_00C7F5C6;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x3)) != 15) goto loc_00C7F5C6;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2)) != 31) goto loc_00C7F5C6;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x1)) == 0) goto loc_00C7F481;
loc_00C7F5C6:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6)) != 204) goto loc_00C7F61A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x5)) != 204) goto loc_00C7F5EE;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x4)) != 204) goto loc_00C7F5EE;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x3)) != 204) goto loc_00C7F5EE;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2)) != 102) goto loc_00C7F5EE;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x1)) == 144) goto loc_00C7F481;
loc_00C7F5EE:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6)) != 204) goto loc_00C7F61A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x5)) != 204) goto loc_00C7F61A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x4)) != 204) goto loc_00C7F61A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x3)) != 204) goto loc_00C7F61A;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2)) == 204) {
        result = 0;
        Arg4 = 1;
        if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x1)) == 144) { Arg4 = 0; }
        *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x34) = Arg4;
    }
    if (Arg4 == 0) {
        *(uint32_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x6) = 0x9800874CULL;
        *(uint16_t *)(*(uint64_t *)(v_rip + 0x347A1F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108))) * 1 - 0x2) = 0x90C3ULL;
    }
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0xA0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108) + 0x4)));
    local_rbx = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108)) + (12);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x140) = local_rbx;
    if (local_rbx == (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x108) + (uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 2 * 4)) goto loc_00C7F671;
    if ((*(uint32_t *)(local_rbx)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x170 + 0xC))))) goto loc_00C7F657;
    if ((*(uint32_t *)(local_rbx + 0x4)) <= ((uint32_t)(local_r10))) goto loc_00C7F42B;
loc_00C7F657:
    result = RtlSectionTableFromVirtualAddress(0, *(uint64_t *)(v_rip + 0x347A1F), (uint32_t)(*(uint32_t *)(local_rbx)), Arg4);
    if (result != 0) goto loc_00C7F1E4;
loc_00C7F671:
    *(uint32_t *)(v_rip + 0x388FD1) = 1;
loc_00C7F67B:
    Arg2 = (*(uint64_t *)(v_rip + 0x347A1F)) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    Arg1 = (Arg2) ^ (result);
    Arg2 = (Arg2) >> (3);
    result = (Arg2 + Arg2 * 4) + (Arg2 + Arg2 * 4);
    Arg1 = (Arg1) - (result);
    if (Arg1 < 1) {
    }
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    Arg1 = (Arg2) ^ (result);
    Arg2 = (Arg2) >> (3);
    result = (Arg2 + Arg2 * 4) + (Arg2 + Arg2 * 4);
    Arg1 = (Arg1) - (result);
    if (Arg1 < 1) {
    }
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    Arg4 = (*(uint8_t *)(v_rip + 0x2C7E91)) | (*(uint8_t *)(v_rip + 0x18B2CA));
    local_r10 = (Arg2) ^ (result);
    result = (local_r10) - (Arg2);
    result = (result) >> (1);
    result = (result) + (Arg2);
    result = (result) >> (6);
    result = (result) * (result);
    local_r10 = (local_r10) - (result);
    if (local_r10 < Arg4) {
        result = KdDisableDebugger(*(uint8_t *)(v_rip + 0x18B2CA), Arg2, result, Arg4);
        *(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0xA4) = (uint32_t)(result);
        Arg2 = v_rip - 591119;
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0xC8);
        result = local_unwind(Arg1, Arg2, result, Arg4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C7EB3D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
