# MmQueryBadAddresses

- RVA: `0x00AD5430`–`0x00AD5889` (길이 `1,113` bytes)
- VA: `0x0000000140AD5430`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEDE4`
- 디코드: `278`개 명령, `1,113/1,113` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AD54B5` → [MiGetListOfPendingBadPages](../../text/67/MiGetListOfPendingBadPages_function_006799D0.md) (function, `0x006799D0`)
- `0x00AD550D` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00AD5597` → [MiUpdateBadPfnIdentity](../../text/67/MiUpdateBadPfnIdentity_function_0067A890.md) (function, `0x0067A890`)
- `0x00AD55E1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD5755` → [MiLocateSharedPageViews](../../text/67/MiLocateSharedPageViews_function_0067F1E4.md) (function, `0x0067F1E4`)
- `0x00AD57CD` → [MiDeleteTrimViewInfoList](../A6/MiDeleteTrimViewInfoList_function_00A610A4.md) (function, `0x00A610A4`)
- `0x00AD5856` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD586E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MmQueryVirtualMemory](../9D/MmQueryVirtualMemory_function_009D9280.md) at `0x009D96A1`

### Static image references
- `0x00AD54A3` → RVA `0x00E2FFC8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00AD54B5` → [MiGetListOfPendingBadPages](../../text/67/MiGetListOfPendingBadPages_function_006799D0.md) (`PAGE` → `.text`)
  - `0x00AD550D` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00AD5597` → [MiUpdateBadPfnIdentity](../../text/67/MiUpdateBadPfnIdentity_function_0067A890.md) (`PAGE` → `.text`)
  - `0x00AD55E1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AD5755` → [MiLocateSharedPageViews](../../text/67/MiLocateSharedPageViews_function_0067F1E4.md) (`PAGE` → `.text`)
  - `0x00AD5856` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AD586E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD5430  48 8B C4                        mov rax, rsp
