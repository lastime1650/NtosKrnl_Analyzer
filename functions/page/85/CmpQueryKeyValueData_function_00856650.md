# CmpQueryKeyValueData

- RVA: `0x00856650`–`0x00856BCD` (길이 `1,405` bytes)
- VA: `0x0000000140856650`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A494`
- 디코드: `351`개 명령, `1,405/1,405` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00856766` → [CmpGetValueData](CmpGetValueData_function_00856DB0.md) (function, `0x00856DB0`)
- `0x00856783` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008567F5` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008568FB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00856961` → [CmpGetValueData](CmpGetValueData_function_00856DB0.md) (function, `0x00856DB0`)
- `0x008569C5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00856A5F` → [CmpCopyCompressedName](../84/CmpCopyCompressedName_function_0084E0D0.md) (function, `0x0084E0D0`)
- `0x00856A6D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00856AAB` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00856ABA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00856B55` → [CmpGetValueData](CmpGetValueData_function_00856DB0.md) (function, `0x00856DB0`)
- `0x00856B72` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [sub_008551B7](Unknown_function_008551B7.md) at `0x00855397`
- [CmEnumerateValueFromLayeredKey](../8B/CmEnumerateValueFromLayeredKey_function_008B31FC.md) at `0x008B341A`
- [NtEnumerateValueKey](../8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B401D`
- [sub_00B428B8](../B4/Unknown_function_00B428B8.md) at `0x00B429C0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00856783` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008568FB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008569C5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00856A6D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00856ABA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00856B72` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00856650  48 8B C4                        mov rax, rsp
00856653  89 50 10                        mov dword ptr [rax + 0x10], edx
00856656  48 89 48 08                     mov qword ptr [rax + 8], rcx
0085665A  53                              push rbx
0085665B  56                              push rsi
0085665C  57                              push rdi
0085665D  41 54                           push r12
0085665F  41 55                           push r13
00856661  41 56                           push r14
00856663  41 57                           push r15
00856665  48 83 EC 70                     sub rsp, 0x70
00856669  49 8B D8                        mov rbx, r8
0085666C  44 8B DA                        mov r11d, edx
0085666F  4C 8B D1                        mov r10, rcx
00856672  45 33 E4                        xor r12d, r12d
00856675  41 8B F4                        mov esi, r12d
00856678  4C 89 60 A0                     mov qword ptr [rax - 0x60], r12
0085667C  40 88 70 20                     mov byte ptr [rax + 0x20], sil
00856680  C7 40 A8 FF FF FF FF            mov dword ptr [rax - 0x58], 0xffffffff
00856687  44 89 60 AC                     mov dword ptr [rax - 0x54], r12d
0085668B  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
0085668F  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00856694  48 8B BC 24 D0 00 00 00         mov rdi, qword ptr [rsp + 0xd0]
0085669C  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
008566A1  41 0F B7 48 02                  movzx ecx, word ptr [r8 + 2]
008566A6  0F B7 D1                        movzx edx, cx
008566A9  66 03 D2                        add dx, dx
008566AC  41 F6 40 10 01                  test byte ptr [r8 + 0x10], 1
008566B1  66 0F 44 D1                     cmove dx, cx
008566B5  41 83 F9 02                     cmp r9d, 2
008566B9  0F 85 4F 01 00 00               jne 0x14085680e
008566BF  41 8B 50 04                     mov edx, dword ptr [r8 + 4]
008566C3  81 FA 00 00 00 80               cmp edx, 0x80000000
008566C9  8D 8A 00 00 00 80               lea ecx, [rdx - 0x80000000]
008566CF  73 02                           jae 0x1408566d3
008566D1  8B CA                           mov ecx, edx
008566D3  89 8C 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], ecx
008566DA  44 8D 41 0C                     lea r8d, [rcx + 0xc]
008566DE  45 8B F4                        mov r14d, r12d
008566E1  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
008566E9  44 89 00                        mov dword ptr [rax], r8d
008566EC  44 8B BC 24 D8 00 00 00         mov r15d, dword ptr [rsp + 0xd8]
008566F4  41 83 FF 0C                     cmp r15d, 0xc
008566F8  0F 82 97 00 00 00               jb 0x140856795
008566FE  44 89 27                        mov dword ptr [rdi], r12d
00856701  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
00856704  89 47 04                        mov dword ptr [rdi + 4], eax
00856707  89 4F 08                        mov dword ptr [rdi + 8], ecx
0085670A  41 83 C7 F4                     add r15d, -0xc
0085670E  B8 05 00 00 80                  mov eax, 0x80000005
00856713  44 3B F9                        cmp r15d, ecx
00856716  44 0F 42 F0                     cmovb r14d, eax
0085671A  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
0085671F  44 0F 43 F9                     cmovae r15d, ecx
00856723  85 C9                           test ecx, ecx
00856725  0F 84 84 00 00 00               je 0x1408567af
0085672B  81 FA 00 00 00 80               cmp edx, 0x80000000
00856731  73 57                           jae 0x14085678a
00856733  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00856738  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0085673D  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
00856745  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0085674A  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0085674F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00856754  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
0085675C  4C 8B C3                        mov r8, rbx
0085675F  41 8B D3                        mov edx, r11d
00856762  49 8B 4A 20                     mov rcx, qword ptr [r10 + 0x20]
00856766  E8 45 06 00 00                  call 0x140856db0
0085676B  84 C0                           test al, al
0085676D  74 33                           je 0x1408567a2
0085676F  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00856774  48 85 F6                        test rsi, rsi
00856777  74 36                           je 0x1408567af
00856779  45 8B C7                        mov r8d, r15d
0085677C  48 8D 4F 0C                     lea rcx, [rdi + 0xc]
00856780  48 8B D6                        mov rdx, rsi
00856783  E8 B8 00 E7 FF                  call 0x1406c6840
00856788  EB 25                           jmp 0x1408567af
0085678A  48 8D 73 08                     lea rsi, [rbx + 8]
0085678E  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00856793  EB DF                           jmp 0x140856774
00856795  41 BE 23 00 00 C0               mov r14d, 0xc0000023
0085679B  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
008567A0  EB 0D                           jmp 0x1408567af
008567A2  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
008567A8  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
008567AD  EB C0                           jmp 0x14085676f
008567AF  EB 11                           jmp 0x1408567c2
008567B1  44 8B F0                        mov r14d, eax
008567B4  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008567B8  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
008567BD  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
008567C2  48 85 F6                        test rsi, rsi
008567C5  74 33                           je 0x1408567fa
008567C7  48 8D 43 08                     lea rax, [rbx + 8]
008567CB  48 3B F0                        cmp rsi, rax
008567CE  74 2A                           je 0x1408567fa
008567D0  80 BC 24 C8 00 00 00 01         cmp byte ptr [rsp + 0xc8], 1
008567D8  0F 84 D7 02 00 00               je 0x140856ab5
008567DE  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008567E3  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
008567E8  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008567EF  0F 85 B6 02 00 00               jne 0x140856aab
008567F5  E8 46 F7 FF FF                  call 0x140855f40
008567FA  41 8B C6                        mov eax, r14d
008567FD  48 83 C4 70                     add rsp, 0x70
00856801  41 5F                           pop r15
00856803  41 5E                           pop r14
00856805  41 5D                           pop r13
00856807  41 5C                           pop r12
00856809  5F                              pop rdi
0085680A  5E                              pop rsi
0085680B  5B                              pop rbx
0085680C  C3                              ret
0085680D  CC                              int3
0085680E  45 85 C9                        test r9d, r9d
00856811  0F 84 EF 01 00 00               je 0x140856a06
00856817  41 83 E9 01                     sub r9d, 1
0085681B  74 0A                           je 0x140856827
0085681D  41 83 E9 02                     sub r9d, 2
00856821  0F 85 73 02 00 00               jne 0x140856a9a
00856827  45 8B 48 04                     mov r9d, dword ptr [r8 + 4]
0085682B  44 89 8C 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r9d
00856833  41 81 F9 00 00 00 80            cmp r9d, 0x80000000
0085683A  45 8D B9 00 00 00 80            lea r15d, [r9 - 0x80000000]
00856841  73 03                           jae 0x140856846
00856843  45 8B F9                        mov r15d, r9d
00856846  44 89 BC 24 D0 00 00 00         mov dword ptr [rsp + 0xd0], r15d
0085684E  44 0F B7 C2                     movzx r8d, dx
00856852  41 8D 50 14                     lea edx, [r8 + 0x14]
00856856  41 03 D7                        add edx, r15d
00856859  45 8B EC                        mov r13d, r12d
0085685C  45 85 FF                        test r15d, r15d
0085685F  74 19                           je 0x14085687a
00856861  8B CA                           mov ecx, edx
00856863  41 2B CF                        sub ecx, r15d
00856866  44 8D 69 07                     lea r13d, [rcx + 7]
0085686A  41 83 E5 F8                     and r13d, 0xfffffff8
0085686E  44 3B E9                        cmp r13d, ecx
00856871  76 07                           jbe 0x14085687a
00856873  41 8B C5                        mov eax, r13d
00856876  2B C1                           sub eax, ecx
00856878  03 D0                           add edx, eax
0085687A  45 8B F4                        mov r14d, r12d
0085687D  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00856885  89 10                           mov dword ptr [rax], edx
00856887  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
0085688E  83 F9 14                        cmp ecx, 0x14
00856891  0F 82 49 01 00 00               jb 0x1408569e0
00856897  44 89 27                        mov dword ptr [rdi], r12d
0085689A  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
0085689D  89 47 04                        mov dword ptr [rdi + 4], eax
008568A0  44 89 7F 0C                     mov dword ptr [rdi + 0xc], r15d
008568A4  44 89 47 10                     mov dword ptr [rdi + 0x10], r8d
008568A8  8D 41 EC                        lea eax, [rcx - 0x14]
008568AB  41 3B C0                        cmp eax, r8d
008568AE  73 0E                           jae 0x1408568be
008568B0  44 8B C0                        mov r8d, eax
008568B3  41 BE 05 00 00 80               mov r14d, 0x80000005
008568B9  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
008568BE  F6 43 10 01                     test byte ptr [rbx + 0x10], 1
008568C2  74 2F                           je 0x1408568f3
008568C4  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
008568C8  44 89 64 24 44                  mov dword ptr [rsp + 0x44], r12d
008568CD  41 D1 E8                        shr r8d, 1
008568D0  44 3B C0                        cmp r8d, eax
008568D3  44 0F 43 C0                     cmovae r8d, eax
008568D7  41 8B C4                        mov eax, r12d
008568DA  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008568DE  41 3B C0                        cmp eax, r8d
008568E1  73 35                           jae 0x140856918
008568E3  8B D0                           mov edx, eax
008568E5  0F B6 4C 1A 14                  movzx ecx, byte ptr [rdx + rbx + 0x14]
008568EA  66 89 4C 57 14                  mov word ptr [rdi + rdx*2 + 0x14], cx
008568EF  FF C0                           inc eax
008568F1  EB E7                           jmp 0x1408568da
008568F3  48 8D 53 14                     lea rdx, [rbx + 0x14]
008568F7  48 8D 4F 14                     lea rcx, [rdi + 0x14]
008568FB  E8 40 FF E6 FF                  call 0x1406c6840
00856900  4C 8B 94 24 B0 00 00 00         mov r10, qword ptr [rsp + 0xb0]
00856908  44 8B 8C 24 C0 00 00 00         mov r9d, dword ptr [rsp + 0xc0]
00856910  44 8B 9C 24 B8 00 00 00         mov r11d, dword ptr [rsp + 0xb8]
00856918  45 85 FF                        test r15d, r15d
0085691B  0F 84 AB 00 00 00               je 0x1408569cc
00856921  41 81 F9 00 00 00 80            cmp r9d, 0x80000000
00856928  0F 83 A7 00 00 00               jae 0x1408569d5
0085692E  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00856933  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00856938  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
00856940  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00856945  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0085694A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0085694F  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
00856957  4C 8B C3                        mov r8, rbx
0085695A  41 8B D3                        mov edx, r11d
0085695D  49 8B 4A 20                     mov rcx, qword ptr [r10 + 0x20]
00856961  E8 4A 04 00 00                  call 0x140856db0
00856966  41 8B CE                        mov ecx, r14d
00856969  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
0085696F  84 C0                           test al, al
00856971  41 0F 44 CE                     cmove ecx, r14d
00856975  44 8B F1                        mov r14d, ecx
00856978  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0085697C  44 8B BC 24 D0 00 00 00         mov r15d, dword ptr [rsp + 0xd0]
00856984  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00856989  44 89 6F 08                     mov dword ptr [rdi + 8], r13d
0085698D  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
00856994  41 3B CD                        cmp ecx, r13d
00856997  72 06                           jb 0x14085699f
00856999  41 2B CD                        sub ecx, r13d
0085699C  44 8B E1                        mov r12d, ecx
0085699F  45 3B E7                        cmp r12d, r15d
008569A2  B8 05 00 00 80                  mov eax, 0x80000005
008569A7  44 0F 42 F0                     cmovb r14d, eax
008569AB  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
008569B0  45 0F 43 E7                     cmovae r12d, r15d
008569B4  48 85 F6                        test rsi, rsi
008569B7  74 32                           je 0x1408569eb
008569B9  45 8B C4                        mov r8d, r12d
008569BC  41 8B CD                        mov ecx, r13d
008569BF  48 03 CF                        add rcx, rdi
008569C2  48 8B D6                        mov rdx, rsi
008569C5  E8 76 FE E6 FF                  call 0x1406c6840
008569CA  EB 1F                           jmp 0x1408569eb
008569CC  C7 47 08 FF FF FF FF            mov dword ptr [rdi + 8], 0xffffffff
008569D3  EB 16                           jmp 0x1408569eb
008569D5  48 8D 73 08                     lea rsi, [rbx + 8]
008569D9  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
008569DE  EB A9                           jmp 0x140856989
008569E0  41 BE 23 00 00 C0               mov r14d, 0xc0000023
008569E6  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
008569EB  E9 D2 FD FF FF                  jmp 0x1408567c2
008569F0  44 8B F0                        mov r14d, eax
008569F3  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008569F7  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
008569FC  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00856A01  E9 BC FD FF FF                  jmp 0x1408567c2
00856A06  0F B7 CA                        movzx ecx, dx
00856A09  8D 51 0C                        lea edx, [rcx + 0xc]
00856A0C  45 8B F4                        mov r14d, r12d
00856A0F  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00856A17  89 10                           mov dword ptr [rax], edx
00856A19  8B 94 24 D8 00 00 00            mov edx, dword ptr [rsp + 0xd8]
00856A20  83 FA 0C                        cmp edx, 0xc
00856A23  72 4F                           jb 0x140856a74
00856A25  44 89 27                        mov dword ptr [rdi], r12d
00856A28  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
00856A2C  89 47 04                        mov dword ptr [rdi + 4], eax
00856A2F  89 4F 08                        mov dword ptr [rdi + 8], ecx
00856A32  8D 42 F4                        lea eax, [rdx - 0xc]
00856A35  3B C1                           cmp eax, ecx
00856A37  73 0D                           jae 0x140856a46
00856A39  8B C8                           mov ecx, eax
00856A3B  41 BE 05 00 00 80               mov r14d, 0x80000005
00856A41  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
00856A46  49 8D 50 14                     lea rdx, [r8 + 0x14]
00856A4A  41 F6 40 10 01                  test byte ptr [r8 + 0x10], 1
00856A4F  74 15                           je 0x140856a66
00856A51  45 0F B7 48 02                  movzx r9d, word ptr [r8 + 2]
00856A56  4C 8B C2                        mov r8, rdx
00856A59  8B D1                           mov edx, ecx
00856A5B  48 8D 4F 0C                     lea rcx, [rdi + 0xc]
00856A5F  E8 6C 76 FF FF                  call 0x14084e0d0
00856A64  EB 19                           jmp 0x140856a7f
00856A66  44 8B C1                        mov r8d, ecx
00856A69  48 8D 4F 0C                     lea rcx, [rdi + 0xc]
00856A6D  E8 CE FD E6 FF                  call 0x1406c6840
00856A72  EB 0B                           jmp 0x140856a7f
00856A74  41 BE 23 00 00 C0               mov r14d, 0xc0000023
00856A7A  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
00856A7F  E9 3E FD FF FF                  jmp 0x1408567c2
00856A84  44 8B F0                        mov r14d, eax
00856A87  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00856A8B  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00856A90  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00856A95  E9 28 FD FF FF                  jmp 0x1408567c2
00856A9A  41 83 F9 01                     cmp r9d, 1
00856A9E  74 24                           je 0x140856ac4
00856AA0  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00856AA6  E9 17 FD FF FF                  jmp 0x1408567c2
00856AAB  E8 70 61 00 00                  call 0x14085cc20
00856AB0  E9 45 FD FF FF                  jmp 0x1408567fa
00856AB5  33 D2                           xor edx, edx
00856AB7  48 8B CE                        mov rcx, rsi
00856ABA  E8 B1 BD 32 00                  call 0x140b82870
00856ABF  E9 36 FD FF FF                  jmp 0x1408567fa
00856AC4  41 8B 50 04                     mov edx, dword ptr [r8 + 4]
00856AC8  8D 8A 00 00 00 80               lea ecx, [rdx - 0x80000000]
00856ACE  81 FA 00 00 00 80               cmp edx, 0x80000000
00856AD4  0F 42 CA                        cmovb ecx, edx
00856AD7  89 8C 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], ecx
00856ADE  44 8D 41 08                     lea r8d, [rcx + 8]
00856AE2  45 8B F4                        mov r14d, r12d
00856AE5  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00856AED  44 89 00                        mov dword ptr [rax], r8d
00856AF0  44 8B 84 24 D8 00 00 00         mov r8d, dword ptr [rsp + 0xd8]
00856AF8  41 83 F8 08                     cmp r8d, 8
00856AFC  72 7B                           jb 0x140856b79
00856AFE  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
00856B01  89 07                           mov dword ptr [rdi], eax
00856B03  89 4F 04                        mov dword ptr [rdi + 4], ecx
00856B06  41 83 C0 F8                     add r8d, -8
00856B0A  44 8B F9                        mov r15d, ecx
00856B0D  44 3B C1                        cmp r8d, ecx
00856B10  72 74                           jb 0x140856b86
00856B12  85 C9                           test ecx, ecx
00856B14  0F 84 98 00 00 00               je 0x140856bb2
00856B1A  81 FA 00 00 00 80               cmp edx, 0x80000000
00856B20  73 78                           jae 0x140856b9a
00856B22  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00856B27  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00856B2C  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
00856B34  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00856B39  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00856B3E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00856B43  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
00856B4B  4C 8B C3                        mov r8, rbx
00856B4E  41 8B D3                        mov edx, r11d
00856B51  49 8B 4A 20                     mov rcx, qword ptr [r10 + 0x20]
00856B55  E8 56 02 00 00                  call 0x140856db0
00856B5A  84 C0                           test al, al
00856B5C  74 47                           je 0x140856ba5
00856B5E  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00856B63  48 85 F6                        test rsi, rsi
00856B66  74 4A                           je 0x140856bb2
00856B68  45 8B C7                        mov r8d, r15d
00856B6B  48 8D 4F 08                     lea rcx, [rdi + 8]
00856B6F  48 8B D6                        mov rdx, rsi
00856B72  E8 C9 FC E6 FF                  call 0x1406c6840
00856B77  EB 39                           jmp 0x140856bb2
00856B79  41 BE 23 00 00 C0               mov r14d, 0xc0000023
00856B7F  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
00856B84  EB 2C                           jmp 0x140856bb2
00856B86  45 8B F8                        mov r15d, r8d
00856B89  B8 05 00 00 80                  mov eax, 0x80000005
00856B8E  44 8B F0                        mov r14d, eax
00856B91  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00856B95  E9 78 FF FF FF                  jmp 0x140856b12
00856B9A  48 8D 73 08                     lea rsi, [rbx + 8]
00856B9E  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00856BA3  EB BE                           jmp 0x140856b63
00856BA5  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
00856BAB  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
00856BB0  EB AC                           jmp 0x140856b5e
00856BB2  E9 0B FC FF FF                  jmp 0x1408567c2
00856BB7  44 8B F0                        mov r14d, eax
00856BBA  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00856BBE  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00856BC3  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00856BC8  E9 F5 FB FF FF                  jmp 0x1408567c2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpQueryKeyValueData(__int64 a1, int a2, __int64 a3, int a4, unsigned int a5, unsigned int a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_pB0;
    unsigned int v_stack_pB8;
    unsigned int v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned int v_stack_pD0;

    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    v_r12 = 0;
    *(unsigned __int64 *)(v_rsp - 96) = 0;
    *(unsigned __int8 *)(v_rsp + 32) = 0;
    *(unsigned int *)(v_rsp - 88) = 0xFFFFFFFFULL;
    *(unsigned int *)(v_rsp - 84) = 0;
    v_stack_m48 = *(unsigned __int64 *)(a1 + 32);
    v_stack_m50 = a3;
    a2 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a3 + 2))) + ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(a3 + 2)))));
    if (((*(unsigned __int8 *)(a3 + 16)) & (1)) == 0) { a2 = (unsigned __int16)(*(unsigned __int16 *)(a3 + 2)); }
    if (a4 != 2) goto loc_0085680E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))) < 0x80000000ULL) {
        a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)));
    }
    v_stack_p28 = (unsigned int)(a1);
    *(unsigned int *)(a7) = (unsigned int)(a1 + 12);
    if (((unsigned int)((unsigned int)(a6))) < 12) goto loc_00856795;
    *(unsigned int *)(a5) = 0;
    *(unsigned int *)(a5 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)));
    *(unsigned int *)(a5 + 8) = (unsigned int)(a1);
    v_r15 = (unsigned int)(((unsigned int)(a6)) + (-12));
    v_r14 = 0;
    if (((unsigned int)(v_r15)) < ((unsigned int)(a1))) { v_r14 = (unsigned int)((unsigned int)(0x80000005ULL)); }
    v_stack_m68 = (unsigned int)(v_r14);
    if (((unsigned int)(v_r15)) >= ((unsigned int)(a1))) { v_r15 = (unsigned int)(a1); }
    if ((unsigned int)(a1) == 0) goto loc_008567AF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))) >= 0x80000000ULL) goto loc_0085678A;
    v_stack_m78 = v_stack_m58;
    v_stack_m80 = v_stack_p20;
    v_stack_m88 = v_stack_m60;
    result = CmpGetValueData(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a5);
    if ((unsigned __int8)(result) == 0) goto loc_008567A2;
loc_0085676F:
loc_00856774:
    if (v_stack_m60 == 0) goto loc_008567AF;
    result = memcpy(a5 + 12, v_stack_m60, (unsigned int)((unsigned int)(v_r15)), a5);
    goto loc_008567AF;
loc_0085678A:
    v_stack_m60 = a3 + 8;
    goto loc_00856774;
loc_00856795:
    v_stack_m68 = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_008567AF;
loc_008567A2:
    v_stack_m68 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_0085676F;
loc_008567AF:
    goto loc_008567C2;
loc_008567C2:
    if (a3 + 8 == 0) goto loc_008567FA;
    if ((a3 + 8) == (a3 + 8)) goto loc_008567FA;
    if (v_stack_p20 == 1) goto loc_00856AB5;
    if (((*(unsigned __int8 *)(v_stack_m48 + 140)) & (1)) != 0) goto loc_00856AAB;
    result = HvpReleaseCellPaged(v_stack_m48, v_stack_m58, (unsigned int)((unsigned int)(v_r15)), a5);
loc_008567FA:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)));
loc_0085680E:
    if (a5 == 0) goto loc_00856A06;
    a4 = (unsigned int)((a5) - (1));
    if (condition_is_equal) goto loc_00856827;
    a4 = (unsigned int)((a4) - (2));
    if (condition_is_not_equal) goto loc_00856A9A;
loc_00856827:
    v_stack_pC0 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r15)) + 4)));
    v_r15 = (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r15)) + 4)) - 2147483648;
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r15)) + 4)))) < 0x80000000ULL) {
        v_r15 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r15)) + 4)));
    }
    v_stack_pD0 = (unsigned int)(v_r15);
    a2 = (unsigned int)(((unsigned __int16)(v_stack_m58) + 20) + ((unsigned int)(v_r15)));
    if ((unsigned int)(v_r15) == 0) goto loc_0085687A;
    a1 = (unsigned int)(((unsigned int)(a2)) - ((unsigned int)(v_r15)));
    v_r13 = (unsigned int)((a1 + 7) & (0xFFFFFFF8ULL));
    result = (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)));
    if (((unsigned int)(v_r13)) >= = ((unsigned int)(a1))) {
        result = (unsigned int)(v_r13);
        result = (unsigned int)((result) - ((unsigned int)(a1)));
        a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    }
    *(unsigned int *)(a7) = a2;
    if (((unsigned int)((unsigned int)(a6))) < 20) goto loc_008569E0;
    *(unsigned int *)(a5) = 0;
    *(unsigned int *)(a5 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)));
    *(unsigned int *)(a5 + 12) = (unsigned int)(v_r15);
    *(unsigned int *)(a5 + 16) = (unsigned int)((unsigned __int16)(v_stack_m58));
    v_r14 = 0;
    if (((unsigned int)((unsigned int)(a6) - 20)) < ((unsigned int)((unsigned __int16)(v_stack_m58)))) {
        a3 = (unsigned int)((unsigned int)(a6) - 20);
        v_r14 = 0x80000005ULL;
        v_stack_p40 = (unsigned int)(v_r14);
    }
    if (((*(unsigned __int8 *)(a3 + 16)) & (1)) == 0) goto loc_008568F3;
    v_stack_p44 = 0;
    a3 = (unsigned int)((a3) >> (1));
    if (((unsigned int)(a3)) >= ((unsigned int)(*(unsigned __int16 *)(a3 + 2)))) { a3 = (unsigned int)(*(unsigned __int16 *)(a3 + 2)); }
loc_008568DA:
    v_stack_p44 = 0;
    if (0 >= ((unsigned int)(a3))) goto loc_00856918;
    *(unsigned __int16 *)(a5 + 0 * 2 + 20) = (unsigned __int16)(*(unsigned __int8 *)(0 + a3 * 1 + 20));
    result = (unsigned int)((0) + 1);
    goto loc_008568DA;
loc_008568F3:
    result = memcpy(a5 + 20, a3 + 20, a3, (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r15)) + 4)));
loc_00856918:
    if ((unsigned int)(v_r15) == 0) goto loc_008569CC;
    if (((unsigned int)((unsigned int)(v_stack_pC0))) >= 0x80000000ULL) goto loc_008569D5;
    v_stack_p30 = v_stack_p50;
    v_stack_p28 = v_stack_pC8;
    v_stack_p20 = v_stack_p48;
    result = CmpGetValueData(*(unsigned __int64 *)(v_stack_pB0 + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_pB8))), a3, a5);
    a1 = (unsigned int)((unsigned int)(v_r14));
    if ((unsigned __int8)(result) == 0) { a1 = (unsigned int)((unsigned int)(0xC000009AULL)); }
    v_stack_p40 = (unsigned int)(a1);
loc_00856989:
    *(unsigned int *)(a5 + 8) = (unsigned int)(v_r13);
    if (((unsigned int)((unsigned int)(a6))) >= ((unsigned int)(v_r13))) {
        a1 = (unsigned int)(((unsigned int)(a6)) - ((unsigned int)(v_r13)));
        v_r12 = (unsigned int)(a1);
    }
    v_r14 = (unsigned int)((unsigned int)(a1));
    if (((unsigned int)(v_r12)) < ((unsigned int)((unsigned int)(a5)))) { v_r14 = (unsigned int)((unsigned int)(0x80000005ULL)); }
    v_stack_p40 = (unsigned int)(v_r14);
    if (((unsigned int)(v_r12)) >= ((unsigned int)((unsigned int)(a5)))) { v_r12 = (unsigned int)((unsigned int)(a5)); }
    if (v_stack_p48 == 0) goto loc_008569EB;
    a1 = ((unsigned int)((unsigned int)(v_r13))) + (a5);
    result = memcpy(a1, v_stack_p48, (unsigned int)((unsigned int)(v_r12)), a5);
    goto loc_008569EB;
loc_008569CC:
    *(unsigned int *)(a5 + 8) = 0xFFFFFFFFULL;
    goto loc_008569EB;
loc_008569D5:
    v_stack_p48 = a3 + 8;
    goto loc_00856989;
loc_008569E0:
    v_stack_p40 = (unsigned int)((unsigned int)(0xC0000023ULL));
loc_008569EB:
    goto loc_008567C2;
loc_00856A06:
    *(unsigned int *)(a7) = (unsigned int)((unsigned __int16)(v_stack_p48) + 12);
    if (((unsigned int)((unsigned int)(a6))) < 12) goto loc_00856A74;
    *(unsigned int *)(a5) = (unsigned int)(v_r12);
    *(unsigned int *)(a5 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r12)) + 12)));
    *(unsigned int *)(a5 + 8) = (unsigned int)((unsigned __int16)(v_stack_p48));
    v_r14 = (unsigned int)((unsigned int)(v_r12));
    if (((unsigned int)((unsigned int)(a6) - 12)) < ((unsigned int)((unsigned __int16)(v_stack_p48)))) {
        a1 = (unsigned int)((unsigned int)(a6) - 12);
        v_r14 = 0x80000005ULL;
        v_stack_p40 = (unsigned int)(v_r14);
    }
    if (((*(unsigned __int8 *)((unsigned int)((unsigned int)(v_r12)) + 16)) & (1)) == 0) goto loc_00856A66;
    result = CmpCopyCompressedName(a5 + 12, (unsigned int)((unsigned int)(a1)), (unsigned int)((unsigned int)(v_r12)) + 20, *(unsigned __int16 *)((unsigned int)((unsigned int)(v_r12)) + 2));
    goto loc_00856A7F;
loc_00856A66:
    result = memcpy(a5 + 12, (unsigned int)((unsigned int)(a1)), (unsigned int)((unsigned int)(a5 + 12)), *(unsigned __int16 *)((unsigned int)((unsigned int)(v_r12)) + 2));
    goto loc_00856A7F;
loc_00856A74:
    v_stack_p40 = (unsigned int)((unsigned int)(0xC0000023ULL));
loc_00856A7F:
    goto loc_008567C2;
loc_00856A9A:
    if (((unsigned int)(*(unsigned __int16 *)((unsigned int)((unsigned int)(v_r12)) + 2))) == 1) goto loc_00856AC4;
    goto loc_008567C2;
loc_00856AAB:
    result = HvpReleaseCellFlat(a5 + 12, (unsigned int)((unsigned int)(a1)), (unsigned int)((unsigned int)(a5 + 12)), *(unsigned __int16 *)((unsigned int)((unsigned int)(v_r12)) + 2));
    goto loc_008567FA;
loc_00856AB5:
    a2 = 0;
    result = ExFreePoolWithTag(a3 + 8, a2, (unsigned int)((unsigned int)(a5 + 12)), *(unsigned __int16 *)((unsigned int)((unsigned int)(v_r12)) + 2));
    goto loc_008567FA;
loc_00856AC4:
    a1 = (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(a5 + 12)) + 4)) - 2147483648;
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(a5 + 12)) + 4)))) < 0x80000000ULL) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(a5 + 12)) + 4))); }
    v_stack_pD0 = (unsigned int)(a1);
    *(unsigned int *)(a7) = (unsigned int)(a1 + 8);
    if (((unsigned int)((unsigned int)(a6))) < 8) goto loc_00856B79;
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)));
    *(unsigned int *)(a5 + 4) = (unsigned int)(a1);
    a3 = (unsigned int)(((unsigned int)(a6)) + (-8));
    if (((unsigned int)(a3)) < ((unsigned int)(a1))) goto loc_00856B86;
loc_00856B12:
    if ((unsigned int)(a1) == 0) goto loc_00856BB2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(a5 + 12)) + 4)))) >= 0x80000000ULL) goto loc_00856B9A;
    v_stack_p30 = v_stack_p50;
    v_stack_p28 = v_stack_pC8;
    v_stack_p20 = v_stack_p48;
    result = CmpGetValueData(*(unsigned __int64 *)(v_stack_pB0 + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_pB8))), a3, a5);
    if ((unsigned __int8)(result) == 0) goto loc_00856BA5;
loc_00856B5E:
loc_00856B63:
    if (v_stack_p48 == 0) goto loc_00856BB2;
    result = memcpy(a5 + 8, v_stack_p48, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))), a5);
    goto loc_00856BB2;
loc_00856B79:
    v_stack_p40 = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_00856BB2;
loc_00856B86:
    v_stack_p40 = (unsigned int)((unsigned int)(0x80000005ULL));
    goto loc_00856B12;
loc_00856B9A:
    v_stack_p48 = a3 + 8;
    goto loc_00856B63;
loc_00856BA5:
    v_stack_p40 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_00856B5E;
loc_00856BB2:
    goto loc_008567C2;
}
```

