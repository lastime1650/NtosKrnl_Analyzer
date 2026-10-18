# PiSwCompleteCreate

- RVA: `0x008DAB90`–`0x008DB05E` (길이 `1,230` bytes)
- VA: `0x00000001408DAB90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000857D4`
- 디코드: `297`개 명령, `1,230/1,230` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x008DAC27` → [PiSwLock](../8F/PiSwLock_function_008F7D50.md) (function, `0x008F7D50`)
- `0x008DAC8A` → [PnpAllocatePWSTR](PnpAllocatePWSTR_function_008DE620.md) (function, `0x008DE620`)
- `0x008DACA2` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x008DAD29` → [PnpCopyDevPropertyArray](PnpCopyDevPropertyArray_function_008DB0F8.md) (function, `0x008DB0F8`)
- `0x008DAD4F` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008DAD6E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008DAD73` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008DADD3` → [PiSwInterfaceFree](PiSwInterfaceFree_function_008DB064.md) (function, `0x008DB064`)
- `0x008DADE3` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008DAE04` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008DAE51` → [PiSwPropertySet](../8F/PiSwPropertySet_function_008F5EEC.md) (function, `0x008F5EEC`)
- `0x008DAEA2` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x008DAED1` → [McTemplateK0zzd_EtwWriteTransfer](../../text/42/McTemplateK0zzd_EtwWriteTransfer_function_00424414.md) (function, `0x00424414`)
- `0x008DAF04` → [RtlStringCbCopyW](../../text/43/RtlStringCbCopyW_function_0043B910.md) (function, `0x0043B910`)
- `0x008DAF84` → [PiSwPropertySet](../8F/PiSwPropertySet_function_008F5EEC.md) (function, `0x008F5EEC`)
- `0x008DAFBE` → [McTemplateK0zzz_EtwWriteTransfer](../../text/5A/McTemplateK0zzz_EtwWriteTransfer_function_005A96BC.md) (function, `0x005A96BC`)
- `0x008DAFCD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008DAFEF` → [PiSwInterfaceCreate](PiSwInterfaceCreate_function_008DA784.md) (function, `0x008DA784`)
- `0x008DB035` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008DB04C` → [PnpFreeDevPropertyArray](PnpFreeDevPropertyArray_function_008DE78C.md) (function, `0x008DE78C`)

### Direct callers
- [PiSwPdoPnPDispatch](../94/PiSwPdoPnPDispatch_function_0094DDF0.md) at `0x0094E169`