00AD5433  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00AD5437  89 50 10                        mov dword ptr [rax + 0x10], edx
00AD543A  48 89 48 08                     mov qword ptr [rax + 8], rcx
00AD543E  53                              push rbx
00AD543F  56                              push rsi
00AD5440  57                              push rdi
00AD5441  41 54                           push r12
00AD5443  41 55                           push r13
00AD5445  41 56                           push r14
00AD5447  41 57                           push r15
00AD5449  48 81 EC 90 00 00 00            sub rsp, 0x90
00AD5450  4D 8B E1                        mov r12, r9
00AD5453  4D 8B F8                        mov r15, r8
00AD5456  0F 57 C0                        xorps xmm0, xmm0
00AD5459  0F 11 40 B0                     movups xmmword ptr [rax - 0x50], xmm0
00AD545D  83 60 9C 00                     and dword ptr [rax - 0x64], 0
00AD5461  48 83 60 A0 00                  and qword ptr [rax - 0x60], 0
00AD5466  83 60 98 00                     and dword ptr [rax - 0x68], 0
00AD546A  48 8D 40 88                     lea rax, [rax - 0x78]
00AD546E  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00AD5473  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00AD5478  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AD547D  45 33 F6                        xor r14d, r14d
00AD5480  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AD5485  33 F6                           xor esi, esi
00AD5487  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00AD548C  33 DB                           xor ebx, ebx
00AD548E  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00AD5492  49 C1 EC 04                     shr r12, 4
00AD5496  4C 89 A4 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r12
00AD549E  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
00AD54A3  48 39 1D 1E AB 35 00            cmp qword ptr [rip + 0x35ab1e], rbx
00AD54AA  0F 84 3E 03 00 00               je 0x140ad57ee
00AD54B0  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00AD54B5  E8 16 45 BA FF                  call 0x1406799d0
00AD54BA  8B D8                           mov ebx, eax
00AD54BC  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00AD54C0  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00AD54C4  85 C0                           test eax, eax
00AD54C6  79 0B                           jns 0x140ad54d3
00AD54C8  8B D8                           mov ebx, eax
00AD54CA  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00AD54CE  E9 1B 03 00 00                  jmp 0x140ad57ee
00AD54D3  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00AD54D8  48 85 C0                        test rax, rax
00AD54DB  0F 84 11 03 00 00               je 0x140ad57f2
00AD54E1  48 B9 AA AA AA AA AA AA AA 0A   movabs rcx, 0xaaaaaaaaaaaaaaa
00AD54EB  48 3B C1                        cmp rax, rcx
00AD54EE  76 0A                           jbe 0x140ad54fa
00AD54F0  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AD54F5  E9 03 03 00 00                  jmp 0x140ad57fd
00AD54FA  48 8D 14 40                     lea rdx, [rax + rax*2]
00AD54FE  48 C1 E2 03                     shl rdx, 3
00AD5502  B9 40 00 00 00                  mov ecx, 0x40
00AD5507  41 B8 4D 69 42 6C               mov r8d, 0x6c42694d
00AD550D  E8 2E 60 88 FF                  call 0x14035b540
00AD5512  4C 8B F0                        mov r14, rax
00AD5515  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AD551A  48 85 C0                        test rax, rax
00AD551D  74 D1                           je 0x140ad54f0
00AD551F  4C 8B E8                        mov r13, rax
00AD5522  33 C0                           xor eax, eax
00AD5524  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AD5529  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00AD552E  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00AD5533  48 3B F8                        cmp rdi, rax
00AD5536  0F 84 AF 00 00 00               je 0x140ad55eb
00AD553C  48 8B 07                        mov rax, qword ptr [rdi]
00AD553F  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00AD5544  48 39 4F 08                     cmp qword ptr [rdi + 8], rcx
00AD5548  0F 85 0F 03 00 00               jne 0x140ad585d
00AD554E  48 39 78 08                     cmp qword ptr [rax + 8], rdi
00AD5552  0F 85 05 03 00 00               jne 0x140ad585d
00AD5558  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AD555D  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00AD5562  48 89 48 08                     mov qword ptr [rax + 8], rcx
00AD5566  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00AD556A  83 64 24 24 00                  and dword ptr [rsp + 0x24], 0
00AD556F  48 83 7F 10 00                  cmp qword ptr [rdi + 0x10], 0
00AD5574  76 66                           jbe 0x140ad55dc
00AD5576  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
00AD557B  4C 8B E0                        mov r12, rax
00AD557E  44 8B 7C 24 24                  mov r15d, dword ptr [rsp + 0x24]
00AD5583  49 8B 0C 24                     mov rcx, qword ptr [r12]
00AD5587  48 B8 FF FF FF FF FF FF 0F 00   movabs rax, 0xfffffffffffff
00AD5591  48 23 C8                        and rcx, rax
00AD5594  49 8B D5                        mov rdx, r13
00AD5597  E8 F4 52 BA FF                  call 0x14067a890
00AD559C  49 8D 4D 18                     lea rcx, [r13 + 0x18]
00AD55A0  85 C0                           test eax, eax
00AD55A2  49 0F 44 CD                     cmove rcx, r13
00AD55A6  4C 8B E9                        mov r13, rcx
00AD55A9  48 8D 4E 01                     lea rcx, [rsi + 1]
00AD55AD  48 0F 44 CE                     cmove rcx, rsi
00AD55B1  48 8B F1                        mov rsi, rcx
00AD55B4  4D 8D 64 24 08                  lea r12, [r12 + 8]
00AD55B9  41 FF C7                        inc r15d
00AD55BC  41 8B C7                        mov eax, r15d
00AD55BF  48 3B 47 10                     cmp rax, qword ptr [rdi + 0x10]
00AD55C3  72 BE                           jb 0x140ad5583
00AD55C5  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00AD55CA  33 F6                           xor esi, esi
00AD55CC  4C 8B BC 24 E0 00 00 00         mov r15, qword ptr [rsp + 0xe0]
00AD55D4  4C 8B A4 24 E8 00 00 00         mov r12, qword ptr [rsp + 0xe8]
00AD55DC  33 D2                           xor edx, edx
00AD55DE  48 8B CF                        mov rcx, rdi
00AD55E1  E8 8A D2 0A 00                  call 0x140b82870
00AD55E6  E9 3E FF FF FF                  jmp 0x140ad5529
00AD55EB  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00AD55F0  4C 8B 9C 24 D0 00 00 00         mov r11, qword ptr [rsp + 0xd0]
00AD55F8  45 8B 9B D0 01 00 00            mov r11d, dword ptr [r11 + 0x1d0]
00AD55FF  44 89 9C 24 E8 00 00 00         mov dword ptr [rsp + 0xe8], r11d
00AD5607  44 89 5C 24 24                  mov dword ptr [rsp + 0x24], r11d
00AD560C  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
00AD5613  83 F8 0D                        cmp eax, 0xd
00AD5616  75 0A                           jne 0x140ad5622
00AD5618  C7 44 24 7C 01 00 00 00         mov dword ptr [rsp + 0x7c], 1
00AD5620  EB 05                           jmp 0x140ad5627
00AD5622  44 89 5C 24 78                  mov dword ptr [rsp + 0x78], r11d
00AD5627  45 33 ED                        xor r13d, r13d
00AD562A  4C 8B 54 24 30                  mov r10, qword ptr [rsp + 0x30]
00AD562F  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00AD5634  4D 3B EA                        cmp r13, r10
00AD5637  0F 83 B1 01 00 00               jae 0x140ad57ee
00AD563D  4E 8D 04 6D 00 00 00 00         lea r8, [r13*2]
00AD5645  4D 03 C5                        add r8, r13
00AD5648  4F 8B 4C C6 08                  mov r9, qword ptr [r14 + r8*8 + 8]
00AD564D  49 83 F9 FF                     cmp r9, -1
00AD5651  0F 84 8F 01 00 00               je 0x140ad57e6
00AD5657  83 F8 0D                        cmp eax, 0xd
00AD565A  74 15                           je 0x140ad5671
00AD565C  43 8A 04 C6                     mov al, byte ptr [r14 + r8*8]
00AD5660  24 0F                           and al, 0xf
00AD5662  3C 0E                           cmp al, 0xe
00AD5664  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
00AD566B  0F 84 75 01 00 00               je 0x140ad57e6
00AD5671  4B 8B 0C C6                     mov rcx, qword ptr [r14 + r8*8]
00AD5675  48 8B F9                        mov rdi, rcx
00AD5678  48 C1 EF 07                     shr rdi, 7
00AD567C  83 E7 01                        and edi, 1
00AD567F  48 8B D1                        mov rdx, rcx
00AD5682  83 E2 0F                        and edx, 0xf
00AD5685  48 83 FA 0E                     cmp rdx, 0xe
00AD5689  75 40                           jne 0x140ad56cb
00AD568B  49 3B F4                        cmp rsi, r12
00AD568E  73 14                           jae 0x140ad56a4
00AD5690  48 83 CF 02                     or rdi, 2
00AD5694  4D 89 0F                        mov qword ptr [r15], r9
00AD5697  49 89 7F 08                     mov qword ptr [r15 + 8], rdi
00AD569B  49 83 C7 10                     add r15, 0x10
00AD569F  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00AD56A4  48 FF C6                        inc rsi
00AD56A7  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00AD56AC  E9 35 01 00 00                  jmp 0x140ad57e6
00AD56B1  8B D8                           mov ebx, eax
00AD56B3  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00AD56B7  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00AD56BC  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00AD56C1  48 8B 74 24 28                  mov rsi, qword ptr [rsp + 0x28]
00AD56C6  E9 23 01 00 00                  jmp 0x140ad57ee
00AD56CB  48 8D 42 FF                     lea rax, [rdx - 1]
00AD56CF  48 83 F8 01                     cmp rax, 1
00AD56D3  76 70                           jbe 0x140ad5745
00AD56D5  48 83 FA 08                     cmp rdx, 8
00AD56D9  74 6A                           je 0x140ad5745
00AD56DB  48 C1 E9 09                     shr rcx, 9
00AD56DF  48 B8 FF FF FF FF FF FF 00 00   movabs rax, 0xffffffffffff
00AD56E9  48 23 C8                        and rcx, rax
00AD56EC  41 8B C3                        mov eax, r11d
00AD56EF  48 3B C1                        cmp rax, rcx
00AD56F2  74 10                           je 0x140ad5704
00AD56F4  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
00AD56FB  83 F8 0D                        cmp eax, 0xd
00AD56FE  0F 85 E2 00 00 00               jne 0x140ad57e6
00AD5704  49 3B F4                        cmp rsi, r12
00AD5707  73 15                           jae 0x140ad571e
00AD5709  4B 8B 44 C6 10                  mov rax, qword ptr [r14 + r8*8 + 0x10]
00AD570E  49 89 07                        mov qword ptr [r15], rax
00AD5711  49 89 7F 08                     mov qword ptr [r15 + 8], rdi
00AD5715  49 83 C7 10                     add r15, 0x10
00AD5719  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00AD571E  48 FF C6                        inc rsi
00AD5721  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00AD5726  E9 B4 00 00 00                  jmp 0x140ad57df
00AD572B  8B D8                           mov ebx, eax
00AD572D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00AD5731  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00AD5736  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00AD573B  48 8B 74 24 28                  mov rsi, qword ptr [rsp + 0x28]
00AD5740  E9 A9 00 00 00                  jmp 0x140ad57ee
00AD5745  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
00AD574D  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00AD5752  49 8B C9                        mov rcx, r9
00AD5755  E8 8A 9A BA FF                  call 0x14067f1e4
00AD575A  85 C0                           test eax, eax
00AD575C  0F 88 8E FD FF FF               js 0x140ad54f0
00AD5762  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
00AD576A  48 8B CA                        mov rcx, rdx
00AD576D  48 85 C9                        test rcx, rcx
00AD5770  74 58                           je 0x140ad57ca
00AD5772  49 3B F4                        cmp rsi, r12
00AD5775  73 14                           jae 0x140ad578b
00AD5777  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00AD577B  49 89 07                        mov qword ptr [r15], rax
00AD577E  49 89 7F 08                     mov qword ptr [r15 + 8], rdi
00AD5782  49 83 C7 10                     add r15, 0x10
00AD5786  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00AD578B  48 FF C6                        inc rsi
00AD578E  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00AD5793  48 8B 09                        mov rcx, qword ptr [rcx]
00AD5796  EB D5                           jmp 0x140ad576d
00AD5798  8B D8                           mov ebx, eax
00AD579A  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00AD579E  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
00AD57A2  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
00AD57A9  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00AD57AE  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
00AD57B3  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00AD57B8  48 8B 74 24 28                  mov rsi, qword ptr [rsp + 0x28]
00AD57BD  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
00AD57C5  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
00AD57CA  48 8B CA                        mov rcx, rdx
00AD57CD  E8 D2 B8 F8 FF                  call 0x140a610a4
00AD57D2  4C 8B 54 24 30                  mov r10, qword ptr [rsp + 0x30]
00AD57D7  44 8B 9C 24 E8 00 00 00         mov r11d, dword ptr [rsp + 0xe8]
00AD57DF  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
00AD57E6  49 FF C5                        inc r13
00AD57E9  E9 41 FE FF FF                  jmp 0x140ad562f
00AD57EE  85 DB                           test ebx, ebx
00AD57F0  78 0F                           js 0x140ad5801
00AD57F2  4C 3B E6                        cmp r12, rsi
00AD57F5  1B DB                           sbb ebx, ebx
00AD57F7  81 E3 23 00 00 C0               and ebx, 0xc0000023
00AD57FD  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00AD5801  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
00AD5809  48 85 C0                        test rax, rax
00AD580C  74 12                           je 0x140ad5820
00AD580E  48 C1 E6 04                     shl rsi, 4
00AD5812  48 89 30                        mov qword ptr [rax], rsi
00AD5815  EB 09                           jmp 0x140ad5820
00AD5817  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00AD581C  8B 5C 24 20                     mov ebx, dword ptr [rsp + 0x20]
00AD5820  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00AD5825  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00AD582A  48 3B F8                        cmp rdi, rax
00AD582D  74 35                           je 0x140ad5864
00AD582F  48 8B 07                        mov rax, qword ptr [rdi]
00AD5832  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00AD5837  48 39 4F 08                     cmp qword ptr [rdi + 8], rcx
00AD583B  75 20                           jne 0x140ad585d
00AD583D  48 39 78 08                     cmp qword ptr [rax + 8], rdi
00AD5841  75 1A                           jne 0x140ad585d
00AD5843  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AD5848  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00AD584D  48 89 48 08                     mov qword ptr [rax + 8], rcx
00AD5851  33 D2                           xor edx, edx
00AD5853  48 8B CF                        mov rcx, rdi
00AD5856  E8 15 D0 0A 00                  call 0x140b82870
00AD585B  EB C3                           jmp 0x140ad5820
00AD585D  B9 03 00 00 00                  mov ecx, 3
00AD5862  CD 29                           int 0x29
00AD5864  4D 85 F6                        test r14, r14
00AD5867  74 0A                           je 0x140ad5873
00AD5869  33 D2                           xor edx, edx
00AD586B  49 8B CE                        mov rcx, r14
00AD586E  E8 FD CF 0A 00                  call 0x140b82870
00AD5873  8B C3                           mov eax, ebx
00AD5875  48 81 C4 90 00 00 00            add rsp, 0x90
00AD587C  41 5F                           pop r15
00AD587E  41 5E                           pop r14
00AD5880  41 5D                           pop r13
00AD5882  41 5C                           pop r12
00AD5884  5F                              pop rdi
00AD5885  5E                              pop rsi
00AD5886  5B                              pop rbx
00AD5887  C3                              ret
00AD5888  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmQueryBadAddresses(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (144);
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm0;
    v_stack_m70 = v_rsp - 120;
    v_stack_m78 = v_stack_m78;
    v_r14 = 0;
    v_stack_m90 = 0;
    v_rsi = 0;
    v_stack_mA0 = 0;
    v_rbx = 0;
    v_stack_mA8 = 0;
    v_r12 = (a4) >> (4);
    v_stack_p20 = v_r12;
    v_stack_m58 = v_r12;
    if ((*(unsigned __int64 *)(v_rip + 3517214)) == 0) goto loc_00AD57EE;
    result = MiGetListOfPendingBadPages(v_stack_m78, a2, a3, a4);
    v_stack_mA8 = (unsigned int)(result);
    if (!sign_flag) goto loc_00AD54D3;
    v_stack_mA8 = (unsigned int)((unsigned int)(v_stack_m68));
    goto loc_00AD57EE;
loc_00AD54D3:
    if (v_stack_m60 == 0) goto loc_00AD57F2;
    if (v_stack_m60 <= v_stack_m78) goto loc_00AD54FA;
loc_00AD54F0:
    goto loc_00AD57FD;
loc_00AD54FA:
    a2 = (v_stack_m60 + v_stack_m60 * 2) << (3);
    result = MiAllocatePool(64, a2, (unsigned int)(0x6C42694DULL), a4);
    v_stack_m90 = result;
    if (result == 0) goto loc_00AD54F0;
    result = 0;
    v_stack_m98 = 0;
loc_00AD5529:
    if (v_stack_m78 == v_stack_m78) goto loc_00AD55EB;
    if ((*(unsigned __int64 *)(v_stack_m78 + 8)) != v_stack_m78) goto loc_00AD585D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m78) + 8)) != v_stack_m78) goto loc_00AD585D;
    v_stack_m78 = *(unsigned __int64 *)(v_stack_m78);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m78) + 8) = v_stack_m78;
    if ((*(unsigned __int64 *)(v_stack_m78 + 16)) <= 0) goto loc_00AD55DC;
