# BiConvertNtDeviceToBootEnvironment

- RVA: `0x00A41760`–`0x00A41DDF` (길이 `1,663` bytes)
- VA: `0x0000000140A41760`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AEAB0`
- 디코드: `456`개 명령, `1,663/1,663` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00A417FA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A41816` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A4184F` → [BiConvertNtFilePathToBootEnvironment](../82/BiConvertNtFilePathToBootEnvironment_function_00824A64.md) (function, `0x00824A64`)
- `0x00A41875` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A4188E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A418B2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A418EB` → [BiConvertNtFilePathToBootEnvironment](../82/BiConvertNtFilePathToBootEnvironment_function_00824A64.md) (function, `0x00824A64`)
- `0x00A41911` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A41924` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A41936` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A41953` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A41967` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A4197E` → [BiIsVolumePartitionInformationRetained](../AC/BiIsVolumePartitionInformationRetained_function_00AC6CFC.md) (function, `0x00AC6CFC`)
- `0x00A4199A` → [BiCreatePartitionDevice](../82/BiCreatePartitionDevice_function_00824D10.md) (function, `0x00824D10`)
- `0x00A419C6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A419E5` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A41A13` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A41A28` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A41A83` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A41AF5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A41B0E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A41B63` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A41B82` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A41BA8` → [strcpy_s](../../text/50/strcpy_s_function_00505FB0.md) (function, `0x00505FB0`)
- `0x00A41C1E` → [BiGetPartitionVhdFilePath](../A9/BiGetPartitionVhdFilePath_function_00A9E5F4.md) (function, `0x00A9E5F4`)
- `0x00A41C34` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A41C72` → [BiConvertNtDeviceToBootEnvironment](BiConvertNtDeviceToBootEnvironment_function_00A41760.md) (function, `0x00A41760`)
- `0x00A41CC9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A41CF2` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A41D3B` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00A41D8A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A41DBB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [BiConvertNtFilePathToBootEnvironment](../82/BiConvertNtFilePathToBootEnvironment_function_00824A64.md) at `0x00824A91`
- [BiCreatePartitionDevice](../82/BiCreatePartitionDevice_function_00824D10.md) at `0x00824F05`
- [BiConvertElementToRegistryData](BiConvertElementToRegistryData_function_00A400A8.md) at `0x00A40425`
- [BiConvertNtDeviceToBootEnvironment](BiConvertNtDeviceToBootEnvironment_function_00A41760.md) at `0x00A41C72`

### Static image references
- `0x00A41A36` → RVA `0x00041B30` (`.rdata`; read)
- `0x00A41ACB` → RVA `0x00041B50` (`.rdata`; read)
- `0x00A41AD8` → RVA `0x00041B58` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x00A417FA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A41816` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A41875` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A4188E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A418B2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A41911` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A41924` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A41936` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A41953` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A41967` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A419C6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A419E5` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A41A13` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A41A28` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A41A83` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A41AF5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A41B0E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A41B63` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A41B82` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A41BA8` → [strcpy_s](../../text/50/strcpy_s_function_00505FB0.md) (`PAGE` → `.text`)
  - `0x00A41C34` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A41CC9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A41CF2` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A41D3B` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
  - `0x00A41D8A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A41DBB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A41760  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00A41765  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00A4176A  55                              push rbp