### Static image references
- `0x008DABB6` → RVA `0x00E0A740` (`.data`; read)
- `0x008DAC51` → RVA `0x00EF012C` (`.data`; read)
- `0x008DACDC` → RVA `0x000116D0` (`.rdata`; read)
- `0x008DACE7` → RVA `0x000116E0` (`.rdata`; read)
- `0x008DAD67` → RVA `0x00F8AB20` (`.data`; read)
- `0x008DAEBD` → RVA `0x00027120` (`.rdata`; read)
- `0x008DAFA5` → RVA `0x00026CE0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x008DACA2` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008DAD4F` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008DAD6E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008DAD73` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008DADE3` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008DAE04` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008DAEA2` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (`PAGE` → `.text`)
  - `0x008DAED1` → [McTemplateK0zzd_EtwWriteTransfer](../../text/42/McTemplateK0zzd_EtwWriteTransfer_function_00424414.md) (`PAGE` → `.text`)
  - `0x008DAF04` → [RtlStringCbCopyW](../../text/43/RtlStringCbCopyW_function_0043B910.md) (`PAGE` → `.text`)
  - `0x008DAFBE` → [McTemplateK0zzz_EtwWriteTransfer](../../text/5A/McTemplateK0zzz_EtwWriteTransfer_function_005A96BC.md) (`PAGE` → `.text`)
  - `0x008DAFCD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008DB035` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008DAE78` → [sub_00B1C3F8](../B1/Unknown_function_00B1C3F8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008DAB90  48 8B C4                        mov rax, rsp
008DAB93  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
008DAB97  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
008DAB9B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
008DAB9F  55                              push rbp
008DABA0  41 54                           push r12
008DABA2  41 55                           push r13
008DABA4  41 56                           push r14
008DABA6  41 57                           push r15
008DABA8  48 8D A8 D8 FD FF FF            lea rbp, [rax - 0x228]
008DABAF  48 81 EC 00 03 00 00            sub rsp, 0x300
008DABB6  48 8B 05 83 FB 52 00            mov rax, qword ptr [rip + 0x52fb83]
008DABBD  48 33 C4                        xor rax, rsp
008DABC0  48 89 85 F0 01 00 00            mov qword ptr [rbp + 0x1f0], rax
008DABC7  33 F6                           xor esi, esi
008DABC9  48 8D 44 24 38                  lea rax, [rsp + 0x38]
008DABCE  0F 57 C9                        xorps xmm1, xmm1
008DABD1  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008DABD6  0F 57 C0                        xorps xmm0, xmm0
008DABD9  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
008DABDE  48 8D 44 24 38                  lea rax, [rsp + 0x38]
008DABE3  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
008DABE7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008DABEC  4C 8B E1                        mov r12, rcx
008DABEF  44 8B FE                        mov r15d, esi
008DABF2  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
008DABF6  44 8B EE                        mov r13d, esi
008DABF9  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
008DABFE  44 8B F6                        mov r14d, esi
008DAC01  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
008DAC06  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
008DAC0A  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
008DAC0F  0F 11 4D 90                     movups xmmword ptr [rbp - 0x70], xmm1
008DAC13  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
008DAC17  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
008DAC1B  0F 11 4D A0                     movups xmmword ptr [rbp - 0x60], xmm1
008DAC1F  0F 11 4D B0                     movups xmmword ptr [rbp - 0x50], xmm1
008DAC23  0F 11 4D C0                     movups xmmword ptr [rbp - 0x40], xmm1
008DAC27  E8 24 D1 01 00                  call 0x1408f7d50
008DAC2C  49 8B 44 24 40                  mov rax, qword ptr [r12 + 0x40]
008DAC31  48 8B 38                        mov rdi, qword ptr [rax]
008DAC34  48 85 FF                        test rdi, rdi
008DAC37  0F 84 19 01 00 00               je 0x1408dad56
008DAC3D  83 60 08 F9                     and dword ptr [rax + 8], 0xfffffff9
008DAC41  49 8B 84 24 38 01 00 00         mov rax, qword ptr [r12 + 0x138]
008DAC49  4C 8B 68 28                     mov r13, qword ptr [rax + 0x28]
008DAC4D  49 83 C5 28                     add r13, 0x28
008DAC51  F6 05 D4 54 61 00 40            test byte ptr [rip + 0x6154d4], 0x40
008DAC58  0F 85 43 03 00 00               jne 0x1408dafa1
008DAC5E  48 8B 4F 50                     mov rcx, qword ptr [rdi + 0x50]
008DAC62  48 85 C9                        test rcx, rcx
008DAC65  0F 85 5D 03 00 00               jne 0x1408dafc8
008DAC6B  41 0F B7 55 00                  movzx edx, word ptr [r13]
008DAC70  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
008DAC75  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
008DAC79  41 B8 50 6E 70 57               mov r8d, 0x57706e50
008DAC7F  48 D1 EA                        shr rdx, 1
008DAC82  48 FF C2                        inc rdx
008DAC85  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
008DAC8A  E8 91 39 00 00                  call 0x1408de620
008DAC8F  8B D8                           mov ebx, eax
008DAC91  85 C0                           test eax, eax
008DAC93  0F 88 CE 00 00 00               js 0x1408dad67
008DAC99  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
008DAC9E  48 8D 4F 48                     lea rcx, [rdi + 0x48]
008DACA2  E8 D9 FA B4 FF                  call 0x14042a780
008DACA7  83 4F 04 04                     or dword ptr [rdi + 4], 4
008DACAB  48 39 77 58                     cmp qword ptr [rdi + 0x58], rsi
008DACAF  0F 85 B2 00 00 00               jne 0x1408dad67
008DACB5  48 8B 8F 90 00 00 00            mov rcx, qword ptr [rdi + 0x90]
008DACBC  48 85 C9                        test rcx, rcx
008DACBF  74 10                           je 0x1408dacd1
008DACC1  48 8B C6                        mov rax, rsi
008DACC4  48 87 41 68                     xchg qword ptr [rcx + 0x68], rax
008DACC8  48 85 C0                        test rax, rax
008DACCB  0F 85 0A 02 00 00               jne 0x1408daedb
008DACD1  8B 87 A4 00 00 00               mov eax, dword ptr [rdi + 0xa4]
008DACD7  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
008DACDC  0F 10 05 ED 69 73 FF            movups xmm0, xmmword ptr [rip - 0x8c9613]
008DACE3  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008DACE7  8B 05 F3 69 73 FF               mov eax, dword ptr [rip - 0x8c960d]
008DACED  89 45 B0                        mov dword ptr [rbp - 0x50], eax
008DACF0  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008DACF5  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
008DACF9  48 8D 44 24 50                  lea rax, [rsp + 0x50]
008DACFE  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
008DAD02  C7 45 C0 07 00 00 00            mov dword ptr [rbp - 0x40], 7
008DAD09  89 75 B4                        mov dword ptr [rbp - 0x4c], esi
008DAD0C  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
008DAD10  C7 45 C4 04 00 00 00            mov dword ptr [rbp - 0x3c], 4
008DAD17  48 8B 97 A8 00 00 00            mov rdx, qword ptr [rdi + 0xa8]
008DAD1E  8B 8F B0 00 00 00               mov ecx, dword ptr [rdi + 0xb0]
008DAD24  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DAD29  E8 CA 03 00 00                  call 0x1408db0f8
008DAD2E  8B D8                           mov ebx, eax
008DAD30  85 C0                           test eax, eax
008DAD32  78 2E                           js 0x1408dad62
008DAD34  4C 8D B7 B8 00 00 00            lea r14, [rdi + 0xb8]
008DAD3B  49 8B 36                        mov rsi, qword ptr [r14]
008DAD3E  49 3B F6                        cmp rsi, r14
008DAD41  0F 85 97 02 00 00               jne 0x1408dafde
008DAD47  49 8B CC                        mov rcx, r12
008DAD4A  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
008DAD4F  E8 CC 4C 93 FF                  call 0x14020fa20
008DAD54  EB 0C                           jmp 0x1408dad62
008DAD56  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008DAD5B  EB 0A                           jmp 0x1408dad67
008DAD5D  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
008DAD62  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
008DAD67  48 8D 0D B2 FD 6A 00            lea rcx, [rip + 0x6afdb2]
008DAD6E  E8 9D 4C 98 FF                  call 0x14025fa10
008DAD73  E8 38 2B 98 FF                  call 0x14025d8b0
008DAD78  85 DB                           test ebx, ebx
008DAD7A  0F 89 AB 00 00 00               jns 0x1408dae2b
008DAD80  45 33 ED                        xor r13d, r13d
008DAD83  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008DAD88  48 85 C0                        test rax, rax
008DAD8B  0F 85 A1 02 00 00               jne 0x1408db032
008DAD91  4D 85 F6                        test r14, r14
008DAD94  0F 85 A5 02 00 00               jne 0x1408db03f
008DAD9A  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
008DAD9F  48 8D 44 24 38                  lea rax, [rsp + 0x38]
008DADA4  48 3B C8                        cmp rcx, rax
008DADA7  74 31                           je 0x1408dadda
008DADA9  48 8D 44 24 38                  lea rax, [rsp + 0x38]
008DADAE  48 39 41 08                     cmp qword ptr [rcx + 8], rax
008DADB2  0F 85 C5 00 00 00               jne 0x1408dae7d
008DADB8  48 8B 01                        mov rax, qword ptr [rcx]
008DADBB  48 39 48 08                     cmp qword ptr [rax + 8], rcx
008DADBF  0F 85 B8 00 00 00               jne 0x1408dae7d
008DADC5  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
008DADCA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008DADCF  48 89 50 08                     mov qword ptr [rax + 8], rdx
008DADD3  E8 8C 02 00 00                  call 0x1408db064
008DADD8  EB C0                           jmp 0x1408dad9a
008DADDA  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
008DADDE  48 85 C9                        test rcx, rcx
008DADE1  74 05                           je 0x1408dade8
008DADE3  E8 68 7A 2A 00                  call 0x140b82850
008DADE8  4D 85 FF                        test r15, r15
008DADEB  0F 85 93 00 00 00               jne 0x1408dae84
008DADF1  48 85 FF                        test rdi, rdi
008DADF4  0F 85 B2 00 00 00               jne 0x1408daeac
008DADFA  48 8B 8D F0 01 00 00            mov rcx, qword ptr [rbp + 0x1f0]
008DAE01  48 33 CC                        xor rcx, rsp
008DAE04  E8 37 18 DD FF                  call 0x1406ac640
008DAE09  4C 8D 9C 24 00 03 00 00         lea r11, [rsp + 0x300]
008DAE11  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
008DAE15  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
008DAE19  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
008DAE1D  49 8B E3                        mov rsp, r11
008DAE20  41 5F                           pop r15
008DAE22  41 5E                           pop r14
008DAE24  41 5D                           pop r13
008DAE26  41 5C                           pop r12
008DAE28  5D                              pop rbp
008DAE29  C3                              ret
008DAE2A  CC                              int3
008DAE2B  49 8D 75 08                     lea rsi, [r13 + 8]
008DAE2F  45 33 ED                        xor r13d, r13d
008DAE32  4C 39 6D C8                     cmp qword ptr [rbp - 0x38], r13
008DAE36  0F 85 38 01 00 00               jne 0x1408daf74
008DAE3C  4D 85 F6                        test r14, r14
008DAE3F  74 1F                           je 0x1408dae60
008DAE41  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
008DAE46  4D 8B C6                        mov r8, r14
008DAE49  48 8B 0E                        mov rcx, qword ptr [rsi]
008DAE4C  BA 01 00 00 00                  mov edx, 1
008DAE51  E8 96 B0 01 00                  call 0x1408f5eec
008DAE56  8B D8                           mov ebx, eax
008DAE58  85 C0                           test eax, eax
008DAE5A  0F 88 23 FF FF FF               js 0x1408dad83
008DAE60  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
008DAE65  48 8D 44 24 38                  lea rax, [rsp + 0x38]
008DAE6A  48 3B F0                        cmp rsi, rax
008DAE6D  0F 84 10 FF FF FF               je 0x1408dad83
008DAE73  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
008DAE78  E9 7B 15 24 00                  jmp 0x140b1c3f8
008DAE7D  B9 03 00 00 00                  mov ecx, 3
008DAE82  CD 29                           int 0x29
008DAE84  85 DB                           test ebx, ebx
008DAE86  0F 88 CA 01 00 00               js 0x1408db056
008DAE8C  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008DAE91  48 83 C0 02                     add rax, 2
008DAE95  49 89 47 38                     mov qword ptr [r15 + 0x38], rax
008DAE99  33 D2                           xor edx, edx
008DAE9B  49 8B CF                        mov rcx, r15
008DAE9E  41 89 5F 30                     mov dword ptr [r15 + 0x30], ebx
008DAEA2  E8 19 07 9C FF                  call 0x14029b5c0
008DAEA7  E9 45 FF FF FF                  jmp 0x1408dadf1
008DAEAC  F6 05 79 52 61 00 40            test byte ptr [rip + 0x615279], 0x40
008DAEB3  0F 84 41 FF FF FF               je 0x1408dadfa
008DAEB9  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008DAEBD  48 8D 15 5C C2 74 FF            lea rdx, [rip - 0x8b3da4]
008DAEC4  4C 8B 4F 08                     mov r9, qword ptr [rdi + 8]
008DAEC8  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
008DAECC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DAED1  E8 3E 95 B4 FF                  call 0x140424414
008DAED6  E9 1F FF FF FF                  jmp 0x1408dadfa
008DAEDB  4C 8B BF 90 00 00 00            mov r15, qword ptr [rdi + 0x90]
008DAEE2  48 89 B7 90 00 00 00            mov qword ptr [rdi + 0x90], rsi
008DAEE9  4D 85 FF                        test r15, r15
008DAEEC  0F 84 DF FD FF FF               je 0x1408dacd1
008DAEF2  49 8B B7 B8 00 00 00            mov rsi, qword ptr [r15 + 0xb8]
008DAEF9  4C 8B 47 50                     mov r8, qword ptr [rdi + 0x50]
008DAEFD  49 8B 4F 18                     mov rcx, qword ptr [r15 + 0x18]
008DAF01  8B 56 08                        mov edx, dword ptr [rsi + 8]
008DAF04  E8 07 0A B6 FF                  call 0x14043b910
008DAF09  8B D8                           mov ebx, eax
008DAF0B  85 C0                           test eax, eax
008DAF0D  0F 88 4F FE FF FF               js 0x1408dad62
008DAF13  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
008DAF17  48 85 C0                        test rax, rax
008DAF1A  74 4C                           je 0x1408daf68
008DAF1C  8B 56 08                        mov edx, dword ptr [rsi + 8]
008DAF1F  48 D1 EA                        shr rdx, 1
008DAF22  4C 8B C2                        mov r8, rdx
008DAF25  74 71                           je 0x1408daf98
008DAF27  33 F6                           xor esi, esi
008DAF29  66 39 30                        cmp word ptr [rax], si
008DAF2C  74 0A                           je 0x1408daf38
008DAF2E  48 83 C0 02                     add rax, 2
008DAF32  48 83 EA 01                     sub rdx, 1
008DAF36  75 F1                           jne 0x1408daf29
008DAF38  48 8B C2                        mov rax, rdx
008DAF3B  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008DAF40  48 F7 D8                        neg rax
008DAF43  1B C9                           sbb ecx, ecx
008DAF45  F7 D1                           not ecx
008DAF47  23 D9                           and ebx, ecx
008DAF49  48 85 D2                        test rdx, rdx
008DAF4C  74 4E                           je 0x1408daf9c
008DAF4E  4C 2B C2                        sub r8, rdx
008DAF51  48 85 D2                        test rdx, rdx
008DAF54  0F 84 03 FE FF FF               je 0x1408dad5d
008DAF5A  4B 8D 04 00                     lea rax, [r8 + r8]
008DAF5E  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008DAF63  E9 69 FD FF FF                  jmp 0x1408dacd1
008DAF68  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008DAF6D  33 F6                           xor esi, esi
008DAF6F  E9 E9 FD FF FF                  jmp 0x1408dad5d
008DAF74  48 8B 0E                        mov rcx, qword ptr [rsi]
008DAF77  4C 8D 45 A0                     lea r8, [rbp - 0x60]
008DAF7B  41 B9 01 00 00 00               mov r9d, 1
008DAF81  41 8B D1                        mov edx, r9d
008DAF84  E8 63 AF 01 00                  call 0x1408f5eec
008DAF89  8B D8                           mov ebx, eax
008DAF8B  85 C0                           test eax, eax
008DAF8D  0F 89 A9 FE FF FF               jns 0x1408dae3c
008DAF93  E9 EB FD FF FF                  jmp 0x1408dad83
008DAF98  33 F6                           xor esi, esi
008DAF9A  EB 9C                           jmp 0x1408daf38
008DAF9C  4C 8B C6                        mov r8, rsi
008DAF9F  EB B0                           jmp 0x1408daf51
008DAFA1  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
008DAFA5  48 8D 15 34 BD 74 FF            lea rdx, [rip - 0x8b42cc]
008DAFAC  4C 8B 4F 08                     mov r9, qword ptr [rdi + 8]
008DAFB0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008DAFB5  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008DAFB9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DAFBE  E8 F9 E6 CC FF                  call 0x1405a96bc
008DAFC3  E9 96 FC FF FF                  jmp 0x1408dac5e
008DAFC8  BA 50 6E 70 57                  mov edx, 0x57706e50
008DAFCD  E8 9E 78 2A 00                  call 0x140b82870
008DAFD2  0F 57 C0                        xorps xmm0, xmm0
008DAFD5  0F 11 47 48                     movups xmmword ptr [rdi + 0x48], xmm0
008DAFD9  E9 8D FC FF FF                  jmp 0x1408dac6b
008DAFDE  44 8B 46 20                     mov r8d, dword ptr [rsi + 0x20]
008DAFE2  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
008DAFE7  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
008DAFEB  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
008DAFEF  E8 90 F7 FF FF                  call 0x1408da784
008DAFF4  8B D8                           mov ebx, eax
008DAFF6  85 C0                           test eax, eax
008DAFF8  0F 88 64 FD FF FF               js 0x1408dad62
008DAFFE  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
008DB003  48 8D 44 24 38                  lea rax, [rsp + 0x38]
008DB008  48 39 01                        cmp qword ptr [rcx], rax
008DB00B  0F 85 6C FE FF FF               jne 0x1408dae7d
008DB011  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
008DB016  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
008DB01B  48 89 10                        mov qword ptr [rax], rdx
008DB01E  48 89 48 08                     mov qword ptr [rax + 8], rcx
008DB022  48 89 01                        mov qword ptr [rcx], rax
008DB025  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008DB02A  48 8B 36                        mov rsi, qword ptr [rsi]
008DB02D  E9 0C FD FF FF                  jmp 0x1408dad3e
008DB032  48 8B C8                        mov rcx, rax
008DB035  E8 16 E3 A1 FF                  call 0x1402f9350
008DB03A  E9 52 FD FF FF                  jmp 0x1408dad91
008DB03F  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
008DB043  41 B8 50 6E 70 57               mov r8d, 0x57706e50
008DB049  49 8B D6                        mov rdx, r14
008DB04C  E8 3B 37 00 00                  call 0x1408de78c
008DB051  E9 44 FD FF FF                  jmp 0x1408dad9a
008DB056  49 8B C5                        mov rax, r13
008DB059  E9 37 FE FF FF                  jmp 0x1408dae95
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiSwCompleteCreate(__int64 a1)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned int v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned int v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned __int64 v_stack_m2F0;
    unsigned int v_stack_m2F8;
    unsigned __int64 v_stack_m308;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (768);
    result = (*(unsigned __int64 *)(v_rip + 5438339)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 552 + 496) = result;
    v_rsi = 0;
    v_stack_m2E8 = v_stack_m2F0;
    v_stack_m2D8 = 0;
    v_stack_m2F8 = 0;
    v_stack_m2F0 = v_stack_m2F0;
    v_stack_m2D0 = 0;
    v_stack_m2C0 = 0;
    v_stack_m2B0 = 0;
    *(unsigned __int64 *)(v_rsp - 552 - 48) = v_xmm0;
    v_stack_m2C8 = 0;
    *(unsigned __int64 *)(v_rsp - 552 - 112) = v_xmm1;
    v_stack_m2E0 = 0;
    *(unsigned __int64 *)(v_rsp - 552 - 128) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 552 - 96) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 552 - 80) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 552 - 64) = v_xmm1;
    result = PiSwLock(a1, a2, a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) == 0) goto loc_008DAD56;
    v_r13 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 40)) + (40);
    if (((*(unsigned __int8 *)(v_rip + 6378708)) & (64)) != 0) goto loc_008DAFA1;
