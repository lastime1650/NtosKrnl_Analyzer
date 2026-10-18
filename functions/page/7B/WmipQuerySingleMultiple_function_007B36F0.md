# WmipQuerySingleMultiple

- RVA: `0x007B36F0`–`0x007B3CEB` (길이 `1,531` bytes)
- VA: `0x00000001407B36F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D3240`
- 디코드: `359`개 명령, `1,531/1,531` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007B379C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007B37A1` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (function, `0x0064E4B4`)
- `0x007B37CF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007B37EE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007B3948` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007B395B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007B39A2` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007B3A29` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007B3A62` → [WmipQuerySetExecuteSI](../9E/WmipQuerySetExecuteSI_function_009E0574.md) (function, `0x009E0574`)
- `0x007B3A97` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (function, `0x0064E4B4`)
- `0x007B3ADF` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (function, `0x0064E4B4`)
- `0x007B3B45` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (function, `0x0064E4B4`)
- `0x007B3B5B` → [Feature_1045423416__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_1045423416__private_IsEnabledDeviceUsageNoInline_function_004F5B08.md) (function, `0x004F5B08`)
- `0x007B3C1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007B3C2C` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (function, `0x0064E4B4`)
- `0x007B3CAF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007B3CC1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x007B3CE4` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [IoWMIQuerySingleInstanceMultiple](IoWMIQuerySingleInstanceMultiple_function_007B21C0.md) at `0x007B2259`
- [sub_00B2FE0C](../B2/Unknown_function_00B2FE0C.md) at `0x00B2FE76`

