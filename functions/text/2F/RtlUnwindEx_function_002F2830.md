# RtlUnwindEx

- RVA: `0x002F2830`–`0x002F2F27` (길이 `1,783` bytes)
- VA: `0x00000001402F2830`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00071F74`
- 디코드: `423`개 명령, `1,783/1,783` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x002F2895` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002F28A9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002F28D2` → [KeGetCurrentStackPointer](../6B/KeGetCurrentStackPointer_function_006B1070.md) (function, `0x006B1070`)
- `0x002F28E6` → [KeQueryCurrentStackInformationEx](KeQueryCurrentStackInformationEx_function_002F7CD0.md) (function, `0x002F7CD0`)
- `0x002F2902` → [RtlpGetStackLimits](RtlpGetStackLimits_function_002F5F50.md) (function, `0x002F5F50`)
- `0x002F2914` → [RtlRaiseStatus](RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x002F2955` → [RtlLookupFunctionEntry](RtlLookupFunctionEntry_function_002F2F30.md) (function, `0x002F2F30`)
- `0x002F2967` → [RtlpCopyContext](RtlpCopyContext_function_002F1E00.md) (function, `0x002F1E00`)
- `0x002F29C2` → [RtlpxVirtualUnwind](RtlpxVirtualUnwind_function_002F5110.md) (function, `0x002F5110`)
- `0x002F2AAB` → [RtlpExecuteHandlerForUnwind](../6B/RtlpExecuteHandlerForUnwind_function_006BB020.md) (function, `0x006BB020`)
- `0x002F2BA2` → [RtlGuardCheckExceptionHandler](RtlGuardCheckExceptionHandler_function_002F2038.md) (function, `0x002F2038`)
- `0x002F2BAD` → [RtlRestoreContext](../4F/RtlRestoreContext_function_004FE870.md) (function, `0x004FE870`)
- `0x002F2BBC` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002F2BE6` → [RtlRaiseStatus](RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x002F2C1B` → [RtlpCopyContext](RtlpCopyContext_function_002F1E00.md) (function, `0x002F1E00`)
- `0x002F2C31` → [RtlpCopyContext](RtlpCopyContext_function_002F1E00.md) (function, `0x002F1E00`)
- `0x002F2C65` → [RtlVirtualUnwind](../47/RtlVirtualUnwind_function_0047D210.md) (function, `0x0047D210`)
- `0x002F2CD4` → [RtlpGetStackLimitsEx](../45/RtlpGetStackLimitsEx_function_0045D2E0.md) (function, `0x0045D2E0`)
- `0x002F2D24` → [RtlGetExtendedContextLength](../3D/RtlGetExtendedContextLength_function_003D7190.md) (function, `0x003D7190`)
- `0x002F2D46` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x002F2D61` → [RtlInitializeExtendedContext](../3D/RtlInitializeExtendedContext_function_003D7220.md) (function, `0x003D7220`)
- `0x002F2D7F` → [RtlpValidateContextFlags2](../4E/RtlpValidateContextFlags2_function_004EF138.md) (function, `0x004EF138`)
- `0x002F2DC4` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x002F2DE2` → [RtlInitializeExtendedContext2](RtlInitializeExtendedContext2_function_002F5D40.md) (function, `0x002F5D40`)
- `0x002F2DF4` → [RtlCaptureContext2](../4F/RtlCaptureContext2_function_004FE6D0.md) (function, `0x004FE6D0`)
- `0x002F2E60` → [RtlpGetEntireXStateAreaLength2](../4E/RtlpGetEntireXStateAreaLength2_function_004EF20C.md) (function, `0x004EF20C`)
- `0x002F2E76` → [RtlpRemoveArchDisallowedXStateFeatures](RtlpRemoveArchDisallowedXStateFeatures_function_002F32FC.md) (function, `0x002F32FC`)
- `0x002F2EA3` → [RtlpGetStackLimitsEx](../45/RtlpGetStackLimitsEx_function_0045D2E0.md) (function, `0x0045D2E0`)
- `0x002F2EC1` → [RtlpExecuteHandlerForUnwind](../6B/RtlpExecuteHandlerForUnwind_function_006BB020.md) (function, `0x006BB020`)
- `0x002F2EF9` → [RtlGuardCheckLongJumpTarget](../5E/RtlGuardCheckLongJumpTarget_function_005EEF28.md) (function, `0x005EEF28`)
- `0x002F2F19` → [RtlRaiseStatus](RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x002F2F21` → [RtlRaiseStatus](RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)

### Direct callers
- [RtlUnwind](RtlUnwind_function_002F1CB0.md) at `0x002F1D91`
- [_C_specific_handler](../4F/_C_specific_handler_function_004FD410.md) at `0x004FD4ED`
- [KiSystemServiceHandler](../6C/KiSystemServiceHandler_function_006C48C0.md) at `0x006C490F`

### Static image references
- `0x002F284F` → RVA `0x00E0A740` (`.data`; read)
- `0x002F2B92` → RVA `0x01201841` (`CFGRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002F2F0E` → [sub_006DF260](../6D/Unknown_function_006DF260.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002F2830  40 55                           push rbp
002F2832  56                              push rsi
002F2833  57                              push rdi
002F2834  41 54                           push r12
002F2836  41 55                           push r13
002F2838  41 56                           push r14
002F283A  41 57                           push r15
002F283C  48 81 EC 00 02 00 00            sub rsp, 0x200
002F2843  48 8D 6C 24 60                  lea rbp, [rsp + 0x60]
002F2848  48 89 9D E0 01 00 00            mov qword ptr [rbp + 0x1e0], rbx
002F284F  48 8B 05 EA 7E B1 00            mov rax, qword ptr [rip + 0xb17eea]
002F2856  48 33 C5                        xor rax, rbp
002F2859  48 89 85 90 01 00 00            mov qword ptr [rbp + 0x190], rax
002F2860  48 8B 85 08 02 00 00            mov rax, qword ptr [rbp + 0x208]
002F2867  4D 8B E0                        mov r12, r8
002F286A  4C 8B AD 00 02 00 00            mov r13, qword ptr [rbp + 0x200]
002F2871  48 8B F9                        mov rdi, rcx
002F2874  48 89 55 78                     mov qword ptr [rbp + 0x78], rdx
002F2878  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
002F287F  33 D2                           xor edx, edx
002F2881  4C 89 45 50                     mov qword ptr [rbp + 0x50], r8
002F2885  4C 89 4D 70                     mov qword ptr [rbp + 0x70], r9
002F2889  4C 89 6D 60                     mov qword ptr [rbp + 0x60], r13
002F288D  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
002F2891  44 8D 42 50                     lea r8d, [rdx + 0x50]
002F2895  E8 A6 43 3D 00                  call 0x1406c6c40
002F289A  33 D2                           xor edx, edx
002F289C  48 8D 8D F0 00 00 00            lea rcx, [rbp + 0xf0]
002F28A3  41 B8 98 00 00 00               mov r8d, 0x98
002F28A9  E8 92 43 3D 00                  call 0x1406c6c40
002F28AE  45 33 FF                        xor r15d, r15d
002F28B1  32 DB                           xor bl, bl
002F28B3  4C 89 7D 38                     mov qword ptr [rbp + 0x38], r15
002F28B7  41 8B F7                        mov esi, r15d
002F28BA  4C 89 7D 40                     mov qword ptr [rbp + 0x40], r15
002F28BE  4C 89 7D 18                     mov qword ptr [rbp + 0x18], r15
002F28C2  4C 89 7D 30                     mov qword ptr [rbp + 0x30], r15
002F28C6  44 89 7D 00                     mov dword ptr [rbp], r15d
002F28CA  4C 89 7D 20                     mov qword ptr [rbp + 0x20], r15
002F28CE  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
002F28D2  E8 99 E7 3B 00                  call 0x1406b1070
002F28D7  48 8B C8                        mov rcx, rax
002F28DA  4C 8D 4D 18                     lea r9, [rbp + 0x18]
002F28DE  4C 8D 45 20                     lea r8, [rbp + 0x20]
002F28E2  48 8D 55 10                     lea rdx, [rbp + 0x10]
002F28E6  E8 E5 53 00 00                  call 0x1402f7cd0
002F28EB  83 7D 10 0A                     cmp dword ptr [rbp + 0x10], 0xa
002F28EF  48 8D 55 18                     lea rdx, [rbp + 0x18]
002F28F3  B8 01 00 00 00                  mov eax, 1
002F28F8  0F B6 DB                        movzx ebx, bl
002F28FB  48 8D 4D 20                     lea rcx, [rbp + 0x20]
002F28FF  0F 44 D8                        cmove ebx, eax
002F2902  E8 49 36 00 00                  call 0x1402f5f50
002F2907  84 C0                           test al, al
002F2909  0F 85 E9 03 00 00               jne 0x1402f2cf8
002F290F  B9 28 00 00 C0                  mov ecx, 0xc0000028
002F2914  E8 37 41 00 00                  call 0x1402f6a50
002F2919  CC                              int3
002F291A  4C 8B 7D 18                     mov r15, qword ptr [rbp + 0x18]
002F291E  48 85 FF                        test rdi, rdi
002F2921  4C 8B 65 20                     mov r12, qword ptr [rbp + 0x20]
002F2925  B8 06 00 00 00                  mov eax, 6
002F292A  41 BD 02 00 00 00               mov r13d, 2
002F2930  48 89 55 08                     mov qword ptr [rbp + 8], rdx
002F2934  44 0F 44 E8                     cmove r13d, eax
002F2938  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
002F2940  48 8B 86 F8 00 00 00            mov rax, qword ptr [rsi + 0xf8]
002F2947  48 8D 55 30                     lea rdx, [rbp + 0x30]
002F294B  4C 8B C1                        mov r8, rcx
002F294E  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
002F2952  48 8B C8                        mov rcx, rax
002F2955  E8 D6 05 00 00                  call 0x1402f2f30
002F295A  48 8B D6                        mov rdx, rsi
002F295D  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
002F2961  49 8B CE                        mov rcx, r14
002F2964  4C 8B C8                        mov r9, rax
002F2967  E8 94 F4 FF FF                  call 0x1402f1e00
002F296C  4C 8B 45 28                     mov r8, qword ptr [rbp + 0x28]
002F2970  48 8D 85 D0 00 00 00            lea rax, [rbp + 0xd0]
002F2977  48 8B 55 30                     mov rdx, qword ptr [rbp + 0x30]
002F297B  33 C9                           xor ecx, ecx
002F297D  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
002F2981  0F 57 D2                        xorps xmm2, xmm2
002F2984  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002F2989  48 8D 45 38                     lea rax, [rbp + 0x38]
002F298D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002F2992  48 8D 45 08                     lea rax, [rbp + 8]
002F2996  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002F299B  48 8D 45 40                     lea rax, [rbp + 0x40]
002F299F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002F29A4  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
002F29A9  48 89 8D E0 00 00 00            mov qword ptr [rbp + 0xe0], rcx
002F29B0  B9 02 00 00 00                  mov ecx, 2
002F29B5  F3 0F 7F 95 D0 00 00 00         movdqu xmmword ptr [rbp + 0xd0], xmm2
002F29BD  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
002F29C2  E8 49 27 00 00                  call 0x1402f5110
002F29C7  85 C0                           test eax, eax
002F29C9  0F 88 50 05 00 00               js 0x1402f2f1f
002F29CF  4C 8B 55 08                     mov r10, qword ptr [rbp + 8]
002F29D3  41 F6 C2 07                     test r10b, 7
002F29D7  0F 85 A4 04 00 00               jne 0x1402f2e81
002F29DD  4D 3B D4                        cmp r10, r12
002F29E0  0F 82 9B 04 00 00               jb 0x1402f2e81
002F29E6  4D 3B D7                        cmp r10, r15
002F29E9  0F 83 92 04 00 00               jae 0x1402f2e81
002F29EF  48 85 FF                        test rdi, rdi
002F29F2  74 0D                           je 0x1402f2a01
002F29F4  84 DB                           test bl, bl
002F29F6  75 09                           jne 0x1402f2a01
002F29F8  49 3B FA                        cmp rdi, r10
002F29FB  0F 82 0E FF FF FF               jb 0x1402f290f
002F2A01  48 83 7D 38 00                  cmp qword ptr [rbp + 0x38], 0
002F2A06  0F 84 27 01 00 00               je 0x1402f2b33
002F2A0C  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
002F2A10  45 33 F6                        xor r14d, r14d
002F2A13  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
002F2A1A  49 3B FA                        cmp rdi, r10
002F2A1D  75 04                           jne 0x1402f2a23
002F2A1F  41 83 CD 20                     or r13d, 0x20
002F2A23  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
002F2A27  4C 8D 8D 80 00 00 00            lea r9, [rbp + 0x80]
002F2A2E  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
002F2A32  4C 8B C6                        mov r8, rsi
002F2A35  44 89 69 04                     mov dword ptr [rcx + 4], r13d
002F2A39  48 89 46 78                     mov qword ptr [rsi + 0x78], rax
002F2A3D  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
002F2A41  48 8B 55 08                     mov rdx, qword ptr [rbp + 8]
002F2A45  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
002F2A4C  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
002F2A50  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
002F2A57  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
002F2A5B  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
002F2A62  48 8B 45 38                     mov rax, qword ptr [rbp + 0x38]
002F2A66  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
002F2A6D  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
002F2A71  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
002F2A78  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
002F2A7C  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
002F2A83  48 89 95 98 00 00 00            mov qword ptr [rbp + 0x98], rdx
002F2A8A  48 89 B5 A8 00 00 00            mov qword ptr [rbp + 0xa8], rsi
002F2A91  44 89 B5 C8 00 00 00            mov dword ptr [rbp + 0xc8], r14d
002F2A98  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
002F2A9B  25 40 00 10 00                  and eax, 0x100040
002F2AA0  3D 40 00 10 00                  cmp eax, 0x100040
002F2AA5  0F 84 16 04 00 00               je 0x1402f2ec1
002F2AAB  E8 70 85 3C 00                  call 0x1406bb020
002F2AB0  8B 56 30                        mov edx, dword ptr [rsi + 0x30]
002F2AB3  8B C8                           mov ecx, eax
002F2AB5  8B C2                           mov eax, edx
002F2AB7  25 40 00 10 00                  and eax, 0x100040
002F2ABC  3D 40 00 10 00                  cmp eax, 0x100040
002F2AC1  0F 84 06 04 00 00               je 0x1402f2ecd
002F2AC7  41 83 E5 9F                     and r13d, 0xffffff9f
002F2ACB  83 E9 01                        sub ecx, 1
002F2ACE  0F 85 08 01 00 00               jne 0x1402f2bdc
002F2AD4  48 39 7D 08                     cmp qword ptr [rbp + 8], rdi
002F2AD8  74 0B                           je 0x1402f2ae5
002F2ADA  48 8B C6                        mov rax, rsi
002F2ADD  48 8B 75 10                     mov rsi, qword ptr [rbp + 0x10]
002F2AE1  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
002F2AE5  0F AE 5D 00                     stmxcsr dword ptr [rbp]
002F2AE9  8B 45 00                        mov eax, dword ptr [rbp]
002F2AEC  89 46 34                        mov dword ptr [rsi + 0x34], eax
002F2AEF  89 86 18 01 00 00               mov dword ptr [rsi + 0x118], eax
002F2AF5  4C 8B 55 08                     mov r10, qword ptr [rbp + 8]
002F2AF9  41 F6 C5 40                     test r13b, 0x40
002F2AFD  0F 85 17 FF FF FF               jne 0x1402f2a1a
002F2B03  4C 8B 75 10                     mov r14, qword ptr [rbp + 0x10]
002F2B07  33 C0                           xor eax, eax
002F2B09  0F B6 CB                        movzx ecx, bl
002F2B0C  80 FB 02                        cmp bl, 2
002F2B0F  0F 45 C1                        cmovne eax, ecx
002F2B12  41 F6 C2 07                     test r10b, 7
002F2B16  75 2F                           jne 0x1402f2b47
002F2B18  4D 3B D7                        cmp r10, r15
002F2B1B  73 2A                           jae 0x1402f2b47
002F2B1D  4D 3B D4                        cmp r10, r12
002F2B20  72 25                           jb 0x1402f2b47
002F2B22  4C 3B D7                        cmp r10, rdi
002F2B25  74 29                           je 0x1402f2b50
002F2B27  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
002F2B2B  0F B6 D8                        movzx ebx, al
002F2B2E  E9 0D FE FF FF                  jmp 0x1402f2940
002F2B33  4C 3B D7                        cmp r10, rdi
002F2B36  74 CF                           je 0x1402f2b07
002F2B38  48 8B C6                        mov rax, rsi
002F2B3B  49 8B F6                        mov rsi, r14
002F2B3E  4C 8B F0                        mov r14, rax
002F2B41  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
002F2B45  EB C0                           jmp 0x1402f2b07
002F2B47  4C 3B D7                        cmp r10, rdi
002F2B4A  0F 85 B3 03 00 00               jne 0x1402f2f03
002F2B50  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
002F2B54  4C 8B 65 50                     mov r12, qword ptr [rbp + 0x50]
002F2B58  48 89 46 78                     mov qword ptr [rsi + 0x78], rax
002F2B5C  41 8B 04 24                     mov eax, dword ptr [r12]
002F2B60  3D 29 00 00 80                  cmp eax, 0x80000029
002F2B65  74 20                           je 0x1402f2b87
002F2B67  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
002F2B6B  48 89 86 F8 00 00 00            mov qword ptr [rsi + 0xf8], rax
002F2B72  41 8B 04 24                     mov eax, dword ptr [r12]
002F2B76  3D 26 00 00 80                  cmp eax, 0x80000026
002F2B7B  74 0A                           je 0x1402f2b87
002F2B7D  41 C7 04 24 27 00 00 C0         mov dword ptr [r12], 0xc0000027
002F2B85  EB 0B                           jmp 0x1402f2b92
002F2B87  3D 27 00 00 C0                  cmp eax, 0xc0000027
002F2B8C  0F 85 46 03 00 00               jne 0x1402f2ed8
002F2B92  80 3D A8 EC F0 00 00            cmp byte ptr [rip + 0xf0eca8], 0
002F2B99  75 0C                           jne 0x1402f2ba7
002F2B9B  48 8B 8E F8 00 00 00            mov rcx, qword ptr [rsi + 0xf8]
002F2BA2  E8 91 F4 FF FF                  call 0x1402f2038
002F2BA7  49 8B D4                        mov rdx, r12
002F2BAA  48 8B CE                        mov rcx, rsi
002F2BAD  E8 BE BC 20 00                  call 0x1404fe870
002F2BB2  48 8B 8D 90 01 00 00            mov rcx, qword ptr [rbp + 0x190]
002F2BB9  48 33 CD                        xor rcx, rbp
002F2BBC  E8 7F 9A 3B 00                  call 0x1406ac640
002F2BC1  48 8B 9D E0 01 00 00            mov rbx, qword ptr [rbp + 0x1e0]
002F2BC8  48 8D A5 A0 01 00 00            lea rsp, [rbp + 0x1a0]
002F2BCF  41 5F                           pop r15
002F2BD1  41 5E                           pop r14
002F2BD3  41 5D                           pop r13
002F2BD5  41 5C                           pop r12
002F2BD7  5F                              pop rdi
002F2BD8  5E                              pop rsi
002F2BD9  5D                              pop rbp
002F2BDA  C3                              ret
002F2BDB  CC                              int3
002F2BDC  83 F9 02                        cmp ecx, 2
002F2BDF  74 0B                           je 0x1402f2bec
002F2BE1  B9 26 00 00 C0                  mov ecx, 0xc0000026
002F2BE6  E8 65 3E 00 00                  call 0x1402f6a50
002F2BEB  CC                              int3
002F2BEC  4C 8B 9D 80 00 00 00            mov r11, qword ptr [rbp + 0x80]
002F2BF3  4C 8B 95 88 00 00 00            mov r10, qword ptr [rbp + 0x88]
002F2BFA  4C 8B 8D 90 00 00 00            mov r9, qword ptr [rbp + 0x90]
002F2C01  4C 8B 75 60                     mov r14, qword ptr [rbp + 0x60]
002F2C05  48 8B 95 A8 00 00 00            mov rdx, qword ptr [rbp + 0xa8]
002F2C0C  49 8B CE                        mov rcx, r14
002F2C0F  4C 89 5D 28                     mov qword ptr [rbp + 0x28], r11
002F2C13  4C 89 55 30                     mov qword ptr [rbp + 0x30], r10
002F2C17  4C 89 4D 58                     mov qword ptr [rbp + 0x58], r9
002F2C1B  E8 E0 F1 FF FF                  call 0x1402f1e00
002F2C20  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
002F2C24  49 8B D6                        mov rdx, r14
002F2C27  48 8B C8                        mov rcx, rax
002F2C2A  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
002F2C2E  49 8B F6                        mov rsi, r14
002F2C31  E8 CA F1 FF FF                  call 0x1402f1e00
002F2C36  48 C7 44 24 38 00 00 00 00      mov qword ptr [rsp + 0x38], 0
002F2C3F  48 8D 45 08                     lea rax, [rbp + 8]
002F2C43  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002F2C48  4D 8B C3                        mov r8, r11
002F2C4B  48 8D 45 40                     lea rax, [rbp + 0x40]
002F2C4F  49 8B D2                        mov rdx, r10
002F2C52  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002F2C57  B9 02 00 00 00                  mov ecx, 2
002F2C5C  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
002F2C60  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002F2C65  E8 A6 A5 18 00                  call 0x14047d210
002F2C6A  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
002F2C6E  48 3B 85 B0 00 00 00            cmp rax, qword ptr [rbp + 0xb0]
002F2C75  75 7A                           jne 0x1402f2cf1
002F2C77  4C 8B 55 08                     mov r10, qword ptr [rbp + 8]
002F2C7B  4C 3B 95 98 00 00 00            cmp r10, qword ptr [rbp + 0x98]
002F2C82  75 6D                           jne 0x1402f2cf1
002F2C84  48 8B 85 B8 00 00 00            mov rax, qword ptr [rbp + 0xb8]
002F2C8B  48 39 45 40                     cmp qword ptr [rbp + 0x40], rax
002F2C8F  75 60                           jne 0x1402f2cf1
002F2C91  48 8B 85 C0 00 00 00            mov rax, qword ptr [rbp + 0xc0]
002F2C98  41 83 CD 40                     or r13d, 0x40
002F2C9C  44 8B B5 C8 00 00 00            mov r14d, dword ptr [rbp + 0xc8]
002F2CA3  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
002F2CA7  41 F6 C2 07                     test r10b, 7
002F2CAB  75 05                           jne 0x1402f2cb2
002F2CAD  4D 3B D7                        cmp r10, r15
002F2CB0  72 34                           jb 0x1402f2ce6
002F2CB2  80 FB 01                        cmp bl, 1
002F2CB5  0F 85 3E FE FF FF               jne 0x1402f2af9
002F2CBB  4C 8B CE                        mov r9, rsi
002F2CBE  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
002F2CC7  4C 8D 45 18                     lea r8, [rbp + 0x18]
002F2CCB  49 8B CA                        mov rcx, r10
002F2CCE  48 8D 55 20                     lea rdx, [rbp + 0x20]
002F2CD2  B3 02                           mov bl, 2
002F2CD4  E8 07 A6 16 00                  call 0x14045d2e0
002F2CD9  4C 8B 7D 18                     mov r15, qword ptr [rbp + 0x18]
002F2CDD  4C 8B 65 20                     mov r12, qword ptr [rbp + 0x20]
002F2CE1  E9 0F FE FF FF                  jmp 0x1402f2af5
002F2CE6  4D 3B D4                        cmp r10, r12
002F2CE9  0F 83 0A FE FF FF               jae 0x1402f2af9
002F2CEF  EB C1                           jmp 0x1402f2cb2
002F2CF1  B9 27 00 00 00                  mov ecx, 0x27
002F2CF6  CD 29                           int 0x29
002F2CF8  40 38 35 42 EB F0 00            cmp byte ptr [rip + 0xf0eb42], sil
002F2CFF  41 BE 0B 00 10 00               mov r14d, 0x10000b
002F2D05  74 5F                           je 0x1402f2d66
002F2D07  41 8B 45 30                     mov eax, dword ptr [r13 + 0x30]
002F2D0B  41 BE 8B 00 10 00               mov r14d, 0x10008b
002F2D11  25 80 00 10 00                  and eax, 0x100080
002F2D16  3D 80 00 10 00                  cmp eax, 0x100080
002F2D1B  74 49                           je 0x1402f2d66
002F2D1D  48 8D 55 00                     lea rdx, [rbp]
002F2D21  41 8B CE                        mov ecx, r14d
002F2D24  E8 67 44 0E 00                  call 0x1403d7190
002F2D29  8B 75 00                        mov esi, dword ptr [rbp]
002F2D2C  48 8D 4E 0F                     lea rcx, [rsi + 0xf]
002F2D30  48 3B CE                        cmp rcx, rsi
002F2D33  77 0A                           ja 0x1402f2d3f
002F2D35  48 B9 F0 FF FF FF FF FF FF 0F   movabs rcx, 0xffffffffffffff0
002F2D3F  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
002F2D43  48 8B C1                        mov rax, rcx
002F2D46  E8 15 7C 3C 00                  call 0x1406ba960
002F2D4B  48 2B E1                        sub rsp, rcx
002F2D4E  4C 8D 45 58                     lea r8, [rbp + 0x58]
002F2D52  41 8B D6                        mov edx, r14d
002F2D55  4C 8D 6C 24 60                  lea r13, [rsp + 0x60]
002F2D5A  49 8B CD                        mov rcx, r13
002F2D5D  4C 89 6D 60                     mov qword ptr [rbp + 0x60], r13
002F2D61  E8 BA 44 0E 00                  call 0x1403d7220
002F2D66  49 B8 D8 03 00 00 80 F7 FF FF   movabs r8, 0xfffff780000003d8
002F2D70  4C 89 7D 28                     mov qword ptr [rbp + 0x28], r15
002F2D74  48 8D 55 00                     lea rdx, [rbp]
002F2D78  44 89 7D 00                     mov dword ptr [rbp], r15d
002F2D7C  41 8B CE                        mov ecx, r14d
002F2D7F  E8 B4 C3 1F 00                  call 0x1404ef138
002F2D84  85 C0                           test eax, eax
002F2D86  78 20                           js 0x1402f2da8
002F2D88  44 8B 5D 00                     mov r11d, dword ptr [rbp]
002F2D8C  B8 F0 04 00 00                  mov eax, 0x4f0
002F2D91  41 F6 C3 02                     test r11b, 2
002F2D95  0F 85 AB 00 00 00               jne 0x1402f2e46
002F2D9B  41 F6 C3 04                     test r11b, 4
002F2D9F  8D 70 20                        lea esi, [rax + 0x20]
002F2DA2  0F 44 F0                        cmove esi, eax
002F2DA5  83 C6 0F                        add esi, 0xf
002F2DA8  8B C6                           mov eax, esi
002F2DAA  48 8D 48 0F                     lea rcx, [rax + 0xf]
002F2DAE  48 3B C8                        cmp rcx, rax
002F2DB1  77 0A                           ja 0x1402f2dbd
002F2DB3  48 B9 F0 FF FF FF FF FF FF 0F   movabs rcx, 0xffffffffffffff0
002F2DBD  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
002F2DC1  48 8B C1                        mov rax, rcx
002F2DC4  E8 97 7B 3C 00                  call 0x1406ba960
002F2DC9  48 2B E1                        sub rsp, rcx
002F2DCC  4C 8D 45 58                     lea r8, [rbp + 0x58]
002F2DD0  45 33 C9                        xor r9d, r9d
002F2DD3  41 8B D6                        mov edx, r14d
002F2DD6  4C 8D 7C 24 60                  lea r15, [rsp + 0x60]
002F2DDB  49 8B CF                        mov rcx, r15
002F2DDE  4C 89 7D 68                     mov qword ptr [rbp + 0x68], r15
002F2DE2  E8 59 2F 00 00                  call 0x1402f5d40
002F2DE7  49 8B CD                        mov rcx, r13
002F2DEA  4C 89 7D 10                     mov qword ptr [rbp + 0x10], r15
002F2DEE  49 8B F5                        mov rsi, r13
002F2DF1  4D 8B F7                        mov r14, r15
002F2DF4  E8 D7 B8 20 00                  call 0x1404fe6d0
002F2DF9  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
002F2DFD  48 85 C9                        test rcx, rcx
002F2E00  74 04                           je 0x1402f2e06
002F2E02  C6 41 06 01                     mov byte ptr [rcx + 6], 1
002F2E06  33 D2                           xor edx, edx
002F2E08  4D 85 E4                        test r12, r12
002F2E0B  0F 85 09 FB FF FF               jne 0x1402f291a
002F2E11  C7 85 F0 00 00 00 27 00 00 C0   mov dword ptr [rbp + 0xf0], 0xc0000027
002F2E1B  4C 8D A5 F0 00 00 00            lea r12, [rbp + 0xf0]
002F2E22  48 89 95 F8 00 00 00            mov qword ptr [rbp + 0xf8], rdx
002F2E29  49 8B 85 F8 00 00 00            mov rax, qword ptr [r13 + 0xf8]
002F2E30  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
002F2E37  4C 89 65 50                     mov qword ptr [rbp + 0x50], r12
002F2E3B  89 95 08 01 00 00               mov dword ptr [rbp + 0x108], edx
002F2E41  E9 D4 FA FF FF                  jmp 0x1402f291a
002F2E46  A1 EC 03 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000003ec]
002F2E4F  A8 02                           test al, 2
002F2E51  75 1C                           jne 0x1402f2e6f
002F2E53  48 BA D8 03 00 00 80 F7 FF FF   movabs rdx, 0xfffff780000003d8
002F2E5D  49 8B CF                        mov rcx, r15
002F2E60  E8 A7 C3 1F 00                  call 0x1404ef20c
002F2E65  05 20 03 00 00                  add eax, 0x320
002F2E6A  E9 2C FF FF FF                  jmp 0x1402f2d9b
002F2E6F  48 8D 55 28                     lea rdx, [rbp + 0x28]
002F2E73  41 8B CE                        mov ecx, r14d
002F2E76  E8 81 04 00 00                  call 0x1402f32fc
002F2E7B  4C 8B 7D 28                     mov r15, qword ptr [rbp + 0x28]
002F2E7F  EB D2                           jmp 0x1402f2e53
002F2E81  80 FB 01                        cmp bl, 1
002F2E84  0F 85 85 FA FF FF               jne 0x1402f290f
002F2E8A  4C 8B CE                        mov r9, rsi
002F2E8D  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
002F2E96  4C 8D 45 18                     lea r8, [rbp + 0x18]
002F2E9A  49 8B CA                        mov rcx, r10
002F2E9D  48 8D 55 20                     lea rdx, [rbp + 0x20]
002F2EA1  B3 02                           mov bl, 2
002F2EA3  E8 38 A4 16 00                  call 0x14045d2e0
002F2EA8  84 C0                           test al, al
002F2EAA  0F 84 5F FA FF FF               je 0x1402f290f
002F2EB0  4C 8B 55 08                     mov r10, qword ptr [rbp + 8]
002F2EB4  4C 8B 7D 18                     mov r15, qword ptr [rbp + 0x18]
002F2EB8  4C 8B 65 20                     mov r12, qword ptr [rbp + 0x20]
002F2EBC  E9 2E FB FF FF                  jmp 0x1402f29ef
002F2EC1  E8 5A 81 3C 00                  call 0x1406bb020
002F2EC6  8B C8                           mov ecx, eax
002F2EC8  E9 FA FB FF FF                  jmp 0x1402f2ac7
002F2ECD  83 E2 BF                        and edx, 0xffffffbf
002F2ED0  89 56 30                        mov dword ptr [rsi + 0x30], edx
002F2ED3  E9 EF FB FF FF                  jmp 0x1402f2ac7
002F2ED8  3D 26 00 00 80                  cmp eax, 0x80000026
002F2EDD  0F 85 C4 FC FF FF               jne 0x1402f2ba7
002F2EE3  80 3D 57 E9 F0 00 00            cmp byte ptr [rip + 0xf0e957], 0
002F2EEA  49 8B 4C 24 20                  mov rcx, qword ptr [r12 + 0x20]
002F2EEF  0F 85 B2 FC FF FF               jne 0x1402f2ba7
002F2EF5  48 8B 49 50                     mov rcx, qword ptr [rcx + 0x50]
002F2EF9  E8 2A C0 2F 00                  call 0x1405eef28
002F2EFE  E9 A4 FC FF FF                  jmp 0x1402f2ba7
002F2F03  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
002F2F07  48 3B 86 F8 00 00 00            cmp rax, qword ptr [rsi + 0xf8]
002F2F0E  0F 85 4C C3 3E 00               jne 0x1406df260
002F2F14  B9 FF 00 00 C0                  mov ecx, 0xc00000ff
002F2F19  E8 32 3B 00 00                  call 0x1402f6a50
002F2F1E  CC                              int3
002F2F1F  8B C8                           mov ecx, eax
002F2F21  E8 2A 3B 00 00                  call 0x1402f6a50
002F2F26  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlUnwindEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (512);
    v_stack_p8 = v_rbx;
    result = (*(unsigned __int64 *)(v_rip + 11632362)) ^ (v_stack_m1D8);
    v_stack_m48 = result;
    v_stack_m160 = a2;
    a2 = 0;
    v_stack_m188 = a3;
    v_stack_m168 = a4;
    v_stack_m178 = a5;
    v_stack_m190 = a6;
    result = memset(v_stack_m158, a2, a2 + 80, a4);
    a2 = 0;
    result = memset(v_stack_mE8, a2, 152, a4);
    v_r15 = 0;
    v_rbx = 0;
    v_stack_m1A0 = 0;
    v_stack_m198 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1A8 = 0;
    v_stack_m1D8 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1C8 = 0;
    result = KeGetCurrentStackPointer(v_stack_mE8, a2, 152, a4);
    result = KeQueryCurrentStackInformationEx(result, v_stack_m1C8, v_stack_m1B8, v_stack_m1C0);
    v_rbx = 0;
    if (v_stack_m1C8 == 10) { v_rbx = 1; }
    result = RtlpGetStackLimits(v_stack_m1B8, v_stack_m1C0, v_stack_m1B8, v_stack_m1C0);
    if ((unsigned __int8)(result) != 0) goto loc_002F2CF8;
loc_002F290F:
    result = RtlRaiseStatus((unsigned int)(0xC0000028ULL), v_stack_m1C0, v_stack_m1B8, v_stack_m1C0);
loc_002F291A:
    v_stack_m1D0 = v_stack_m1C0;
    v_r13 = 2;
    if (a1 == 0) { v_r13 = 6; }
loc_002F2940:
    v_stack_m1B0 = *(unsigned __int64 *)(0 + 248);
    result = RtlLookupFunctionEntry(*(unsigned __int64 *)(0 + 248), v_stack_m1A8, (unsigned int)(0xC0000028ULL), v_stack_m1C0);
    v_stack_m180 = result;
    result = RtlpCopyContext(v_r14, 0, (unsigned int)(0xC0000028ULL), result);
    a1 = 0;
    v_stack_m1E8 = 0;
    v_stack_m1F0 = v_stack_m108;
    v_stack_m1F8 = v_stack_m1A0;
    v_stack_m200 = v_stack_m1D0;
    v_stack_m208 = v_stack_m198;
    v_stack_m210 = 0;
    v_stack_mF8 = 0;
    v_stack_m108 = v_xmm2;
    v_stack_m218 = v_r14;
    result = RtlpxVirtualUnwind(2, v_stack_m1A8, v_stack_m1B0, result);
    if (sign_flag) goto loc_002F2F1F;
    if ((((unsigned __int8)(v_stack_m1D0)) & (7)) != 0) goto loc_002F2E81;
    if (v_stack_m1D0 < v_stack_m1B8) goto loc_002F2E81;
    if (v_stack_m1D0 >= v_stack_m1C0) goto loc_002F2E81;
loc_002F29EF:
    if (0 == 0) goto loc_002F2A01;
    if ((unsigned __int8)(v_rbx) != 0) goto loc_002F2A01;
    if (0 < v_stack_m1D0) goto loc_002F290F;
loc_002F2A01:
    if (v_stack_m1A0 == 0) goto loc_002F2B33;
    v_r14 = 0;
    v_stack_m138 = v_stack_m160;
loc_002F2A1A:
    if (0 == v_stack_m1D0) {
        v_r13 = (unsigned int)((v_r13) | (32));
    }
    *(unsigned int *)(v_stack_m188 + 4) = (unsigned int)(v_r13);
    *(unsigned __int64 *)(0 + 120) = v_stack_m168;
    v_stack_m158 = v_stack_m1B0;
    v_stack_m150 = v_stack_m1A8;
    v_stack_m148 = v_stack_m180;
    v_stack_m128 = v_stack_m1A0;
    v_stack_m120 = v_stack_m198;
    v_stack_m118 = v_stack_m190;
    v_stack_m140 = v_stack_m1D0;
    v_stack_m130 = 0;
    v_stack_m110 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 48))) & (0x100040ULL));
    if (((unsigned int)(result)) == 0x100040ULL) goto loc_002F2EC1;
    result = RtlpExecuteHandlerForUnwind(v_stack_m188, v_stack_m1D0, 0, v_stack_m158);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 48))))) & (0x100040ULL));
    if (((unsigned int)(result)) == 0x100040ULL) goto loc_002F2ECD;
loc_002F2AC7:
    v_r13 = (unsigned int)((v_r13) & (0xFFFFFF9FULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (1));
    if (condition_is_not_equal) goto loc_002F2BDC;
    v_rsi = 0;
    if (v_stack_m1D0 != a1) {
        result = 0;
        v_rsi = v_stack_m1C8;
        v_stack_m1C8 = result;
    }
    *(unsigned int *)(v_rsi + 52) = (unsigned int)((unsigned int)(v_stack_m1D8));
    *(unsigned int *)(v_rsi + 280) = (unsigned int)((unsigned int)(v_stack_m1D8));
loc_002F2AF5:
loc_002F2AF9:
    if ((((unsigned __int8)(v_r13)) & (64)) != 0) goto loc_002F2A1A;
loc_002F2B07:
    result = 0;
    if (((unsigned __int8)(v_rbx)) != 2) { result = (unsigned int)((unsigned __int8)(v_rbx)); }
    if ((((unsigned __int8)(v_stack_m1D0)) & (7)) != 0) goto loc_002F2B47;
    if (v_stack_m1D0 >= v_stack_m1C0) goto loc_002F2B47;
    if (v_stack_m1D0 < v_stack_m1B8) goto loc_002F2B47;
    if (v_stack_m1D0 == a1) goto loc_002F2B50;
    goto loc_002F2940;
loc_002F2B33:
    if (v_stack_m1D0 == a1) goto loc_002F2B07;
    v_stack_m1C8 = v_rsi;
    goto loc_002F2B07;
loc_002F2B47:
    if (v_stack_m1D0 != a1) goto loc_002F2F03;
loc_002F2B50:
    *(unsigned __int64 *)(v_stack_m1C8 + 120) = v_stack_m168;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188)))) == 0x80000029ULL) goto loc_002F2B87;
    *(unsigned __int64 *)(v_stack_m1C8 + 248) = v_stack_m160;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188)))) == 0x80000026ULL) goto loc_002F2B87;
    *(unsigned int *)(v_stack_m188) = 0xC0000027ULL;
    goto loc_002F2B92;
loc_002F2B87:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188)))) != 0xC0000027ULL) goto loc_002F2ED8;
loc_002F2B92:
    result = (unsigned int)(*(unsigned int *)(v_stack_m188));
    if ((*(unsigned __int8 *)(v_rip + 15789224)) == 0) {
        a1 = *(unsigned __int64 *)(v_stack_m1C8 + 248);
        result = RtlGuardCheckExceptionHandler(a1, (unsigned int)(*(unsigned int *)(0 + 48)), 0, v_stack_m158);
    }
    result = RtlRestoreContext(v_stack_m1C8, v_stack_m188, 0, v_stack_m158);
    a1 = (v_stack_m48) ^ (v_stack_m1D8);
    result = _security_check_cookie(a1, v_stack_m188, 0, v_stack_m158);
    return result;
loc_002F2BDC:
    if (((unsigned int)(a1)) != 2) {
        a1 = 0xC0000026ULL;
        result = RtlRaiseStatus(a1, v_stack_m188, 0, v_stack_m158);
    }
    v_stack_m1B0 = v_stack_m158;
    v_stack_m1A8 = v_stack_m150;
    v_stack_m180 = v_stack_m148;
    result = RtlpCopyContext(v_stack_m178, v_stack_m130, 0, v_stack_m148);
    v_stack_m1C8 = v_stack_m170;
    result = RtlpCopyContext(v_stack_m170, v_stack_m178, 0, v_stack_m148);
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_m1D0;
    v_stack_p28 = v_stack_m198;
    v_stack_p20 = v_stack_m170;
    result = RtlVirtualUnwind(2, v_stack_m150, v_stack_m158, v_stack_m148);
    v_stack_m1A0 = result;
    if (result != v_stack_m128) goto loc_002F2CF1;
    if (v_stack_m1D0 != v_stack_m140) goto loc_002F2CF1;
    if (v_stack_m198 != v_stack_m120) goto loc_002F2CF1;
    v_r13 = (unsigned int)((v_r13) | (64));
    v_stack_m190 = v_stack_m118;
    if ((((unsigned __int8)(v_stack_m1D0)) & (7)) != 0) goto loc_002F2CB2;
    if (v_stack_m1D0 < v_stack_m1C0) goto loc_002F2CE6;
loc_002F2CB2:
    if (((unsigned __int8)(v_stack_p8)) != 1) goto loc_002F2AF9;
    v_stack_p20 = 0;
    result = RtlpGetStackLimitsEx(v_stack_m1D0, v_stack_m1B8, v_stack_m1C0, v_stack_m178);
    goto loc_002F2AF5;
loc_002F2CE6:
    if (v_stack_m1D0 >= v_stack_m1B8) goto loc_002F2AF9;
    goto loc_002F2CB2;
loc_002F2CF1:
loc_002F2CF8:
    if ((*(unsigned __int8 *)(v_rip + 15788866)) == ((unsigned __int8)(v_stack_m178))) goto loc_002F2D66;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r13 + 48))) & (0x100080ULL));
    if (((unsigned int)(result)) == 0x100080ULL) goto loc_002F2D66;
    result = RtlGetExtendedContextLength((unsigned int)((unsigned int)((unsigned int)(0x10008BULL))), v_stack_m1D8, v_stack_m1C0, v_stack_m178);
    if (((unsigned int)(v_stack_m1D8) + 15) <= ((unsigned int)(v_stack_m1D8))) {
    }
    a1 = ((unsigned int)(v_stack_m1D8) + 15) & (-16);
    result = _chkstk(a1, v_stack_m1D8, v_stack_m1C0, v_stack_m178);
    v_rsp = (v_stack_m38) - (a1);
    v_stack_m178 = v_stack_p60;
    result = RtlInitializeExtendedContext(v_stack_p60, (unsigned int)((unsigned int)((unsigned int)(0x10008BULL))), v_stack_m180, v_stack_m178);
loc_002F2D66:
    v_stack_m1B0 = v_stack_m1C0;
    v_stack_m1D8 = (unsigned int)(v_stack_m1C0);
    result = RtlpValidateContextFlags2((unsigned int)((unsigned int)((unsigned int)(0x10008BULL))), v_stack_m1D8, v_stack_m180, v_stack_m178);
    if (sign_flag) goto loc_002F2DA8;
    if ((((unsigned __int8)((unsigned int)(v_stack_m1D8))) & (2)) != 0) goto loc_002F2E46;
loc_002F2D9B:
    v_rsi = (unsigned int)(0x4F0ULL) + 32;
    if ((((unsigned __int8)((unsigned int)(v_stack_m1D8))) & (4)) == 0) { v_rsi = (unsigned int)((unsigned int)(0x4F0ULL)); }
    v_rsi = (unsigned int)((v_rsi) + (15));
loc_002F2DA8:
    if (((unsigned int)((unsigned int)(v_rsi)) + 15) <= ((unsigned int)((unsigned int)(v_rsi)))) {
    }
    a1 = ((unsigned int)((unsigned int)(v_rsi)) + 15) & (-16);
    result = _chkstk(a1, v_stack_m1D8, v_stack_m180, v_stack_m178);
    v_rsp = (v_rsp) - (a1);
    a4 = 0;
    v_stack_m170 = v_stack_p60;
    result = RtlInitializeExtendedContext2(v_stack_p60, (unsigned int)((unsigned int)((unsigned int)(0x10008BULL))), v_stack_m180, a4);
    v_stack_m1C8 = v_stack_p60;
    result = RtlCaptureContext2(v_stack_p60, (unsigned int)((unsigned int)((unsigned int)(0x10008BULL))), v_stack_m180, a4);
    if (v_stack_m190 != 0) {
        *(unsigned __int8 *)(v_stack_m190 + 6) = 1;
    }
    a2 = 0;
    if (v_stack_m1B8 != 0) goto loc_002F291A;
    v_stack_mE8 = 0xC0000027ULL;
    v_stack_mE0 = 0;
    v_stack_mD8 = *(unsigned __int64 *)(v_stack_p60 + 248);
    v_stack_m188 = v_stack_mE8;
    v_stack_mD0 = 0;
    goto loc_002F291A;
loc_002F2E46:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p60 + 248))) & (2)) != 0) goto loc_002F2E6F;
loc_002F2E53:
    result = RtlpGetEntireXStateAreaLength2(v_stack_p60, a2, v_stack_m180, a4);
    result = (unsigned int)((result) + (800));
    goto loc_002F2D9B;
loc_002F2E6F:
    result = RtlpRemoveArchDisallowedXStateFeatures((unsigned int)((unsigned int)(v_stack_p60)), v_stack_m1B0, v_stack_m180, a4);
    goto loc_002F2E53;
loc_002F2E81:
    if (2 != 1) goto loc_002F290F;
    v_stack_p20 = 0;
    result = RtlpGetStackLimitsEx(v_stack_m1D0, v_stack_m1B8, v_stack_m1C0, v_stack_p60);
    if ((unsigned __int8)(result) == 0) goto loc_002F290F;
    goto loc_002F29EF;
loc_002F2EC1:
    result = RtlpExecuteHandlerForUnwind(v_stack_m1D0, v_stack_m1B8, v_stack_m1C0, v_stack_p60);
    goto loc_002F2AC7;
loc_002F2ECD:
    a2 = (unsigned int)((v_stack_m1B8) & (0xFFFFFFBFULL));
    *(unsigned int *)(v_stack_p60 + 48) = (unsigned int)(a2);
    goto loc_002F2AC7;
loc_002F2ED8:
    if (((unsigned int)(result)) != 0x80000026ULL) goto loc_002F2BA7;
    if ((*(unsigned __int8 *)(v_rip + 15788375)) != 0) goto loc_002F2BA7;
    result = RtlGuardCheckLongJumpTarget(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1B8 + 32) + 80), a2, v_stack_m1C0, v_stack_p60);
    goto loc_002F2BA7;
loc_002F2F03:
    result = RtlRaiseStatus((unsigned int)(0xC00000FFULL), a2, v_stack_m1C0, v_stack_p60);
loc_002F2F1F:
    result = RtlRaiseStatus((unsigned int)((unsigned int)(result)), a2, v_stack_m1C0, v_stack_p60);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlUnwindEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p60;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (512);
    v_stack_p8 = local_rbx;
    result = (*(uint64_t *)(v_rip + 0xB17EEA)) ^ (v_stack_m1D8);
    v_stack_m48 = result;
    v_stack_m160 = Arg2;
    Arg2 = 0;
    v_stack_m188 = Arg3;
    v_stack_m168 = Arg4;
    v_stack_m178 = Arg5;
    v_stack_m190 = Arg6;
    result = memset(v_stack_m158, Arg2, Arg2 + 80, Arg4);
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, 152, Arg4);
    local_r15 = 0;
    local_rbx = 0;
    v_stack_m1A0 = 0;
    v_stack_m198 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1A8 = 0;
    v_stack_m1D8 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1C8 = 0;
    result = KeGetCurrentStackPointer(v_stack_mE8, Arg2, 152, Arg4);
    result = KeQueryCurrentStackInformationEx(result, v_stack_m1C8, v_stack_m1B8, v_stack_m1C0);
    local_rbx = 0;
    if (v_stack_m1C8 == 10) { local_rbx = 1; }
    result = RtlpGetStackLimits(v_stack_m1B8, v_stack_m1C0, v_stack_m1B8, v_stack_m1C0);
    if ((uint8_t)(result) != 0) goto loc_002F2CF8;
loc_002F290F:
    result = RtlRaiseStatus((uint32_t)(0xC0000028ULL), v_stack_m1C0, v_stack_m1B8, v_stack_m1C0);
loc_002F291A:
    v_stack_m1D0 = v_stack_m1C0;
    local_r13 = 2;
    if (Arg1 == 0) { local_r13 = 6; }
loc_002F2940:
    v_stack_m1B0 = *(uint64_t *)(0 + 0xF8);
    result = RtlLookupFunctionEntry(*(uint64_t *)(0 + 0xF8), v_stack_m1A8, (uint32_t)(0xC0000028ULL), v_stack_m1C0);
    v_stack_m180 = result;
    result = RtlpCopyContext(local_r14, 0, (uint32_t)(0xC0000028ULL), result);
    Arg1 = 0;
    v_stack_m1E8 = 0;
    v_stack_m1F0 = v_stack_m108;
    v_stack_m1F8 = v_stack_m1A0;
    v_stack_m200 = v_stack_m1D0;
    v_stack_m208 = v_stack_m198;
    v_stack_m210 = 0;
    v_stack_mF8 = 0;
    v_stack_m108 = v_xmm2;
    v_stack_m218 = local_r14;
    result = RtlpxVirtualUnwind(2, v_stack_m1A8, v_stack_m1B0, result);
    if (sign_flag) goto loc_002F2F1F;
    if ((((uint8_t)(v_stack_m1D0)) & (7)) != 0) goto loc_002F2E81;
    if (v_stack_m1D0 < v_stack_m1B8) goto loc_002F2E81;
    if (v_stack_m1D0 >= v_stack_m1C0) goto loc_002F2E81;
loc_002F29EF:
    if (0 == 0) goto loc_002F2A01;
    if ((uint8_t)(local_rbx) != 0) goto loc_002F2A01;
    if (0 < v_stack_m1D0) goto loc_002F290F;
loc_002F2A01:
    if (v_stack_m1A0 == 0) goto loc_002F2B33;
    local_r14 = 0;
    v_stack_m138 = v_stack_m160;
loc_002F2A1A:
    if (0 == v_stack_m1D0) {
        local_r13 = (uint32_t)((local_r13) | (32));
    }
    *(uint32_t *)(v_stack_m188 + 0x4) = (uint32_t)(local_r13);
    *(uint64_t *)(0 + 0x78) = v_stack_m168;
    v_stack_m158 = v_stack_m1B0;
    v_stack_m150 = v_stack_m1A8;
    v_stack_m148 = v_stack_m180;
    v_stack_m128 = v_stack_m1A0;
    v_stack_m120 = v_stack_m198;
    v_stack_m118 = v_stack_m190;
    v_stack_m140 = v_stack_m1D0;
    v_stack_m130 = 0;
    v_stack_m110 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x30))) & (0x100040ULL));
    if (((uint32_t)(result)) == 0x100040ULL) goto loc_002F2EC1;
    result = RtlpExecuteHandlerForUnwind(v_stack_m188, v_stack_m1D0, 0, v_stack_m158);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x30))))) & (0x100040ULL));
    if (((uint32_t)(result)) == 0x100040ULL) goto loc_002F2ECD;
loc_002F2AC7:
    local_r13 = (uint32_t)((local_r13) & (0xFFFFFF9FULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (1));
    if (condition_is_not_equal) goto loc_002F2BDC;
    local_rsi = 0;
    if (v_stack_m1D0 != Arg1) {
        result = 0;
        local_rsi = v_stack_m1C8;
        v_stack_m1C8 = result;
    }
    *(uint32_t *)(local_rsi + 0x34) = (uint32_t)((uint32_t)(v_stack_m1D8));
    *(uint32_t *)(local_rsi + 0x118) = (uint32_t)((uint32_t)(v_stack_m1D8));
loc_002F2AF5:
loc_002F2AF9:
    if ((((uint8_t)(local_r13)) & (64)) != 0) goto loc_002F2A1A;
loc_002F2B07:
    result = 0;
    if (((uint8_t)(local_rbx)) != 2) { result = (uint32_t)((uint8_t)(local_rbx)); }
    if ((((uint8_t)(v_stack_m1D0)) & (7)) != 0) goto loc_002F2B47;
    if (v_stack_m1D0 >= v_stack_m1C0) goto loc_002F2B47;
    if (v_stack_m1D0 < v_stack_m1B8) goto loc_002F2B47;
    if (v_stack_m1D0 == Arg1) goto loc_002F2B50;
    goto loc_002F2940;
loc_002F2B33:
    if (v_stack_m1D0 == Arg1) goto loc_002F2B07;
    v_stack_m1C8 = local_rsi;
    goto loc_002F2B07;
loc_002F2B47:
    if (v_stack_m1D0 != Arg1) goto loc_002F2F03;
loc_002F2B50:
    *(uint64_t *)(v_stack_m1C8 + 0x78) = v_stack_m168;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188)))) == 0x80000029ULL) goto loc_002F2B87;
    *(uint64_t *)(v_stack_m1C8 + 0xF8) = v_stack_m160;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188)))) == 0x80000026ULL) goto loc_002F2B87;
    *(uint32_t *)(v_stack_m188) = 0xC0000027ULL;
    goto loc_002F2B92;
loc_002F2B87:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188)))) != 0xC0000027ULL) goto loc_002F2ED8;
loc_002F2B92:
    result = (uint32_t)(*(uint32_t *)(v_stack_m188));
    if ((*(uint8_t *)(v_rip + 0xF0ECA8)) == 0) {
        Arg1 = *(uint64_t *)(v_stack_m1C8 + 0xF8);
        result = RtlGuardCheckExceptionHandler(Arg1, (uint32_t)(*(uint32_t *)(0 + 0x30)), 0, v_stack_m158);
    }
    result = RtlRestoreContext(v_stack_m1C8, v_stack_m188, 0, v_stack_m158);
    Arg1 = (v_stack_m48) ^ (v_stack_m1D8);
    result = _security_check_cookie(Arg1, v_stack_m188, 0, v_stack_m158);
    return result;
loc_002F2BDC:
    if (((uint32_t)(Arg1)) != 2) {
        Arg1 = 0xC0000026ULL;
        result = RtlRaiseStatus(Arg1, v_stack_m188, 0, v_stack_m158);
    }
    v_stack_m1B0 = v_stack_m158;
    v_stack_m1A8 = v_stack_m150;
    v_stack_m180 = v_stack_m148;
    result = RtlpCopyContext(v_stack_m178, v_stack_m130, 0, v_stack_m148);
    v_stack_m1C8 = v_stack_m170;
    result = RtlpCopyContext(v_stack_m170, v_stack_m178, 0, v_stack_m148);
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_m1D0;
    v_stack_p28 = v_stack_m198;
    v_stack_p20 = v_stack_m170;
    result = RtlVirtualUnwind(2, v_stack_m150, v_stack_m158, v_stack_m148);
    v_stack_m1A0 = result;
    if (result != v_stack_m128) goto loc_002F2CF1;
    if (v_stack_m1D0 != v_stack_m140) goto loc_002F2CF1;
    if (v_stack_m198 != v_stack_m120) goto loc_002F2CF1;
    local_r13 = (uint32_t)((local_r13) | (64));
    v_stack_m190 = v_stack_m118;
    if ((((uint8_t)(v_stack_m1D0)) & (7)) != 0) goto loc_002F2CB2;
    if (v_stack_m1D0 < v_stack_m1C0) goto loc_002F2CE6;
loc_002F2CB2:
    if (((uint8_t)(v_stack_p8)) != 1) goto loc_002F2AF9;
    v_stack_p20 = 0;
    result = RtlpGetStackLimitsEx(v_stack_m1D0, v_stack_m1B8, v_stack_m1C0, v_stack_m178);
    goto loc_002F2AF5;
loc_002F2CE6:
    if (v_stack_m1D0 >= v_stack_m1B8) goto loc_002F2AF9;
    goto loc_002F2CB2;
loc_002F2CF1:
loc_002F2CF8:
    if ((*(uint8_t *)(v_rip + 0xF0EB42)) == ((uint8_t)(v_stack_m178))) goto loc_002F2D66;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r13 + 0x30))) & (0x100080ULL));
    if (((uint32_t)(result)) == 0x100080ULL) goto loc_002F2D66;
    result = RtlGetExtendedContextLength((uint32_t)((uint32_t)((uint32_t)(0x10008BULL))), v_stack_m1D8, v_stack_m1C0, v_stack_m178);
    if (((uint32_t)(v_stack_m1D8) + 15) <= ((uint32_t)(v_stack_m1D8))) {
    }
    Arg1 = ((uint32_t)(v_stack_m1D8) + 15) & (-16);
    result = _chkstk(Arg1, v_stack_m1D8, v_stack_m1C0, v_stack_m178);
    local_rsp = (v_stack_m38) - (Arg1);
    v_stack_m178 = v_stack_p60;
    result = RtlInitializeExtendedContext(v_stack_p60, (uint32_t)((uint32_t)((uint32_t)(0x10008BULL))), v_stack_m180, v_stack_m178);
loc_002F2D66:
    v_stack_m1B0 = v_stack_m1C0;
    v_stack_m1D8 = (uint32_t)(v_stack_m1C0);
    result = RtlpValidateContextFlags2((uint32_t)((uint32_t)((uint32_t)(0x10008BULL))), v_stack_m1D8, v_stack_m180, v_stack_m178);
    if (sign_flag) goto loc_002F2DA8;
    if ((((uint8_t)((uint32_t)(v_stack_m1D8))) & (2)) != 0) goto loc_002F2E46;
loc_002F2D9B:
    local_rsi = (uint32_t)(0x4F0ULL) + 32;
    if ((((uint8_t)((uint32_t)(v_stack_m1D8))) & (4)) == 0) { local_rsi = (uint32_t)((uint32_t)(0x4F0ULL)); }
    local_rsi = (uint32_t)((local_rsi) + (15));
loc_002F2DA8:
    if (((uint32_t)((uint32_t)(local_rsi)) + 15) <= ((uint32_t)((uint32_t)(local_rsi)))) {
    }
    Arg1 = ((uint32_t)((uint32_t)(local_rsi)) + 15) & (-16);
    result = _chkstk(Arg1, v_stack_m1D8, v_stack_m180, v_stack_m178);
    local_rsp = (local_rsp) - (Arg1);
    Arg4 = 0;
    v_stack_m170 = v_stack_p60;
    result = RtlInitializeExtendedContext2(v_stack_p60, (uint32_t)((uint32_t)((uint32_t)(0x10008BULL))), v_stack_m180, Arg4);
    v_stack_m1C8 = v_stack_p60;
    result = RtlCaptureContext2(v_stack_p60, (uint32_t)((uint32_t)((uint32_t)(0x10008BULL))), v_stack_m180, Arg4);
    if (v_stack_m190 != 0) {
        *(uint8_t *)(v_stack_m190 + 0x6) = 1;
    }
    Arg2 = 0;
    if (v_stack_m1B8 != 0) goto loc_002F291A;
    v_stack_mE8 = 0xC0000027ULL;
    v_stack_mE0 = 0;
    v_stack_mD8 = *(uint64_t *)(v_stack_p60 + 0xF8);
    v_stack_m188 = v_stack_mE8;
    v_stack_mD0 = 0;
    goto loc_002F291A;
loc_002F2E46:
    if ((((uint8_t)(*(uint64_t *)(v_stack_p60 + 0xF8))) & (2)) != 0) goto loc_002F2E6F;
loc_002F2E53:
    result = RtlpGetEntireXStateAreaLength2(v_stack_p60, Arg2, v_stack_m180, Arg4);
    result = (uint32_t)((result) + (800));
    goto loc_002F2D9B;
loc_002F2E6F:
    result = RtlpRemoveArchDisallowedXStateFeatures((uint32_t)((uint32_t)(v_stack_p60)), v_stack_m1B0, v_stack_m180, Arg4);
    goto loc_002F2E53;
loc_002F2E81:
    if (2 != 1) goto loc_002F290F;
    v_stack_p20 = 0;
    result = RtlpGetStackLimitsEx(v_stack_m1D0, v_stack_m1B8, v_stack_m1C0, v_stack_p60);
    if ((uint8_t)(result) == 0) goto loc_002F290F;
    goto loc_002F29EF;
loc_002F2EC1:
    result = RtlpExecuteHandlerForUnwind(v_stack_m1D0, v_stack_m1B8, v_stack_m1C0, v_stack_p60);
    goto loc_002F2AC7;
loc_002F2ECD:
    Arg2 = (uint32_t)((v_stack_m1B8) & (0xFFFFFFBFULL));
    *(uint32_t *)(v_stack_p60 + 0x30) = (uint32_t)(Arg2);
    goto loc_002F2AC7;
loc_002F2ED8:
    if (((uint32_t)(result)) != 0x80000026ULL) goto loc_002F2BA7;
    if ((*(uint8_t *)(v_rip + 0xF0E957)) != 0) goto loc_002F2BA7;
    result = RtlGuardCheckLongJumpTarget(*(uint64_t *)(*(uint64_t *)(v_stack_m1B8 + 0x20) + 0x50), Arg2, v_stack_m1C0, v_stack_p60);
    goto loc_002F2BA7;
loc_002F2F03:
    result = RtlRaiseStatus((uint32_t)(0xC00000FFULL), Arg2, v_stack_m1C0, v_stack_p60);
loc_002F2F1F:
    result = RtlRaiseStatus((uint32_t)((uint32_t)(result)), Arg2, v_stack_m1C0, v_stack_p60);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F2830&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
