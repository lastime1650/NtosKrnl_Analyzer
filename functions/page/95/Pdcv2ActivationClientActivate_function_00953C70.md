# Pdcv2ActivationClientActivate

- RVA: `0x00953C70`–`0x009540B4` (길이 `1,092` bytes)
- VA: `0x0000000140953C70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00092148`
- 디코드: `271`개 명령, `1,092/1,092` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00953CB0` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00953D08` → [Pdcv2pValidateActivationParameters](../A7/Pdcv2pValidateActivationParameters_function_00A7FC90.md) (function, `0x00A7FC90`)
- `0x00953D1C` → [Pdcv2pValidateExtraActivationParameters](../../text/4A/Pdcv2pValidateExtraActivationParameters_function_004AB520.md) (function, `0x004AB520`)
- `0x00953D5E` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00953DBD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00953E2C` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (function, `0x0026E9A4`)
- `0x00953EC6` → [PdcPortSendMessageSynchronously](../../text/49/PdcPortSendMessageSynchronously_function_0049A6B4.md) (function, `0x0049A6B4`)
- `0x00953ED6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00953EE3` → [Pdcv2EventWrite_ACTIVATION_CLIENT_ACTIVATE](../../text/42/Pdcv2EventWrite_ACTIVATION_CLIENT_ACTIVATE_function_004249F8.md) (function, `0x004249F8`)
- `0x00953F2E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00953F6D` → [Feature_Servicing_PDCActivationsAVL__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCActivationsAVL__private_IsEnabledDeviceUsageNoInline_function_004F4F6C.md) (function, `0x004F4F6C`)
- `0x00953F88` → [PdcpActivationClientTableCompareRoutine](../79/PdcpActivationClientTableCompareRoutine_function_0079AF04.md) (function, `0x0079AF04`)
- `0x00953FB6` → [RtlAvlInsertNodeEx](../../text/26/RtlAvlInsertNodeEx_function_00265790.md) (function, `0x00265790`)
- `0x00954070` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (function, `0x0026E9A4`)
- `0x00954084` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (function, `0x0026E9A4`)
- `0x00954095` → [PdcpResizeDiagnosticContext](../../text/60/PdcpResizeDiagnosticContext_function_0060588C.md) (function, `0x0060588C`)
- `0x009540AA` → [PdcReleaseRwLockExclusive2](../A7/PdcReleaseRwLockExclusive2_function_00A71898.md) (function, `0x00A71898`)

### Direct callers
- [PopAdaptiveStandbyQueryReserveConfiguration](../76/PopAdaptiveStandbyQueryReserveConfiguration_function_0076E6D0.md) at `0x0076E7D6`
- [PiPdcActivate](PiPdcActivate_function_00953BF4.md) at `0x00953C54`
- [PopWin32kActivatorWorker](PopWin32kActivatorWorker_function_009540C0.md) at `0x0095422D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00953CB0` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00953D1C` → [Pdcv2pValidateExtraActivationParameters](../../text/4A/Pdcv2pValidateExtraActivationParameters_function_004AB520.md) (`PAGE` → `.text`)
  - `0x00953D5E` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00953DBD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00953E2C` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (`PAGE` → `.text`)
  - `0x00953EC6` → [PdcPortSendMessageSynchronously](../../text/49/PdcPortSendMessageSynchronously_function_0049A6B4.md) (`PAGE` → `.text`)
  - `0x00953ED6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00953EE3` → [Pdcv2EventWrite_ACTIVATION_CLIENT_ACTIVATE](../../text/42/Pdcv2EventWrite_ACTIVATION_CLIENT_ACTIVATE_function_004249F8.md) (`PAGE` → `.text`)
  - `0x00953F2E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00953F6D` → [Feature_Servicing_PDCActivationsAVL__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCActivationsAVL__private_IsEnabledDeviceUsageNoInline_function_004F4F6C.md) (`PAGE` → `.text`)
  - `0x00953FB6` → [RtlAvlInsertNodeEx](../../text/26/RtlAvlInsertNodeEx_function_00265790.md) (`PAGE` → `.text`)
  - `0x00954070` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (`PAGE` → `.text`)
  - `0x00954084` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (`PAGE` → `.text`)
  - `0x00954095` → [PdcpResizeDiagnosticContext](../../text/60/PdcpResizeDiagnosticContext_function_0060588C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00953C70  48 8B C4                        mov rax, rsp
00953C73  48 89 58 08                     mov qword ptr [rax + 8], rbx
00953C77  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00953C7B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00953C7F  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00953C83  55                              push rbp
00953C84  41 54                           push r12
00953C86  41 55                           push r13
00953C88  41 56                           push r14
00953C8A  41 57                           push r15
00953C8C  48 8D A8 88 FD FF FF            lea rbp, [rax - 0x278]
00953C93  48 81 EC 50 03 00 00            sub rsp, 0x350
00953C9A  4D 8B E8                        mov r13, r8
00953C9D  48 8B DA                        mov rbx, rdx
00953CA0  48 8B F9                        mov rdi, rcx
00953CA3  33 D2                           xor edx, edx
00953CA5  41 B8 20 03 00 00               mov r8d, 0x320
00953CAB  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00953CB0  E8 8B 2F D7 FF                  call 0x1406c6c40
00953CB5  4C 8B A5 B8 02 00 00            mov r12, qword ptr [rbp + 0x2b8]
00953CBC  45 33 F6                        xor r14d, r14d
00953CBF  44 88 B5 98 02 00 00            mov byte ptr [rbp + 0x298], r14b
00953CC6  45 8B FE                        mov r15d, r14d
00953CC9  4D 85 E4                        test r12, r12
00953CCC  0F 84 47 03 00 00               je 0x140954019
00953CD2  48 8B 85 B0 02 00 00            mov rax, qword ptr [rbp + 0x2b0]
00953CD9  41 C7 04 24 01 00 00 00         mov dword ptr [r12], 1
00953CE1  48 85 C0                        test rax, rax
00953CE4  0F 84 39 03 00 00               je 0x140954023
00953CEA  4C 89 30                        mov qword ptr [rax], r14
00953CED  48 85 FF                        test rdi, rdi
00953CF0  0F 84 3A 03 00 00               je 0x140954030
00953CF6  81 3F 50 44 41 32               cmp dword ptr [rdi], 0x32414450
00953CFC  4C 8B FF                        mov r15, rdi
00953CFF  0F 85 28 03 00 00               jne 0x14095402d
00953D05  48 8B CB                        mov rcx, rbx
00953D08  E8 83 BF 12 00                  call 0x140a7fc90
00953D0D  84 C0                           test al, al
00953D0F  0F 84 25 03 00 00               je 0x14095403a
00953D15  41 8D 56 01                     lea edx, [r14 + 1]
00953D19  48 8B CB                        mov rcx, rbx
00953D1C  E8 FF 77 B5 FF                  call 0x1404ab520
00953D21  84 C0                           test al, al
00953D23  0F 84 11 03 00 00               je 0x14095403a
00953D29  4C 8B B5 A0 02 00 00            mov r14, qword ptr [rbp + 0x2a0]
00953D30  33 F6                           xor esi, esi
00953D32  4D 85 F6                        test r14, r14
00953D35  0F 84 09 03 00 00               je 0x140954044
00953D3B  48 C7 85 B8 02 00 00 00 BA 3C DC  mov qword ptr [rbp + 0x2b8], 0xffffffffdc3cba00
00953D46  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00953D4A  48 8D 85 B8 02 00 00            lea rax, [rbp + 0x2b8]
00953D51  45 33 C9                        xor r9d, r9d
00953D54  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00953D59  45 33 C0                        xor r8d, r8d
00953D5C  33 D2                           xor edx, edx
00953D5E  E8 4D A9 8B FF                  call 0x14020e6b0
00953D63  8B C8                           mov ecx, eax
00953D65  85 C0                           test eax, eax
00953D67  0F 85 7A 02 00 00               jne 0x140953fe7
00953D6D  C6 85 98 02 00 00 01            mov byte ptr [rbp + 0x298], 1
00953D74  8D 41 01                        lea eax, [rcx + 1]
00953D77  F0 0F C1 47 18                  lock xadd dword ptr [rdi + 0x18], eax
00953D7C  FF C0                           inc eax
00953D7E  83 F8 01                        cmp eax, 1
00953D81  75 0D                           jne 0x140953d90
00953D83  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00953D8C  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00953D90  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00953D99  48 39 47 10                     cmp qword ptr [rdi + 0x10], rax
00953D9D  0F 85 B5 02 00 00               jne 0x140954058
00953DA3  48 39 77 28                     cmp qword ptr [rdi + 0x28], rsi
00953DA7  0F 84 B2 02 00 00               je 0x14095405f
00953DAD  BA 60 02 00 00                  mov edx, 0x260
00953DB2  B9 00 01 00 00                  mov ecx, 0x100
00953DB7  41 B8 50 44 43 41               mov r8d, 0x41434450
00953DBD  E8 2E E3 22 00                  call 0x140b820f0
00953DC2  45 33 DB                        xor r11d, r11d
00953DC5  48 8B F0                        mov rsi, rax
00953DC8  48 85 C0                        test rax, rax
00953DCB  0F 84 7A 02 00 00               je 0x14095404b
00953DD1  C7 40 18 50 44 43 41            mov dword ptr [rax + 0x18], 0x41434450
00953DD8  4D 8B C6                        mov r8, r14
00953DDB  C7 40 1C 01 00 00 00            mov dword ptr [rax + 0x1c], 1
00953DE2  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00953DE6  48 B8 04 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000004
00953DF0  8B 08                           mov ecx, dword ptr [rax]
00953DF2  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
00953DFC  48 C1 E1 20                     shl rcx, 0x20
00953E00  48 8B 00                        mov rax, qword ptr [rax]
00953E03  48 C1 E0 08                     shl rax, 8
00953E07  48 F7 E1                        mul rcx
00953E0A  8B 43 04                        mov eax, dword ptr [rbx + 4]
00953E0D  48 8D 4E 50                     lea rcx, [rsi + 0x50]
00953E11  4C 89 6E 28                     mov qword ptr [rsi + 0x28], r13
00953E15  41 BD 80 00 00 00               mov r13d, 0x80
00953E1B  48 89 56 30                     mov qword ptr [rsi + 0x30], rdx
00953E1F  41 8B D5                        mov edx, r13d
00953E22  C7 46 38 01 00 00 00            mov dword ptr [rsi + 0x38], 1
00953E29  89 46 3C                        mov dword ptr [rsi + 0x3c], eax
00953E2C  E8 73 AB 91 FF                  call 0x14026e9a4
00953E31  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
00953E35  4D 85 C0                        test r8, r8
00953E38  0F 85 28 02 00 00               jne 0x140954066
00953E3E  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00953E42  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00953E46  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00953E4A  4D 8B C5                        mov r8, r13
00953E4D  8B 43 04                        mov eax, dword ptr [rbx + 4]
00953E50  89 45 8C                        mov dword ptr [rbp - 0x74], eax
00953E53  48 8D 45 90                     lea rax, [rbp - 0x70]
00953E57  4C 2B F0                        sub r14, rax
00953E5A  C7 44 24 58 0A 00 00 00         mov dword ptr [rsp + 0x58], 0xa
00953E62  C7 44 24 78 01 00 00 00         mov dword ptr [rsp + 0x78], 1
00953E6A  44 89 5D 88                     mov dword ptr [rbp - 0x78], r11d
00953E6E  49 8D 80 7E FF FF 7F            lea rax, [r8 + 0x7fffff7e]
00953E75  48 85 C0                        test rax, rax
00953E78  74 17                           je 0x140953e91
00953E7A  41 0F B7 04 0E                  movzx eax, word ptr [r14 + rcx]
00953E7F  66 85 C0                        test ax, ax
00953E82  74 0D                           je 0x140953e91
00953E84  66 89 01                        mov word ptr [rcx], ax
00953E87  48 83 C1 02                     add rcx, 2
00953E8B  49 83 E8 01                     sub r8, 1
00953E8F  75 DD                           jne 0x140953e6e
00953E91  45 33 F6                        xor r14d, r14d
00953E94  48 8D 41 FE                     lea rax, [rcx - 2]
00953E98  4D 85 C0                        test r8, r8
00953E9B  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
00953E9F  48 0F 45 C1                     cmovne rax, rcx
00953EA3  66 44 89 30                     mov word ptr [rax], r14w
00953EA7  4D 85 C0                        test r8, r8
00953EAA  0F 85 CA 01 00 00               jne 0x14095407a
00953EB0  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00953EB4  48 85 C9                        test rcx, rcx
00953EB7  0F 85 D1 01 00 00               jne 0x14095408e
00953EBD  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
00953EC1  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00953EC6  E8 E9 67 B4 FF                  call 0x14049a6b4
00953ECB  8B D8                           mov ebx, eax
00953ECD  85 C0                           test eax, eax
00953ECF  79 48                           jns 0x140953f19
00953ED1  33 D2                           xor edx, edx
00953ED3  48 8B CE                        mov rcx, rsi
00953ED6  E8 95 E9 22 00                  call 0x140b82870
00953EDB  49 8B D7                        mov rdx, r15
00953EDE  33 C9                           xor ecx, ecx
00953EE0  44 8B C3                        mov r8d, ebx
00953EE3  E8 10 0B AD FF                  call 0x1404249f8
00953EE8  44 38 B5 98 02 00 00            cmp byte ptr [rbp + 0x298], r14b
00953EEF  0F 85 AA 01 00 00               jne 0x14095409f
00953EF5  4C 8D 9C 24 50 03 00 00         lea r11, [rsp + 0x350]
00953EFD  8B C3                           mov eax, ebx
00953EFF  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00953F03  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00953F07  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00953F0B  49 8B E3                        mov rsp, r11
00953F0E  41 5F                           pop r15
00953F10  41 5E                           pop r14
00953F12  41 5D                           pop r13
00953F14  41 5C                           pop r12
00953F16  5D                              pop rbp
00953F17  C3                              ret
00953F18  CC                              int3
00953F19  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
00953F1D  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
00953F21  41 89 04 24                     mov dword ptr [r12], eax
00953F25  85 DB                           test ebx, ebx
00953F27  79 10                           jns 0x140953f39
00953F29  33 D2                           xor edx, edx
00953F2B  48 8B CE                        mov rcx, rsi
00953F2E  E8 3D E9 22 00                  call 0x140b82870
00953F33  85 DB                           test ebx, ebx
00953F35  79 B1                           jns 0x140953ee8
00953F37  EB A2                           jmp 0x140953edb
00953F39  3D 2C 01 00 00                  cmp eax, 0x12c
00953F3E  74 E9                           je 0x140953f29
00953F40  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00953F45  4C 8D AE 58 02 00 00            lea r13, [rsi + 0x258]
00953F4C  49 89 45 00                     mov qword ptr [r13], rax
00953F50  44 88 76 44                     mov byte ptr [rsi + 0x44], r14b
00953F54  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
00953F58  89 46 40                        mov dword ptr [rsi + 0x40], eax
00953F5B  FF 87 00 01 00 00               inc dword ptr [rdi + 0x100]
00953F61  FF 87 04 01 00 00               inc dword ptr [rdi + 0x104]
00953F67  FF 87 0C 01 00 00               inc dword ptr [rdi + 0x10c]
00953F6D  E8 FA 0F BA FF                  call 0x1404f4f6c
00953F72  85 C0                           test eax, eax
00953F74  74 5D                           je 0x140953fd3
00953F76  4C 8B 77 60                     mov r14, qword ptr [rdi + 0x60]
00953F7A  45 32 C0                        xor r8b, r8b
00953F7D  4D 85 F6                        test r14, r14
00953F80  74 2A                           je 0x140953fac
00953F82  49 8B D6                        mov rdx, r14
00953F85  49 8B CD                        mov rcx, r13
00953F88  E8 77 6F E4 FF                  call 0x14079af04
00953F8D  33 C9                           xor ecx, ecx
00953F8F  85 C0                           test eax, eax
00953F91  79 0D                           jns 0x140953fa0
00953F93  49 8B 06                        mov rax, qword ptr [r14]
00953F96  48 85 C0                        test rax, rax
00953F99  74 79                           je 0x140954014
00953F9B  4C 8B F0                        mov r14, rax
00953F9E  EB E2                           jmp 0x140953f82
00953FA0  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00953FA4  48 85 C0                        test rax, rax
00953FA7  75 F2                           jne 0x140953f9b
00953FA9  41 B0 01                        mov r8b, 1
00953FAC  4C 8B CE                        mov r9, rsi
00953FAF  48 8D 4F 60                     lea rcx, [rdi + 0x60]
00953FB3  49 8B D6                        mov rdx, r14
00953FB6  E8 D5 17 91 FF                  call 0x140265790
00953FBB  45 33 F6                        xor r14d, r14d
00953FBE  48 8B 85 B0 02 00 00            mov rax, qword ptr [rbp + 0x2b0]
00953FC5  48 8B D7                        mov rdx, rdi
00953FC8  48 8B CE                        mov rcx, rsi
00953FCB  48 89 30                        mov qword ptr [rax], rsi
00953FCE  E9 0D FF FF FF                  jmp 0x140953ee0
00953FD3  48 8D 47 50                     lea rax, [rdi + 0x50]
00953FD7  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00953FDB  48 39 01                        cmp qword ptr [rcx], rax
00953FDE  74 24                           je 0x140954004
00953FE0  B9 03 00 00 00                  mov ecx, 3
00953FE5  CD 29                           int 0x29
00953FE7  81 E9 C0 00 00 00               sub ecx, 0xc0
00953FED  74 0E                           je 0x140953ffd
00953FEF  83 E9 41                        sub ecx, 0x41
00953FF2  74 09                           je 0x140953ffd
00953FF4  83 F9 01                        cmp ecx, 1
00953FF7  0F 84 49 FD FF FF               je 0x140953d46
00953FFD  B9 05 00 00 00                  mov ecx, 5
00954002  CD 29                           int 0x29
00954004  48 89 06                        mov qword ptr [rsi], rax
00954007  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
0095400B  48 89 31                        mov qword ptr [rcx], rsi
0095400E  48 89 70 08                     mov qword ptr [rax + 8], rsi
00954012  EB AA                           jmp 0x140953fbe
00954014  44 8A C1                        mov r8b, cl
00954017  EB 93                           jmp 0x140953fac
00954019  BB F6 00 00 C0                  mov ebx, 0xc00000f6
0095401E  E9 B8 FE FF FF                  jmp 0x140953edb
00954023  BB F5 00 00 C0                  mov ebx, 0xc00000f5
00954028  E9 AE FE FF FF                  jmp 0x140953edb
0095402D  4D 8B FE                        mov r15, r14
00954030  BB EF 00 00 C0                  mov ebx, 0xc00000ef
00954035  E9 A1 FE FF FF                  jmp 0x140953edb
0095403A  BB F0 00 00 C0                  mov ebx, 0xc00000f0
0095403F  E9 97 FE FF FF                  jmp 0x140953edb
00954044  BB F3 00 00 C0                  mov ebx, 0xc00000f3
00954049  EB 05                           jmp 0x140954050
0095404B  BB 17 00 00 C0                  mov ebx, 0xc0000017
00954050  45 33 F6                        xor r14d, r14d
00954053  E9 83 FE FF FF                  jmp 0x140953edb
00954058  B9 28 00 00 00                  mov ecx, 0x28
0095405D  CD 29                           int 0x29
0095405F  BB 00 07 00 C0                  mov ebx, 0xc0000700
00954064  EB EA                           jmp 0x140954050
00954066  48 8D 8E 50 01 00 00            lea rcx, [rsi + 0x150]
0095406D  49 8B D5                        mov rdx, r13
00954070  E8 2F A9 91 FF                  call 0x14026e9a4
00954075  E9 C4 FD FF FF                  jmp 0x140953e3e
0095407A  49 8B D5                        mov rdx, r13
0095407D  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
00954084  E8 1B A9 91 FF                  call 0x14026e9a4
00954089  E9 22 FE FF FF                  jmp 0x140953eb0
0095408E  48 8D 95 A8 01 00 00            lea rdx, [rbp + 0x1a8]
00954095  E8 F2 17 CB FF                  call 0x14060588c
0095409A  E9 1E FE FF FF                  jmp 0x140953ebd
0095409F  49 8D 4F 08                     lea rcx, [r15 + 8]
009540A3  48 8D 95 98 02 00 00            lea rdx, [rbp + 0x298]
009540AA  E8 E9 D7 11 00                  call 0x140a71898
009540AF  E9 41 FE FF FF                  jmp 0x140953ef5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Pdcv2ActivationClientActivate(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m2E0;
    unsigned int v_stack_m2E4;
    unsigned int v_stack_m2E8;
    unsigned int v_stack_m300;
    unsigned int v_stack_m320;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m358;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned int *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (848);
    a2 = 0;
    result = memset(v_stack_m348, a2, 800, a4);
    v_r14 = 0;
    *(unsigned __int8 *)(v_rsp - 632 + 664) = 0;
    if (*(unsigned __int64 *)(v_rsp - 632 + 696) == 0) goto loc_00954019;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 632 + 696)) = 1;
    if (*(unsigned __int64 *)(v_rsp - 632 + 688) == 0) goto loc_00954023;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 632 + 688)) = 0;
    if (a1 == 0) goto loc_00954030;
    if ((*(unsigned int *)(a1)) != 0x32414450ULL) goto loc_0095402D;
    result = Pdcv2pValidateActivationParameters(0, a2, 800, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0095403A;
    result = Pdcv2pValidateExtraActivationParameters(0, v_r14 + 1, 800, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0095403A;
    v_rsi = 0;
    if (*(unsigned __int64 *)(v_rsp - 632 + 672) == 0) goto loc_00954044;
    *(unsigned __int64 *)(v_rsp - 632 + 696) = 0xFFFFFFFFDC3CBA00ULL;
loc_00953D46:
    a4 = 0;
    v_stack_m358 = v_rsp - 632 + 696;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00953FE7;
    *(unsigned __int8 *)(v_rsp - 632 + 664) = 1;
    result = (unsigned int)(((unsigned int)((unsigned int)(result)) + 1) + 1);
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        *(unsigned __int64 *)(a1 + 16) = result;
    }
    if ((*(unsigned __int64 *)(a1 + 16)) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00954058;
    if ((*(unsigned __int64 *)(a1 + 40)) == 0) goto loc_0095405F;
    result = ExAllocatePool2(256, 608, (unsigned int)(0x41434450ULL), a4);
    v_r11 = 0;
    if (result == 0) goto loc_0095404B;
    *(unsigned int *)(result + 24) = 0x41434450ULL;
    *(unsigned int *)(result + 28) = 1;
    *(unsigned __int64 *)(result + 32) = a1;
    a1 = ((unsigned int)(*(unsigned int *)(result))) << (32);
    result = (*(unsigned __int64 *)(result)) << (8);
    *(unsigned __int64 *)(result + 40) = 0;
    *(unsigned __int64 *)(result + 48) = 608;
    *(unsigned int *)(result + 56) = 1;
    *(unsigned int *)(result + 60) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)));
    result = RtlStringCchCopyW(result + 80, 128, *(unsigned __int64 *)(v_rsp - 632 + 672), a4);
    if (*(unsigned __int64 *)(a2 + 16) != 0) goto loc_00954066;
loc_00953E3E:
    *(unsigned __int64 *)(v_rsp - 632 - 128) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned int *)(v_rsp - 632 - 116) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)));
    v_r14 = (*(unsigned __int64 *)(v_rsp - 632 + 672)) - (v_rsp - 632 - 112);
    v_stack_m320 = 10;
    v_stack_m300 = 1;
    *(unsigned int *)(v_rsp - 632 - 120) = 0;
loc_00953E6E:
    if (128 + 2147483518 == 0) goto loc_00953E91;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r14 + v_rsp - 632 - 112 * 1)) == 0) goto loc_00953E91;
    *(unsigned __int16 *)(v_rsp - 632 - 112) = (unsigned __int16)(*(unsigned __int16 *)(v_r14 + v_rsp - 632 - 112 * 1));
    a1 = (v_rsp - 632 - 112) + (2);
    a3 = (128) - (1);
    if (condition_is_not_equal) goto loc_00953E6E;
loc_00953E91:
    v_r14 = 0;
    result = a1 - 2;
    if (a3 != 0) { result = a1; }
    *(unsigned __int16 *)(result) = 0;
    if (*(unsigned __int64 *)(a2 + 16) != 0) goto loc_0095407A;
loc_00953EB0:
    if (*(unsigned __int64 *)(a2 + 24) != 0) goto loc_0095408E;
loc_00953EBD:
    result = PdcPortSendMessageSynchronously(*(unsigned __int64 *)(a1 + 40), v_stack_m348, *(unsigned __int64 *)(a2 + 16), a4);
    if (!sign_flag) goto loc_00953F19;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, *(unsigned __int64 *)(a2 + 16), a4);
loc_00953EDB:
    a1 = 0;
loc_00953EE0:
    result = Pdcv2EventWrite_ACTIVATION_CLIENT_ACTIVATE(a1, a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
loc_00953EE8:
    if ((*(unsigned __int8 *)(v_rsp - 632 + 664)) != 0) goto loc_0095409F;
loc_00953EF5:
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00953F19:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 632 + 696)) = (unsigned int)((unsigned int)(v_stack_m2E4));
    if (!sign_flag) goto loc_00953F39;
loc_00953F29:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m28 + 56), a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    if (!sign_flag) goto loc_00953EE8;
    goto loc_00953EDB;
loc_00953F39:
    if (((unsigned int)(result)) == 300) goto loc_00953F29;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 600) = v_stack_m2E0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 68) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 64) = (unsigned int)((unsigned int)(v_stack_m2E4));
    result = Feature_Servicing_PDCActivationsAVL__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_stack_m28 + 56), a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    if ((unsigned int)(result) == 0) goto loc_00953FD3;
    a3 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 96) == 0) goto loc_00953FAC;
loc_00953F82:
    result = PdcpActivationClientTableCompareRoutine(*(unsigned __int64 *)(v_stack_m28 + 56) + 600, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 96), a3, a4);
    a1 = 0;
    if (!sign_flag) goto loc_00953FA0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 96)) == 0) goto loc_00954014;
loc_00953F9B:
    goto loc_00953F82;
loc_00953FA0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 96)) + 8) != 0) goto loc_00953F9B;
loc_00953FAC:
    result = RtlAvlInsertNodeEx(*(unsigned __int64 *)(v_stack_m28 + 64) + 96, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 96)), 1, *(unsigned __int64 *)(v_stack_m28 + 56));
    v_r14 = 0;
loc_00953FBE:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 632 + 688)) = *(unsigned __int64 *)(v_stack_m28 + 56);
    goto loc_00953EE0;
loc_00953FD3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 80 + 8))) == (*(unsigned __int64 *)(v_stack_m28 + 64) + 80)) goto loc_00954004;
loc_00953FE7:
    a1 = (unsigned int)((3) - (192));
    if (condition_is_equal) goto loc_00953FFD;
    a1 = (unsigned int)((a1) - (65));
    if (condition_is_equal) goto loc_00953FFD;
    if (((unsigned int)(a1)) == 1) goto loc_00953D46;
loc_00953FFD:
loc_00954004:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56)) = *(unsigned __int64 *)(v_stack_m28 + 64) + 80;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 8) = 5;
    *(unsigned __int64 *)(5) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 80 + 8) = *(unsigned __int64 *)(v_stack_m28 + 56);
    goto loc_00953FBE;
loc_00954014:
    goto loc_00953FAC;
loc_00954019:
    goto loc_00953EDB;
loc_00954023:
    goto loc_00953EDB;
loc_0095402D:
loc_00954030:
    goto loc_00953EDB;
loc_0095403A:
    goto loc_00953EDB;
loc_00954044:
    goto loc_00954050;
loc_0095404B:
loc_00954050:
    v_r14 = 0;
    goto loc_00953EDB;
loc_00954058:
loc_0095405F:
    goto loc_00954050;
loc_00954066:
    result = RtlStringCchCopyW(*(unsigned __int64 *)(v_stack_m28 + 56) + 336, *(unsigned __int64 *)(v_stack_m28 + 56) + 600, 5, *(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00953E3E;
loc_0095407A:
    result = RtlStringCchCopyW(v_rsp - 632 + 144, *(unsigned __int64 *)(v_stack_m28 + 56) + 600, 5, *(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00953EB0;
loc_0095408E:
    result = PdcpResizeDiagnosticContext(v_rsp - 632 + 144, v_rsp - 632 + 424, 5, *(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00953EBD;
loc_0095409F:
    result = PdcReleaseRwLockExclusive2(0 + 8, v_rsp - 632 + 664, 5, *(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00953EF5;
}
```