loc_008DAC5E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 80) != 0) goto loc_008DAFC8;
loc_008DAC6B:
    a2 = (*(unsigned __int16 *)(v_r13)) >> (1);
    a2 = (a2) + 1;
    v_stack_m2B8 = 0;
    result = PnpAllocatePWSTR(*(unsigned __int64 *)(v_r13 + 8), a2, (unsigned int)(0x57706E50ULL), v_stack_m2B8);
    if (sign_flag) goto loc_008DAD67;
    result = RtlInitUnicodeString(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 72, v_stack_m2B8, (unsigned int)(0x57706E50ULL), v_stack_m2B8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 88)) != 0) goto loc_008DAD67;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 144) == 0) goto loc_008DACD1;
    if (0 != 0) goto loc_008DAEDB;
loc_008DACD1:
    v_stack_m2E0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 164)));
    *(unsigned int *)(v_rsp - 552 - 80) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 9213453)));
    *(unsigned __int64 *)(v_rsp - 552 - 56) = v_stack_m2E0;
    *(unsigned __int64 *)(v_rsp - 552 - 96) = v_xmm0;
    *(unsigned int *)(v_rsp - 552 - 64) = 7;
    *(unsigned int *)(v_rsp - 552 - 76) = 0;
    *(unsigned __int64 *)(v_rsp - 552 - 72) = 0;
    *(unsigned int *)(v_rsp - 552 - 60) = 4;
    v_stack_m308 = v_stack_m2D8;
    result = PnpCopyDevPropertyArray((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 176)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 168), (unsigned int)(0x57706E50ULL), v_stack_m2F8);
    if (sign_flag) goto loc_008DAD62;