00A4176B  56                              push rsi
00A4176C  57                              push rdi
00A4176D  41 54                           push r12
00A4176F  41 55                           push r13
00A41771  41 56                           push r14
00A41773  41 57                           push r15
00A41775  48 8B EC                        mov rbp, rsp
00A41778  48 83 EC 40                     sub rsp, 0x40
00A4177C  8B 01                           mov eax, dword ptr [rcx]
00A4177E  45 33 E4                        xor r12d, r12d
00A41781  44 89 65 40                     mov dword ptr [rbp + 0x40], r12d
00A41785  4D 8B E9                        mov r13, r9
00A41788  4C 89 65 F0                     mov qword ptr [rbp - 0x10], r12
00A4178C  45 8B F0                        mov r14d, r8d
00A4178F  4C 89 65 F8                     mov qword ptr [rbp - 8], r12
00A41793  8B DA                           mov ebx, edx
00A41795  48 8B F1                        mov rsi, rcx
00A41798  41 8B FC                        mov edi, r12d
00A4179B  41 BF 42 43 44 4B               mov r15d, 0x4b444342
00A417A1  83 F8 07                        cmp eax, 7
00A417A4  0F 87 A3 02 00 00               ja 0x140a41a4d
00A417AA  0F 84 4B 02 00 00               je 0x140a419fb
00A417B0  83 E8 01                        sub eax, 1
00A417B3  0F 84 F5 01 00 00               je 0x140a419ae
00A417B9  83 E8 01                        sub eax, 1
00A417BC  0F 84 AF 01 00 00               je 0x140a41971
00A417C2  83 E8 01                        sub eax, 1
00A417C5  0F 84 F1 00 00 00               je 0x140a418bc
00A417CB  83 E8 01                        sub eax, 1
00A417CE  74 50                           je 0x140a41820
00A417D0  83 F8 01                        cmp eax, 1
00A417D3  0F 85 14 04 00 00               jne 0x140a41bed
00A417D9  83 FA 20                        cmp edx, 0x20
00A417DC  0F 82 0B 04 00 00               jb 0x140a41bed
00A417E2  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
00A417E5  3D 00 00 10 00                  cmp eax, 0x100000
00A417EA  0F 87 FD 03 00 00               ja 0x140a41bed
00A417F0  8B D0                           mov edx, eax
00A417F2  45 8B C7                        mov r8d, r15d
00A417F5  B9 02 01 00 00                  mov ecx, 0x102
00A417FA  E8 F1 08 14 00                  call 0x140b820f0
00A417FF  48 8B F8                        mov rdi, rax
00A41802  48 85 C0                        test rax, rax
00A41805  0F 84 C8 01 00 00               je 0x140a419d3
00A4180B  44 8B 46 1C                     mov r8d, dword ptr [rsi + 0x1c]
00A4180F  48 8D 56 14                     lea rdx, [rsi + 0x14]
00A41813  48 8B C8                        mov rcx, rax
00A41816  E8 25 50 C8 FF                  call 0x1406c6840
00A4181B  E9 D3 01 00 00                  jmp 0x140a419f3
00A41820  83 FB 2E                        cmp ebx, 0x2e
00A41823  0F 82 C4 03 00 00               jb 0x140a41bed
00A41829  8B 41 14                        mov eax, dword ptr [rcx + 0x14]
00A4182C  85 C0                           test eax, eax
00A4182E  0F 84 B9 03 00 00               je 0x140a41bed
00A41834  2B D8                           sub ebx, eax
00A41836  4C 89 65 58                     mov qword ptr [rbp + 0x58], r12
00A4183A  4C 8D 41 18                     lea r8, [rcx + 0x18]
00A4183E  45 8B CE                        mov r9d, r14d
00A41841  48 03 C8                        add rcx, rax
00A41844  8B D3                           mov edx, ebx
00A41846  48 8D 45 58                     lea rax, [rbp + 0x58]
00A4184A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A4184F  E8 10 32 DE FF                  call 0x140824a64
00A41854  8B D8                           mov ebx, eax
00A41856  85 C0                           test eax, eax
00A41858  0F 88 4E 05 00 00               js 0x140a41dac
00A4185E  48 8B 5D 58                     mov rbx, qword ptr [rbp + 0x58]
00A41862  45 8B C7                        mov r8d, r15d
00A41865  B9 02 01 00 00                  mov ecx, 0x102
00A4186A  8B 73 04                        mov esi, dword ptr [rbx + 4]
00A4186D  83 C6 28                        add esi, 0x28
00A41870  8B D6                           mov edx, esi
00A41872  44 8B F6                        mov r14d, esi
00A41875  E8 76 08 14 00                  call 0x140b820f0
00A4187A  48 8B F8                        mov rdi, rax
00A4187D  48 85 C0                        test rax, rax
00A41880  0F 84 98 00 00 00               je 0x140a4191e
00A41886  45 8B C6                        mov r8d, r14d
00A41889  33 D2                           xor edx, edx
00A4188B  48 8B C8                        mov rcx, rax
00A4188E  E8 AD 53 C8 FF                  call 0x1406c6c40
00A41893  44 89 27                        mov dword ptr [rdi], r12d
00A41896  48 8D 4F 28                     lea rcx, [rdi + 0x28]
00A4189A  C7 47 04 01 00 00 00            mov dword ptr [rdi + 4], 1
00A418A1  48 8B D3                        mov rdx, rbx
00A418A4  89 77 08                        mov dword ptr [rdi + 8], esi
00A418A7  C7 47 10 03 00 00 00            mov dword ptr [rdi + 0x10], 3
00A418AE  44 8B 43 04                     mov r8d, dword ptr [rbx + 4]
00A418B2  E8 89 4F C8 FF                  call 0x1406c6840
00A418B7  E9 A5 00 00 00                  jmp 0x140a41961
00A418BC  83 FB 2E                        cmp ebx, 0x2e
00A418BF  0F 82 28 03 00 00               jb 0x140a41bed
00A418C5  8B 41 14                        mov eax, dword ptr [rcx + 0x14]
00A418C8  85 C0                           test eax, eax
00A418CA  0F 84 1D 03 00 00               je 0x140a41bed
00A418D0  2B D8                           sub ebx, eax
00A418D2  4C 89 65 58                     mov qword ptr [rbp + 0x58], r12
00A418D6  4C 8D 41 18                     lea r8, [rcx + 0x18]
00A418DA  45 8B CE                        mov r9d, r14d
00A418DD  48 03 C8                        add rcx, rax
00A418E0  8B D3                           mov edx, ebx
00A418E2  48 8D 45 58                     lea rax, [rbp + 0x58]
00A418E6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A418EB  E8 74 31 DE FF                  call 0x140824a64
00A418F0  8B D8                           mov ebx, eax
00A418F2  85 C0                           test eax, eax
00A418F4  0F 88 B2 04 00 00               js 0x140a41dac
00A418FA  48 8B 5D 58                     mov rbx, qword ptr [rbp + 0x58]
00A418FE  45 8B C7                        mov r8d, r15d
00A41901  B9 02 01 00 00                  mov ecx, 0x102
00A41906  8B 73 04                        mov esi, dword ptr [rbx + 4]
00A41909  83 C6 14                        add esi, 0x14
00A4190C  8B D6                           mov edx, esi
00A4190E  44 8B F6                        mov r14d, esi
00A41911  E8 DA 07 14 00                  call 0x140b820f0
00A41916  48 8B F8                        mov rdi, rax
00A41919  48 85 C0                        test rax, rax
00A4191C  75 10                           jne 0x140a4192e
00A4191E  41 8B D7                        mov edx, r15d
00A41921  48 8B CB                        mov rcx, rbx
00A41924  E8 47 0F 14 00                  call 0x140b82870
00A41929  E9 A5 00 00 00                  jmp 0x140a419d3
00A4192E  4D 8B C6                        mov r8, r14
00A41931  33 D2                           xor edx, edx
00A41933  48 8B CF                        mov rcx, rdi
00A41936  E8 05 53 C8 FF                  call 0x1406c6c40
00A4193B  44 89 27                        mov dword ptr [rdi], r12d
00A4193E  48 8D 4F 14                     lea rcx, [rdi + 0x14]
00A41942  89 77 08                        mov dword ptr [rdi + 8], esi
00A41945  48 8B D3                        mov rdx, rbx
00A41948  C7 47 10 05 00 00 00            mov dword ptr [rdi + 0x10], 5
00A4194F  44 8B 43 04                     mov r8d, dword ptr [rbx + 4]
00A41953  E8 E8 4E C8 FF                  call 0x1406c6840
00A41958  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00A4195B  83 E0 20                        and eax, 0x20
00A4195E  89 47 04                        mov dword ptr [rdi + 4], eax
00A41961  41 8B D7                        mov edx, r15d
00A41964  48 8B CB                        mov rcx, rbx
00A41967  E8 04 0F 14 00                  call 0x140b82870
00A4196C  E9 82 00 00 00                  jmp 0x140a419f3
00A41971  83 FB 16                        cmp ebx, 0x16
00A41974  0F 82 73 02 00 00               jb 0x140a41bed
00A4197A  48 83 C1 14                     add rcx, 0x14
00A4197E  E8 79 53 08 00                  call 0x140ac6cfc
00A41983  84 C0                           test al, al
00A41985  0F 84 AE 02 00 00               je 0x140a41c39
00A4198B  4C 8D 4D 40                     lea r9, [rbp + 0x40]
00A4198F  41 8B D6                        mov edx, r14d
00A41992  4C 8D 45 F8                     lea r8, [rbp - 8]
00A41996  48 8D 4E 14                     lea rcx, [rsi + 0x14]
00A4199A  E8 71 33 DE FF                  call 0x140824d10
00A4199F  48 8B 7D F8                     mov rdi, qword ptr [rbp - 8]
00A419A3  8B D8                           mov ebx, eax
00A419A5  85 C0                           test eax, eax
00A419A7  79 4A                           jns 0x140a419f3
00A419A9  E9 FE 03 00 00                  jmp 0x140a41dac
00A419AE  83 FB 14                        cmp ebx, 0x14
00A419B1  0F 82 36 02 00 00               jb 0x140a41bed
00A419B7  BB 48 00 00 00                  mov ebx, 0x48
00A419BC  45 8B C7                        mov r8d, r15d
00A419BF  8B D3                           mov edx, ebx
00A419C1  B9 02 01 00 00                  mov ecx, 0x102
00A419C6  E8 25 07 14 00                  call 0x140b820f0
00A419CB  48 8B F8                        mov rdi, rax
00A419CE  48 85 C0                        test rax, rax
00A419D1  75 0A                           jne 0x140a419dd
00A419D3  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A419D8  E9 CF 03 00 00                  jmp 0x140a41dac
00A419DD  4C 8B C3                        mov r8, rbx
00A419E0  33 D2                           xor edx, edx
00A419E2  48 8B CF                        mov rcx, rdi
00A419E5  E8 56 52 C8 FF                  call 0x1406c6c40
00A419EA  C7 07 05 00 00 00               mov dword ptr [rdi], 5
00A419F0  89 5F 08                        mov dword ptr [rdi + 8], ebx
00A419F3  41 8B DC                        mov ebx, r12d
00A419F6  E9 B1 03 00 00                  jmp 0x140a41dac
00A419FB  83 FB 24                        cmp ebx, 0x24
00A419FE  0F 82 E9 01 00 00               jb 0x140a41bed
00A41A04  BB 48 00 00 00                  mov ebx, 0x48
00A41A09  45 8B C7                        mov r8d, r15d
00A41A0C  8B D3                           mov edx, ebx
00A41A0E  B9 02 01 00 00                  mov ecx, 0x102
00A41A13  E8 D8 06 14 00                  call 0x140b820f0
00A41A18  48 8B F8                        mov rdi, rax
00A41A1B  48 85 C0                        test rax, rax
00A41A1E  74 B3                           je 0x140a419d3
00A41A20  44 8B C3                        mov r8d, ebx
00A41A23  33 D2                           xor edx, edx
00A41A25  48 8B C8                        mov rcx, rax
00A41A28  E8 13 52 C8 FF                  call 0x1406c6c40
00A41A2D  C7 07 07 00 00 00               mov dword ptr [rdi], 7
00A41A33  89 5F 08                        mov dword ptr [rdi + 8], ebx
00A41A36  0F 10 05 F3 00 60 FF            movups xmm0, xmmword ptr [rip - 0x9fff0d]
00A41A3D  F3 0F 7F 47 10                  movdqu xmmword ptr [rdi + 0x10], xmm0
00A41A42  0F 10 46 14                     movups xmm0, xmmword ptr [rsi + 0x14]
00A41A46  F3 0F 7F 47 20                  movdqu xmmword ptr [rdi + 0x20], xmm0
00A41A4B  EB A6                           jmp 0x140a419f3
00A41A4D  83 E8 08                        sub eax, 8
00A41A50  0F 84 5F 01 00 00               je 0x140a41bb5
00A41A56  83 E8 01                        sub eax, 1
00A41A59  0F 84 D8 00 00 00               je 0x140a41b37
00A41A5F  83 E8 01                        sub eax, 1
00A41A62  74 5A                           je 0x140a41abe
00A41A64  83 F8 01                        cmp eax, 1
00A41A67  0F 85 80 01 00 00               jne 0x140a41bed
00A41A6D  83 FB 28                        cmp ebx, 0x28
00A41A70  0F 82 77 01 00 00               jb 0x140a41bed
00A41A76  8D 58 2F                        lea ebx, [rax + 0x2f]
00A41A79  45 8B C7                        mov r8d, r15d
00A41A7C  8B D3                           mov edx, ebx
00A41A7E  B9 02 01 00 00                  mov ecx, 0x102
00A41A83  E8 68 06 14 00                  call 0x140b820f0
00A41A88  48 8B F8                        mov rdi, rax
00A41A8B  48 85 C0                        test rax, rax
00A41A8E  0F 84 3F FF FF FF               je 0x140a419d3
00A41A94  0F 57 C0                        xorps xmm0, xmm0
00A41A97  0F 11 00                        movups xmmword ptr [rax], xmm0
00A41A9A  0F 11 40 10                     movups xmmword ptr [rax + 0x10], xmm0
00A41A9E  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00A41AA2  C7 00 0B 00 00 00               mov dword ptr [rax], 0xb
00A41AA8  89 58 08                        mov dword ptr [rax + 8], ebx
00A41AAB  C7 40 04 01 00 00 00            mov dword ptr [rax + 4], 1
00A41AB2  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
00A41AB5  89 47 10                        mov dword ptr [rdi + 0x10], eax
00A41AB8  0F 10 46 18                     movups xmm0, xmmword ptr [rsi + 0x18]
00A41ABC  EB 88                           jmp 0x140a41a46
00A41ABE  83 FB 28                        cmp ebx, 0x28
00A41AC1  0F 82 26 01 00 00               jb 0x140a41bed
00A41AC7  48 8B 41 14                     mov rax, qword ptr [rcx + 0x14]
00A41ACB  48 2B 05 7E 00 60 FF            sub rax, qword ptr [rip - 0x9fff82]
00A41AD2  75 0B                           jne 0x140a41adf
00A41AD4  48 8B 41 1C                     mov rax, qword ptr [rcx + 0x1c]
00A41AD8  48 2B 05 79 00 60 FF            sub rax, qword ptr [rip - 0x9fff87]
00A41ADF  48 85 C0                        test rax, rax
00A41AE2  0F 85 05 01 00 00               jne 0x140a41bed
00A41AE8  8D 58 48                        lea ebx, [rax + 0x48]
00A41AEB  45 8B C7                        mov r8d, r15d
00A41AEE  8B D3                           mov edx, ebx
00A41AF0  B9 02 01 00 00                  mov ecx, 0x102
00A41AF5  E8 F6 05 14 00                  call 0x140b820f0
00A41AFA  48 8B F8                        mov rdi, rax
00A41AFD  48 85 C0                        test rax, rax
00A41B00  0F 84 CD FE FF FF               je 0x140a419d3
00A41B06  44 8B C3                        mov r8d, ebx
00A41B09  33 D2                           xor edx, edx
00A41B0B  48 8B C8                        mov rcx, rax
00A41B0E  E8 2D 51 C8 FF                  call 0x1406c6c40
00A41B13  C7 07 0A 00 00 00               mov dword ptr [rdi], 0xa
00A41B19  89 5F 08                        mov dword ptr [rdi + 8], ebx
00A41B1C  C7 47 04 01 00 00 00            mov dword ptr [rdi + 4], 1
00A41B23  0F 10 46 14                     movups xmm0, xmmword ptr [rsi + 0x14]
00A41B27  F3 0F 7F 47 10                  movdqu xmmword ptr [rdi + 0x10], xmm0
00A41B2C  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
00A41B2F  89 47 20                        mov dword ptr [rdi + 0x20], eax
00A41B32  E9 BC FE FF FF                  jmp 0x140a419f3
00A41B37  83 FB 15                        cmp ebx, 0x15
00A41B3A  0F 82 AD 00 00 00               jb 0x140a41bed
00A41B40  48 83 CB FF                     or rbx, 0xffffffffffffffff
00A41B44  48 FF C3                        inc rbx
00A41B47  44 38 64 19 14                  cmp byte ptr [rcx + rbx + 0x14], r12b
00A41B4C  75 F6                           jne 0x140a41b44
00A41B4E  44 8D 73 15                     lea r14d, [rbx + 0x15]
00A41B52  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00A41B58  41 8B D6                        mov edx, r14d
00A41B5B  B9 02 01 00 00                  mov ecx, 0x102
00A41B60  45 8B FE                        mov r15d, r14d
00A41B63  E8 88 05 14 00                  call 0x140b820f0
00A41B68  48 8B F8                        mov rdi, rax
00A41B6B  48 85 C0                        test rax, rax
00A41B6E  75 0A                           jne 0x140a41b7a
00A41B70  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A41B75  E9 65 01 00 00                  jmp 0x140a41cdf
00A41B7A  4D 8B C7                        mov r8, r15
00A41B7D  33 D2                           xor edx, edx
00A41B7F  48 8B CF                        mov rcx, rdi
00A41B82  E8 B9 50 C8 FF                  call 0x1406c6c40
00A41B87  C7 07 09 00 00 00               mov dword ptr [rdi], 9
00A41B8D  8D 43 01                        lea eax, [rbx + 1]
00A41B90  C7 47 04 20 00 00 00            mov dword ptr [rdi + 4], 0x20
00A41B97  48 8D 4F 14                     lea rcx, [rdi + 0x14]
00A41B9B  44 89 77 08                     mov dword ptr [rdi + 8], r14d
00A41B9F  4C 8D 46 14                     lea r8, [rsi + 0x14]
00A41BA3  8B D0                           mov edx, eax
00A41BA5  89 47 10                        mov dword ptr [rdi + 0x10], eax
00A41BA8  E8 03 44 AC FF                  call 0x140505fb0
00A41BAD  41 8B DC                        mov ebx, r12d
00A41BB0  E9 2A 01 00 00                  jmp 0x140a41cdf
00A41BB5  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
00A41BB8  83 FB 22                        cmp ebx, 0x22
00A41BBB  0F 82 E6 01 00 00               jb 0x140a41da7
00A41BC1  3B D8                           cmp ebx, eax
00A41BC3  0F 86 DE 01 00 00               jbe 0x140a41da7
00A41BC9  33 C9                           xor ecx, ecx
00A41BCB  44 8B F9                        mov r15d, ecx
00A41BCE  44 8D 61 1E                     lea r12d, [rcx + 0x1e]
00A41BD2  85 C0                           test eax, eax
00A41BD4  0F 84 C3 00 00 00               je 0x140a41c9d
00A41BDA  2B D8                           sub ebx, eax
00A41BDC  4C 8D 34 06                     lea r14, [rsi + rax]
00A41BE0  41 8B 06                        mov eax, dword ptr [r14]
00A41BE3  83 F8 03                        cmp eax, 3
00A41BE6  75 0F                           jne 0x140a41bf7
00A41BE8  83 FB 2E                        cmp ebx, 0x2e
00A41BEB  73 14                           jae 0x140a41c01
00A41BED  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A41BF2  E9 C9 01 00 00                  jmp 0x140a41dc0
00A41BF7  83 F8 0C                        cmp eax, 0xc
00A41BFA  75 F1                           jne 0x140a41bed
00A41BFC  83 FB 18                        cmp ebx, 0x18
00A41BFF  72 EC                           jb 0x140a41bed
00A41C01  41 8B 56 14                     mov edx, dword ptr [r14 + 0x14]
00A41C05  8B C3                           mov eax, ebx
00A41C07  2B C2                           sub eax, edx
00A41C09  42 8B 0C 32                     mov ecx, dword ptr [rdx + r14]
00A41C0D  83 F9 02                        cmp ecx, 2
00A41C10  75 31                           jne 0x140a41c43
00A41C12  83 F8 16                        cmp eax, 0x16
00A41C15  72 D6                           jb 0x140a41bed
00A41C17  49 8D 4E 14                     lea rcx, [r14 + 0x14]
00A41C1B  48 03 CA                        add rcx, rdx
00A41C1E  E8 D1 C9 05 00                  call 0x140a9e5f4
00A41C23  48 85 C0                        test rax, rax
00A41C26  74 3E                           je 0x140a41c66
00A41C28  41 BF 42 43 44 4B               mov r15d, 0x4b444342
00A41C2E  48 8B C8                        mov rcx, rax
00A41C31  41 8B D7                        mov edx, r15d
00A41C34  E8 37 0C 14 00                  call 0x140b82870
00A41C39  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00A41C3E  E9 69 01 00 00                  jmp 0x140a41dac
00A41C43  83 F9 06                        cmp ecx, 6
00A41C46  74 1E                           je 0x140a41c66
00A41C48  83 F9 08                        cmp ecx, 8
00A41C4B  75 05                           jne 0x140a41c52
00A41C4D  83 F8 22                        cmp eax, 0x22
00A41C50  73 14                           jae 0x140a41c66
00A41C52  83 F9 01                        cmp ecx, 1
00A41C55  75 05                           jne 0x140a41c5c
00A41C57  83 F8 14                        cmp eax, 0x14
00A41C5A  73 0A                           jae 0x140a41c66
00A41C5C  83 F9 09                        cmp ecx, 9
00A41C5F  75 8C                           jne 0x140a41bed
00A41C61  83 F8 15                        cmp eax, 0x15
00A41C64  72 87                           jb 0x140a41bed
00A41C66  4C 8D 4D F0                     lea r9, [rbp - 0x10]
00A41C6A  45 33 C0                        xor r8d, r8d
00A41C6D  8B D3                           mov edx, ebx
00A41C6F  49 8B CE                        mov rcx, r14
00A41C72  E8 E9 FA FF FF                  call 0x140a41760
00A41C77  8B D8                           mov ebx, eax
00A41C79  85 C0                           test eax, eax
00A41C7B  78 62                           js 0x140a41cdf
00A41C7D  41 8B 06                        mov eax, dword ptr [r14]
00A41C80  83 E8 0C                        sub eax, 0xc
00A41C83  F7 D8                           neg eax
00A41C85  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00A41C89  45 1B FF                        sbb r15d, r15d
00A41C8C  41 83 E7 28                     and r15d, 0x28
00A41C90  44 8B 60 08                     mov r12d, dword ptr [rax + 8]
00A41C94  41 83 C4 1E                     add r12d, 0x1e
00A41C98  45 03 E7                        add r12d, r15d
00A41C9B  33 C9                           xor ecx, ecx
00A41C9D  48 83 CB FF                     or rbx, 0xffffffffffffffff
00A41CA1  83 7E 14 01                     cmp dword ptr [rsi + 0x14], 1
00A41CA5  75 11                           jne 0x140a41cb8
00A41CA7  48 8B C3                        mov rax, rbx
00A41CAA  48 FF C0                        inc rax
00A41CAD  66 39 4C 46 20                  cmp word ptr [rsi + rax*2 + 0x20], cx
00A41CB2  75 F6                           jne 0x140a41caa
00A41CB4  45 8D 24 44                     lea r12d, [r12 + rax*2]
00A41CB8  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00A41CBE  41 8B D4                        mov edx, r12d
00A41CC1  B9 02 01 00 00                  mov ecx, 0x102
00A41CC6  45 8B EC                        mov r13d, r12d
00A41CC9  E8 22 04 14 00                  call 0x140b820f0
00A41CCE  48 8B F8                        mov rdi, rax
00A41CD1  48 85 C0                        test rax, rax
00A41CD4  75 14                           jne 0x140a41cea
00A41CD6  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A41CDB  4C 8B 6D 58                     mov r13, qword ptr [rbp + 0x58]
00A41CDF  41 BF 42 43 44 4B               mov r15d, 0x4b444342
00A41CE5  E9 C2 00 00 00                  jmp 0x140a41dac
00A41CEA  4D 8B C5                        mov r8, r13
00A41CED  33 D2                           xor edx, edx
00A41CEF  48 8B CF                        mov rcx, rdi
00A41CF2  E8 49 4F C8 FF                  call 0x1406c6c40
00A41CF7  C7 07 08 00 00 00               mov dword ptr [rdi], 8
00A41CFD  44 89 67 08                     mov dword ptr [rdi + 8], r12d
00A41D01  45 33 E4                        xor r12d, r12d
00A41D04  44 39 66 14                     cmp dword ptr [rsi + 0x14], r12d
00A41D08  75 11                           jne 0x140a41d1b
00A41D0A  44 89 67 10                     mov dword ptr [rdi + 0x10], r12d
00A41D0E  41 8D 5C 24 1E                  lea ebx, [r12 + 0x1e]
00A41D13  8B 46 1C                        mov eax, dword ptr [rsi + 0x1c]
00A41D16  89 47 14                        mov dword ptr [rdi + 0x14], eax
00A41D19  EB 37                           jmp 0x140a41d52
00A41D1B  C7 47 10 01 00 00 00            mov dword ptr [rdi + 0x10], 1
00A41D22  48 8B D3                        mov rdx, rbx
00A41D25  48 FF C2                        inc rdx
00A41D28  66 44 39 64 56 20               cmp word ptr [rsi + rdx*2 + 0x20], r12w
00A41D2E  75 F5                           jne 0x140a41d25
00A41D30  48 FF C2                        inc rdx
00A41D33  48 8D 4F 1C                     lea rcx, [rdi + 0x1c]
00A41D37  4C 8D 46 20                     lea r8, [rsi + 0x20]
00A41D3B  E8 70 47 AC FF                  call 0x1405064b0
00A41D40  48 FF C3                        inc rbx
00A41D43  66 44 39 64 5E 20               cmp word ptr [rsi + rbx*2 + 0x20], r12w
00A41D49  75 F5                           jne 0x140a41d40
00A41D4B  8D 1C 5D 1E 00 00 00            lea ebx, [rbx*2 + 0x1e]
00A41D52  4C 39 65 F0                     cmp qword ptr [rbp - 0x10], r12
00A41D56  74 47                           je 0x140a41d9f
00A41D58  8B D3                           mov edx, ebx
00A41D5A  48 03 D7                        add rdx, rdi
00A41D5D  45 85 FF                        test r15d, r15d
00A41D60  74 17                           je 0x140a41d79
00A41D62  44 89 22                        mov dword ptr [rdx], r12d
00A41D65  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00A41D69  8B 40 08                        mov eax, dword ptr [rax + 8]
00A41D6C  41 03 C7                        add eax, r15d
00A41D6F  C7 42 10 06 00 00 00            mov dword ptr [rdx + 0x10], 6
00A41D76  89 42 08                        mov dword ptr [rdx + 8], eax
00A41D79  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00A41D7D  41 8B CF                        mov ecx, r15d
00A41D80  48 03 CA                        add rcx, rdx
00A41D83  48 8B D0                        mov rdx, rax
00A41D86  44 8B 40 08                     mov r8d, dword ptr [rax + 8]
00A41D8A  E8 B1 4A C8 FF                  call 0x1406c6840
00A41D8F  89 5F 18                        mov dword ptr [rdi + 0x18], ebx
00A41D92  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00A41D96  8B 48 04                        mov ecx, dword ptr [rax + 4]
00A41D99  83 E1 20                        and ecx, 0x20
00A41D9C  09 4F 04                        or dword ptr [rdi + 4], ecx
00A41D9F  41 8B DC                        mov ebx, r12d
00A41DA2  E9 34 FF FF FF                  jmp 0x140a41cdb
00A41DA7  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A41DAC  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00A41DB0  48 85 C0                        test rax, rax
00A41DB3  74 0B                           je 0x140a41dc0
00A41DB5  41 8B D7                        mov edx, r15d
00A41DB8  48 8B C8                        mov rcx, rax
00A41DBB  E8 B0 0A 14 00                  call 0x140b82870
00A41DC0  8B C3                           mov eax, ebx
00A41DC2  49 89 7D 00                     mov qword ptr [r13], rdi
00A41DC6  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00A41DCE  48 83 C4 40                     add rsp, 0x40
00A41DD2  41 5F                           pop r15
00A41DD4  41 5E                           pop r14
00A41DD6  41 5D                           pop r13
00A41DD8  41 5C                           pop r12
00A41DDA  5F                              pop rdi
00A41DDB  5E                              pop rsi
00A41DDC  5D                              pop rbp
00A41DDD  C3                              ret
00A41DDE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BiConvertNtDeviceToBootEnvironment(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (64);
    v_r12 = 0;
    v_stack_p8 = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) > 7) goto loc_00A41A4D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) == 7) goto loc_00A419FB;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) - (1));
    if (condition_is_equal) goto loc_00A419AE;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A41971;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A418BC;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A41820;
    if (((unsigned int)(result)) != 1) goto loc_00A41BED;
    if (a2 < 32) goto loc_00A41BED;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)))) > 0x100000ULL) goto loc_00A41BED;
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)))), (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), a4);
    if (result == 0) goto loc_00A419D3;
    result = memcpy(result, a1 + 20, (unsigned int)(*(unsigned int *)(a1 + 28)), a4);
    goto loc_00A419F3;