## 5. (Beta) C Style

```c
int64_t Pdcv2ActivationClientActivate(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m2E0;
    uint32_t v_stack_m2E4;
    uint32_t v_stack_m2E8;
    uint32_t v_stack_m300;
    uint32_t v_stack_m320;
    uint64_t v_stack_m348;
    uint64_t v_stack_m358;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (848);
    Arg2 = 0;
    result = memset(v_stack_m348, Arg2, 800, Arg4);
    local_r14 = 0;
    *(uint8_t *)(local_rsp - 0x278 + 0x298) = 0;
    if (*(uint64_t *)(local_rsp - 0x278 + 0x2B8) == 0) goto loc_00954019;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x278 + 0x2B8)) = 1;
    if (*(uint64_t *)(local_rsp - 0x278 + 0x2B0) == 0) goto loc_00954023;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x278 + 0x2B0)) = 0;
    if (Arg1 == 0) goto loc_00954030;
    if ((*(uint32_t *)(Arg1)) != 0x32414450ULL) goto loc_0095402D;
    result = Pdcv2pValidateActivationParameters(0, Arg2, 800, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0095403A;
    result = Pdcv2pValidateExtraActivationParameters(0, local_r14 + 1, 800, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0095403A;
    local_rsi = 0;
    if (*(uint64_t *)(local_rsp - 0x278 + 0x2A0) == 0) goto loc_00954044;
    *(uint64_t *)(local_rsp - 0x278 + 0x2B8) = 0xFFFFFFFFDC3CBA00ULL;
loc_00953D46:
    Arg4 = 0;
    v_stack_m358 = local_rsp - 632 + 696;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(*(uint64_t *)(Arg1 + 0x8), Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00953FE7;
    *(uint8_t *)(local_rsp - 0x278 + 0x298) = 1;
    result = (uint32_t)(((uint32_t)((uint32_t)(result)) + 1) + 1);
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        *(uint64_t *)(Arg1 + 0x10) = result;
    }
    if ((*(uint64_t *)(Arg1 + 0x10)) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00954058;
    if ((*(uint64_t *)(Arg1 + 0x28)) == 0) goto loc_0095405F;
    result = ExAllocatePool2(256, 608, (uint32_t)(0x41434450ULL), Arg4);
    local_r11 = 0;
    if (result == 0) goto loc_0095404B;
    *(uint32_t *)(result + 0x18) = 0x41434450ULL;
    *(uint32_t *)(result + 0x1C) = 1;
    *(uint64_t *)(result + 0x20) = Arg1;
    Arg1 = ((uint32_t)(*(uint32_t *)(result))) << (32);
    result = (*(uint64_t *)(result)) << (8);
    *(uint64_t *)(result + 0x28) = 0;
    *(uint64_t *)(result + 0x30) = 608;
    *(uint32_t *)(result + 0x38) = 1;
    *(uint32_t *)(result + 0x3C) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    result = RtlStringCchCopyW(result + 80, 128, *(uint64_t *)(local_rsp - 0x278 + 0x2A0), Arg4);
    if (*(uint64_t *)(Arg2 + 0x10) != 0) goto loc_00954066;
loc_00953E3E:
    *(uint64_t *)(local_rsp - 0x278 - 0x80) = *(uint64_t *)(Arg2 + 0x8);
    *(uint32_t *)(local_rsp - 0x278 - 0x74) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    local_r14 = (*(uint64_t *)(local_rsp - 0x278 + 0x2A0)) - (local_rsp - 632 - 112);
    v_stack_m320 = 10;
    v_stack_m300 = 1;
    *(uint32_t *)(local_rsp - 0x278 - 0x78) = 0;
loc_00953E6E:
    if (128 + 2147483518 == 0) goto loc_00953E91;
    if ((uint16_t)(*(uint16_t *)(local_r14 + local_rsp - 0x278 - 0x70 * 1)) == 0) goto loc_00953E91;
    *(uint16_t *)(local_rsp - 0x278 - 0x70) = (uint16_t)(*(uint16_t *)(local_r14 + local_rsp - 0x278 - 0x70 * 1));
    Arg1 = (local_rsp - 632 - 112) + (2);
    Arg3 = (128) - (1);
    if (condition_is_not_equal) goto loc_00953E6E;
loc_00953E91:
    local_r14 = 0;
    result = Arg1 - 2;
    if (Arg3 != 0) { result = Arg1; }
    *(uint16_t *)(result) = 0;
    if (*(uint64_t *)(Arg2 + 0x10) != 0) goto loc_0095407A;
loc_00953EB0:
    if (*(uint64_t *)(Arg2 + 0x18) != 0) goto loc_0095408E;
loc_00953EBD:
    result = PdcPortSendMessageSynchronously(*(uint64_t *)(Arg1 + 0x28), v_stack_m348, *(uint64_t *)(Arg2 + 0x10), Arg4);
    if (!sign_flag) goto loc_00953F19;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, *(uint64_t *)(Arg2 + 0x10), Arg4);
loc_00953EDB:
    Arg1 = 0;
loc_00953EE0:
    result = Pdcv2EventWrite_ACTIVATION_CLIENT_ACTIVATE(Arg1, Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4);
loc_00953EE8:
    if ((*(uint8_t *)(local_rsp - 0x278 + 0x298)) != 0) goto loc_0095409F;
loc_00953EF5:
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00953F19:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x278 + 0x2B8)) = (uint32_t)((uint32_t)(v_stack_m2E4));
    if (!sign_flag) goto loc_00953F39;
loc_00953F29:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4);
    if (!sign_flag) goto loc_00953EE8;
    goto loc_00953EDB;
loc_00953F39:
    if (((uint32_t)(result)) == 300) goto loc_00953F29;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x258) = v_stack_m2E0;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x44) = 0;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x40) = (uint32_t)((uint32_t)(v_stack_m2E4));
    result = Feature_Servicing_PDCActivationsAVL__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00953FD3;
    Arg3 = 0;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x60) == 0) goto loc_00953FAC;
loc_00953F82:
    result = PdcpActivationClientTableCompareRoutine(*(uint64_t *)(v_stack_m28 + 0x38) + 600, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x60), Arg3, Arg4);
    Arg1 = 0;
    if (!sign_flag) goto loc_00953FA0;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x60)) == 0) goto loc_00954014;
loc_00953F9B:
    goto loc_00953F82;
loc_00953FA0:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x60)) + 0x8) != 0) goto loc_00953F9B;
loc_00953FAC:
    result = RtlAvlInsertNodeEx(*(uint64_t *)(v_stack_m28 + 0x40) + 96, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x60)), 1, *(uint64_t *)(v_stack_m28 + 0x38));
    local_r14 = 0;
loc_00953FBE:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x278 + 0x2B0)) = *(uint64_t *)(v_stack_m28 + 0x38);
    goto loc_00953EE0;
loc_00953FD3:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x50 + 0x8))) == (*(uint64_t *)(v_stack_m28 + 0x40) + 80)) goto loc_00954004;
loc_00953FE7:
    Arg1 = (uint32_t)((3) - (192));
    if (condition_is_equal) goto loc_00953FFD;
    Arg1 = (uint32_t)((Arg1) - (65));
    if (condition_is_equal) goto loc_00953FFD;
    if (((uint32_t)(Arg1)) == 1) goto loc_00953D46;
loc_00953FFD:
loc_00954004:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38)) = *(uint64_t *)(v_stack_m28 + 0x40) + 80;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8) = 5;
    *(uint64_t *)(5) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x50 + 0x8) = *(uint64_t *)(v_stack_m28 + 0x38);
    goto loc_00953FBE;
loc_00954014:
    goto loc_00953FAC;
loc_00954019:
    goto loc_00953EDB;
loc_00954023:
    goto loc_00953EDB;
loc_0095402D:
loc_00954030:
    goto loc_00953EDB;
loc_0095403A:
    goto loc_00953EDB;
loc_00954044:
    goto loc_00954050;
loc_0095404B:
loc_00954050:
    local_r14 = 0;
    goto loc_00953EDB;
loc_00954058:
loc_0095405F:
    goto loc_00954050;
loc_00954066:
    result = RtlStringCchCopyW(*(uint64_t *)(v_stack_m28 + 0x38) + 336, *(uint64_t *)(v_stack_m28 + 0x38) + 600, 5, *(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00953E3E;
loc_0095407A:
    result = RtlStringCchCopyW(local_rsp - 632 + 144, *(uint64_t *)(v_stack_m28 + 0x38) + 600, 5, *(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00953EB0;
loc_0095408E:
    result = PdcpResizeDiagnosticContext(local_rsp - 632 + 144, local_rsp - 632 + 424, 5, *(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00953EBD;
loc_0095409F:
    result = PdcReleaseRwLockExclusive2(0 + 8, local_rsp - 632 + 664, 5, *(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00953EF5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00953C70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