loc_008DAD3E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 184)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 184)) goto loc_008DAFDE;
    v_stack_m2C8 = a1;
    result = ObfReferenceObject(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 168), (unsigned int)(0x57706E50ULL), v_stack_m2F8);
    goto loc_008DAD62;
loc_008DAD56:
    goto loc_008DAD67;
loc_008DAD5D:
    v_stack_m2C0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 184);
loc_008DAD62:
loc_008DAD67:
    result = ExReleaseResourceLite(v_rip + 7011762, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 168), (unsigned int)(0x57706E50ULL), v_stack_m2F8);
    result = KeLeaveCriticalRegion(v_rip + 7011762, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 168), (unsigned int)(0x57706E50ULL), v_stack_m2F8);
    if (!sign_flag) goto loc_008DAE2B;
    v_r13 = 0;
loc_008DAD83:
    if (v_stack_m2C8 != 0) goto loc_008DB032;
loc_008DAD91:
    if (v_stack_m2D8 != 0) goto loc_008DB03F;
loc_008DAD9A:
    if (v_stack_m2F0 == v_stack_m2F0) goto loc_008DADDA;
    if ((*(unsigned __int64 *)(v_stack_m2F0 + 8)) != v_stack_m2F0) goto loc_008DAE7D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2F0) + 8)) != v_stack_m2F0) goto loc_008DAE7D;
    v_stack_m2F0 = *(unsigned __int64 *)(v_stack_m2F0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2F0) + 8) = v_stack_m2F0;
    result = PiSwInterfaceFree(v_stack_m2F0, v_stack_m2F0, (unsigned int)(0x57706E50ULL), v_stack_m2F8);
    goto loc_008DAD9A;