loc_00A41820:
    if (((unsigned int)((unsigned int)(a2))) < 46) goto loc_00A41BED;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 20))) == 0) goto loc_00A41BED;
    v_rbx = (unsigned int)(((unsigned int)(a2)) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + 20)))));
    v_stack_p20 = 0;
    a1 = (result) + ((unsigned int)(*(unsigned int *)(result + 20)));
    v_stack_m58 = v_stack_p20;
    result = BiConvertNtFilePathToBootEnvironment(a1, (unsigned int)((unsigned int)(v_rbx)), result + 24, (unsigned int)((unsigned int)((unsigned int)(a3))));
    if (sign_flag) goto loc_00A41DAC;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 4))) + (40));
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), (unsigned int)((unsigned int)((unsigned int)(a3))));
    if (result == 0) goto loc_00A4191E;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(a3))));
    *(unsigned int *)(result) = 0;
    *(unsigned int *)(result + 4) = 1;
    *(unsigned int *)(result + 8) = (unsigned int)(v_rsi);
    *(unsigned int *)(result + 16) = 3;
    result = memcpy(result + 40, v_stack_p20, (unsigned int)(*(unsigned int *)(v_stack_p20 + 4)), (unsigned int)((unsigned int)((unsigned int)(a3))));
    goto loc_00A41961;