loc_00AD5583:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m78 + 24))) & (*(unsigned __int64 *)(v_stack_m78 + 24));
    result = MiUpdateBadPfnIdentity(a1, 0, (unsigned int)(0x6C42694DULL), a4);
    a1 = result + 24;
    if ((unsigned int)(result) == 0) { a1 = result; }
    a1 = v_stack_m98 + 1;
    if ((unsigned int)(result) == 0) { a1 = v_stack_m98; }
    v_r15 = (unsigned int)(((unsigned int)(v_stack_mA4)) + 1);
    if (((unsigned int)((unsigned int)(v_r15))) < (*(unsigned __int64 *)(v_stack_m78 + 16))) goto loc_00AD5583;
    v_stack_m98 = a1;
    v_rsi = 0;
loc_00AD55DC:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m78, a2, (unsigned int)(0x6C42694DULL), a4);
    goto loc_00AD5529;
loc_00AD55EB:
    v_stack_m88 = v_stack_p18;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 464)));
    v_stack_mA4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 464)));
    if (((unsigned int)((unsigned int)(v_stack_p10))) != 13) goto loc_00AD5622;
    v_stack_m4C = 1;
    goto loc_00AD5627;
loc_00AD5622:
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 464)));
loc_00AD5627:
    v_r13 = 0;