loc_008DADDA:
    if (*(unsigned __int64 *)(v_rsp - 552 - 120) != 0) {
        result = ExFreePool(*(unsigned __int64 *)(v_rsp - 552 - 120), v_stack_m2F0, (unsigned int)(0x57706E50ULL), v_stack_m2F8);
    }
    if (0 != 0) goto loc_008DAE84;
loc_008DADF1:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) != 0) goto loc_008DAEAC;
loc_008DADFA:
    a1 = (*(unsigned __int64 *)(v_rsp - 552 + 496)) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m2F0, (unsigned int)(0x57706E50ULL), v_stack_m2F8);
    return result;
loc_008DAE2B:
    v_r13 = 0;
    if ((*(unsigned __int64 *)(v_rsp - 552 - 56)) != 0) goto loc_008DAF74;
loc_008DAE3C:
    if (v_stack_m2D8 == 0) goto loc_008DAE60;
    result = PiSwPropertySet(*(unsigned __int64 *)(v_r13 + 8), 1, v_stack_m2D8, (unsigned int)(v_stack_m2D0));
    if (sign_flag) goto loc_008DAD83;
loc_008DAE60:
    if (v_stack_m2C8 == v_stack_m2C8) goto loc_008DAD83;
loc_008DAE7D:
loc_008DAE84:
    if (sign_flag) goto loc_008DB056;
    result = (v_stack_m298) + (2);