loc_00A418BC:
    if (((unsigned int)(v_stack_p20)) < 46) goto loc_00A41BED;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 40 + 20))) == 0) goto loc_00A41BED;
    v_rbx = (unsigned int)((v_stack_p20) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + 40 + 20)))));
    v_stack_p20 = 0;
    a1 = (result + 40) + ((unsigned int)(*(unsigned int *)(result + 40 + 20)));
    v_stack_m58 = v_stack_p20;
    result = BiConvertNtFilePathToBootEnvironment(a1, (unsigned int)((unsigned int)(v_rbx)), result + 40 + 24, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    if (sign_flag) goto loc_00A41DAC;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 4))) + (20));
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    if (result != 0) goto loc_00A4192E;
loc_00A4191E:
    result = ExFreePoolWithTag(v_stack_p20, (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    goto loc_00A419D3;
loc_00A4192E:
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    *(unsigned int *)(result) = 0;
    *(unsigned int *)(result + 8) = (unsigned int)(v_rsi);
    *(unsigned int *)(result + 16) = 5;
    result = memcpy(result + 20, v_stack_p20, (unsigned int)(*(unsigned int *)(v_stack_p20 + 4)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 16))) & (32));
    *(unsigned int *)(result + 4) = (unsigned int)(result);
loc_00A41961:
    result = ExFreePoolWithTag(v_stack_p20, (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), (unsigned int)(*(unsigned int *)(v_stack_p20 + 4)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    goto loc_00A419F3;
loc_00A41971:
    if (((unsigned int)(v_stack_p20)) < 22) goto loc_00A41BED;
    a1 = (v_stack_p20) + (20);
    result = BiIsVolumePartitionInformationRetained(a1, (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), (unsigned int)(*(unsigned int *)(v_stack_p20 + 4)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    if ((unsigned __int8)(result) == 0) goto loc_00A41C39;
    result = BiCreatePartitionDevice(v_rsi + 20, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))), v_stack_m40, v_stack_p8);
    if (!sign_flag) goto loc_00A419F3;
    goto loc_00A41DAC;
loc_00A419AE:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) < 20) goto loc_00A41BED;
    result = ExAllocatePool2(258, 72, (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), v_stack_p8);
    if (result != 0) goto loc_00A419DD;
