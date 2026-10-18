# PspCopyAndFixupParameters

- RVA: `0x00AEB878`–`0x00AEBDBF` (길이 `1,351` bytes)
- VA: `0x0000000140AEB878`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CEF20`
- 디코드: `333`개 명령, `1,351/1,351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AEB92F` → [ObDuplicateObject](../8C/ObDuplicateObject_function_008C4FA0.md) (function, `0x008C4FA0`)
- `0x00AEB9A3` → [ObDuplicateObject](../8C/ObDuplicateObject_function_008C4FA0.md) (function, `0x008C4FA0`)
- `0x00AEBA15` → [Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline_function_005E33C0.md) (function, `0x005E33C0`)
- `0x00AEBB9C` → [RtlCopyToUser](../70/RtlCopyToUser_function_00705D68.md) (function, `0x00705D68`)
- `0x00AEBBBF` → [RtlWriteULong64ToUser](../70/RtlWriteULong64ToUser_function_00705E44.md) (function, `0x00705E44`)
- `0x00AEBC63` → [PspCopyUserAttributes](../78/PspCopyUserAttributes_function_00784234.md) (function, `0x00784234`)
- `0x00AEBC7A` → [RtlWriteULong64ToUser](../70/RtlWriteULong64ToUser_function_00705E44.md) (function, `0x00705E44`)
- `0x00AEBC97` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [PspSetupUserProcessAddressSpace](PspSetupUserProcessAddressSpace_function_00AEBDC8.md) at `0x00AEBF7C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AEBA15` → [Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline_function_005E33C0.md) (`PAGE` → `.text`)
  - `0x00AEBC97` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AEB878  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00AEB87D  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00AEB882  53                              push rbx
00AEB883  56                              push rsi
00AEB884  57                              push rdi
00AEB885  41 54                           push r12
00AEB887  41 55                           push r13
00AEB889  41 56                           push r14
00AEB88B  41 57                           push r15
00AEB88D  48 81 EC B0 04 00 00            sub rsp, 0x4b0
00AEB894  4D 8B F8                        mov r15, r8
00AEB897  48 8B F2                        mov rsi, rdx
00AEB89A  45 33 ED                        xor r13d, r13d
00AEB89D  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00AEB8A2  49 8B 98 D8 00 00 00            mov rbx, qword ptr [r8 + 0xd8]
00AEB8A9  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00AEB8AE  44 8B 33                        mov r14d, dword ptr [rbx]
00AEB8B1  4C 03 B3 F0 03 00 00            add r14, qword ptr [rbx + 0x3f0]
00AEB8B8  49 8B B8 E0 00 00 00            mov rdi, qword ptr [r8 + 0xe0]
00AEB8BF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEB8C8  4C 8B 90 B8 00 00 00            mov r10, qword ptr [rax + 0xb8]
00AEB8CF  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
00AEB8D4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEB8DD  44 8A 88 32 02 00 00            mov r9b, byte ptr [rax + 0x232]
00AEB8E4  44 88 8C 24 00 05 00 00         mov byte ptr [rsp + 0x500], r9b
00AEB8EC  41 F6 40 10 40                  test byte ptr [r8 + 0x10], 0x40
00AEB8F1  74 0C                           je 0x140aeb8ff
00AEB8F3  41 F6 40 11 01                  test byte ptr [r8 + 0x11], 1
00AEB8F8  75 05                           jne 0x140aeb8ff
00AEB8FA  0F BA 6B 08 0E                  bts dword ptr [rbx + 8], 0xe
00AEB8FF  41 83 78 58 03                  cmp dword ptr [r8 + 0x58], 3
00AEB904  75 50                           jne 0x140aeb956
00AEB906  44 39 6B 10                     cmp dword ptr [rbx + 0x10], r13d
00AEB90A  7E 4A                           jle 0x140aeb956
00AEB90C  44 88 4C 24 38                  mov byte ptr [rsp + 0x38], r9b
00AEB911  C7 44 24 30 06 00 00 00         mov dword ptr [rsp + 0x30], 6
00AEB919  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
00AEB91E  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00AEB923  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00AEB928  4D 8B C2                        mov r8, r10
00AEB92B  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
00AEB92F  E8 6C 96 DD FF                  call 0x1408c4fa0
00AEB934  48 8B 8C 24 F0 04 00 00         mov rcx, qword ptr [rsp + 0x4f0]
00AEB93C  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
00AEB941  44 8A 8C 24 00 05 00 00         mov r9b, byte ptr [rsp + 0x500]
00AEB949  85 C0                           test eax, eax
00AEB94B  78 09                           js 0x140aeb956
00AEB94D  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AEB952  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00AEB956  41 BC 08 00 00 00               mov r12d, 8
00AEB95C  48 85 F6                        test rsi, rsi
00AEB95F  0F 84 AA 00 00 00               je 0x140aeba0f
00AEB965  4C 8D 43 20                     lea r8, [rbx + 0x20]
00AEB969  4D 8B E8                        mov r13, r8
00AEB96C  33 D2                           xor edx, edx
00AEB96E  89 94 24 08 05 00 00            mov dword ptr [rsp + 0x508], edx
00AEB975  48 8B 06                        mov rax, qword ptr [rsi]
00AEB978  48 85 C0                        test rax, rax
00AEB97B  74 61                           je 0x140aeb9de
00AEB97D  85 C0                           test eax, eax
00AEB97F  7C 39                           jl 0x140aeb9ba
00AEB981  44 88 4C 24 38                  mov byte ptr [rsp + 0x38], r9b
00AEB986  C7 44 24 30 06 00 00 00         mov dword ptr [rsp + 0x30], 6
00AEB98E  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00AEB993  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00AEB998  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00AEB99D  4D 8B C2                        mov r8, r10
00AEB9A0  48 8B D0                        mov rdx, rax
00AEB9A3  E8 F8 95 DD FF                  call 0x1408c4fa0
00AEB9A8  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AEB9AD  8B 94 24 08 05 00 00            mov edx, dword ptr [rsp + 0x508]
00AEB9B4  4C 8D 43 20                     lea r8, [rbx + 0x20]
00AEB9B8  EB 0C                           jmp 0x140aeb9c6
00AEB9BA  33 C9                           xor ecx, ecx
00AEB9BC  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00AEB9C1  B8 08 00 00 C0                  mov eax, 0xc0000008
00AEB9C6  85 C0                           test eax, eax
00AEB9C8  78 06                           js 0x140aeb9d0
00AEB9CA  49 89 4D 00                     mov qword ptr [r13], rcx
00AEB9CE  EB 0E                           jmp 0x140aeb9de
00AEB9D0  4C 39 84 24 F8 04 00 00         cmp qword ptr [rsp + 0x4f8], r8
00AEB9D8  0F 84 CD 03 00 00               je 0x140aebdab
00AEB9DE  4D 03 EC                        add r13, r12
00AEB9E1  FF C2                           inc edx
00AEB9E3  89 94 24 08 05 00 00            mov dword ptr [rsp + 0x508], edx
00AEB9EA  49 03 F4                        add rsi, r12
00AEB9ED  83 FA 03                        cmp edx, 3
00AEB9F0  73 1A                           jae 0x140aeba0c
00AEB9F2  48 8B 8C 24 F0 04 00 00         mov rcx, qword ptr [rsp + 0x4f0]
00AEB9FA  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
00AEB9FF  44 8A 8C 24 00 05 00 00         mov r9b, byte ptr [rsp + 0x500]
00AEBA07  E9 69 FF FF FF                  jmp 0x140aeb975
00AEBA0C  45 33 ED                        xor r13d, r13d
00AEBA0F  48 8B F7                        mov rsi, rdi
00AEBA12  48 2B F3                        sub rsi, rbx
00AEBA15  E8 A6 79 AF FF                  call 0x1405e33c0
00AEBA1A  85 C0                           test eax, eax
00AEBA1C  0F 84 6C 02 00 00               je 0x140aebc8e
00AEBA22  48 8B C3                        mov rax, rbx
00AEBA25  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00AEBA2A  49 8B D4                        mov rdx, r12
00AEBA2D  41 B8 80 00 00 00               mov r8d, 0x80
00AEBA33  0F 10 00                        movups xmm0, xmmword ptr [rax]
00AEBA36  0F 11 01                        movups xmmword ptr [rcx], xmm0
00AEBA39  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00AEBA3D  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00AEBA41  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00AEBA45  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00AEBA49  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
00AEBA4D  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
00AEBA51  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
00AEBA55  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
00AEBA59  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
00AEBA5D  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
00AEBA61  0F 10 40 60                     movups xmm0, xmmword ptr [rax + 0x60]
00AEBA65  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
00AEBA69  49 03 C8                        add rcx, r8
00AEBA6C  0F 10 48 70                     movups xmm1, xmmword ptr [rax + 0x70]
00AEBA70  0F 11 49 F0                     movups xmmword ptr [rcx - 0x10], xmm1
00AEBA74  49 03 C0                        add rax, r8
00AEBA77  48 83 EA 01                     sub rdx, 1
00AEBA7B  75 B6                           jne 0x140aeba33
00AEBA7D  0F 10 00                        movups xmm0, xmmword ptr [rax]
00AEBA80  0F 11 01                        movups xmmword ptr [rcx], xmm0
00AEBA83  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00AEBA87  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00AEBA8B  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00AEBA8F  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00AEBA93  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
00AEBA97  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
00AEBA9B  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
00AEBA9F  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
00AEBAA3  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00AEBAA7  48 85 C0                        test rax, rax
00AEBAAA  74 07                           je 0x140aebab3
00AEBAAC  48 03 C6                        add rax, rsi
00AEBAAF  48 89 43 40                     mov qword ptr [rbx + 0x40], rax
00AEBAB3  48 8B 43 58                     mov rax, qword ptr [rbx + 0x58]
00AEBAB7  48 85 C0                        test rax, rax
00AEBABA  74 07                           je 0x140aebac3
00AEBABC  48 03 C6                        add rax, rsi
00AEBABF  48 89 43 58                     mov qword ptr [rbx + 0x58], rax
00AEBAC3  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
00AEBAC7  48 85 C0                        test rax, rax
00AEBACA  74 07                           je 0x140aebad3
00AEBACC  48 03 C6                        add rax, rsi
00AEBACF  48 89 43 68                     mov qword ptr [rbx + 0x68], rax
00AEBAD3  48 8B 43 78                     mov rax, qword ptr [rbx + 0x78]
00AEBAD7  48 85 C0                        test rax, rax
00AEBADA  74 07                           je 0x140aebae3
00AEBADC  48 03 C6                        add rax, rsi
00AEBADF  48 89 43 78                     mov qword ptr [rbx + 0x78], rax
00AEBAE3  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
00AEBAEA  48 85 C0                        test rax, rax
00AEBAED  74 0A                           je 0x140aebaf9
00AEBAEF  48 03 C6                        add rax, rsi
00AEBAF2  48 89 83 B8 00 00 00            mov qword ptr [rbx + 0xb8], rax
00AEBAF9  48 8B 83 C8 00 00 00            mov rax, qword ptr [rbx + 0xc8]
00AEBB00  48 85 C0                        test rax, rax
00AEBB03  74 0A                           je 0x140aebb0f
00AEBB05  48 03 C6                        add rax, rsi
00AEBB08  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
00AEBB0F  48 8B 83 D8 00 00 00            mov rax, qword ptr [rbx + 0xd8]
00AEBB16  48 85 C0                        test rax, rax
00AEBB19  74 0A                           je 0x140aebb25
00AEBB1B  48 03 C6                        add rax, rsi
00AEBB1E  48 89 83 D8 00 00 00            mov qword ptr [rbx + 0xd8], rax
00AEBB25  48 8B 83 E8 00 00 00            mov rax, qword ptr [rbx + 0xe8]
00AEBB2C  48 85 C0                        test rax, rax
00AEBB2F  74 0A                           je 0x140aebb3b
00AEBB31  48 03 C6                        add rax, rsi
00AEBB34  48 89 83 E8 00 00 00            mov qword ptr [rbx + 0xe8], rax
00AEBB3B  48 8B 83 18 04 00 00            mov rax, qword ptr [rbx + 0x418]
00AEBB42  48 85 C0                        test rax, rax
00AEBB45  74 0A                           je 0x140aebb51
00AEBB47  48 03 C6                        add rax, rsi
00AEBB4A  48 89 83 18 04 00 00            mov qword ptr [rbx + 0x418], rax
00AEBB51  48 8B 83 28 04 00 00            mov rax, qword ptr [rbx + 0x428]
00AEBB58  48 85 C0                        test rax, rax
00AEBB5B  74 0A                           je 0x140aebb67
00AEBB5D  48 03 C6                        add rax, rsi
00AEBB60  48 89 83 28 04 00 00            mov qword ptr [rbx + 0x428], rax
00AEBB67  48 8B 83 30 04 00 00            mov rax, qword ptr [rbx + 0x430]
00AEBB6E  48 85 C0                        test rax, rax
00AEBB71  74 0A                           je 0x140aebb7d
00AEBB73  48 03 C6                        add rax, rsi
00AEBB76  48 89 83 30 04 00 00            mov qword ptr [rbx + 0x430], rax
00AEBB7D  48 8B 83 80 00 00 00            mov rax, qword ptr [rbx + 0x80]
00AEBB84  48 85 C0                        test rax, rax
00AEBB87  74 0A                           je 0x140aebb93
00AEBB89  48 03 C6                        add rax, rsi
00AEBB8C  48 89 83 80 00 00 00            mov qword ptr [rbx + 0x80], rax
00AEBB93  4D 8B C6                        mov r8, r14
00AEBB96  48 8B D3                        mov rdx, rbx
00AEBB99  48 8B CF                        mov rcx, rdi
00AEBB9C  E8 C7 A1 C1 FF                  call 0x140705d68
00AEBBA1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEBBAA  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AEBBB1  48 8B 89 E0 02 00 00            mov rcx, qword ptr [rcx + 0x2e0]
00AEBBB8  48 83 C1 20                     add rcx, 0x20
00AEBBBC  48 8B D7                        mov rdx, rdi
00AEBBBF  E8 80 A2 C1 FF                  call 0x140705e44
00AEBBC4  90                              nop
00AEBBC5  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00AEBBCA  B9 80 00 00 00                  mov ecx, 0x80
00AEBBCF  0F 10 00                        movups xmm0, xmmword ptr [rax]
00AEBBD2  0F 11 03                        movups xmmword ptr [rbx], xmm0
00AEBBD5  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00AEBBD9  0F 11 4B 10                     movups xmmword ptr [rbx + 0x10], xmm1
00AEBBDD  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00AEBBE1  0F 11 43 20                     movups xmmword ptr [rbx + 0x20], xmm0
00AEBBE5  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
00AEBBE9  0F 11 4B 30                     movups xmmword ptr [rbx + 0x30], xmm1
00AEBBED  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
00AEBBF1  0F 11 43 40                     movups xmmword ptr [rbx + 0x40], xmm0
00AEBBF5  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
00AEBBF9  0F 11 4B 50                     movups xmmword ptr [rbx + 0x50], xmm1
00AEBBFD  0F 10 40 60                     movups xmm0, xmmword ptr [rax + 0x60]
00AEBC01  0F 11 43 60                     movups xmmword ptr [rbx + 0x60], xmm0
00AEBC05  48 03 D9                        add rbx, rcx
00AEBC08  0F 10 48 70                     movups xmm1, xmmword ptr [rax + 0x70]
00AEBC0C  0F 11 4B F0                     movups xmmword ptr [rbx - 0x10], xmm1
00AEBC10  48 03 C1                        add rax, rcx
00AEBC13  49 83 EC 01                     sub r12, 1
00AEBC17  75 B6                           jne 0x140aebbcf
00AEBC19  0F 10 00                        movups xmm0, xmmword ptr [rax]
00AEBC1C  0F 11 03                        movups xmmword ptr [rbx], xmm0
00AEBC1F  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00AEBC23  0F 11 4B 10                     movups xmmword ptr [rbx + 0x10], xmm1
00AEBC27  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00AEBC2B  0F 11 43 20                     movups xmmword ptr [rbx + 0x20], xmm0
00AEBC2F  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
00AEBC33  0F 11 4B 30                     movups xmmword ptr [rbx + 0x30], xmm1
00AEBC37  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
00AEBC3B  0F 11 43 40                     movups xmmword ptr [rbx + 0x40], xmm0
00AEBC3F  45 39 AF 50 02 00 00            cmp dword ptr [r15 + 0x250], r13d
00AEBC46  0F 86 5B 01 00 00               jbe 0x140aebda7
00AEBC4C  49 8D 46 FF                     lea rax, [r14 - 1]
00AEBC50  83 E0 07                        and eax, 7
00AEBC53  4C 2B F0                        sub r14, rax
00AEBC56  48 8D 5F 07                     lea rbx, [rdi + 7]
00AEBC5A  49 03 DE                        add rbx, r14
00AEBC5D  4D 8B C7                        mov r8, r15
00AEBC60  48 8B CB                        mov rcx, rbx
00AEBC63  E8 CC 85 C9 FF                  call 0x140784234
00AEBC68  85 C0                           test eax, eax
00AEBC6A  0F 88 3B 01 00 00               js 0x140aebdab
00AEBC70  48 8D 8F 48 04 00 00            lea rcx, [rdi + 0x448]
00AEBC77  48 8B D3                        mov rdx, rbx
00AEBC7A  E8 C5 A1 C1 FF                  call 0x140705e44
00AEBC7F  E9 23 01 00 00                  jmp 0x140aebda7
00AEBC84  E9 22 01 00 00                  jmp 0x140aebdab
00AEBC89  E9 1D 01 00 00                  jmp 0x140aebdab
00AEBC8E  4D 8B C6                        mov r8, r14
00AEBC91  48 8B D3                        mov rdx, rbx
00AEBC94  48 8B CF                        mov rcx, rdi
00AEBC97  E8 A4 AB BD FF                  call 0x1406c6840
00AEBC9C  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
00AEBCA0  48 85 C0                        test rax, rax
00AEBCA3  74 07                           je 0x140aebcac
00AEBCA5  48 03 C6                        add rax, rsi
00AEBCA8  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
00AEBCAC  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
00AEBCB0  48 85 C0                        test rax, rax
00AEBCB3  74 07                           je 0x140aebcbc
00AEBCB5  48 03 C6                        add rax, rsi
00AEBCB8  48 89 47 58                     mov qword ptr [rdi + 0x58], rax
00AEBCBC  48 8B 47 68                     mov rax, qword ptr [rdi + 0x68]
00AEBCC0  48 85 C0                        test rax, rax
00AEBCC3  74 07                           je 0x140aebccc
00AEBCC5  48 03 C6                        add rax, rsi
00AEBCC8  48 89 47 68                     mov qword ptr [rdi + 0x68], rax
00AEBCCC  48 8B 47 78                     mov rax, qword ptr [rdi + 0x78]
00AEBCD0  48 85 C0                        test rax, rax
00AEBCD3  74 07                           je 0x140aebcdc
00AEBCD5  48 03 C6                        add rax, rsi
00AEBCD8  48 89 47 78                     mov qword ptr [rdi + 0x78], rax
00AEBCDC  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
00AEBCE3  48 85 C0                        test rax, rax
00AEBCE6  74 0A                           je 0x140aebcf2
00AEBCE8  48 03 C6                        add rax, rsi
00AEBCEB  48 89 87 B8 00 00 00            mov qword ptr [rdi + 0xb8], rax
00AEBCF2  48 8B 87 C8 00 00 00            mov rax, qword ptr [rdi + 0xc8]
00AEBCF9  48 85 C0                        test rax, rax
00AEBCFC  74 0A                           je 0x140aebd08
00AEBCFE  48 03 C6                        add rax, rsi
00AEBD01  48 89 87 C8 00 00 00            mov qword ptr [rdi + 0xc8], rax
00AEBD08  48 8B 87 D8 00 00 00            mov rax, qword ptr [rdi + 0xd8]
00AEBD0F  48 85 C0                        test rax, rax
00AEBD12  74 0A                           je 0x140aebd1e
00AEBD14  48 03 C6                        add rax, rsi
00AEBD17  48 89 87 D8 00 00 00            mov qword ptr [rdi + 0xd8], rax
00AEBD1E  48 8B 87 E8 00 00 00            mov rax, qword ptr [rdi + 0xe8]
00AEBD25  48 85 C0                        test rax, rax
00AEBD28  74 0A                           je 0x140aebd34
00AEBD2A  48 03 C6                        add rax, rsi
00AEBD2D  48 89 87 E8 00 00 00            mov qword ptr [rdi + 0xe8], rax
00AEBD34  48 8B 87 18 04 00 00            mov rax, qword ptr [rdi + 0x418]
00AEBD3B  48 85 C0                        test rax, rax
00AEBD3E  74 0A                           je 0x140aebd4a
00AEBD40  48 03 C6                        add rax, rsi
00AEBD43  48 89 87 18 04 00 00            mov qword ptr [rdi + 0x418], rax
00AEBD4A  48 8B 87 28 04 00 00            mov rax, qword ptr [rdi + 0x428]
00AEBD51  48 85 C0                        test rax, rax
00AEBD54  74 0A                           je 0x140aebd60
00AEBD56  48 03 C6                        add rax, rsi
00AEBD59  48 89 87 28 04 00 00            mov qword ptr [rdi + 0x428], rax
00AEBD60  48 8B 87 30 04 00 00            mov rax, qword ptr [rdi + 0x430]
00AEBD67  48 85 C0                        test rax, rax
00AEBD6A  74 0A                           je 0x140aebd76
00AEBD6C  48 03 C6                        add rax, rsi
00AEBD6F  48 89 87 30 04 00 00            mov qword ptr [rdi + 0x430], rax
00AEBD76  48 8B 87 80 00 00 00            mov rax, qword ptr [rdi + 0x80]
00AEBD7D  48 85 C0                        test rax, rax
00AEBD80  74 0A                           je 0x140aebd8c
00AEBD82  48 03 C6                        add rax, rsi
00AEBD85  48 89 87 80 00 00 00            mov qword ptr [rdi + 0x80], rax
00AEBD8C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEBD95  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AEBD9C  48 8B 81 E0 02 00 00            mov rax, qword ptr [rcx + 0x2e0]
00AEBDA3  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00AEBDA7  33 C0                           xor eax, eax
00AEBDA9  EB 00                           jmp 0x140aebdab
00AEBDAB  48 81 C4 B0 04 00 00            add rsp, 0x4b0
00AEBDB2  41 5F                           pop r15
00AEBDB4  41 5E                           pop r14
00AEBDB6  41 5D                           pop r13
00AEBDB8  41 5C                           pop r12
00AEBDBA  5F                              pop rdi
00AEBDBB  5E                              pop rsi
00AEBDBC  5B                              pop rbx
00AEBDBD  C3                              ret
00AEBDBE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspCopyAndFixupParameters(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m488;
    unsigned __int64 v_stack_m498;
    unsigned __int64 v_stack_m4A0;
    unsigned __int64 v_stack_m4A8;
    unsigned __int8 v_stack_m4B0;
    unsigned int v_stack_m4B8;
    unsigned int v_stack_m4C0;
    unsigned int v_stack_m4C8;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (0x4B0ULL);
    v_r13 = 0;
    v_stack_m4A8 = 0;
    v_stack_m498 = *(unsigned __int64 *)(a3 + 216);
    v_r14 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 216)))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1008));
    v_stack_m4A0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_p18 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (((*(unsigned __int8 *)(a3 + 16)) & (64)) == 0) goto loc_00AEB8FF;
    if (((*(unsigned __int8 *)(a3 + 17)) & (1)) == 0) {
    }
    if ((*(unsigned int *)(a3 + 88)) != 3) goto loc_00AEB956;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a3 + 216) + 16)) <= 0) goto loc_00AEB956;
    v_stack_m4B0 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m4B8 = 6;
    v_stack_m4C0 = 0;
    v_stack_m4C8 = 0;
    result = ObDuplicateObject(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_m4A8);
    if (!(sign_flag)) {
        result = v_stack_m4A8;
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 16) = result;
    }
    if (a2 == 0) goto loc_00AEBA0F;
    a2 = 0;
    v_stack_p20 = 0;
loc_00AEB975:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00AEB9DE;
    if (condition_is_less) goto loc_00AEB9BA;
    v_stack_m4B0 = (unsigned __int8)(v_stack_p18);
    v_stack_m4B8 = 6;
    result = ObDuplicateObject(v_stack_p8, *(unsigned __int64 *)(a2), v_stack_m4A0, v_stack_m4A8);
    goto loc_00AEB9C6;
loc_00AEB9BA:
    a1 = 0;
    v_stack_m4A8 = 0;
loc_00AEB9C6:
    if (sign_flag) goto loc_00AEB9D0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 32) = 0;
    goto loc_00AEB9DE;
loc_00AEB9D0:
    if (v_stack_p10 == (*(unsigned __int64 *)(a3 + 216) + 32)) goto loc_00AEBDAB;
loc_00AEB9DE:
    v_r13 = (*(unsigned __int64 *)(a3 + 216) + 32) + (8);
    a2 = (unsigned int)(((unsigned int)(v_stack_p20)) + 1);
    v_stack_p20 = (unsigned int)(a2);
    v_rsi = (a2) + (8);
    if (((unsigned int)(a2)) >= 3) goto loc_00AEBA0C;
    goto loc_00AEB975;
loc_00AEBA0C:
    v_r13 = 0;
loc_00AEBA0F:
    v_rsi = (*(unsigned __int64 *)(a3 + 224)) - (*(unsigned __int64 *)(a3 + 216));
    result = Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline(v_stack_p8, a2, *(unsigned __int64 *)(a3 + 216) + 32, v_stack_p18);
    if ((unsigned int)(result) == 0) goto loc_00AEBC8E;
loc_00AEBA33:
    *(unsigned __int64 *)(v_stack_m488) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m488 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m488 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m488 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m488 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m488 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m488 + 96) = v_xmm0;
    a1 = (v_stack_m488) + (128);
    *(unsigned __int64 *)(a1 - 16) = v_xmm1;
    result = (*(unsigned __int64 *)(a3 + 216)) + (128);
    a2 = (8) - (1);
    if (condition_is_not_equal) goto loc_00AEBA33;
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    *(unsigned __int64 *)(a1 + 32) = v_xmm0;
    *(unsigned __int64 *)(a1 + 48) = v_xmm1;
    *(unsigned __int64 *)(a1 + 64) = v_xmm0;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 64);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 64) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 64)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 64) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 88);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 88) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 88)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 88) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 104);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 104) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 104)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 104) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 120);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 120) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 120)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 120) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 184);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 184) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 184)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 184) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 200);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 200) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 200)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 200) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 216);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 216) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 216)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 216) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 232);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 232) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 232)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 232) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1048);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1048) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1048)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1048) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1064);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1064) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1064)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1064) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1072);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1072) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1072)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 1072) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 128);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 128) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 128)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 128) = result;
    }
    result = RtlCopyToUser(*(unsigned __int64 *)(a3 + 224), *(unsigned __int64 *)(a3 + 216), v_r14, v_stack_p18);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 736)) + (32);
    result = RtlWriteULong64ToUser(a1, *(unsigned __int64 *)(a3 + 224), v_r14, v_stack_p18);
loc_00AEBBCF:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 16) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 32) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 48) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 64) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 80) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 216) + 96) = v_xmm0;
    v_rbx = (*(unsigned __int64 *)(a3 + 216)) + (128);
    *(unsigned __int64 *)(v_rbx - 16) = v_xmm1;
    result = (v_stack_m488) + (128);
    v_r12 = (8) - (1);
    if (condition_is_not_equal) goto loc_00AEBBCF;
    *(unsigned __int64 *)(v_rbx) = v_xmm0;
    *(unsigned __int64 *)(v_rbx + 16) = v_xmm1;
    *(unsigned __int64 *)(v_rbx + 32) = v_xmm0;
    *(unsigned __int64 *)(v_rbx + 48) = v_xmm1;
    *(unsigned __int64 *)(v_rbx + 64) = v_xmm0;
    if ((*(unsigned int *)(a3 + 592)) <= 0) goto loc_00AEBDA7;
    result = (unsigned int)((v_r14 - 1) & (7));
    v_r14 = (v_r14) - (result);
    v_rbx = (*(unsigned __int64 *)(a3 + 224) + 7) + (v_r14);
    result = PspCopyUserAttributes(v_rbx, *(unsigned __int64 *)(a3 + 224), a3, v_stack_p18);
    if (sign_flag) goto loc_00AEBDAB;
    result = RtlWriteULong64ToUser(*(unsigned __int64 *)(a3 + 224) + 1096, v_rbx, a3, v_stack_p18);
    goto loc_00AEBDA7;
loc_00AEBC8E:
    result = memcpy(*(unsigned __int64 *)(a3 + 224), v_rbx, v_r14, v_stack_p18);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 64);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 64) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 64)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 64) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 88);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 88) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 88)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 88) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 104);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 104) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 104)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 104) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 120);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 120) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 120)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 120) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 184);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 184) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 184)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 184) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 200);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 200) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 200)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 200) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 216);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 216) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 216)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 216) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 232);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 232) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 232)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 232) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1048);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1048) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1048)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1048) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1064);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1064) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1064)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1064) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1072);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1072) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1072)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 1072) = result;
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 128);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 128) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 128)) + (v_rsi);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 128) = result;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 736) + 32) = *(unsigned __int64 *)(a3 + 224);
loc_00AEBDA7:
    result = 0;
    goto loc_00AEBDAB;
loc_00AEBDAB:
    v_rsp = (v_rsp) + (0x4B0ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspCopyAndFixupParameters(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m488;
    uint64_t v_stack_m498;
    uint64_t v_stack_m4A0;
    uint64_t v_stack_m4A8;
    uint8_t v_stack_m4B0;
    uint32_t v_stack_m4B8;
    uint32_t v_stack_m4C0;
    uint32_t v_stack_m4C8;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (0x4B0ULL);
    local_r13 = 0;
    v_stack_m4A8 = 0;
    v_stack_m498 = *(uint64_t *)(arg3 + 0xD8);
    local_r14 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0xD8)))) + (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x3F0));
    v_stack_m4A0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_p18 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (((*(uint8_t *)(arg3 + 0x10)) & (64)) == 0) goto loc_00AEB8FF;
    if (((*(uint8_t *)(arg3 + 0x11)) & (1)) == 0) {
    }
    if ((*(uint32_t *)(arg3 + 0x58)) != 3) goto loc_00AEB956;
    if ((*(uint32_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x10)) <= 0) goto loc_00AEB956;
    v_stack_m4B0 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m4B8 = 6;
    v_stack_m4C0 = 0;
    v_stack_m4C8 = 0;
    result = ObDuplicateObject(Arg1, *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x10), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_m4A8);
    if (!(sign_flag)) {
        result = v_stack_m4A8;
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x10) = result;
    }
    if (Arg2 == 0) goto loc_00AEBA0F;
    Arg2 = 0;
    v_stack_p20 = 0;
loc_00AEB975:
    if (*(uint64_t *)(Arg2) == 0) goto loc_00AEB9DE;
    if (condition_is_less) goto loc_00AEB9BA;
    v_stack_m4B0 = (uint8_t)(v_stack_p18);
    v_stack_m4B8 = 6;
    result = ObDuplicateObject(v_stack_p8, *(uint64_t *)(Arg2), v_stack_m4A0, v_stack_m4A8);
    goto loc_00AEB9C6;
loc_00AEB9BA:
    Arg1 = 0;
    v_stack_m4A8 = 0;
loc_00AEB9C6:
    if (sign_flag) goto loc_00AEB9D0;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x20) = 0;
    goto loc_00AEB9DE;
loc_00AEB9D0:
    if (v_stack_p10 == (*(uint64_t *)(arg3 + 0xD8) + 32)) goto loc_00AEBDAB;
loc_00AEB9DE:
    local_r13 = (*(uint64_t *)(arg3 + 0xD8) + 32) + (8);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p20)) + 1);
    v_stack_p20 = (uint32_t)(Arg2);
    local_rsi = (Arg2) + (8);
    if (((uint32_t)(Arg2)) >= 3) goto loc_00AEBA0C;
    goto loc_00AEB975;
loc_00AEBA0C:
    local_r13 = 0;
loc_00AEBA0F:
    local_rsi = (*(uint64_t *)(arg3 + 0xE0)) - (*(uint64_t *)(arg3 + 0xD8));
    result = Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline(v_stack_p8, Arg2, *(uint64_t *)(arg3 + 0xD8) + 32, v_stack_p18);
    if ((uint32_t)(result) == 0) goto loc_00AEBC8E;
loc_00AEBA33:
    *(uint64_t *)(v_stack_m488) = v_xmm0;
    *(uint64_t *)(v_stack_m488 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m488 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m488 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_m488 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_m488 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_m488 + 0x60) = v_xmm0;
    Arg1 = (v_stack_m488) + (128);
    *(uint64_t *)(Arg1 - 0x10) = v_xmm1;
    result = (*(uint64_t *)(arg3 + 0xD8)) + (128);
    Arg2 = (8) - (1);
    if (condition_is_not_equal) goto loc_00AEBA33;
    *(uint64_t *)(Arg1) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x10) = v_xmm1;
    *(uint64_t *)(Arg1 + 0x20) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x30) = v_xmm1;
    *(uint64_t *)(Arg1 + 0x40) = v_xmm0;
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x40);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x40) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x40)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x40) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x58);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x58) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x58)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x58) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x68);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x68) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x68)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x68) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x78);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x78) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x78)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x78) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xB8);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xB8) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xB8)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xB8) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xC8);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xC8) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xC8)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xC8) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xD8);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xD8) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xD8)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xD8) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xE8);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xE8) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xE8)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0xE8) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x418);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x418) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x418)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x418) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x428);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x428) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x428)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x428) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x430);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x430) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x430)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x430) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x80);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x80) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x80)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x80) = result;
    }
    result = RtlCopyToUser(*(uint64_t *)(arg3 + 0xE0), *(uint64_t *)(arg3 + 0xD8), local_r14, v_stack_p18);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x2E0)) + (32);
    result = RtlWriteULong64ToUser(Arg1, *(uint64_t *)(arg3 + 0xE0), local_r14, v_stack_p18);
loc_00AEBBCF:
    *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x10) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x20) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x30) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x40) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x50) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0xD8) + 0x60) = v_xmm0;
    local_rbx = (*(uint64_t *)(arg3 + 0xD8)) + (128);
    *(uint64_t *)(local_rbx - 0x10) = v_xmm1;
    result = (v_stack_m488) + (128);
    local_r12 = (8) - (1);
    if (condition_is_not_equal) goto loc_00AEBBCF;
    *(uint64_t *)(local_rbx) = v_xmm0;
    *(uint64_t *)(local_rbx + 0x10) = v_xmm1;
    *(uint64_t *)(local_rbx + 0x20) = v_xmm0;
    *(uint64_t *)(local_rbx + 0x30) = v_xmm1;
    *(uint64_t *)(local_rbx + 0x40) = v_xmm0;
    if ((*(uint32_t *)(arg3 + 0x250)) <= 0) goto loc_00AEBDA7;
    result = (uint32_t)((local_r14 - 1) & (7));
    local_r14 = (local_r14) - (result);
    local_rbx = (*(uint64_t *)(arg3 + 0xE0) + 7) + (local_r14);
    result = PspCopyUserAttributes(local_rbx, *(uint64_t *)(arg3 + 0xE0), Arg3, v_stack_p18);
    if (sign_flag) goto loc_00AEBDAB;
    result = RtlWriteULong64ToUser(*(uint64_t *)(arg3 + 0xE0) + 1096, local_rbx, Arg3, v_stack_p18);
    goto loc_00AEBDA7;
loc_00AEBC8E:
    result = memcpy(*(uint64_t *)(arg3 + 0xE0), local_rbx, local_r14, v_stack_p18);
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x40);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x40) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x40)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x40) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x58);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x58) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x58)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x58) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x68);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x68) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x68)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x68) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x78);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x78) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x78)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x78) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xB8);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xB8) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xB8)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xB8) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xC8);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xC8) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xC8)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xC8) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xD8);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xD8) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xD8)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xD8) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xE8);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xE8) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xE8)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xE8) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x418);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x418) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x418)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x418) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x428);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x428) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x428)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x428) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x430);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x430) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x430)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x430) = result;
    }
    result = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x80);
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x80) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x80)) + (local_rsi);
        *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x80) = result;
    }
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x2E0) + 0x20) = *(uint64_t *)(arg3 + 0xE0);
loc_00AEBDA7:
    result = 0;
    goto loc_00AEBDAB;
loc_00AEBDAB:
    local_rsp = (local_rsp) + (0x4B0ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x10` | `8` | `R` |
| `Arg3` | `+ 0x11` | `8` | `R` |
| `Arg3` | `+ 0x58` | `32` | `R` |
| `Arg3` | `+ 0xD8` | `64` | `R` |
| `Arg3` | `+ 0xE0` | `64` | `R` |
| `Arg3` | `+ 0x250` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AEB878&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