loc_008DAE95:
    *(unsigned __int64 *)(0 + 56) = result;
    a2 = 0;
    *(unsigned int *)(0 + 48) = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = IofCompleteRequest(0, a2, v_stack_m2D8, (unsigned int)(v_stack_m2D0));
    goto loc_008DADF1;
loc_008DAEAC:
    if (((*(unsigned __int8 *)(v_rip + 6378105)) & (64)) == 0) goto loc_008DADFA;
    v_stack_m2D8 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_m2E0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16);
    result = McTemplateK0zzd_EtwWriteTransfer(0, v_rip - 9125284, v_stack_m2D8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8));
    goto loc_008DADFA;
loc_008DAEDB:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 144) = v_stack_m2C8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 144) == 0) goto loc_008DACD1;
    result = RtlStringCbCopyW(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 144) + 24), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 144) + 184) + 8)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 80), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8));
    if (sign_flag) goto loc_008DAD62;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 144) + 24) == 0) goto loc_008DAF68;
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 144) + 184) + 8))) >> (1);
    if (condition_is_equal) goto loc_008DAF98;
    v_rsi = 0;
loc_008DAF29:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 144) + 24))) == 0) goto loc_008DAF38;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 144) + 24)) + (2);
    a2 = (a2) - (1);
    if (condition_is_not_equal) goto loc_008DAF29;
loc_008DAF38:
    result = -(a2);
    a1 = (unsigned int)(~(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 144) + 24)));
    v_rbx = (unsigned int)(((unsigned int)(0xC000000DULL)) & ((unsigned int)(a1)));
    if (a2 == 0) goto loc_008DAF9C;
    a3 = (a2) - (a2);
loc_008DAF51:
    if (a2 == 0) goto loc_008DAD5D;
    v_stack_m298 = a3 + a3 * 1;
    goto loc_008DACD1;
loc_008DAF68:
    v_rsi = 0;
    goto loc_008DAD5D;
loc_008DAF74:
    result = PiSwPropertySet(*(unsigned __int64 *)(v_rsi), 1, v_rsp - 552 - 96, 1);
    if (!sign_flag) goto loc_008DAE3C;
    goto loc_008DAD83;
loc_008DAF98:
    v_rsi = 0;
    goto loc_008DAF38;
loc_008DAF9C:
    goto loc_008DAF51;
loc_008DAFA1:
    v_stack_m2D8 = *(unsigned __int64 *)(v_r13 + 8);
    v_stack_m2E0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16);
    result = McTemplateK0zzz_EtwWriteTransfer(*(unsigned __int64 *)(v_rsi), v_rip - 9126604, 0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8));
    goto loc_008DAC5E;
loc_008DAFC8:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsi), (unsigned int)(0x57706E50ULL), 0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 72) = v_xmm0;
    goto loc_008DAC6B;
loc_008DAFDE:
    result = PiSwInterfaceCreate(*(unsigned __int64 *)(v_rsi + 16), *(unsigned __int64 *)(v_rsi + 24), (unsigned int)(*(unsigned int *)(v_rsi + 32)), v_stack_m288);
    if (sign_flag) goto loc_008DAD62;
    if ((*(unsigned __int64 *)(v_stack_m2C0)) != v_stack_m2C8) goto loc_008DAE7D;
    *(unsigned __int64 *)(v_stack_m288) = v_stack_m2C8;
    *(unsigned __int64 *)(v_stack_m288 + 8) = v_stack_m2C0;
    *(unsigned __int64 *)(v_stack_m2C0) = v_stack_m288;
    v_stack_m2C0 = v_stack_m288;
    goto loc_008DAD3E;
loc_008DB032:
    result = ObfDereferenceObject(v_stack_m288, v_stack_m2C8, (unsigned int)(*(unsigned int *)(v_rsi + 32)), v_stack_m288);
    goto loc_008DAD91;