loc_00AD562F:
    v_stack_m80 = 0;
    if (0 >= v_stack_m98) goto loc_00AD57EE;
    a3 = (v_r13 * 2) + (0);
    if ((*(unsigned __int64 *)(result + a3 * 8 + 8)) == -1) goto loc_00AD57E6;
    if (((unsigned int)((unsigned int)(v_stack_p10))) == 13) goto loc_00AD5671;
    result = (unsigned __int8)((*(unsigned __int8 *)(result + a3 * 8)) & (15));
    if (((unsigned __int8)(result)) == 14) goto loc_00AD57E6;
loc_00AD5671:
    v_rdi = (*(unsigned __int64 *)(result + a3 * 8)) >> (7);
    v_rdi = (unsigned int)((v_rdi) & (1));
    a2 = (unsigned int)((*(unsigned __int64 *)(result + a3 * 8)) & (15));
    if (a2 != 14) goto loc_00AD56CB;
    v_r15 = v_stack_p18;
    if (0 < v_stack_p20) {
        v_rdi = (v_rdi) | (2);
        *(unsigned __int64 *)(v_stack_p18) = *(unsigned __int64 *)(result + a3 * 8 + 8);
        *(unsigned __int64 *)(v_stack_p18 + 8) = v_rdi;
        v_r15 = (v_stack_p18) + (16);
        v_stack_m88 = v_r15;
    }
    v_rsi = (v_rsi) + 1;
    v_stack_mA0 = v_rsi;
    goto loc_00AD57E6;