### Static image references
- `0x007B370A` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x007B379C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007B37A1` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (`PAGE` → `.text`)
  - `0x007B37CF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007B37EE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007B3948` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007B395B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007B39A2` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007B3A29` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007B3A97` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (`PAGE` → `.text`)
  - `0x007B3ADF` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (`PAGE` → `.text`)
  - `0x007B3B45` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (`PAGE` → `.text`)
  - `0x007B3B5B` → [Feature_1045423416__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_1045423416__private_IsEnabledDeviceUsageNoInline_function_004F5B08.md) (`PAGE` → `.text`)
  - `0x007B3C1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007B3C2C` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (`PAGE` → `.text`)
  - `0x007B3CAF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007B3CC1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B36F0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
007B36F5  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
007B36FA  57                              push rdi
007B36FB  41 54                           push r12
007B36FD  41 55                           push r13
007B36FF  41 56                           push r14
007B3701  41 57                           push r15
007B3703  48 81 EC 60 03 00 00            sub rsp, 0x360
007B370A  48 8B 05 2F 70 65 00            mov rax, qword ptr [rip + 0x65702f]
007B3711  48 33 C4                        xor rax, rsp
007B3714  48 89 84 24 50 03 00 00         mov qword ptr [rsp + 0x350], rax
007B371C  44 89 4C 24 4C                  mov dword ptr [rsp + 0x4c], r9d
007B3721  4D 8B E0                        mov r12, r8
007B3724  88 54 24 48                     mov byte ptr [rsp + 0x48], dl
007B3728  48 89 8C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rcx
007B3730  4C 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r8
007B3738  4C 8B B4 24 B0 03 00 00         mov r14, qword ptr [rsp + 0x3b0]
007B3740  8B BC 24 B8 03 00 00            mov edi, dword ptr [rsp + 0x3b8]
007B3747  89 BC 24 98 00 00 00            mov dword ptr [rsp + 0x98], edi
007B374E  48 8B 84 24 C0 03 00 00         mov rax, qword ptr [rsp + 0x3c0]
007B3756  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
007B375E  48 8B 84 24 C8 03 00 00         mov rax, qword ptr [rsp + 0x3c8]
007B3766  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
007B376E  48 8B 84 24 D0 03 00 00         mov rax, qword ptr [rsp + 0x3d0]
007B3776  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
007B377E  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
007B3786  33 DB                           xor ebx, ebx
007B3788  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
007B378C  33 D2                           xor edx, edx
007B378E  41 B8 48 02 00 00               mov r8d, 0x248
007B3794  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
007B379C  E8 9F 34 F1 FF                  call 0x1406c6c40
007B37A1  E8 0E AD E9 FF                  call 0x14064e4b4
007B37A6  8B F3                           mov esi, ebx
007B37A8  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
007B37AC  4C 8B 94 24 88 00 00 00         mov r10, qword ptr [rsp + 0x88]
007B37B4  4D 85 D2                        test r10, r10
007B37B7  75 4B                           jne 0x1407b3804
007B37B9  48 8D 3C 7F                     lea rdi, [rdi + rdi*2]
007B37BD  48 C1 E7 03                     shl rdi, 3
007B37C1  41 B8 57 6D 69 70               mov r8d, 0x70696d57
007B37C7  48 8B D7                        mov rdx, rdi
007B37CA  B9 00 01 00 00                  mov ecx, 0x100
007B37CF  E8 1C E9 3C 00                  call 0x140b820f0
007B37D4  4C 8B E8                        mov r13, rax
007B37D7  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
007B37DF  48 85 C0                        test rax, rax
007B37E2  74 11                           je 0x1407b37f5
007B37E4  49 8D 56 08                     lea rdx, [r14 + 8]
007B37E8  4C 8B C7                        mov r8, rdi
007B37EB  48 8B C8                        mov rcx, rax
007B37EE  E8 4D 30 F1 FF                  call 0x1406c6840
007B37F3  EB 05                           jmp 0x1407b37fa
007B37F5  BE 9A 00 00 C0                  mov esi, 0xc000009a
007B37FA  4C 8B 94 24 88 00 00 00         mov r10, qword ptr [rsp + 0x88]
007B3802  EB 0B                           jmp 0x1407b380f
007B3804  4C 8B EB                        mov r13, rbx
007B3807  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
007B380F  85 F6                           test esi, esi
007B3811  0F 88 9D 04 00 00               js 0x1407b3cb4
007B3817  8B C3                           mov eax, ebx
007B3819  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
007B381D  4C 8B FB                        mov r15, rbx
007B3820  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
007B3828  44 8A F3                        mov r14b, bl
007B382B  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
007B382F  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
007B3837  49 8B D4                        mov rdx, r12
007B383A  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
007B383F  4C 8D 84 24 00 01 00 00         lea r8, [rsp + 0x100]
007B3847  4C 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r8
007B384F  41 B9 44 02 00 00               mov r9d, 0x244
007B3855  44 89 4C 24 70                  mov dword ptr [rsp + 0x70], r9d
007B385A  8B CB                           mov ecx, ebx
007B385C  48 89 9C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rbx
007B3864  41 BB F8 FF FF FF               mov r11d, 0xfffffff8
007B386A  89 4C 24 6C                     mov dword ptr [rsp + 0x6c], ecx
007B386E  8B F8                           mov edi, eax
007B3870  89 84 24 9C 00 00 00            mov dword ptr [rsp + 0x9c], eax
007B3877  3B 8C 24 98 00 00 00            cmp ecx, dword ptr [rsp + 0x98]
007B387E  0F 83 85 03 00 00               jae 0x1407b3c09
007B3884  4D 85 D2                        test r10, r10
007B3887  75 38                           jne 0x1407b38c1
007B3889  48 8D 04 49                     lea rax, [rcx + rcx*2]
007B388D  41 0F B7 4C C5 08               movzx ecx, word ptr [r13 + rax*8 + 8]
007B3893  66 89 8C 24 D0 00 00 00         mov word ptr [rsp + 0xd0], cx
007B389B  49 8B 54 C5 10                  mov rdx, qword ptr [r13 + rax*8 + 0x10]
007B38A0  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
007B38A5  48 89 94 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rdx
007B38AD  49 8B 54 C5 00                  mov rdx, qword ptr [r13 + rax*8]
007B38B2  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
007B38BA  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
007B38BF  EB 48                           jmp 0x1407b3909
007B38C1  48 8B C1                        mov rax, rcx
007B38C4  48 03 C0                        add rax, rax
007B38C7  4C 8B 9C 24 E0 00 00 00         mov r11, qword ptr [rsp + 0xe0]
007B38CF  41 0F 10 0C C3                  movups xmm1, xmmword ptr [r11 + rax*8]
007B38D4  0F 11 8C 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm1
007B38DC  49 8B 04 CA                     mov rax, qword ptr [r10 + rcx*8]
007B38E0  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
007B38E8  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
007B38F0  66 0F 6F C1                     movdqa xmm0, xmm1
007B38F4  66 0F 73 D8 08                  psrldq xmm0, 8
007B38F9  66 0F D6 44 24 78               movq qword ptr [rsp + 0x78], xmm0
007B38FF  66 0F 7E C9                     movd ecx, xmm1
007B3903  41 BB F8 FF FF FF               mov r11d, 0xfffffff8
007B3909  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
007B390D  44 0F B7 F1                     movzx r14d, cx
007B3911  41 83 C6 49                     add r14d, 0x49
007B3915  45 23 F3                        and r14d, r11d
007B3918  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
007B391D  75 12                           jne 0x1407b3931
007B391F  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
007B3923  41 3B C6                        cmp eax, r14d
007B3926  72 09                           jb 0x1407b3931
007B3928  48 8B FA                        mov rdi, rdx
007B392B  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
007B392F  EB 68                           jmp 0x1407b3999
007B3931  45 3B F1                        cmp r14d, r9d
007B3934  76 4E                           jbe 0x1407b3984
007B3936  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
007B393E  4C 3B C0                        cmp r8, rax
007B3941  74 0A                           je 0x1407b394d
007B3943  33 D2                           xor edx, edx
007B3945  49 8B C8                        mov rcx, r8
007B3948  E8 23 EF 3C 00                  call 0x140b82870
007B394D  41 8B D6                        mov edx, r14d
007B3950  B9 40 00 00 00                  mov ecx, 0x40
007B3955  41 B8 57 6D 69 70               mov r8d, 0x70696d57
007B395B  E8 90 E7 3C 00                  call 0x140b820f0
007B3960  4C 8B C0                        mov r8, rax
007B3963  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
007B396B  48 85 C0                        test rax, rax
007B396E  75 0F                           jne 0x1407b397f
007B3970  BE 9A 00 00 C0                  mov esi, 0xc000009a
007B3975  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
007B397A  E9 8A 02 00 00                  jmp 0x1407b3c09
007B397F  44 89 74 24 70                  mov dword ptr [rsp + 0x70], r14d
007B3984  49 8B F8                        mov rdi, r8
007B3987  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
007B398C  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
007B3994  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
007B3999  33 D2                           xor edx, edx
007B399B  44 8D 42 40                     lea r8d, [rdx + 0x40]
007B399F  48 8B CF                        mov rcx, rdi
007B39A2  E8 99 32 F1 FF                  call 0x1406c6c40
007B39A7  C7 47 2C 02 00 00 00            mov dword ptr [rdi + 0x2c], 2
007B39AE  44 89 37                        mov dword ptr [rdi], r14d
007B39B1  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
007B39B9  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
007B39BD  C7 47 30 40 00 00 00            mov dword ptr [rdi + 0x30], 0x40
007B39C4  44 89 77 38                     mov dword ptr [rdi + 0x38], r14d
007B39C8  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
007B39CC  66 89 4F 40                     mov word ptr [rdi + 0x40], cx
007B39D0  44 8A 74 24 48                  mov r14b, byte ptr [rsp + 0x48]
007B39D5  41 80 FE 01                     cmp r14b, 1
007B39D9  75 41                           jne 0x1407b3a1c
007B39DB  66 85 C9                        test cx, cx
007B39DE  74 3C                           je 0x1407b3a1c
007B39E0  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
007B39E5  45 84 C6                        test r14b, r8b
007B39E8  0F 85 F6 02 00 00               jne 0x1407b3ce4
007B39EE  0F B7 D1                        movzx edx, cx
007B39F1  49 03 D0                        add rdx, r8
007B39F4  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
007B39FE  48 3B D0                        cmp rdx, rax
007B3A01  77 05                           ja 0x1407b3a08
007B3A03  49 3B D0                        cmp rdx, r8
007B3A06  73 14                           jae 0x1407b3a1c
007B3A08  8A 00                           mov al, byte ptr [rax]
007B3A0A  48 8B 94 24 D8 00 00 00         mov rdx, qword ptr [rsp + 0xd8]
007B3A12  0F B7 8C 24 D0 00 00 00         movzx ecx, word ptr [rsp + 0xd0]
007B3A1A  EB 05                           jmp 0x1407b3a21
007B3A1C  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
007B3A21  44 0F B7 C1                     movzx r8d, cx
007B3A25  48 8D 4F 42                     lea rcx, [rdi + 0x42]
007B3A29  E8 12 2E F1 FF                  call 0x1406c6840
007B3A2E  90                              nop
007B3A2F  8B 07                           mov eax, dword ptr [rdi]
007B3A31  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
007B3A35  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007B3A3A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007B3A3F  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
007B3A43  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007B3A47  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
007B3A4C  41 B1 01                        mov r9b, 1
007B3A4F  45 8A C6                        mov r8b, r14b
007B3A52  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
007B3A5A  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
007B3A62  E8 0D CB 22 00                  call 0x1409e0574
007B3A67  85 C0                           test eax, eax
007B3A69  0F 88 36 01 00 00               js 0x1407b3ba5
007B3A6F  8B 47 2C                        mov eax, dword ptr [rdi + 0x2c]
007B3A72  0F BA E0 08                     bt eax, 8
007B3A76  0F 82 29 01 00 00               jb 0x1407b3ba5
007B3A7C  FF 44 24 60                     inc dword ptr [rsp + 0x60]
007B3A80  A8 20                           test al, 0x20
007B3A82  74 3D                           je 0x1407b3ac1
007B3A84  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
007B3A87  83 C0 07                        add eax, 7
007B3A8A  41 BE F8 FF FF FF               mov r14d, 0xfffffff8
007B3A90  41 23 C6                        and eax, r14d
007B3A93  01 44 24 44                     add dword ptr [rsp + 0x44], eax
007B3A97  E8 18 AA E9 FF                  call 0x14064e4b4
007B3A9C  85 C0                           test eax, eax
007B3A9E  74 14                           je 0x1407b3ab4
007B3AA0  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
007B3AA3  83 C0 07                        add eax, 7
007B3AA6  49 23 C6                        and rax, r14
007B3AA9  4C 03 F8                        add r15, rax
007B3AAC  4C 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r15
007B3AB4  41 B6 01                        mov r14b, 1
007B3AB7  44 88 74 24 40                  mov byte ptr [rsp + 0x40], r14b
007B3ABC  E9 E9 00 00 00                  jmp 0x1407b3baa
007B3AC1  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
007B3AC6  45 84 F6                        test r14b, r14b
007B3AC9  74 3A                           je 0x1407b3b05
007B3ACB  8B 7C 24 50                     mov edi, dword ptr [rsp + 0x50]
007B3ACF  83 C7 07                        add edi, 7
007B3AD2  8B C7                           mov eax, edi
007B3AD4  B9 F8 FF FF FF                  mov ecx, 0xfffffff8
007B3AD9  23 C1                           and eax, ecx
007B3ADB  01 44 24 44                     add dword ptr [rsp + 0x44], eax
007B3ADF  E8 D0 A9 E9 FF                  call 0x14064e4b4
007B3AE4  85 C0                           test eax, eax
007B3AE6  0F 84 BE 00 00 00               je 0x1407b3baa
007B3AEC  41 BB F8 FF FF FF               mov r11d, 0xfffffff8
007B3AF2  49 23 FB                        and rdi, r11
007B3AF5  4C 03 FF                        add r15, rdi
007B3AF8  4C 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r15
007B3B00  E9 AB 00 00 00                  jmp 0x1407b3bb0
007B3B05  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007B3B0D  48 85 C0                        test rax, rax
007B3B10  74 07                           je 0x1407b3b19
007B3B12  8B 4C 24 68                     mov ecx, dword ptr [rsp + 0x68]
007B3B16  89 48 0C                        mov dword ptr [rax + 0xc], ecx
007B3B19  48 8B CF                        mov rcx, rdi
007B3B1C  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
007B3B1F  EB 06                           jmp 0x1407b3b27
007B3B21  48 03 C8                        add rcx, rax
007B3B24  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
007B3B27  85 C0                           test eax, eax
007B3B29  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
007B3B31  75 EE                           jne 0x1407b3b21
007B3B33  8B 7C 24 50                     mov edi, dword ptr [rsp + 0x50]
007B3B37  83 C7 07                        add edi, 7
007B3B3A  B9 F8 FF FF FF                  mov ecx, 0xfffffff8
007B3B3F  23 F9                           and edi, ecx
007B3B41  01 7C 24 44                     add dword ptr [rsp + 0x44], edi
007B3B45  E8 6A A9 E9 FF                  call 0x14064e4b4
007B3B4A  85 C0                           test eax, eax
007B3B4C  74 0D                           je 0x1407b3b5b
007B3B4E  8B C7                           mov eax, edi
007B3B50  4C 03 F8                        add r15, rax
007B3B53  4C 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r15
007B3B5B  E8 A8 1F D4 FF                  call 0x1404f5b08
007B3B60  85 C0                           test eax, eax
007B3B62  74 16                           je 0x1407b3b7a
007B3B64  8B 54 24 4C                     mov edx, dword ptr [rsp + 0x4c]
007B3B68  3B D7                           cmp edx, edi
007B3B6A  76 08                           jbe 0x1407b3b74
007B3B6C  2B D7                           sub edx, edi
007B3B6E  89 54 24 4C                     mov dword ptr [rsp + 0x4c], edx
007B3B72  EB 0A                           jmp 0x1407b3b7e
007B3B74  89 5C 24 4C                     mov dword ptr [rsp + 0x4c], ebx
007B3B78  EB 04                           jmp 0x1407b3b7e
007B3B7A  29 7C 24 4C                     sub dword ptr [rsp + 0x4c], edi
007B3B7E  8B C7                           mov eax, edi
007B3B80  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
007B3B85  48 03 D0                        add rdx, rax
007B3B88  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
007B3B8D  8B C2                           mov eax, edx
007B3B8F  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007B3B97  2B C1                           sub eax, ecx
007B3B99  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
007B3B9D  41 BB F8 FF FF FF               mov r11d, 0xfffffff8
007B3BA3  EB 10                           jmp 0x1407b3bb5
007B3BA5  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
007B3BAA  41 BB F8 FF FF FF               mov r11d, 0xfffffff8
007B3BB0  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
007B3BB5  8B 4C 24 6C                     mov ecx, dword ptr [rsp + 0x6c]
007B3BB9  FF C1                           inc ecx
007B3BBB  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
007B3BBF  4C 8B 84 24 A0 00 00 00         mov r8, qword ptr [rsp + 0xa0]
007B3BC7  44 8B 4C 24 70                  mov r9d, dword ptr [rsp + 0x70]
007B3BCC  4C 8B 94 24 88 00 00 00         mov r10, qword ptr [rsp + 0x88]
007B3BD4  E9 91 FC FF FF                  jmp 0x1407b386a
007B3BD9  8B F0                           mov esi, eax
007B3BDB  33 DB                           xor ebx, ebx
007B3BDD  4C 8B AC 24 C0 00 00 00         mov r13, qword ptr [rsp + 0xc0]
007B3BE5  4C 8B BC 24 90 00 00 00         mov r15, qword ptr [rsp + 0x90]
007B3BED  4C 8B A4 24 F0 00 00 00         mov r12, qword ptr [rsp + 0xf0]
007B3BF5  8B BC 24 9C 00 00 00            mov edi, dword ptr [rsp + 0x9c]
007B3BFC  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
007B3C01  4C 8B 84 24 A0 00 00 00         mov r8, qword ptr [rsp + 0xa0]
007B3C09  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
007B3C11  4C 3B C0                        cmp r8, rax
007B3C14  74 0A                           je 0x1407b3c20
007B3C16  33 D2                           xor edx, edx
007B3C18  49 8B C8                        mov rcx, r8
007B3C1B  E8 50 EC 3C 00                  call 0x140b82870
007B3C20  B8 95 02 00 C0                  mov eax, 0xc0000295
007B3C25  39 5C 24 60                     cmp dword ptr [rsp + 0x60], ebx
007B3C29  0F 44 F0                        cmove esi, eax
007B3C2C  E8 83 A8 E9 FF                  call 0x14064e4b4
007B3C31  85 C0                           test eax, eax
007B3C33  74 42                           je 0x1407b3c77
007B3C35  B8 FF FF FF FF                  mov eax, 0xffffffff
007B3C3A  4C 3B F8                        cmp r15, rax
007B3C3D  76 09                           jbe 0x1407b3c48
007B3C3F  BE 95 00 00 C0                  mov esi, 0xc0000095
007B3C44  8B FB                           mov edi, ebx
007B3C46  EB 25                           jmp 0x1407b3c6d
007B3C48  85 F6                           test esi, esi
007B3C4A  78 1E                           js 0x1407b3c6a
007B3C4C  45 84 F6                        test r14b, r14b
007B3C4F  74 19                           je 0x1407b3c6a
007B3C51  BF 38 00 00 00                  mov edi, 0x38
007B3C56  41 89 3C 24                     mov dword ptr [r12], edi
007B3C5A  41 C7 44 24 2C 20 00 00 00      mov dword ptr [r12 + 0x2c], 0x20
007B3C63  45 89 7C 24 30                  mov dword ptr [r12 + 0x30], r15d
007B3C68  EB 03                           jmp 0x1407b3c6d
007B3C6A  41 8B FF                        mov edi, r15d
007B3C6D  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
007B3C75  EB 2C                           jmp 0x1407b3ca3
007B3C77  85 F6                           test esi, esi
007B3C79  78 20                           js 0x1407b3c9b
007B3C7B  45 84 F6                        test r14b, r14b
007B3C7E  74 1B                           je 0x1407b3c9b
007B3C80  BF 38 00 00 00                  mov edi, 0x38
007B3C85  41 89 3C 24                     mov dword ptr [r12], edi
007B3C89  41 C7 44 24 2C 20 00 00 00      mov dword ptr [r12 + 0x2c], 0x20
007B3C92  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
007B3C96  41 89 4C 24 30                  mov dword ptr [r12 + 0x30], ecx
007B3C9B  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
007B3CA3  89 38                           mov dword ptr [rax], edi
007B3CA5  4D 85 ED                        test r13, r13
007B3CA8  74 0A                           je 0x1407b3cb4
007B3CAA  33 D2                           xor edx, edx
007B3CAC  49 8B CD                        mov rcx, r13
007B3CAF  E8 BC EB 3C 00                  call 0x140b82870
007B3CB4  8B C6                           mov eax, esi
007B3CB6  48 8B 8C 24 50 03 00 00         mov rcx, qword ptr [rsp + 0x350]
007B3CBE  48 33 CC                        xor rcx, rsp
007B3CC1  E8 7A 89 EF FF                  call 0x1406ac640
007B3CC6  4C 8D 9C 24 60 03 00 00         lea r11, [rsp + 0x360]
007B3CCE  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
007B3CD2  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
007B3CD6  49 8B E3                        mov rsp, r11
007B3CD9  41 5F                           pop r15
007B3CDB  41 5E                           pop r14
007B3CDD  41 5D                           pop r13
007B3CDF  41 5C                           pop r12
007B3CE1  5F                              pop rdi
007B3CE2  C3                              ret
007B3CE3  CC                              int3
007B3CE4  E8 E7 62 0E 00                  call 0x140899fd0
007B3CE9  90                              nop
007B3CEA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmipQuerySingleMultiple(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int16 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned int v_stack_m2EC;
    unsigned int v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned int v_stack_m318;
    unsigned int v_stack_m31C;
    unsigned int v_stack_m320;
    unsigned int v_stack_m324;
    unsigned int v_stack_m328;
    unsigned __int64 v_stack_m330;
    unsigned int v_stack_m338;
    unsigned int v_stack_m33C;
    unsigned __int8 v_stack_m340;
    unsigned int v_stack_m344;
    unsigned __int8 v_stack_m348;
    unsigned __int64 v_stack_m358;
    unsigned int v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (864);
    result = (*(unsigned __int64 *)(v_rip + 6647855)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m33C = a4;
    v_stack_m340 = (unsigned __int8)(a2);
    v_stack_m2A0 = a1;
    v_stack_m298 = a3;
    v_stack_m2F0 = (unsigned int)((unsigned int)(a6));
    v_stack_m300 = a7;
    v_stack_m2A8 = a8;
    v_stack_m2E0 = a9;
    v_stack_m2C0 = a9;
    v_rbx = 0;
    v_stack_m320 = 0;
    a2 = 0;
    result = memset(v_stack_m288, a2, 584, a4);
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline(v_stack_m288, a2, 584, a4);
    v_stack_m328 = 0;
    if (v_stack_m300 != 0) goto loc_007B3804;
    v_rdi = ((unsigned int)(a6) + (unsigned int)(a6) * 2) << (3);
    result = ExAllocatePool2(256, v_rdi, (unsigned int)(0x70696D57ULL), a4);
    v_stack_m2C8 = result;
    if (result == 0) goto loc_007B37F5;
    result = memcpy(result, a5 + 8, v_rdi, a4);
    goto loc_007B37FA;
loc_007B37F5:
loc_007B37FA:
    goto loc_007B380F;
loc_007B3804:
    v_stack_m2C8 = 0;
loc_007B380F:
    if (sign_flag) goto loc_007B3CB4;
    v_stack_m344 = 0;
    v_stack_m2F8 = 0;
    v_stack_m348 = 0;
    v_stack_m308 = 0;
    v_stack_m330 = a3;
    v_stack_m2E8 = v_stack_m288;
    v_stack_m318 = 580;
    v_stack_m2D0 = 0;
loc_007B386A:
    v_stack_m31C = 0;
    v_stack_m2EC = 0;
    if (0 >= v_stack_m2F0) goto loc_007B3C09;
    if (v_stack_m300 != 0) goto loc_007B38C1;
    v_stack_m2B8 = (unsigned __int16)(*(unsigned __int16 *)(0 + 0 + 0 * 2 * 8 + 8));
    v_stack_m310 = *(unsigned __int64 *)(0 + 0 + 0 * 2 * 8 + 16);
    v_stack_m2B0 = *(unsigned __int64 *)(0 + 0 + 0 * 2 * 8 + 16);
    v_stack_m2D8 = *(unsigned __int64 *)(0 + 0 + 0 * 2 * 8);
    goto loc_007B3909;
loc_007B38C1:
    result = (*(unsigned __int16 *)(0 + 0 + 0 * 2 * 8 + 8)) + (*(unsigned __int16 *)(0 + 0 + 0 * 2 * 8 + 8));
    v_stack_m2B8 = v_xmm1;
    v_stack_m2D0 = *(unsigned __int64 *)(v_stack_m300 + *(unsigned __int16 *)(0 + 0 + 0 * 2 * 8 + 8) * 8);
    v_stack_m2D8 = 0;
    v_stack_m310 = v_xmm0;
loc_007B3909:
    v_stack_m338 = (unsigned int)(*(unsigned __int16 *)(0 + 0 + 0 * 2 * 8 + 8));
    v_r14 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(0 + 0 + 0 * 2 * 8 + 8))) + (73));
    v_r14 = (unsigned int)((v_r14) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    if (v_stack_m348 != 0) goto loc_007B3931;
    if (((unsigned int)((unsigned int)(v_stack_m33C))) < ((unsigned int)(v_r14))) goto loc_007B3931;
    v_stack_m324 = (unsigned int)((unsigned int)(v_stack_m33C));
    goto loc_007B3999;
loc_007B3931:
    if (((unsigned int)(v_r14)) <= 580) goto loc_007B3984;
    result = v_stack_m288;
    if (v_stack_m288 != v_stack_m288) {
        a2 = 0;
        a1 = v_stack_m288;
        result = ExFreePoolWithTag(a1, a2, v_stack_m288, 580);
    }
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(0x70696D57ULL), 580);
    v_stack_m2E8 = result;
    if (result != 0) goto loc_007B397F;
    goto loc_007B3C09;
loc_007B397F:
    v_stack_m318 = (unsigned int)(v_stack_m348);
loc_007B3984:
    v_stack_m324 = (unsigned int)(v_stack_m348);
    v_stack_m308 = 0;
    v_stack_m348 = 1;
loc_007B3999:
    a2 = 0;
    result = memset(result, a2, a2 + 64, 580);
    *(unsigned int *)(result + 44) = 2;
    *(unsigned int *)(result) = (unsigned int)(v_stack_m348);
    *(unsigned __int64 *)(result + 16) = v_stack_m2D8;
    *(unsigned int *)(result + 48) = 64;
    *(unsigned int *)(result + 56) = (unsigned int)(v_stack_m348);
    *(unsigned __int16 *)(result + 64) = (unsigned __int16)((unsigned int)(v_stack_m338));
    if (((unsigned __int8)(v_stack_m340)) != 1) goto loc_007B3A1C;
    if ((unsigned __int16)((unsigned int)(v_stack_m338)) == 0) goto loc_007B3A1C;
    if ((((unsigned __int8)(v_stack_m340)) & ((unsigned __int8)(v_stack_m310))) != 0) goto loc_007B3CE4;
    a2 = ((unsigned __int16)((unsigned int)(v_stack_m338))) + (v_stack_m310);
    if (a2 > v_stack_m2D8) goto loc_007B3A08;
    if (a2 >= v_stack_m310) goto loc_007B3A1C;
loc_007B3A08:
    goto loc_007B3A21;
loc_007B3A1C:
loc_007B3A21:
    result = memcpy(result + 66, v_stack_m310, (unsigned __int16)(v_stack_m2B8), 580);
    v_stack_m338 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    v_stack_m358 = v_stack_m338;
    v_stack_m360 = (unsigned int)((unsigned int)(v_stack_m324));
    v_stack_m368 = result;
    result = WmipQuerySetExecuteSI(v_stack_m2D0, v_stack_m2A0, (unsigned __int8)(v_stack_m340), 1);
    if (sign_flag) goto loc_007B3BA5;
    if (condition_is_below) goto loc_007B3BA5;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 44)))) & (32)) == 0) goto loc_007B3AC1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) + (7));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline(v_stack_m2D0, v_stack_m2A0, (unsigned __int8)(v_stack_m340), 1);
    v_r15 = 0;
    if ((unsigned int)(result) != 0) {
        result = *(unsigned int *)(result + 48);
        result = (unsigned int)((result) + (7));
        result = (result) & ((unsigned int)(0xFFFFFFF8ULL));
        v_r15 = (0) + (result);
        v_stack_m2F8 = v_r15;
    }
    v_stack_m348 = 1;
    goto loc_007B3BAA;
loc_007B3AC1:
    if ((unsigned __int8)(v_stack_m348) == 0) goto loc_007B3B05;
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m338)) + (7));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline((unsigned int)(0xFFFFFFF8ULL), v_stack_m2A0, (unsigned __int8)(v_stack_m340), 1);
    if ((unsigned int)(result) == 0) goto loc_007B3BAA;
    v_rdi = (v_rdi) & ((unsigned int)(0xFFFFFFF8ULL));
    v_r15 = (v_r15) + (v_rdi);
    v_stack_m2F8 = v_r15;
    goto loc_007B3BB0;
loc_007B3B05:
    if (v_stack_m308 != 0) {
        a1 = v_stack_m320;
        *(unsigned int *)(v_stack_m308 + 12) = (unsigned int)(a1);
    }
    goto loc_007B3B27;
loc_007B3B21:
    a1 = (v_rdi) + ((unsigned int)(*(unsigned int *)(v_rdi + 12)));
loc_007B3B27:
    v_stack_m308 = a1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))) != 0) goto loc_007B3B21;
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m338)) + (7));
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline((unsigned int)(0xFFFFFFF8ULL), v_stack_m2A0, (unsigned __int8)(v_stack_m340), 1);
    if ((unsigned int)(result) != 0) {
        result = (unsigned int)(v_rdi);
        v_r15 = (v_r15) + (result);
        v_stack_m2F8 = v_r15;
    }
    result = Feature_1045423416__private_IsEnabledDeviceUsageNoInline((unsigned int)(0xFFFFFFF8ULL), v_stack_m2A0, (unsigned __int8)(v_stack_m340), 1);
    if ((unsigned int)(result) == 0) goto loc_007B3B7A;
    if (((unsigned int)((unsigned int)(v_stack_m33C))) <= ((unsigned int)(v_rdi))) goto loc_007B3B74;
    a2 = (unsigned int)(((unsigned int)(v_stack_m33C)) - ((unsigned int)(v_rdi)));
    v_stack_m33C = a2;
    goto loc_007B3B7E;
loc_007B3B74:
    v_stack_m33C = 0;
    goto loc_007B3B7E;
loc_007B3B7A:
loc_007B3B7E:
    a2 = (v_stack_m330) + ((unsigned int)((unsigned int)(v_rdi)));
    v_stack_m330 = a2;
    result = (unsigned int)(((unsigned int)(a2)) - ((unsigned int)(v_stack_m308)));
    v_stack_m320 = (unsigned int)(result);
    goto loc_007B3BB5;
loc_007B3BA5:
loc_007B3BAA:
loc_007B3BB0:
loc_007B3BB5:
    a1 = (unsigned int)(((unsigned int)(v_stack_m31C)) + 1);
    goto loc_007B386A;
loc_007B3C09:
    result = v_stack_m288;
    if (v_stack_m2E8 != v_stack_m288) {
        a2 = 0;
        a1 = v_stack_m2E8;
        result = ExFreePoolWithTag(a1, a2, v_stack_m2E8, (unsigned int)(v_stack_m318));
    }
    v_rsi = (unsigned int)(0xC000009AULL);
    if (v_stack_m328 == 0) { v_rsi = (unsigned int)((unsigned int)(0xC0000295ULL)); }
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline(a1, a2, v_stack_m2E8, (unsigned int)(v_stack_m318));
    if ((unsigned int)(result) == 0) goto loc_007B3C77;
    if (v_r15 <= ((unsigned int)(0xFFFFFFFFULL))) goto loc_007B3C48;
    goto loc_007B3C6D;
loc_007B3C48:
    if (sign_flag) goto loc_007B3C6A;
    if ((unsigned __int8)(v_stack_m348) == 0) goto loc_007B3C6A;
    *(unsigned int *)(a3) = 56;
    *(unsigned int *)(a3 + 44) = 32;
    *(unsigned int *)(a3 + 48) = (unsigned int)(v_r15);
    goto loc_007B3C6D;
loc_007B3C6A:
loc_007B3C6D:
    goto loc_007B3CA3;
loc_007B3C77:
    if (sign_flag) goto loc_007B3C9B;
    v_rdi = (unsigned int)((unsigned int)(v_r15));
    if ((unsigned __int8)(v_stack_m348) != 0) {
        v_rdi = 56;
        *(unsigned int *)(a3) = (unsigned int)(v_rdi);
        *(unsigned int *)(a3 + 44) = 32;
        a1 = v_stack_m344;
        *(unsigned int *)(a3 + 48) = (unsigned int)(a1);
    }
loc_007B3CA3:
    *(unsigned int *)(v_stack_m2E0) = (unsigned int)(v_rdi);
    result = v_stack_m2E0;
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, v_stack_m2E8, (unsigned int)(v_stack_m318));
    }
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m2E8, (unsigned int)(v_stack_m318));
    return result;
loc_007B3CE4:
    result = ExRaiseDatatypeMisalignment(a1, a2, v_stack_m2E8, (unsigned int)(v_stack_m318));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WmipQuerySingleMultiple(int64_t Arg1, int32_t Arg2, void *Arg3, int32_t Arg4, void *Arg5, void *Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m288;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint16_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint32_t v_stack_m2EC;
    uint32_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_m310;
    uint32_t v_stack_m318;
    uint32_t v_stack_m31C;
    uint32_t v_stack_m320;
    uint32_t v_stack_m324;
    uint32_t v_stack_m328;
    uint64_t v_stack_m330;
    uint32_t v_stack_m338;
    uint32_t v_stack_m33C;
    uint8_t v_stack_m340;
    uint32_t v_stack_m344;
    uint8_t v_stack_m348;
    uint64_t v_stack_m358;
    uint32_t v_stack_m360;
    uint64_t v_stack_m368;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (864);
    result = (*(uint64_t *)(v_rip + 0x65702F)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m33C = Arg4;
    v_stack_m340 = (uint8_t)(Arg2);
    v_stack_m2A0 = Arg1;
    v_stack_m298 = Arg3;
    v_stack_m2F0 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m300 = Arg7;
    v_stack_m2A8 = Arg8;
    v_stack_m2E0 = Arg9;
    v_stack_m2C0 = Arg9;
    local_rbx = 0;
    v_stack_m320 = 0;
    Arg2 = 0;
    result = memset(v_stack_m288, Arg2, 584, Arg4);
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline(v_stack_m288, Arg2, 584, Arg4);
    v_stack_m328 = 0;
    if (v_stack_m300 != 0) goto loc_007B3804;
    local_rdi = ((uint32_t)(Arg6) + (uint32_t)(Arg6) * 2) << (3);
    result = ExAllocatePool2(256, local_rdi, (uint32_t)(0x70696D57ULL), Arg4);
    v_stack_m2C8 = result;
    if (result == 0) goto loc_007B37F5;
    result = memcpy(result, Arg5 + 8, local_rdi, Arg4);
    goto loc_007B37FA;
loc_007B37F5:
loc_007B37FA:
    goto loc_007B380F;
loc_007B3804:
    v_stack_m2C8 = 0;
loc_007B380F:
    if (sign_flag) goto loc_007B3CB4;
    v_stack_m344 = 0;
    v_stack_m2F8 = 0;
    v_stack_m348 = 0;
    v_stack_m308 = 0;
    v_stack_m330 = Arg3;
    v_stack_m2E8 = v_stack_m288;
    v_stack_m318 = 580;
    v_stack_m2D0 = 0;
loc_007B386A:
    v_stack_m31C = 0;
    v_stack_m2EC = 0;
    if (0 >= v_stack_m2F0) goto loc_007B3C09;
    if (v_stack_m300 != 0) goto loc_007B38C1;
    v_stack_m2B8 = (uint16_t)(*(uint16_t *)(0 + 0x0 + 0x0 * 2 * 8 + 0x8));
    v_stack_m310 = *(uint64_t *)(0 + 0x0 + 0x0 * 2 * 8 + 0x10);
    v_stack_m2B0 = *(uint64_t *)(0 + 0x0 + 0x0 * 2 * 8 + 0x10);
    v_stack_m2D8 = *(uint64_t *)(0 + 0x0 + 0x0 * 2 * 8);
    goto loc_007B3909;
loc_007B38C1:
    result = (*(uint16_t *)(0 + 0x0 + 0x0 * 2 * 8 + 0x8)) + (*(uint16_t *)(0 + 0x0 + 0x0 * 2 * 8 + 0x8));
    v_stack_m2B8 = v_xmm1;
    v_stack_m2D0 = *(uint64_t *)(v_stack_m300 + *(uint16_t *)(0 + 0x0 + 0x0 * 2 * 8 + 0x8) * 8);
    v_stack_m2D8 = 0;
    v_stack_m310 = v_xmm0;
loc_007B3909:
    v_stack_m338 = (uint32_t)(*(uint16_t *)(0 + 0x0 + 0x0 * 2 * 8 + 0x8));
    local_r14 = (uint32_t)(((uint16_t)(*(uint16_t *)(0 + 0x0 + 0x0 * 2 * 8 + 0x8))) + (73));
    local_r14 = (uint32_t)((local_r14) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    if (v_stack_m348 != 0) goto loc_007B3931;
    if (((uint32_t)((uint32_t)(v_stack_m33C))) < ((uint32_t)(local_r14))) goto loc_007B3931;
    v_stack_m324 = (uint32_t)((uint32_t)(v_stack_m33C));
    goto loc_007B3999;
loc_007B3931:
    if (((uint32_t)(local_r14)) <= 580) goto loc_007B3984;
    result = v_stack_m288;
    if (v_stack_m288 != v_stack_m288) {
        Arg2 = 0;
        Arg1 = v_stack_m288;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m288, 580);
    }
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(0x70696D57ULL), 580);
    v_stack_m2E8 = result;
    if (result != 0) goto loc_007B397F;
    goto loc_007B3C09;
loc_007B397F:
    v_stack_m318 = (uint32_t)(v_stack_m348);
loc_007B3984:
    v_stack_m324 = (uint32_t)(v_stack_m348);
    v_stack_m308 = 0;
    v_stack_m348 = 1;
loc_007B3999:
    Arg2 = 0;
    result = memset(result, Arg2, Arg2 + 64, 580);
    *(uint32_t *)(result + 0x2C) = 2;
    *(uint32_t *)(result) = (uint32_t)(v_stack_m348);
    *(uint64_t *)(result + 0x10) = v_stack_m2D8;
    *(uint32_t *)(result + 0x30) = 64;
    *(uint32_t *)(result + 0x38) = (uint32_t)(v_stack_m348);
    *(uint16_t *)(result + 0x40) = (uint16_t)((uint32_t)(v_stack_m338));
    if (((uint8_t)(v_stack_m340)) != 1) goto loc_007B3A1C;
    if ((uint16_t)((uint32_t)(v_stack_m338)) == 0) goto loc_007B3A1C;
    if ((((uint8_t)(v_stack_m340)) & ((uint8_t)(v_stack_m310))) != 0) goto loc_007B3CE4;
    Arg2 = ((uint16_t)((uint32_t)(v_stack_m338))) + (v_stack_m310);
    if (Arg2 > v_stack_m2D8) goto loc_007B3A08;
    if (Arg2 >= v_stack_m310) goto loc_007B3A1C;
loc_007B3A08:
    goto loc_007B3A21;
loc_007B3A1C:
loc_007B3A21:
    result = memcpy(result + 66, v_stack_m310, (uint16_t)(v_stack_m2B8), 580);
    v_stack_m338 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    v_stack_m358 = v_stack_m338;
    v_stack_m360 = (uint32_t)((uint32_t)(v_stack_m324));
    v_stack_m368 = result;
    result = WmipQuerySetExecuteSI(v_stack_m2D0, v_stack_m2A0, (uint8_t)(v_stack_m340), 1);
    if (sign_flag) goto loc_007B3BA5;
    if (condition_is_below) goto loc_007B3BA5;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x2C)))) & (32)) == 0) goto loc_007B3AC1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) + (7));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline(v_stack_m2D0, v_stack_m2A0, (uint8_t)(v_stack_m340), 1);
    local_r15 = 0;
    if ((uint32_t)(result) != 0) {
        result = *(uint32_t *)(result + 0x30);
        result = (uint32_t)((result) + (7));
        result = (result) & ((uint32_t)(0xFFFFFFF8ULL));
        local_r15 = (0) + (result);
        v_stack_m2F8 = local_r15;
    }
    v_stack_m348 = 1;
    goto loc_007B3BAA;
loc_007B3AC1:
    if ((uint8_t)(v_stack_m348) == 0) goto loc_007B3B05;
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m338)) + (7));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline((uint32_t)(0xFFFFFFF8ULL), v_stack_m2A0, (uint8_t)(v_stack_m340), 1);
    if ((uint32_t)(result) == 0) goto loc_007B3BAA;
    local_rdi = (local_rdi) & ((uint32_t)(0xFFFFFFF8ULL));
    local_r15 = (local_r15) + (local_rdi);
    v_stack_m2F8 = local_r15;
    goto loc_007B3BB0;
loc_007B3B05:
    if (v_stack_m308 != 0) {
        Arg1 = v_stack_m320;
        *(uint32_t *)(v_stack_m308 + 0xC) = (uint32_t)(Arg1);
    }
    goto loc_007B3B27;
loc_007B3B21:
    Arg1 = (local_rdi) + ((uint32_t)(*(uint32_t *)(local_rdi + 0xC)));
loc_007B3B27:
    v_stack_m308 = Arg1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0xC))) != 0) goto loc_007B3B21;
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m338)) + (7));
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline((uint32_t)(0xFFFFFFF8ULL), v_stack_m2A0, (uint8_t)(v_stack_m340), 1);
    if ((uint32_t)(result) != 0) {
        result = (uint32_t)(local_rdi);
        local_r15 = (local_r15) + (result);
        v_stack_m2F8 = local_r15;
    }
    result = Feature_1045423416__private_IsEnabledDeviceUsageNoInline((uint32_t)(0xFFFFFFF8ULL), v_stack_m2A0, (uint8_t)(v_stack_m340), 1);
    if ((uint32_t)(result) == 0) goto loc_007B3B7A;
    if (((uint32_t)((uint32_t)(v_stack_m33C))) <= ((uint32_t)(local_rdi))) goto loc_007B3B74;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m33C)) - ((uint32_t)(local_rdi)));
    v_stack_m33C = Arg2;
    goto loc_007B3B7E;
loc_007B3B74:
    v_stack_m33C = 0;
    goto loc_007B3B7E;
loc_007B3B7A:
loc_007B3B7E:
    Arg2 = (v_stack_m330) + ((uint32_t)((uint32_t)(local_rdi)));
    v_stack_m330 = Arg2;
    result = (uint32_t)(((uint32_t)(Arg2)) - ((uint32_t)(v_stack_m308)));
    v_stack_m320 = (uint32_t)(result);
    goto loc_007B3BB5;
loc_007B3BA5:
loc_007B3BAA:
loc_007B3BB0:
loc_007B3BB5:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m31C)) + 1);
    goto loc_007B386A;
loc_007B3C09:
    result = v_stack_m288;
    if (v_stack_m2E8 != v_stack_m288) {
        Arg2 = 0;
        Arg1 = v_stack_m2E8;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m2E8, (uint32_t)(v_stack_m318));
    }
    local_rsi = (uint32_t)(0xC000009AULL);
    if (v_stack_m328 == 0) { local_rsi = (uint32_t)((uint32_t)(0xC0000295ULL)); }
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, v_stack_m2E8, (uint32_t)(v_stack_m318));
    if ((uint32_t)(result) == 0) goto loc_007B3C77;
    if (local_r15 <= ((uint32_t)(0xFFFFFFFFULL))) goto loc_007B3C48;
    goto loc_007B3C6D;
loc_007B3C48:
    if (sign_flag) goto loc_007B3C6A;
    if ((uint8_t)(v_stack_m348) == 0) goto loc_007B3C6A;
    *(uint32_t *)(arg3) = 56;
    *(uint32_t *)(arg3 + 0x2C) = 32;
    *(uint32_t *)(arg3 + 0x30) = (uint32_t)(local_r15);
    goto loc_007B3C6D;
loc_007B3C6A:
loc_007B3C6D:
    goto loc_007B3CA3;
loc_007B3C77:
    if (sign_flag) goto loc_007B3C9B;
    local_rdi = (uint32_t)((uint32_t)(local_r15));
    if ((uint8_t)(v_stack_m348) != 0) {
        local_rdi = 56;
        *(uint32_t *)(arg3) = (uint32_t)(local_rdi);
        *(uint32_t *)(arg3 + 0x2C) = 32;
        Arg1 = v_stack_m344;
        *(uint32_t *)(arg3 + 0x30) = (uint32_t)(Arg1);
    }
loc_007B3CA3:
    *(uint32_t *)(v_stack_m2E0) = (uint32_t)(local_rdi);
    result = v_stack_m2E0;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m2E8, (uint32_t)(v_stack_m318));
    }
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m2E8, (uint32_t)(v_stack_m318));
    return result;
loc_007B3CE4:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, v_stack_m2E8, (uint32_t)(v_stack_m318));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x2C` | `32` | `W` |
| `Arg3` | `+ 0x30` | `32` | `W` |
| `Arg5` | `+ 0x8` | `64` | `R` |
| `Arg6` | `+ 0x0 + rdi*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B36F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