loc_00A419D3:
    goto loc_00A41DAC;
loc_00A419DD:
    a2 = 0;
    result = memset(result, a2, (unsigned int)(0xC000009AULL), v_stack_p8);
    *(unsigned int *)(result) = 5;
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(0xC000009AULL));
loc_00A419F3:
    goto loc_00A41DAC;
loc_00A419FB:
    if (0 < 36) goto loc_00A41BED;
    result = ExAllocatePool2(258, 72, (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), v_stack_p8);
    if (result == 0) goto loc_00A419D3;
    a2 = 0;
    result = memset(result, a2, 72, v_stack_p8);
    *(unsigned int *)(result) = 7;
    *(unsigned int *)(result + 8) = 72;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
loc_00A41A46:
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    goto loc_00A419F3;
loc_00A41A4D:
    result = (unsigned int)((result) - (8));
    if (condition_is_equal) goto loc_00A41BB5;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A41B37;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A41ABE;
    if (((unsigned int)(result)) != 1) goto loc_00A41BED;
    if (72 < 40) goto loc_00A41BED;
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(result + 47)), (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), v_stack_p8);
    if (result == 0) goto loc_00A419D3;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned int *)(result) = 11;
    *(unsigned int *)(result + 8) = (unsigned int)(result + 47);
    *(unsigned int *)(result + 4) = 1;
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 20)));
    goto loc_00A41A46;