loc_008DB03F:
    result = PnpFreeDevPropertyArray((unsigned int)(v_stack_m2D0), v_stack_m2D8, (unsigned int)(0x57706E50ULL), v_stack_m288);
    goto loc_008DAD9A;
loc_008DB056:
    goto loc_008DAE95;
}
```

## 5. (Beta) C Style

```c
int64_t PiSwCompleteCreate(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m288;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint32_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint32_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint64_t v_stack_m2F0;
    uint32_t v_stack_m2F8;
    uint64_t v_stack_m308;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (768);
    result = (*(uint64_t *)(v_rip + 0x52FB83)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x228 + 0x1F0) = result;
    local_rsi = 0;
    v_stack_m2E8 = v_stack_m2F0;
    v_stack_m2D8 = 0;
    v_stack_m2F8 = 0;
    v_stack_m2F0 = v_stack_m2F0;
    v_stack_m2D0 = 0;
    v_stack_m2C0 = 0;
    v_stack_m2B0 = 0;
    *(uint64_t *)(local_rsp - 0x228 - 0x30) = v_xmm0;
    v_stack_m2C8 = 0;
    *(uint64_t *)(local_rsp - 0x228 - 0x70) = v_xmm1;
    v_stack_m2E0 = 0;
    *(uint64_t *)(local_rsp - 0x228 - 0x80) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x228 - 0x60) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x228 - 0x50) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x228 - 0x40) = v_xmm1;
    result = PiSwLock(Arg1, a2, a3, a4);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) == 0) goto loc_008DAD56;
    local_r13 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x138) + 0x28)) + (40);
    if (((*(uint8_t *)(v_rip + 0x6154D4)) & (64)) != 0) goto loc_008DAFA1;
loc_008DAC5E:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x50) != 0) goto loc_008DAFC8;
loc_008DAC6B:
    a2 = (*(uint16_t *)(local_r13)) >> (1);
    a2 = (a2) + 1;
    v_stack_m2B8 = 0;
    result = PnpAllocatePWSTR(*(uint64_t *)(local_r13 + 0x8), a2, (uint32_t)(0x57706E50ULL), v_stack_m2B8);
    if (sign_flag) goto loc_008DAD67;
    result = RtlInitUnicodeString(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 72, v_stack_m2B8, (uint32_t)(0x57706E50ULL), v_stack_m2B8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x58)) != 0) goto loc_008DAD67;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x90) == 0) goto loc_008DACD1;
    if (0 != 0) goto loc_008DAEDB;
loc_008DACD1:
    v_stack_m2E0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0xA4)));
    *(uint32_t *)(local_rsp - 0x228 - 0x50) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x8C960D)));
    *(uint64_t *)(local_rsp - 0x228 - 0x38) = v_stack_m2E0;
    *(uint64_t *)(local_rsp - 0x228 - 0x60) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x228 - 0x40) = 7;
    *(uint32_t *)(local_rsp - 0x228 - 0x4C) = 0;
    *(uint64_t *)(local_rsp - 0x228 - 0x48) = 0;
    *(uint32_t *)(local_rsp - 0x228 - 0x3C) = 4;
    v_stack_m308 = v_stack_m2D8;
    result = PnpCopyDevPropertyArray((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0xB0)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0xA8), (uint32_t)(0x57706E50ULL), v_stack_m2F8);
    if (sign_flag) goto loc_008DAD62;
loc_008DAD3E:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0xB8)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 184)) goto loc_008DAFDE;
    v_stack_m2C8 = Arg1;
    result = ObfReferenceObject(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0xA8), (uint32_t)(0x57706E50ULL), v_stack_m2F8);
    goto loc_008DAD62;
loc_008DAD56:
    goto loc_008DAD67;
loc_008DAD5D:
    v_stack_m2C0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0xB8);
loc_008DAD62:
loc_008DAD67:
    result = ExReleaseResourceLite(v_rip + 7011762, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0xA8), (uint32_t)(0x57706E50ULL), v_stack_m2F8);
    result = KeLeaveCriticalRegion(v_rip + 7011762, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0xA8), (uint32_t)(0x57706E50ULL), v_stack_m2F8);
    if (!sign_flag) goto loc_008DAE2B;
    local_r13 = 0;
loc_008DAD83:
    if (v_stack_m2C8 != 0) goto loc_008DB032;
loc_008DAD91:
    if (v_stack_m2D8 != 0) goto loc_008DB03F;
loc_008DAD9A:
    if (v_stack_m2F0 == v_stack_m2F0) goto loc_008DADDA;
    if ((*(uint64_t *)(v_stack_m2F0 + 0x8)) != v_stack_m2F0) goto loc_008DAE7D;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m2F0) + 0x8)) != v_stack_m2F0) goto loc_008DAE7D;
    v_stack_m2F0 = *(uint64_t *)(v_stack_m2F0);
    *(uint64_t *)(*(uint64_t *)(v_stack_m2F0) + 0x8) = v_stack_m2F0;
    result = PiSwInterfaceFree(v_stack_m2F0, v_stack_m2F0, (uint32_t)(0x57706E50ULL), v_stack_m2F8);
    goto loc_008DAD9A;
loc_008DADDA:
    if (*(uint64_t *)(local_rsp - 0x228 - 0x78) != 0) {
        result = ExFreePool(*(uint64_t *)(local_rsp - 0x228 - 0x78), v_stack_m2F0, (uint32_t)(0x57706E50ULL), v_stack_m2F8);
    }
    if (0 != 0) goto loc_008DAE84;