loc_00AD56CB:
    if ((a2 - 1) <= 1) goto loc_00AD5745;
    if (a2 == 8) goto loc_00AD5745;
    a1 = (*(unsigned __int64 *)(result + a3 * 8)) >> (9);
    a1 = (a1) & (a2 - 1);
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 464))))) == a1) goto loc_00AD5704;
    if (((unsigned int)((unsigned int)(v_stack_p10))) != 13) goto loc_00AD57E6;
loc_00AD5704:
    result = (unsigned int)(v_stack_p10);
    if (v_rsi < v_stack_p20) {
        result = *(unsigned __int64 *)(result + a3 * 8 + 16);
        *(unsigned __int64 *)(v_r15) = result;
        *(unsigned __int64 *)(v_r15 + 8) = v_rdi;
        v_r15 = (v_r15) + (16);
        v_stack_m88 = v_r15;
    }
    v_rsi = (v_rsi) + 1;
    v_stack_mA0 = v_rsi;
    goto loc_00AD57DF;
loc_00AD5745:
    result = MiLocateSharedPageViews(*(unsigned __int64 *)(result + a3 * 8 + 8), v_stack_m50, v_stack_p8, *(unsigned __int64 *)(result + a3 * 8 + 8));
    if (sign_flag) goto loc_00AD54F0;