loc_00A41ABE:
    if (((unsigned int)(result + 47)) < 40) goto loc_00A41BED;
    result = (*(unsigned __int64 *)(258 + 20)) - (*(unsigned __int64 *)(v_rip - 10485634));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(258 + 28);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10485639));
    }
    if (result != 0) goto loc_00A41BED;
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(result + 72)), (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), v_stack_p8);
    if (result == 0) goto loc_00A419D3;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)(result + 72)), v_stack_p8);
    *(unsigned int *)(result) = 10;
    *(unsigned int *)(result + 8) = (unsigned int)(result + 72);
    *(unsigned int *)(result + 4) = 1;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 36)));
    goto loc_00A419F3;
loc_00A41B37:
    if (((unsigned int)(result + 72)) < 21) goto loc_00A41BED;
    v_rbx = (result + 72) | (-1);
loc_00A41B44:
    v_rbx = (v_rbx) + 1;
    if ((*(unsigned __int8 *)(result + v_rbx * 1 + 20)) != 0) goto loc_00A41B44;
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(v_rbx + 21)), (unsigned int)(0x4B444342ULL), v_stack_p8);
    if (result != 0) goto loc_00A41B7A;
    goto loc_00A41CDF;
loc_00A41B7A:
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)(v_rbx + 21)), v_stack_p8);
    *(unsigned int *)(result) = 9;
    *(unsigned int *)(result + 4) = 32;
    *(unsigned int *)(result + 8) = (unsigned int)(v_rbx + 21);
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(0xC000009AULL) + 1);
    result = strcpy_s(result + 20, (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL) + 1)), v_rsi + 20, v_stack_p8);
    goto loc_00A41CDF;
loc_00A41BB5:
    if (0 < 34) goto loc_00A41DA7;
    if (0 <= ((unsigned int)((unsigned int)(*(unsigned int *)(result + 20 + 24))))) goto loc_00A41DA7;
    a1 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 20 + 24))) == 0) goto loc_00A41C9D;
    v_rbx = (unsigned int)((0) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + 20 + 24)))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + (unsigned int)(*(unsigned int *)(result + 20 + 24)) * 1)))) != 3) goto loc_00A41BF7;
    if (((unsigned int)(v_rbx)) >= 46) goto loc_00A41C01;
loc_00A41BED:
    goto loc_00A41DC0;
loc_00A41BF7:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + (unsigned int)(*(unsigned int *)(result + 20 + 24)) * 1)))) != 12) goto loc_00A41BED;
    if (((unsigned int)((unsigned int)(0xC000000DULL))) < 24) goto loc_00A41BED;
loc_00A41C01:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + (unsigned int)(*(unsigned int *)(result + 20 + 24)) * 1 + 20)))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsi + (unsigned int)(*(unsigned int *)(result + 20 + 24)) * 1 + 20)) + v_rsi + (unsigned int)(*(unsigned int *)(result + 20 + 24)) * 1 * 1)))) != 2) goto loc_00A41C43;
    if (((unsigned int)(result)) < 22) goto loc_00A41BED;
    a1 = (v_rsi + (unsigned int)(*(unsigned int *)(result + 20 + 24)) * 1 + 20) + ((unsigned int)(*(unsigned int *)(v_rsi + (unsigned int)(*(unsigned int *)(result + 20 + 24)) * 1 + 20)));
    result = BiGetPartitionVhdFilePath(a1, (unsigned int)(*(unsigned int *)(v_rsi + (unsigned int)(*(unsigned int *)(result + 20 + 24)) * 1 + 20)), v_rsi + 20, v_stack_p8);
    if (result == 0) goto loc_00A41C66;
    result = ExFreePoolWithTag(result, (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), v_rsi + 20, v_stack_p8);
loc_00A41C39:
    goto loc_00A41DAC;
loc_00A41C43:
    if (((unsigned int)(result)) == 6) goto loc_00A41C66;
    if (((unsigned int)(result)) != 8) goto loc_00A41C52;
    if (((unsigned int)(result)) >= 34) goto loc_00A41C66;
loc_00A41C52:
    if (((unsigned int)(result)) != 1) goto loc_00A41C5C;
    if (((unsigned int)(result)) >= 20) goto loc_00A41C66;
loc_00A41C5C:
    if (((unsigned int)(result)) != 9) goto loc_00A41BED;
    if (((unsigned int)(result)) < 21) goto loc_00A41BED;
loc_00A41C66:
    a3 = 0;
    result = BiConvertNtDeviceToBootEnvironment(v_rsi + (unsigned int)(*(unsigned int *)(result + 20 + 24)) * 1, (unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL))), a3, v_stack_m48);
    if (sign_flag) goto loc_00A41CDF;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + (unsigned int)(*(unsigned int *)(result + 20 + 24)) * 1))) - (12));
    result = (unsigned int)(-(result));
    v_r15 = (unsigned int)(((unsigned int)(0x4B444342ULL)) & (40));
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m48 + 8))) + (30));
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(v_r15)));
    a1 = 0;
loc_00A41C9D:
    v_rbx = ((unsigned int)((unsigned int)(result))) | (-1);
    if ((*(unsigned int *)(v_rsi + 20)) != 1) goto loc_00A41CB8;
loc_00A41CAA:
    result = (v_rbx) + 1;
    if ((*(unsigned __int16 *)(v_rsi + result * 2 + 32)) != 0) goto loc_00A41CAA;
loc_00A41CB8:
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(v_r12 + result * 2)), (unsigned int)(0x4B444342ULL), v_stack_m48);
    if (result != 0) goto loc_00A41CEA;
loc_00A41CDB:
loc_00A41CDF:
    goto loc_00A41DAC;
loc_00A41CEA:
    a2 = 0;
    result = memset(result, a2, v_stack_p20, v_stack_m48);
    *(unsigned int *)(result) = 8;
    *(unsigned int *)(result + 8) = (unsigned int)(v_r12 + result * 2);
    v_r12 = 0;
    if ((*(unsigned int *)(v_rsi + 20)) != 0) goto loc_00A41D1B;
    *(unsigned int *)(result + 16) = 0;
    *(unsigned int *)(result + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 28)));
    goto loc_00A41D52;
loc_00A41D1B:
    *(unsigned int *)(result + 16) = 1;
loc_00A41D25:
    a2 = (v_r12 + 30) + 1;
    if ((*(unsigned __int16 *)(v_rsi + a2 * 2 + 32)) != 0) goto loc_00A41D25;
    a2 = (a2) + 1;
    result = wcscpy_s(result + 28, a2, v_rsi + 32, v_stack_m48);
loc_00A41D40:
    v_rbx = (v_r12 + 30) + 1;
    if ((*(unsigned __int16 *)(v_rsi + v_rbx * 2 + 32)) != 0) goto loc_00A41D40;