loc_008DADF1:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) != 0) goto loc_008DAEAC;
loc_008DADFA:
    Arg1 = (*(uint64_t *)(local_rsp - 0x228 + 0x1F0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m2F0, (uint32_t)(0x57706E50ULL), v_stack_m2F8);
    return result;
loc_008DAE2B:
    local_r13 = 0;
    if ((*(uint64_t *)(local_rsp - 0x228 - 0x38)) != 0) goto loc_008DAF74;
loc_008DAE3C:
    if (v_stack_m2D8 == 0) goto loc_008DAE60;
    result = PiSwPropertySet(*(uint64_t *)(local_r13 + 0x8), 1, v_stack_m2D8, (uint32_t)(v_stack_m2D0));
    if (sign_flag) goto loc_008DAD83;
loc_008DAE60:
    if (v_stack_m2C8 == v_stack_m2C8) goto loc_008DAD83;
loc_008DAE7D:
loc_008DAE84:
    if (sign_flag) goto loc_008DB056;
    result = (v_stack_m298) + (2);
loc_008DAE95:
    *(uint64_t *)(0 + 0x38) = result;
    a2 = 0;
    *(uint32_t *)(0 + 0x30) = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = IofCompleteRequest(0, a2, v_stack_m2D8, (uint32_t)(v_stack_m2D0));
    goto loc_008DADF1;
loc_008DAEAC:
    if (((*(uint8_t *)(v_rip + 0x615279)) & (64)) == 0) goto loc_008DADFA;
    v_stack_m2D8 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_m2E0 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10);
    result = McTemplateK0zzd_EtwWriteTransfer(0, v_rip - 9125284, v_stack_m2D8, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8));
    goto loc_008DADFA;
loc_008DAEDB:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x90) = v_stack_m2C8;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x90) == 0) goto loc_008DACD1;
    result = RtlStringCbCopyW(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x90) + 0x18), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x90) + 0xB8) + 0x8)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x50), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8));
    if (sign_flag) goto loc_008DAD62;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x90) + 0x18) == 0) goto loc_008DAF68;
    a2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x90) + 0xB8) + 0x8))) >> (1);
    if (condition_is_equal) goto loc_008DAF98;
    local_rsi = 0;
loc_008DAF29:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x90) + 0x18))) == 0) goto loc_008DAF38;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x90) + 0x18)) + (2);
    a2 = (a2) - (1);
    if (condition_is_not_equal) goto loc_008DAF29;
loc_008DAF38:
    result = -(a2);
    Arg1 = (uint32_t)(~(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x90) + 0x18)));
    local_rbx = (uint32_t)(((uint32_t)(0xC000000DULL)) & ((uint32_t)(Arg1)));
    if (a2 == 0) goto loc_008DAF9C;
    a3 = (a2) - (a2);
loc_008DAF51:
    if (a2 == 0) goto loc_008DAD5D;
    v_stack_m298 = a3 + a3 * 1;
    goto loc_008DACD1;
loc_008DAF68:
    local_rsi = 0;
    goto loc_008DAD5D;
loc_008DAF74:
    result = PiSwPropertySet(*(uint64_t *)(local_rsi), 1, local_rsp - 552 - 96, 1);
    if (!sign_flag) goto loc_008DAE3C;
    goto loc_008DAD83;
loc_008DAF98:
    local_rsi = 0;
    goto loc_008DAF38;
loc_008DAF9C:
    goto loc_008DAF51;
loc_008DAFA1:
    v_stack_m2D8 = *(uint64_t *)(local_r13 + 0x8);
    v_stack_m2E0 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10);
    result = McTemplateK0zzz_EtwWriteTransfer(*(uint64_t *)(local_rsi), v_rip - 9126604, 0, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8));
    goto loc_008DAC5E;
loc_008DAFC8:
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsi), (uint32_t)(0x57706E50ULL), 0, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8));
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x48) = v_xmm0;
    goto loc_008DAC6B;
loc_008DAFDE:
    result = PiSwInterfaceCreate(*(uint64_t *)(local_rsi + 0x10), *(uint64_t *)(local_rsi + 0x18), (uint32_t)(*(uint32_t *)(local_rsi + 0x20)), v_stack_m288);
    if (sign_flag) goto loc_008DAD62;
    if ((*(uint64_t *)(v_stack_m2C0)) != v_stack_m2C8) goto loc_008DAE7D;
    *(uint64_t *)(v_stack_m288) = v_stack_m2C8;
    *(uint64_t *)(v_stack_m288 + 0x8) = v_stack_m2C0;
    *(uint64_t *)(v_stack_m2C0) = v_stack_m288;
    v_stack_m2C0 = v_stack_m288;
    goto loc_008DAD3E;
loc_008DB032:
    result = ObfDereferenceObject(v_stack_m288, v_stack_m2C8, (uint32_t)(*(uint32_t *)(local_rsi + 0x20)), v_stack_m288);
    goto loc_008DAD91;
loc_008DB03F:
    result = PnpFreeDevPropertyArray((uint32_t)(v_stack_m2D0), v_stack_m2D8, (uint32_t)(0x57706E50ULL), v_stack_m288);
    goto loc_008DAD9A;
loc_008DB056:
    goto loc_008DAE95;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x138` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DAB90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