loc_00AD576D:
    if (v_stack_m48 == 0) goto loc_00AD57CA;
    if (v_rsi < v_stack_p20) {
        result = *(unsigned __int64 *)(v_stack_m48 + 16);
        *(unsigned __int64 *)(v_r15) = result;
        *(unsigned __int64 *)(v_r15 + 8) = v_rdi;
        v_r15 = (v_r15) + (16);
        v_stack_m88 = v_r15;
    }
    v_rsi = (v_rsi) + 1;
    v_stack_mA0 = v_rsi;
    goto loc_00AD576D;
loc_00AD57CA:
    result = MiDeleteTrimViewInfoList(v_stack_m48, v_stack_m48, v_stack_p8, *(unsigned __int64 *)(result + a3 * 8 + 8));
loc_00AD57DF:
loc_00AD57E6:
    v_r13 = (v_r13) + 1;
    goto loc_00AD562F;
loc_00AD57EE:
    if (sign_flag) goto loc_00AD5801;
loc_00AD57F2:
    v_rbx = (unsigned int)(((unsigned int)(0xC000009AULL)) & (0xC0000023ULL));
loc_00AD57FD:
    v_stack_mA8 = (unsigned int)(v_rbx);
loc_00AD5801:
    if (a5 == 0) goto loc_00AD5820;
    v_rsi = (v_rsi) << (4);
    *(unsigned __int64 *)(a5) = v_rsi;
    goto loc_00AD5820;
loc_00AD5820:
    if (v_stack_m78 == v_stack_m78) goto loc_00AD5864;
    if ((*(unsigned __int64 *)(v_stack_m78 + 8)) != v_stack_m78) goto loc_00AD585D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m78) + 8)) != v_stack_m78) goto loc_00AD585D;
    v_stack_m78 = *(unsigned __int64 *)(v_stack_m78);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m78) + 8) = v_stack_m78;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m78, a2, v_stack_p8, *(unsigned __int64 *)(result + a3 * 8 + 8));
    goto loc_00AD5820;