loc_00A41D52:
    if (v_stack_m48 == 0) goto loc_00A41D9F;
    a2 = ((unsigned int)((unsigned int)(v_rbx * 2 + 30))) + (result);
    if ((unsigned int)((unsigned int)(0x4B444342ULL)) != 0) {
        *(unsigned int *)(a2) = 0;
        result = v_stack_m48;
        result = *(unsigned int *)(result + 8);
        result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x4B444342ULL))));
        *(unsigned int *)(a2 + 16) = 6;
        *(unsigned int *)(a2 + 8) = (unsigned int)(result);
    }
    a1 = ((unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL)))) + (a2);
    result = memcpy(a1, v_stack_m48, (unsigned int)(*(unsigned int *)(v_stack_m48 + 8)), v_stack_m48);
    *(unsigned int *)(result + 24) = (unsigned int)(v_rbx * 2 + 30);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m48 + 4))) & (32));
loc_00A41D9F:
    goto loc_00A41CDB;
loc_00A41DA7:
loc_00A41DAC:
    result = v_stack_m48;
    if (v_stack_m48 != 0) {
        a2 = (unsigned int)((unsigned int)(0x4B444342ULL));
        a1 = v_stack_m48;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(*(unsigned int *)(v_stack_m48 + 8)), v_stack_m48);
    }
    *(unsigned __int64 *)(v_stack_p20) = result;
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
}
```

## 5. (Beta) C Style

```c
int64_t BiConvertNtDeviceToBootEnvironment(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (64);
    local_r12 = 0;
    v_stack_p8 = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) > 7) goto loc_00A41A4D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) == 7) goto loc_00A419FB;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) - (1));
    if (condition_is_equal) goto loc_00A419AE;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A41971;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A418BC;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A41820;
    if (((uint32_t)(result)) != 1) goto loc_00A41BED;
    if (Arg2 < 32) goto loc_00A41BED;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))) > 0x100000ULL) goto loc_00A41BED;
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))), (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), Arg4);
    if (result == 0) goto loc_00A419D3;
    result = memcpy(result, Arg1 + 20, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), Arg4);
    goto loc_00A419F3;
loc_00A41820:
    if (((uint32_t)((uint32_t)(Arg2))) < 46) goto loc_00A41BED;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x14))) == 0) goto loc_00A41BED;
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x14)))));
    v_stack_p20 = 0;
    Arg1 = (result) + ((uint32_t)(*(uint32_t *)(result + 0x14)));
    v_stack_m58 = v_stack_p20;
    result = BiConvertNtFilePathToBootEnvironment(Arg1, (uint32_t)((uint32_t)(local_rbx)), result + 24, (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    if (sign_flag) goto loc_00A41DAC;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x4))) + (40));
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    if (result == 0) goto loc_00A4191E;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    *(uint32_t *)(result) = 0;
    *(uint32_t *)(result + 0x4) = 1;
    *(uint32_t *)(result + 0x8) = (uint32_t)(local_rsi);
    *(uint32_t *)(result + 0x10) = 3;
    result = memcpy(result + 40, v_stack_p20, (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x4)), (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    goto loc_00A41961;
loc_00A418BC:
    if (((uint32_t)(v_stack_p20)) < 46) goto loc_00A41BED;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28 + 0x14))) == 0) goto loc_00A41BED;
    local_rbx = (uint32_t)((v_stack_p20) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28 + 0x14)))));
    v_stack_p20 = 0;
    Arg1 = (result + 40) + ((uint32_t)(*(uint32_t *)(result + 0x28 + 0x14)));
    v_stack_m58 = v_stack_p20;
    result = BiConvertNtFilePathToBootEnvironment(Arg1, (uint32_t)((uint32_t)(local_rbx)), result + 40 + 24, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    if (sign_flag) goto loc_00A41DAC;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x4))) + (20));
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    if (result != 0) goto loc_00A4192E;
loc_00A4191E:
    result = ExFreePoolWithTag(v_stack_p20, (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    goto loc_00A419D3;
loc_00A4192E:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    *(uint32_t *)(result) = 0;
    *(uint32_t *)(result + 0x8) = (uint32_t)(local_rsi);
    *(uint32_t *)(result + 0x10) = 5;
    result = memcpy(result + 20, v_stack_p20, (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x4)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x10))) & (32));
    *(uint32_t *)(result + 0x4) = (uint32_t)(result);
loc_00A41961:
    result = ExFreePoolWithTag(v_stack_p20, (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x4)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    goto loc_00A419F3;
loc_00A41971:
    if (((uint32_t)(v_stack_p20)) < 22) goto loc_00A41BED;
    Arg1 = (v_stack_p20) + (20);
    result = BiIsVolumePartitionInformationRetained(Arg1, (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x4)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    if ((uint8_t)(result) == 0) goto loc_00A41C39;
    result = BiCreatePartitionDevice(local_rsi + 20, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))), v_stack_m40, v_stack_p8);
    if (!sign_flag) goto loc_00A419F3;
    goto loc_00A41DAC;
loc_00A419AE:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) < 20) goto loc_00A41BED;
    result = ExAllocatePool2(258, 72, (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), v_stack_p8);
    if (result != 0) goto loc_00A419DD;
loc_00A419D3:
    goto loc_00A41DAC;
loc_00A419DD:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(0xC000009AULL), v_stack_p8);
    *(uint32_t *)(result) = 5;
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(0xC000009AULL));
loc_00A419F3:
    goto loc_00A41DAC;
loc_00A419FB:
    if (0 < 36) goto loc_00A41BED;
    result = ExAllocatePool2(258, 72, (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), v_stack_p8);
    if (result == 0) goto loc_00A419D3;
    Arg2 = 0;
    result = memset(result, Arg2, 72, v_stack_p8);
    *(uint32_t *)(result) = 7;
    *(uint32_t *)(result + 0x8) = 72;
    *(uint64_t *)(result + 0x10) = v_xmm0;
loc_00A41A46:
    *(uint64_t *)(result + 0x20) = v_xmm0;
    goto loc_00A419F3;
loc_00A41A4D:
    result = (uint32_t)((result) - (8));
    if (condition_is_equal) goto loc_00A41BB5;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A41B37;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A41ABE;
    if (((uint32_t)(result)) != 1) goto loc_00A41BED;
    if (72 < 40) goto loc_00A41BED;
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(result + 47)), (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), v_stack_p8);
    if (result == 0) goto loc_00A419D3;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint32_t *)(result) = 11;
    *(uint32_t *)(result + 0x8) = (uint32_t)(result + 47);
    *(uint32_t *)(result + 0x4) = 1;
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x14)));
    goto loc_00A41A46;
loc_00A41ABE:
    if (((uint32_t)(result + 47)) < 40) goto loc_00A41BED;
    result = (*(uint64_t *)(258 + 0x14)) - (*(uint64_t *)(v_rip - 0x9FFF82));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(258 + 0x1C);
        result = (result) - (*(uint64_t *)(v_rip - 0x9FFF87));
    }
    if (result != 0) goto loc_00A41BED;
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(result + 72)), (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), v_stack_p8);
    if (result == 0) goto loc_00A419D3;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)(result + 72)), v_stack_p8);
    *(uint32_t *)(result) = 10;
    *(uint32_t *)(result + 0x8) = (uint32_t)(result + 72);
    *(uint32_t *)(result + 0x4) = 1;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x24)));
    goto loc_00A419F3;
loc_00A41B37:
    if (((uint32_t)(result + 72)) < 21) goto loc_00A41BED;
    local_rbx = (result + 72) | (-1);