## 5. (Beta) C Style

```c
int64_t CmpQueryKeyValueData(void *Arg1, int32_t Arg2, void *Arg3, int32_t Arg4, void *Arg5, uint32_t Arg6, void *Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_pB0;
    uint32_t v_stack_pB8;
    uint32_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint32_t v_stack_pD0;

    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    local_r12 = 0;
    *(uint64_t *)(local_rsp - 0x60) = 0;
    *(uint8_t *)(local_rsp + 0x20) = 0;
    *(uint32_t *)(local_rsp - 0x58) = 0xFFFFFFFFULL;
    *(uint32_t *)(local_rsp - 0x54) = 0;
    v_stack_m48 = *(uint64_t *)(arg1 + 0x20);
    v_stack_m50 = Arg3;
    Arg2 = (uint16_t)(((uint16_t)(*(uint16_t *)(arg3 + 0x2))) + ((uint16_t)((uint16_t)(*(uint16_t *)(arg3 + 0x2)))));
    if (((*(uint8_t *)(arg3 + 0x10)) & (1)) == 0) { Arg2 = (uint16_t)(*(uint16_t *)(arg3 + 0x2)); }
    if (Arg4 != 2) goto loc_0085680E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4)))) < 0x80000000ULL) {
        Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4)));
    }
    v_stack_p28 = (uint32_t)(Arg1);
    *(uint32_t *)(arg7) = (uint32_t)(Arg1 + 12);
    if (((uint32_t)((uint32_t)(Arg6))) < 12) goto loc_00856795;
    *(uint32_t *)(arg5) = 0;
    *(uint32_t *)(arg5 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)));
    *(uint32_t *)(arg5 + 0x8) = (uint32_t)(Arg1);
    local_r15 = (uint32_t)(((uint32_t)(Arg6)) + (-12));
    local_r14 = 0;
    if (((uint32_t)(local_r15)) < ((uint32_t)(Arg1))) { local_r14 = (uint32_t)((uint32_t)(0x80000005ULL)); }
    v_stack_m68 = (uint32_t)(local_r14);
    if (((uint32_t)(local_r15)) >= ((uint32_t)(Arg1))) { local_r15 = (uint32_t)(Arg1); }
    if ((uint32_t)(Arg1) == 0) goto loc_008567AF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4)))) >= 0x80000000ULL) goto loc_0085678A;
    v_stack_m78 = v_stack_m58;
    v_stack_m80 = v_stack_p20;
    v_stack_m88 = v_stack_m60;
    result = CmpGetValueData(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg5);
    if ((uint8_t)(result) == 0) goto loc_008567A2;
loc_0085676F:
loc_00856774:
    if (v_stack_m60 == 0) goto loc_008567AF;
    result = memcpy(Arg5 + 12, v_stack_m60, (uint32_t)((uint32_t)(local_r15)), Arg5);
    goto loc_008567AF;
loc_0085678A:
    v_stack_m60 = Arg3 + 8;
    goto loc_00856774;
loc_00856795:
    v_stack_m68 = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_008567AF;
loc_008567A2:
    v_stack_m68 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_0085676F;
loc_008567AF:
    goto loc_008567C2;
loc_008567C2:
    if (Arg3 + 8 == 0) goto loc_008567FA;
    if ((Arg3 + 8) == (Arg3 + 8)) goto loc_008567FA;
    if (v_stack_p20 == 1) goto loc_00856AB5;
    if (((*(uint8_t *)(v_stack_m48 + 0x8C)) & (1)) != 0) goto loc_00856AAB;
    result = HvpReleaseCellPaged(v_stack_m48, v_stack_m58, (uint32_t)((uint32_t)(local_r15)), Arg5);
loc_008567FA:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)));
loc_0085680E:
    if (Arg5 == NULL) goto loc_00856A06;
    Arg4 = (uint32_t)((Arg5) - (1));
    if (condition_is_equal) goto loc_00856827;
    Arg4 = (uint32_t)((Arg4) - (2));
    if (condition_is_not_equal) goto loc_00856A9A;
loc_00856827:
    v_stack_pC0 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r15)) + 0x4)));
    local_r15 = (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r15)) + 0x4)) - 2147483648;
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r15)) + 0x4)))) < 0x80000000ULL) {
        local_r15 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r15)) + 0x4)));
    }
    v_stack_pD0 = (uint32_t)(local_r15);
    Arg2 = (uint32_t)(((uint16_t)(v_stack_m58) + 20) + ((uint32_t)(local_r15)));
    if ((uint32_t)(local_r15) == 0) goto loc_0085687A;
    Arg1 = (uint32_t)(((uint32_t)(Arg2)) - ((uint32_t)(local_r15)));
    local_r13 = (uint32_t)((Arg1 + 7) & (0xFFFFFFF8ULL));
    result = (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)));
    if (((uint32_t)(local_r13)) >= = ((uint32_t)(Arg1))) {
        result = (uint32_t)(local_r13);
        result = (uint32_t)((result) - ((uint32_t)(Arg1)));
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    }
    *(uint32_t *)(arg7) = Arg2;
    if (((uint32_t)((uint32_t)(Arg6))) < 20) goto loc_008569E0;
    *(uint32_t *)(arg5) = 0;
    *(uint32_t *)(arg5 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)));
    *(uint32_t *)(arg5 + 0xC) = (uint32_t)(local_r15);
    *(uint32_t *)(arg5 + 0x10) = (uint32_t)((uint16_t)(v_stack_m58));
    local_r14 = 0;
    if (((uint32_t)((uint32_t)(Arg6) - 20)) < ((uint32_t)((uint16_t)(v_stack_m58)))) {
        Arg3 = (uint32_t)((uint32_t)(Arg6) - 20);
        local_r14 = 0x80000005ULL;
        v_stack_p40 = (uint32_t)(local_r14);
    }
    if (((*(uint8_t *)(arg3 + 0x10)) & (1)) == 0) goto loc_008568F3;
    v_stack_p44 = 0;
    Arg3 = (uint32_t)((Arg3) >> (1));
    if (((uint32_t)(Arg3)) >= ((uint32_t)(*(uint16_t *)(arg3 + 0x2)))) { Arg3 = (uint32_t)(*(uint16_t *)(arg3 + 0x2)); }
loc_008568DA:
    v_stack_p44 = 0;
    if (0 >= ((uint32_t)(Arg3))) goto loc_00856918;
    *(uint16_t *)(arg5 + 0x0 * 2 + 0x14) = (uint16_t)(*(uint8_t *)(0 + arg3 * 1 + 0x14));
    result = (uint32_t)((0) + 1);
    goto loc_008568DA;
loc_008568F3:
    result = memcpy(Arg5 + 20, Arg3 + 20, Arg3, (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r15)) + 0x4)));
loc_00856918:
    if ((uint32_t)(local_r15) == 0) goto loc_008569CC;
    if (((uint32_t)((uint32_t)(v_stack_pC0))) >= 0x80000000ULL) goto loc_008569D5;
    v_stack_p30 = v_stack_p50;
    v_stack_p28 = v_stack_pC8;
    v_stack_p20 = v_stack_p48;
    result = CmpGetValueData(*(uint64_t *)(v_stack_pB0 + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_pB8))), Arg3, Arg5);
    Arg1 = (uint32_t)((uint32_t)(local_r14));
    if ((uint8_t)(result) == 0) { Arg1 = (uint32_t)((uint32_t)(0xC000009AULL)); }
    v_stack_p40 = (uint32_t)(Arg1);
loc_00856989:
    *(uint32_t *)(arg5 + 0x8) = (uint32_t)(local_r13);
    if (((uint32_t)((uint32_t)(Arg6))) >= ((uint32_t)(local_r13))) {
        Arg1 = (uint32_t)(((uint32_t)(Arg6)) - ((uint32_t)(local_r13)));
        local_r12 = (uint32_t)(Arg1);
    }
    local_r14 = (uint32_t)((uint32_t)(Arg1));
    if (((uint32_t)(local_r12)) < ((uint32_t)((uint32_t)(Arg5)))) { local_r14 = (uint32_t)((uint32_t)(0x80000005ULL)); }
    v_stack_p40 = (uint32_t)(local_r14);
    if (((uint32_t)(local_r12)) >= ((uint32_t)((uint32_t)(Arg5)))) { local_r12 = (uint32_t)((uint32_t)(Arg5)); }
    if (v_stack_p48 == 0) goto loc_008569EB;
    Arg1 = ((uint32_t)((uint32_t)(local_r13))) + (Arg5);
    result = memcpy(Arg1, v_stack_p48, (uint32_t)((uint32_t)(local_r12)), Arg5);
    goto loc_008569EB;
loc_008569CC:
    *(uint32_t *)(arg5 + 0x8) = 0xFFFFFFFFULL;
    goto loc_008569EB;
loc_008569D5:
    v_stack_p48 = Arg3 + 8;
    goto loc_00856989;
loc_008569E0:
    v_stack_p40 = (uint32_t)((uint32_t)(0xC0000023ULL));
loc_008569EB:
    goto loc_008567C2;
loc_00856A06:
    *(uint32_t *)(arg7) = (uint32_t)((uint16_t)(v_stack_p48) + 12);
    if (((uint32_t)((uint32_t)(Arg6))) < 12) goto loc_00856A74;
    *(uint32_t *)(arg5) = (uint32_t)(local_r12);
    *(uint32_t *)(arg5 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r12)) + 0xC)));
    *(uint32_t *)(arg5 + 0x8) = (uint32_t)((uint16_t)(v_stack_p48));
    local_r14 = (uint32_t)((uint32_t)(local_r12));
    if (((uint32_t)((uint32_t)(Arg6) - 12)) < ((uint32_t)((uint16_t)(v_stack_p48)))) {
        Arg1 = (uint32_t)((uint32_t)(Arg6) - 12);
        local_r14 = 0x80000005ULL;
        v_stack_p40 = (uint32_t)(local_r14);
    }
    if (((*(uint8_t *)((uint32_t)((uint32_t)(local_r12)) + 0x10)) & (1)) == 0) goto loc_00856A66;
    result = CmpCopyCompressedName(Arg5 + 12, (uint32_t)((uint32_t)(Arg1)), (uint32_t)((uint32_t)(local_r12)) + 20, *(uint16_t *)((uint32_t)((uint32_t)(local_r12)) + 0x2));
    goto loc_00856A7F;
loc_00856A66:
    result = memcpy(Arg5 + 12, (uint32_t)((uint32_t)(Arg1)), (uint32_t)((uint32_t)(Arg5 + 12)), *(uint16_t *)((uint32_t)((uint32_t)(local_r12)) + 0x2));
    goto loc_00856A7F;
loc_00856A74:
    v_stack_p40 = (uint32_t)((uint32_t)(0xC0000023ULL));
loc_00856A7F:
    goto loc_008567C2;
loc_00856A9A:
    if (((uint32_t)(*(uint16_t *)((uint32_t)((uint32_t)(local_r12)) + 0x2))) == 1) goto loc_00856AC4;
    goto loc_008567C2;
loc_00856AAB:
    result = HvpReleaseCellFlat(Arg5 + 12, (uint32_t)((uint32_t)(Arg1)), (uint32_t)((uint32_t)(Arg5 + 12)), *(uint16_t *)((uint32_t)((uint32_t)(local_r12)) + 0x2));
    goto loc_008567FA;
loc_00856AB5:
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg3 + 8, Arg2, (uint32_t)((uint32_t)(Arg5 + 12)), *(uint16_t *)((uint32_t)((uint32_t)(local_r12)) + 0x2));
    goto loc_008567FA;
loc_00856AC4:
    Arg1 = (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(arg5 + 0xC)) + 0x4)) - 2147483648;
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(arg5 + 0xC)) + 0x4)))) < 0x80000000ULL) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(arg5 + 0xC)) + 0x4))); }
    v_stack_pD0 = (uint32_t)(Arg1);
    *(uint32_t *)(arg7) = (uint32_t)(Arg1 + 8);
    if (((uint32_t)((uint32_t)(Arg6))) < 8) goto loc_00856B79;
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)));
    *(uint32_t *)(arg5 + 0x4) = (uint32_t)(Arg1);
    Arg3 = (uint32_t)(((uint32_t)(Arg6)) + (-8));
    if (((uint32_t)(Arg3)) < ((uint32_t)(Arg1))) goto loc_00856B86;
loc_00856B12:
    if ((uint32_t)(Arg1) == 0) goto loc_00856BB2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(arg5 + 0xC)) + 0x4)))) >= 0x80000000ULL) goto loc_00856B9A;
    v_stack_p30 = v_stack_p50;
    v_stack_p28 = v_stack_pC8;
    v_stack_p20 = v_stack_p48;
    result = CmpGetValueData(*(uint64_t *)(v_stack_pB0 + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_pB8))), Arg3, Arg5);
    if ((uint8_t)(result) == 0) goto loc_00856BA5;
loc_00856B5E:
loc_00856B63:
    if (v_stack_p48 == 0) goto loc_00856BB2;
    result = memcpy(Arg5 + 8, v_stack_p48, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))), Arg5);
    goto loc_00856BB2;
loc_00856B79:
    v_stack_p40 = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_00856BB2;
loc_00856B86:
    v_stack_p40 = (uint32_t)((uint32_t)(0x80000005ULL));
    goto loc_00856B12;
loc_00856B9A:
    v_stack_p48 = Arg3 + 8;
    goto loc_00856B63;
loc_00856BA5:
    v_stack_p40 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_00856B5E;
loc_00856BB2:
    goto loc_008567C2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x2` | `16` | `R` |
| `Arg3` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0xC` | `32` | `R` |
| `Arg3` | `+ 0x10` | `8` | `R` |
| `Arg3` | `+ 0x14` | `64` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |
| `Arg5` | `+ 0x4` | `32` | `W` |
| `Arg5` | `+ 0x8` | `32` | `W` |
| `Arg5` | `+ 0x8` | `64` | `R` |
| `Arg5` | `+ 0xC` | `32` | `W` |
| `Arg5` | `+ 0xC` | `64` | `R` |
| `Arg5` | `+ 0x10` | `32` | `W` |
| `Arg5` | `+ 0x14` | `64` | `R` |
| `Arg5` | `+ 0x14 + rdx*2` | `16` | `W` |
| `Arg7` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00856650&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