loc_00AD585D:
loc_00AD5864:
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_p8, *(unsigned __int64 *)(result + a3 * 8 + 8));
    }
    v_rsp = (v_rsp) + (144);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t MmQueryBadAddresses(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (144);
    *(uint64_t *)(local_rsp - 0x50) = v_xmm0;
    v_stack_m70 = local_rsp - 120;
    v_stack_m78 = v_stack_m78;
    local_r14 = 0;
    v_stack_m90 = 0;
    local_rsi = 0;
    v_stack_mA0 = 0;
    local_rbx = 0;
    v_stack_mA8 = 0;
    local_r12 = (Arg4) >> (4);
    v_stack_p20 = local_r12;
    v_stack_m58 = local_r12;
    if ((*(uint64_t *)(v_rip + 0x35AB1E)) == 0) goto loc_00AD57EE;
    result = MiGetListOfPendingBadPages(v_stack_m78, Arg2, Arg3, Arg4);
    v_stack_mA8 = (uint32_t)(result);
    if (!sign_flag) goto loc_00AD54D3;
    v_stack_mA8 = (uint32_t)((uint32_t)(v_stack_m68));
    goto loc_00AD57EE;
loc_00AD54D3:
    if (v_stack_m60 == 0) goto loc_00AD57F2;
    if (v_stack_m60 <= v_stack_m78) goto loc_00AD54FA;
loc_00AD54F0:
    goto loc_00AD57FD;
loc_00AD54FA:
    Arg2 = (v_stack_m60 + v_stack_m60 * 2) << (3);
    result = MiAllocatePool(64, Arg2, (uint32_t)(0x6C42694DULL), Arg4);
    v_stack_m90 = result;
    if (result == 0) goto loc_00AD54F0;
    result = 0;
    v_stack_m98 = 0;
loc_00AD5529:
    if (v_stack_m78 == v_stack_m78) goto loc_00AD55EB;
    if ((*(uint64_t *)(v_stack_m78 + 0x8)) != v_stack_m78) goto loc_00AD585D;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m78) + 0x8)) != v_stack_m78) goto loc_00AD585D;
    v_stack_m78 = *(uint64_t *)(v_stack_m78);
    *(uint64_t *)(*(uint64_t *)(v_stack_m78) + 0x8) = v_stack_m78;
    if ((*(uint64_t *)(v_stack_m78 + 0x10)) <= 0) goto loc_00AD55DC;
loc_00AD5583:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m78 + 0x18))) & (*(uint64_t *)(v_stack_m78 + 0x18));
    result = MiUpdateBadPfnIdentity(Arg1, 0, (uint32_t)(0x6C42694DULL), Arg4);
    Arg1 = result + 24;
    if ((uint32_t)(result) == 0) { Arg1 = result; }
    Arg1 = v_stack_m98 + 1;
    if ((uint32_t)(result) == 0) { Arg1 = v_stack_m98; }
    local_r15 = (uint32_t)(((uint32_t)(v_stack_mA4)) + 1);
    if (((uint32_t)((uint32_t)(local_r15))) < (*(uint64_t *)(v_stack_m78 + 0x10))) goto loc_00AD5583;
    v_stack_m98 = Arg1;
    local_rsi = 0;
loc_00AD55DC:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m78, Arg2, (uint32_t)(0x6C42694DULL), Arg4);
    goto loc_00AD5529;
loc_00AD55EB:
    v_stack_m88 = v_stack_p18;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x1D0)));
    v_stack_mA4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x1D0)));
    if (((uint32_t)((uint32_t)(v_stack_p10))) != 13) goto loc_00AD5622;
    v_stack_m4C = 1;
    goto loc_00AD5627;
loc_00AD5622:
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x1D0)));
loc_00AD5627:
    local_r13 = 0;
loc_00AD562F:
    v_stack_m80 = 0;
    if (0 >= v_stack_m98) goto loc_00AD57EE;
    Arg3 = (local_r13 * 2) + (0);
    if ((*(uint64_t *)(result + Arg3 * 8 + 0x8)) == -1) goto loc_00AD57E6;
    if (((uint32_t)((uint32_t)(v_stack_p10))) == 13) goto loc_00AD5671;
    result = (uint8_t)((*(uint8_t *)(result + Arg3 * 8)) & (15));
    if (((uint8_t)(result)) == 14) goto loc_00AD57E6;