loc_00A41B44:
    local_rbx = (local_rbx) + 1;
    if ((*(uint8_t *)(result + local_rbx * 1 + 0x14)) != 0) goto loc_00A41B44;
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(local_rbx + 21)), (uint32_t)(0x4B444342ULL), v_stack_p8);
    if (result != 0) goto loc_00A41B7A;
    goto loc_00A41CDF;
loc_00A41B7A:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)(local_rbx + 21)), v_stack_p8);
    *(uint32_t *)(result) = 9;
    *(uint32_t *)(result + 0x4) = 32;
    *(uint32_t *)(result + 0x8) = (uint32_t)(local_rbx + 21);
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(0xC000009AULL) + 1);
    result = strcpy_s(result + 20, (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL) + 1)), local_rsi + 20, v_stack_p8);
    goto loc_00A41CDF;
loc_00A41BB5:
    if (0 < 34) goto loc_00A41DA7;
    if (0 <= ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x14 + 0x18))))) goto loc_00A41DA7;
    Arg1 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x14 + 0x18))) == 0) goto loc_00A41C9D;
    local_rbx = (uint32_t)((0) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x14 + 0x18)))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + (uint32_t)(*(uint32_t *)(result + 0x14 + 0x18)) * 1)))) != 3) goto loc_00A41BF7;
    if (((uint32_t)(local_rbx)) >= 46) goto loc_00A41C01;
loc_00A41BED:
    goto loc_00A41DC0;
loc_00A41BF7:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + (uint32_t)(*(uint32_t *)(result + 0x14 + 0x18)) * 1)))) != 12) goto loc_00A41BED;
    if (((uint32_t)((uint32_t)(0xC000000DULL))) < 24) goto loc_00A41BED;
loc_00A41C01:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + (uint32_t)(*(uint32_t *)(result + 0x14 + 0x18)) * 1 + 0x14)))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsi + (uint32_t)(*(uint32_t *)(result + 0x14 + 0x18)) * 1 + 0x14)) + local_rsi + (uint32_t)(*(uint32_t *)(result + 0x14 + 0x18)) * 1 * 1)))) != 2) goto loc_00A41C43;
    if (((uint32_t)(result)) < 22) goto loc_00A41BED;
    Arg1 = (local_rsi + (uint32_t)(*(uint32_t *)(result + 0x14 + 0x18)) * 1 + 20) + ((uint32_t)(*(uint32_t *)(local_rsi + (uint32_t)(*(uint32_t *)(result + 0x14 + 0x18)) * 1 + 0x14)));
    result = BiGetPartitionVhdFilePath(Arg1, (uint32_t)(*(uint32_t *)(local_rsi + (uint32_t)(*(uint32_t *)(result + 0x14 + 0x18)) * 1 + 0x14)), local_rsi + 20, v_stack_p8);
    if (result == 0) goto loc_00A41C66;
    result = ExFreePoolWithTag(result, (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), local_rsi + 20, v_stack_p8);
loc_00A41C39:
    goto loc_00A41DAC;
loc_00A41C43:
    if (((uint32_t)(result)) == 6) goto loc_00A41C66;
    if (((uint32_t)(result)) != 8) goto loc_00A41C52;
    if (((uint32_t)(result)) >= 34) goto loc_00A41C66;
loc_00A41C52:
    if (((uint32_t)(result)) != 1) goto loc_00A41C5C;
    if (((uint32_t)(result)) >= 20) goto loc_00A41C66;
loc_00A41C5C:
    if (((uint32_t)(result)) != 9) goto loc_00A41BED;
    if (((uint32_t)(result)) < 21) goto loc_00A41BED;
loc_00A41C66:
    Arg3 = 0;
    result = BiConvertNtDeviceToBootEnvironment(local_rsi + (uint32_t)(*(uint32_t *)(result + 0x14 + 0x18)) * 1, (uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL))), Arg3, v_stack_m48);
    if (sign_flag) goto loc_00A41CDF;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + (uint32_t)(*(uint32_t *)(result + 0x14 + 0x18)) * 1))) - (12));
    result = (uint32_t)(-(result));
    local_r15 = (uint32_t)(((uint32_t)(0x4B444342ULL)) & (40));
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x8))) + (30));
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(local_r15)));
    Arg1 = 0;
loc_00A41C9D:
    local_rbx = ((uint32_t)((uint32_t)(result))) | (-1);
    if ((*(uint32_t *)(local_rsi + 0x14)) != 1) goto loc_00A41CB8;
loc_00A41CAA:
    result = (local_rbx) + 1;
    if ((*(uint16_t *)(local_rsi + result * 2 + 0x20)) != 0) goto loc_00A41CAA;
loc_00A41CB8:
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(local_r12 + result * 2)), (uint32_t)(0x4B444342ULL), v_stack_m48);
    if (result != 0) goto loc_00A41CEA;
loc_00A41CDB:
loc_00A41CDF:
    goto loc_00A41DAC;
loc_00A41CEA:
    Arg2 = 0;
    result = memset(result, Arg2, v_stack_p20, v_stack_m48);
    *(uint32_t *)(result) = 8;
    *(uint32_t *)(result + 0x8) = (uint32_t)(local_r12 + result * 2);
    local_r12 = 0;
    if ((*(uint32_t *)(local_rsi + 0x14)) != 0) goto loc_00A41D1B;
    *(uint32_t *)(result + 0x10) = 0;
    *(uint32_t *)(result + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x1C)));
    goto loc_00A41D52;
loc_00A41D1B:
    *(uint32_t *)(result + 0x10) = 1;
loc_00A41D25:
    Arg2 = (local_r12 + 30) + 1;
    if ((*(uint16_t *)(local_rsi + Arg2 * 2 + 0x20)) != 0) goto loc_00A41D25;
    Arg2 = (Arg2) + 1;
    result = wcscpy_s(result + 28, Arg2, local_rsi + 32, v_stack_m48);
loc_00A41D40:
    local_rbx = (local_r12 + 30) + 1;
    if ((*(uint16_t *)(local_rsi + local_rbx * 2 + 0x20)) != 0) goto loc_00A41D40;
loc_00A41D52:
    if (v_stack_m48 == 0) goto loc_00A41D9F;
    Arg2 = ((uint32_t)((uint32_t)(local_rbx * 2 + 30))) + (result);
    if ((uint32_t)((uint32_t)(0x4B444342ULL)) != 0) {
        *(uint32_t *)(Arg2) = 0;
        result = v_stack_m48;
        result = *(uint32_t *)(result + 0x8);
        result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x4B444342ULL))));
        *(uint32_t *)(Arg2 + 0x10) = 6;
        *(uint32_t *)(Arg2 + 0x8) = (uint32_t)(result);
    }
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL)))) + (Arg2);
    result = memcpy(Arg1, v_stack_m48, (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x8)), v_stack_m48);
    *(uint32_t *)(result + 0x18) = (uint32_t)(local_rbx * 2 + 30);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x4))) & (32));
loc_00A41D9F:
    goto loc_00A41CDB;
loc_00A41DA7:
loc_00A41DAC:
    result = v_stack_m48;
    if (v_stack_m48 != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x4B444342ULL));
        Arg1 = v_stack_m48;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x8)), v_stack_m48);
    }
    *(uint64_t *)(v_stack_p20) = result;
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0 + rax*1` | `64` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x14` | `64` | `R` |
| `Arg1` | `+ 0x14` | `128` | `R` |
| `Arg1` | `+ 0x14 + rbx*1` | `8` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `128` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20 + rax*2` | `16` | `R` |
| `Arg1` | `+ 0x20 + rbx*2` | `16` | `R` |
| `Arg1` | `+ 0x20 + rdx*2` | `16` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A41760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