loc_00AD5671:
    local_rdi = (*(uint64_t *)(result + Arg3 * 8)) >> (7);
    local_rdi = (uint32_t)((local_rdi) & (1));
    Arg2 = (uint32_t)((*(uint64_t *)(result + Arg3 * 8)) & (15));
    if (Arg2 != 14) goto loc_00AD56CB;
    local_r15 = v_stack_p18;
    if (0 < v_stack_p20) {
        local_rdi = (local_rdi) | (2);
        *(uint64_t *)(v_stack_p18) = *(uint64_t *)(result + Arg3 * 8 + 0x8);
        *(uint64_t *)(v_stack_p18 + 0x8) = local_rdi;
        local_r15 = (v_stack_p18) + (16);
        v_stack_m88 = local_r15;
    }
    local_rsi = (local_rsi) + 1;
    v_stack_mA0 = local_rsi;
    goto loc_00AD57E6;
loc_00AD56CB:
    if ((Arg2 - 1) <= 1) goto loc_00AD5745;
    if (Arg2 == 8) goto loc_00AD5745;
    Arg1 = (*(uint64_t *)(result + Arg3 * 8)) >> (9);
    Arg1 = (Arg1) & (Arg2 - 1);
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x1D0))))) == Arg1) goto loc_00AD5704;
    if (((uint32_t)((uint32_t)(v_stack_p10))) != 13) goto loc_00AD57E6;
loc_00AD5704:
    result = (uint32_t)(v_stack_p10);
    if (local_rsi < v_stack_p20) {
        result = *(uint64_t *)(result + Arg3 * 8 + 0x10);
        *(uint64_t *)(local_r15) = result;
        *(uint64_t *)(local_r15 + 0x8) = local_rdi;
        local_r15 = (local_r15) + (16);
        v_stack_m88 = local_r15;
    }
    local_rsi = (local_rsi) + 1;
    v_stack_mA0 = local_rsi;
    goto loc_00AD57DF;
loc_00AD5745:
    result = MiLocateSharedPageViews(*(uint64_t *)(result + Arg3 * 8 + 0x8), v_stack_m50, v_stack_p8, *(uint64_t *)(result + Arg3 * 8 + 0x8));
    if (sign_flag) goto loc_00AD54F0;
loc_00AD576D:
    if (v_stack_m48 == 0) goto loc_00AD57CA;
    if (local_rsi < v_stack_p20) {
        result = *(uint64_t *)(v_stack_m48 + 0x10);
        *(uint64_t *)(local_r15) = result;
        *(uint64_t *)(local_r15 + 0x8) = local_rdi;
        local_r15 = (local_r15) + (16);
        v_stack_m88 = local_r15;
    }
    local_rsi = (local_rsi) + 1;
    v_stack_mA0 = local_rsi;
    goto loc_00AD576D;
loc_00AD57CA:
    result = MiDeleteTrimViewInfoList(v_stack_m48, v_stack_m48, v_stack_p8, *(uint64_t *)(result + Arg3 * 8 + 0x8));
loc_00AD57DF:
loc_00AD57E6:
    local_r13 = (local_r13) + 1;
    goto loc_00AD562F;
loc_00AD57EE:
    if (sign_flag) goto loc_00AD5801;
loc_00AD57F2:
    local_rbx = (uint32_t)(((uint32_t)(0xC000009AULL)) & (0xC0000023ULL));
loc_00AD57FD:
    v_stack_mA8 = (uint32_t)(local_rbx);
loc_00AD5801:
    if (Arg5 == 0) goto loc_00AD5820;
    local_rsi = (local_rsi) << (4);
    *(uint64_t *)(Arg5) = local_rsi;
    goto loc_00AD5820;
loc_00AD5820:
    if (v_stack_m78 == v_stack_m78) goto loc_00AD5864;
    if ((*(uint64_t *)(v_stack_m78 + 0x8)) != v_stack_m78) goto loc_00AD585D;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m78) + 0x8)) != v_stack_m78) goto loc_00AD585D;
    v_stack_m78 = *(uint64_t *)(v_stack_m78);
    *(uint64_t *)(*(uint64_t *)(v_stack_m78) + 0x8) = v_stack_m78;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m78, Arg2, v_stack_p8, *(uint64_t *)(result + Arg3 * 8 + 0x8));
    goto loc_00AD5820;
loc_00AD585D:
loc_00AD5864:
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_p8, *(uint64_t *)(result + Arg3 * 8 + 0x8));
    }
    local_rsp = (local_rsp) + (144);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD5430&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
