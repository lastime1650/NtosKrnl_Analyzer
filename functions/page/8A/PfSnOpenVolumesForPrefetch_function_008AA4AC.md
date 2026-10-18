# PfSnOpenVolumesForPrefetch

- RVA: `0x008AA4AC`–`0x008AAAC6` (길이 `1,562` bytes)
- VA: `0x00000001408AA4AC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F61C`
- 디코드: `400`개 명령, `1,562/1,562` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x008AA53D` → [PfSnLogOpenVolumesForPrefetch](../A6/PfSnLogOpenVolumesForPrefetch_function_00A629EC.md) (function, `0x00A629EC`)
- `0x008AA568` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008AA595` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008AA5F7` → [NtCreateEvent](../8B/NtCreateEvent_function_008B9140.md) (function, `0x008B9140`)
- `0x008AA617` → [IoGetDeviceInterfaces](../95/IoGetDeviceInterfaces_function_00953340.md) (function, `0x00953340`)
- `0x008AA666` → [PfSnIsVolumeMounted](PfSnIsVolumeMounted_function_008AAACC.md) (function, `0x008AAACC`)
- `0x008AA6B4` → [PfSnQueryVolumeInfo](PfSnQueryVolumeInfo_function_008AD38C.md) (function, `0x008AD38C`)
- `0x008AA6CD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008AA6E7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008AA76E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008AA827` → [PfSnVolumeCheckSeekPenalty](../A6/PfSnVolumeCheckSeekPenalty_function_00A6ECB4.md) (function, `0x00A6ECB4`)
- `0x008AA850` → [PfSnVolumeCheckIsSdBus](../A6/PfSnVolumeCheckIsSdBus_function_00A6AF38.md) (function, `0x00A6AF38`)
- `0x008AA87B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AA8E1` → [PfpOpenHandleClose](PfpOpenHandleClose_function_008A9E74.md) (function, `0x008A9E74`)
- `0x008AA8EB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AA8FC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AA90A` → [NtClose](../86/NtClose_function_00868870.md) (function, `0x00868870`)
- `0x008AA914` → [PfSnLogOpenVolumesForPrefetch](../A6/PfSnLogOpenVolumesForPrefetch_function_00A629EC.md) (function, `0x00A629EC`)
- `0x008AA986` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (function, `0x0040FB40`)
- `0x008AA9FE` → [PfpOpenHandleCreate](PfpOpenHandleCreate_function_008A9EDC.md) (function, `0x008A9EDC`)
- `0x008AAABC` → [PfpOpenHandleClose](PfpOpenHandleClose_function_008A9E74.md) (function, `0x008A9E74`)

### Direct callers
- [PfSnAsyncPrefetchWorker](../93/PfSnAsyncPrefetchWorker_function_009394B0.md) at `0x0093962A`

### Static image references
- `0x008AA610` → RVA `0x00011190` (`.rdata`; read)
- `0x008AA978` → RVA `0x00B01530` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x008AA568` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008AA595` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008AA6CD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008AA6E7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008AA76E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008AA87B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AA8EB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AA8FC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AA986` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008AA4AC  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
008AA4B1  55                              push rbp
008AA4B2  53                              push rbx
008AA4B3  56                              push rsi
008AA4B4  57                              push rdi
008AA4B5  41 54                           push r12
008AA4B7  41 55                           push r13
008AA4B9  41 56                           push r14
008AA4BB  41 57                           push r15
008AA4BD  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
008AA4C2  48 81 EC F8 00 00 00            sub rsp, 0xf8
008AA4C9  4C 8B 31                        mov r14, qword ptr [rcx]
008AA4CC  48 8D 44 24 40                  lea rax, [rsp + 0x40]
008AA4D1  45 33 FF                        xor r15d, r15d
008AA4D4  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008AA4D9  0F 57 C0                        xorps xmm0, xmm0
008AA4DC  44 89 7D EB                     mov dword ptr [rbp - 0x15], r15d
008AA4E0  48 8D 44 24 40                  lea rax, [rsp + 0x40]
008AA4E5  44 89 7D 03                     mov dword ptr [rbp + 3], r15d
008AA4E9  4C 8B E1                        mov r12, rcx
008AA4EC  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008AA4F1  49 BD 00 00 00 00 02 00 00 00   movabs r13, 0x200000000
008AA4FB  4C 89 7D 8F                     mov qword ptr [rbp - 0x71], r15
008AA4FF  B2 01                           mov dl, 1
008AA501  44 89 7D 7F                     mov dword ptr [rbp + 0x7f], r15d
008AA505  49 8B CE                        mov rcx, r14
008AA508  44 89 7D 67                     mov dword ptr [rbp + 0x67], r15d
008AA50C  0F 11 45 97                     movups xmmword ptr [rbp - 0x69], xmm0
008AA510  44 89 7D 77                     mov dword ptr [rbp + 0x77], r15d
008AA514  41 8B F7                        mov esi, r15d
008AA517  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
008AA51C  41 8B DF                        mov ebx, r15d
008AA51F  4C 89 7D C7                     mov qword ptr [rbp - 0x39], r15
008AA523  F3 0F 7F 45 CF                  movdqu xmmword ptr [rbp - 0x31], xmm0
008AA528  4C 89 6D DF                     mov qword ptr [rbp - 0x21], r13
008AA52C  4C 89 7D A7                     mov qword ptr [rbp - 0x59], r15
008AA530  F3 0F 7F 45 AF                  movdqu xmmword ptr [rbp - 0x51], xmm0
008AA535  4C 89 6D BF                     mov qword ptr [rbp - 0x41], r13
008AA539  4C 89 7D 87                     mov qword ptr [rbp - 0x79], r15
008AA53D  E8 AA 84 1B 00                  call 0x140a629ec
008AA542  4D 85 F6                        test r14, r14
008AA545  0F 84 3B 05 00 00               je 0x1408aaa86
008AA54B  41 8B 46 70                     mov eax, dword ptr [r14 + 0x70]
008AA54F  3D 00 40 00 00                  cmp eax, 0x4000
008AA554  0F 83 2C 05 00 00               jae 0x1408aaa86
008AA55A  6B D0 70                        imul edx, eax, 0x70
008AA55D  B9 00 01 00 00                  mov ecx, 0x100
008AA562  41 B8 43 63 50 76               mov r8d, 0x76506343
008AA568  E8 83 7B 2D 00                  call 0x140b820f0
008AA56D  49 89 44 24 10                  mov qword ptr [r12 + 0x10], rax
008AA572  48 85 C0                        test rax, rax
008AA575  0F 84 15 05 00 00               je 0x1408aaa90
008AA57B  45 39 7E 70                     cmp dword ptr [r14 + 0x70], r15d
008AA57F  76 43                           jbe 0x1408aa5c4
008AA581  8B C6                           mov eax, esi
008AA583  33 D2                           xor edx, edx
008AA585  48 6B F8 70                     imul rdi, rax, 0x70
008AA589  44 8D 42 70                     lea r8d, [rdx + 0x70]
008AA58D  49 03 7C 24 10                  add rdi, qword ptr [r12 + 0x10]
008AA592  48 8B CF                        mov rcx, rdi
008AA595  E8 A6 C6 E1 FF                  call 0x1406c6c40
008AA59A  48 89 7F 08                     mov qword ptr [rdi + 8], rdi
008AA59E  0F 57 C0                        xorps xmm0, xmm0
008AA5A1  48 89 3F                        mov qword ptr [rdi], rdi
008AA5A4  FF C6                           inc esi
008AA5A6  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
008AA5AA  0F 11 47 30                     movups xmmword ptr [rdi + 0x30], xmm0
008AA5AE  4C 09 6F 38                     or qword ptr [rdi + 0x38], r13
008AA5B2  0F 11 47 40                     movups xmmword ptr [rdi + 0x40], xmm0
008AA5B6  0F 11 47 50                     movups xmmword ptr [rdi + 0x50], xmm0
008AA5BA  4C 09 6F 58                     or qword ptr [rdi + 0x58], r13
008AA5BE  41 3B 76 70                     cmp esi, dword ptr [r14 + 0x70]
008AA5C2  72 BD                           jb 0x1408aa581
008AA5C4  0F 57 C0                        xorps xmm0, xmm0
008AA5C7  C7 45 E7 30 00 00 00            mov dword ptr [rbp - 0x19], 0x30
008AA5CE  45 33 C9                        xor r9d, r9d
008AA5D1  4C 89 7D EF                     mov qword ptr [rbp - 0x11], r15
008AA5D5  4C 8D 45 E7                     lea r8, [rbp - 0x19]
008AA5D9  C7 45 FF 00 02 00 00            mov dword ptr [rbp - 1], 0x200
008AA5E0  BA 03 00 1F 00                  mov edx, 0x1f0003
008AA5E5  4C 89 7D F7                     mov qword ptr [rbp - 9], r15
008AA5E9  48 8D 4D 87                     lea rcx, [rbp - 0x79]
008AA5ED  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
008AA5F2  F3 0F 7F 45 07                  movdqu xmmword ptr [rbp + 7], xmm0
008AA5F7  E8 44 EB 00 00                  call 0x1408b9140
008AA5FC  8B F8                           mov edi, eax
008AA5FE  85 C0                           test eax, eax
008AA600  0F 88 7A 02 00 00               js 0x1408aa880
008AA606  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
008AA60B  45 33 C0                        xor r8d, r8d
008AA60E  33 D2                           xor edx, edx
008AA610  48 8D 0D 79 6B 76 FF            lea rcx, [rip - 0x899487]
008AA617  E8 24 8D 0A 00                  call 0x140953340
008AA61C  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
008AA621  8B F8                           mov edi, eax
008AA623  85 C0                           test eax, eax
008AA625  0F 88 5A 02 00 00               js 0x1408aa885
008AA62B  41 8B FF                        mov edi, r15d
008AA62E  44 89 7C 24 58                  mov dword ptr [rsp + 0x58], r15d
008AA633  66 44 39 3E                     cmp word ptr [rsi], r15w
008AA637  0F 84 1D 01 00 00               je 0x1408aa75a
008AA63D  49 83 CF FF                     or r15, 0xffffffffffffffff
008AA641  33 C0                           xor eax, eax
008AA643  49 FF C7                        inc r15
008AA646  66 42 39 04 7E                  cmp word ptr [rsi + r15*2], ax
008AA64B  75 F6                           jne 0x1408aa643
008AA64D  45 8D 6F 01                     lea r13d, [r15 + 1]
008AA651  8B C7                           mov eax, edi
008AA653  4D 03 ED                        add r13, r13
008AA656  49 3B C5                        cmp rax, r13
008AA659  76 2D                           jbe 0x1408aa688
008AA65B  4C 8D 45 77                     lea r8, [rbp + 0x77]
008AA65F  48 8B CE                        mov rcx, rsi
008AA662  48 8D 55 67                     lea rdx, [rbp + 0x67]
008AA666  E8 61 04 00 00                  call 0x1408aaacc
008AA66B  8B 4D 67                        mov ecx, dword ptr [rbp + 0x67]
008AA66E  33 FF                           xor edi, edi
008AA670  85 C0                           test eax, eax
008AA672  0F 48 CF                        cmovs ecx, edi
008AA675  89 4D 67                        mov dword ptr [rbp + 0x67], ecx
008AA678  85 C9                           test ecx, ecx
008AA67A  75 1A                           jne 0x1408aa696
008AA67C  8B 7C 24 58                     mov edi, dword ptr [rsp + 0x58]
008AA680  49 03 F5                        add rsi, r13
008AA683  45 33 FF                        xor r15d, r15d
008AA686  EB AB                           jmp 0x1408aa633
008AA688  42 8D 04 7D 02 00 00 00         lea eax, [r15*2 + 2]
008AA690  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
008AA694  EB C5                           jmp 0x1408aa65b
008AA696  39 7D 77                        cmp dword ptr [rbp + 0x77], edi
008AA699  75 E1                           jne 0x1408aa67c
008AA69B  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
008AA6A0  48 8D 45 7F                     lea rax, [rbp + 0x7f]
008AA6A4  4C 8D 4D 8F                     lea r9, [rbp - 0x71]
008AA6A8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008AA6AD  4C 8D 45 C7                     lea r8, [rbp - 0x39]
008AA6B1  48 8B D6                        mov rdx, rsi
008AA6B4  E8 D3 2C 00 00                  call 0x1408ad38c
008AA6B9  85 C0                           test eax, eax
008AA6BB  78 BF                           js 0x1408aa67c
008AA6BD  BA 48 00 00 00                  mov edx, 0x48
008AA6C2  B9 00 01 00 00                  mov ecx, 0x100
008AA6C7  41 B8 43 63 50 76               mov r8d, 0x76506343
008AA6CD  E8 1E 7A 2D 00                  call 0x140b820f0
008AA6D2  48 8B F8                        mov rdi, rax
008AA6D5  48 85 C0                        test rax, rax
008AA6D8  0F 84 65 02 00 00               je 0x1408aa943
008AA6DE  33 D2                           xor edx, edx
008AA6E0  48 8B C8                        mov rcx, rax
008AA6E3  44 8D 42 48                     lea r8d, [rdx + 0x48]
008AA6E7  E8 54 C5 E1 FF                  call 0x1406c6c40
008AA6EC  0F 10 45 C7                     movups xmm0, xmmword ptr [rbp - 0x39]
008AA6F0  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
008AA6F3  48 BA 00 00 00 00 02 00 00 00   movabs rdx, 0x200000000
008AA6FD  0F 10 4D D7                     movups xmm1, xmmword ptr [rbp - 0x29]
008AA701  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
008AA705  0F 11 47 10                     movups xmmword ptr [rdi + 0x10], xmm0
008AA709  89 47 3C                        mov dword ptr [rdi + 0x3c], eax
008AA70C  33 C0                           xor eax, eax
008AA70E  48 89 4F 40                     mov qword ptr [rdi + 0x40], rcx
008AA712  0F 57 C0                        xorps xmm0, xmm0
008AA715  0F 11 4F 20                     movups xmmword ptr [rdi + 0x20], xmm1
008AA719  48 89 77 30                     mov qword ptr [rdi + 0x30], rsi
008AA71D  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
008AA722  44 89 7F 38                     mov dword ptr [rdi + 0x38], r15d
008AA726  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
008AA72A  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008AA72F  F3 0F 7F 45 CF                  movdqu xmmword ptr [rbp - 0x31], xmm0
008AA734  48 89 55 DF                     mov qword ptr [rbp - 0x21], rdx
008AA738  48 39 08                        cmp qword ptr [rax], rcx
008AA73B  0F 85 C9 00 00 00               jne 0x1408aa80a
008AA741  48 89 47 08                     mov qword ptr [rdi + 8], rax
008AA745  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
008AA74A  48 89 0F                        mov qword ptr [rdi], rcx
008AA74D  48 89 38                        mov qword ptr [rax], rdi
008AA750  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
008AA755  E9 22 FF FF FF                  jmp 0x1408aa67c
008AA75A  8D 47 02                        lea eax, [rdi + 2]
008AA75D  41 B8 43 63 50 76               mov r8d, 0x76506343
008AA763  8B D0                           mov edx, eax
008AA765  48 89 45 67                     mov qword ptr [rbp + 0x67], rax
008AA769  B9 00 01 00 00                  mov ecx, 0x100
008AA76E  E8 7D 79 2D 00                  call 0x140b820f0
008AA773  48 8B F0                        mov rsi, rax
008AA776  48 85 C0                        test rax, rax
008AA779  0F 84 C4 01 00 00               je 0x1408aa943
008AA77F  41 8B 56 6C                     mov edx, dword ptr [r14 + 0x6c]
008AA783  45 8B EF                        mov r13d, r15d
008AA786  49 03 D6                        add rdx, r14
008AA789  48 89 55 77                     mov qword ptr [rbp + 0x77], rdx
008AA78D  45 39 7E 70                     cmp dword ptr [r14 + 0x70], r15d
008AA791  0F 86 D6 00 00 00               jbe 0x1408aa86d
008AA797  41 8B C5                        mov eax, r13d
008AA79A  48 6B F8 70                     imul rdi, rax, 0x70
008AA79E  48 8D 0C 40                     lea rcx, [rax + rax*2]
008AA7A2  49 03 7C 24 10                  add rdi, qword ptr [r12 + 0x10]
008AA7A7  48 C1 E1 05                     shl rcx, 5
008AA7AB  48 03 CA                        add rcx, rdx
008AA7AE  8B 01                           mov eax, dword ptr [rcx]
008AA7B0  48 03 C2                        add rax, rdx
008AA7B3  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
008AA7B7  8B 41 04                        mov eax, dword ptr [rcx + 4]
008AA7BA  89 47 18                        mov dword ptr [rdi + 0x18], eax
008AA7BD  44 89 7F 68                     mov dword ptr [rdi + 0x68], r15d
008AA7C1  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
008AA7C4  48 03 C2                        add rax, rdx
008AA7C7  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
008AA7CC  48 89 47 60                     mov qword ptr [rdi + 0x60], rax
008AA7D0  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
008AA7D5  48 3B C2                        cmp rax, rdx
008AA7D8  0F 85 BC 02 00 00               jne 0x1408aaa9a
008AA7DE  48 B8 00 00 00 00 02 00 00 00   movabs rax, 0x200000000
008AA7E8  4C 89 7D A7                     mov qword ptr [rbp - 0x59], r15
008AA7EC  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
008AA7F0  0F 57 C0                        xorps xmm0, xmm0
008AA7F3  49 8D 44 24 18                  lea rax, [r12 + 0x18]
008AA7F8  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
008AA7FC  F3 0F 7F 45 AF                  movdqu xmmword ptr [rbp - 0x51], xmm0
008AA801  48 39 01                        cmp qword ptr [rcx], rax
008AA804  0F 84 26 01 00 00               je 0x1408aa930
008AA80A  B9 03 00 00 00                  mov ecx, 3
008AA80F  CD 29                           int 0x29
008AA811  48 89 0F                        mov qword ptr [rdi], rcx
008AA814  48 89 57 08                     mov qword ptr [rdi + 8], rdx
008AA818  48 89 3A                        mov qword ptr [rdx], rdi
008AA81B  48 8B 55 87                     mov rdx, qword ptr [rbp - 0x79]
008AA81F  48 89 79 08                     mov qword ptr [rcx + 8], rdi
008AA823  48 8D 4F 20                     lea rcx, [rdi + 0x20]
008AA827  E8 88 44 1C 00                  call 0x140a6ecb4
008AA82C  8B 4F 6C                        mov ecx, dword ptr [rdi + 0x6c]
008AA82F  8B D1                           mov edx, ecx
008AA831  33 D0                           xor edx, eax
008AA833  83 E2 01                        and edx, 1
008AA836  33 D1                           xor edx, ecx
008AA838  89 57 6C                        mov dword ptr [rdi + 0x6c], edx
008AA83B  A8 01                           test al, 1
008AA83D  0F 85 60 02 00 00               jne 0x1408aaaa3
008AA843  F6 C3 03                        test bl, 3
008AA846  75 14                           jne 0x1408aa85c
008AA848  48 8B 55 87                     mov rdx, qword ptr [rbp - 0x79]
008AA84C  48 8D 4F 20                     lea rcx, [rdi + 0x20]
008AA850  E8 E3 06 1C 00                  call 0x140a6af38
008AA855  85 C0                           test eax, eax
008AA857  75 03                           jne 0x1408aa85c
008AA859  83 CB 02                        or ebx, 2
008AA85C  48 8B 55 77                     mov rdx, qword ptr [rbp + 0x77]
008AA860  41 FF C5                        inc r13d
008AA863  45 3B 6E 70                     cmp r13d, dword ptr [r14 + 0x70]
008AA867  0F 82 2A FF FF FF               jb 0x1408aa797
008AA86D  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
008AA871  41 8B FF                        mov edi, r15d
008AA874  89 18                           mov dword ptr [rax], ebx
008AA876  33 D2                           xor edx, edx
008AA878  48 8B CE                        mov rcx, rsi
008AA87B  E8 F0 7F 2D 00                  call 0x140b82870
008AA880  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
008AA885  49 BD 00 00 00 00 04 00 00 00   movabs r13, 0x400000000
008AA88F  4C 85 6D DF                     test qword ptr [rbp - 0x21], r13
008AA893  0F 85 1A 02 00 00               jne 0x1408aaab3
008AA899  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
008AA89E  48 8D 44 24 40                  lea rax, [rsp + 0x40]
008AA8A3  48 3B D8                        cmp rbx, rax
008AA8A6  74 4A                           je 0x1408aa8f2
008AA8A8  48 8D 44 24 40                  lea rax, [rsp + 0x40]
008AA8AD  48 39 43 08                     cmp qword ptr [rbx + 8], rax
008AA8B1  0F 85 53 FF FF FF               jne 0x1408aa80a
008AA8B7  48 8B 03                        mov rax, qword ptr [rbx]
008AA8BA  48 39 58 08                     cmp qword ptr [rax + 8], rbx
008AA8BE  0F 85 46 FF FF FF               jne 0x1408aa80a
008AA8C4  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008AA8C9  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
008AA8CE  48 89 48 08                     mov qword ptr [rax + 8], rcx
008AA8D2  4C 85 6B 28                     test qword ptr [rbx + 0x28], r13
008AA8D6  74 0E                           je 0x1408aa8e6
008AA8D8  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
008AA8DD  48 8D 4B 10                     lea rcx, [rbx + 0x10]
008AA8E1  E8 8E F5 FF FF                  call 0x1408a9e74
008AA8E6  33 D2                           xor edx, edx
008AA8E8  48 8B CB                        mov rcx, rbx
008AA8EB  E8 80 7F 2D 00                  call 0x140b82870
008AA8F0  EB A7                           jmp 0x1408aa899
008AA8F2  48 85 F6                        test rsi, rsi
008AA8F5  74 0A                           je 0x1408aa901
008AA8F7  33 D2                           xor edx, edx
008AA8F9  48 8B CE                        mov rcx, rsi
008AA8FC  E8 6F 7F 2D 00                  call 0x140b82870
008AA901  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
008AA905  48 85 C9                        test rcx, rcx
008AA908  74 05                           je 0x1408aa90f
008AA90A  E8 61 DF FB FF                  call 0x140868870
008AA90F  33 D2                           xor edx, edx
008AA911  49 8B CE                        mov rcx, r14
008AA914  E8 D3 80 1B 00                  call 0x140a629ec
008AA919  8B C7                           mov eax, edi
008AA91B  48 81 C4 F8 00 00 00            add rsp, 0xf8
008AA922  41 5F                           pop r15
008AA924  41 5E                           pop r14
008AA926  41 5D                           pop r13
008AA928  41 5C                           pop r12
008AA92A  5F                              pop rdi
008AA92B  5E                              pop rsi
008AA92C  5B                              pop rbx
008AA92D  5D                              pop rbp
008AA92E  C3                              ret
008AA92F  CC                              int3
008AA930  48 89 07                        mov qword ptr [rdi], rax
008AA933  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
008AA937  48 89 39                        mov qword ptr [rcx], rdi
008AA93A  48 89 78 08                     mov qword ptr [rax + 8], rdi
008AA93E  E9 19 FF FF FF                  jmp 0x1408aa85c
008AA943  BF 9A 00 00 C0                  mov edi, 0xc000009a
008AA948  E9 33 FF FF FF                  jmp 0x1408aa880
008AA94D  4C 8B F8                        mov r15, rax
008AA950  8B 50 3C                        mov edx, dword ptr [rax + 0x3c]
008AA953  4C 3B 40 40                     cmp r8, qword ptr [rax + 0x40]
008AA957  0F 85 13 01 00 00               jne 0x1408aaa70
008AA95D  39 51 10                        cmp dword ptr [rcx + 0x10], edx
008AA960  0F 85 0A 01 00 00               jne 0x1408aaa70
008AA966  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
008AA96B  48 3B C1                        cmp rax, rcx
008AA96E  0F 84 37 01 00 00               je 0x1408aaaab
008AA974  4D 8B 4F 30                     mov r9, qword ptr [r15 + 0x30]
008AA978  4C 8D 05 B1 6B 25 00            lea r8, [rip + 0x256bb1]
008AA97F  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
008AA983  48 8B CE                        mov rcx, rsi
008AA986  E8 B5 51 B6 FF                  call 0x14040fb40
008AA98B  33 D2                           xor edx, edx
008AA98D  0F 57 C0                        xorps xmm0, xmm0
008AA990  41 B9 FF 7F 00 00               mov r9d, 0x7fff
008AA996  48 8B C6                        mov rax, rsi
008AA999  0F 11 45 97                     movups xmmword ptr [rbp - 0x69], xmm0
008AA99D  41 8B C9                        mov ecx, r9d
008AA9A0  44 8D 42 02                     lea r8d, [rdx + 2]
008AA9A4  66 39 10                        cmp word ptr [rax], dx
008AA9A7  74 0B                           je 0x1408aa9b4
008AA9A9  49 03 C0                        add rax, r8
008AA9AC  48 83 E9 01                     sub rcx, 1
008AA9B0  75 F2                           jne 0x1408aa9a4
008AA9B2  EB 19                           jmp 0x1408aa9cd
008AA9B4  49 8B C1                        mov rax, r9
008AA9B7  48 89 75 9F                     mov qword ptr [rbp - 0x61], rsi
008AA9BB  48 2B C1                        sub rax, rcx
008AA9BE  66 03 C0                        add ax, ax
008AA9C1  66 89 45 97                     mov word ptr [rbp - 0x69], ax
008AA9C5  66 41 03 C0                     add ax, r8w
008AA9C9  66 89 45 99                     mov word ptr [rbp - 0x67], ax
008AA9CD  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
008AA9D2  4C 8D 45 97                     lea r8, [rbp - 0x69]
008AA9D6  49 83 C7 10                     add r15, 0x10
008AA9DA  48 8D 4D A7                     lea rcx, [rbp - 0x59]
008AA9DE  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
008AA9E3  45 33 C9                        xor r9d, r9d
008AA9E6  C7 44 24 30 80 00 00 00         mov dword ptr [rsp + 0x30], 0x80
008AA9EE  C7 44 24 28 21 00 00 00         mov dword ptr [rsp + 0x28], 0x21
008AA9F6  C7 44 24 20 89 00 12 00         mov dword ptr [rsp + 0x20], 0x120089
008AA9FE  E8 D9 F4 FF FF                  call 0x1408a9edc
008AAA03  85 C0                           test eax, eax
008AAA05  0F 88 A0 00 00 00               js 0x1408aaaab
008AAA0B  41 0F 10 07                     movups xmm0, xmmword ptr [r15]
008AAA0F  48 B9 00 00 00 00 02 00 00 00   movabs rcx, 0x200000000
008AAA19  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
008AAA1D  41 0F 10 4F 10                  movups xmm1, xmmword ptr [r15 + 0x10]
008AAA22  0F 57 C0                        xorps xmm0, xmm0
008AAA25  0F 11 4F 30                     movups xmmword ptr [rdi + 0x30], xmm1
008AAA29  0F 10 4D B7                     movups xmm1, xmmword ptr [rbp - 0x49]
008AAA2D  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
008AAA31  41 0F 11 07                     movups xmmword ptr [r15], xmm0
008AAA35  41 0F 11 47 10                  movups xmmword ptr [r15 + 0x10], xmm0
008AAA3A  49 09 4F 18                     or qword ptr [r15 + 0x18], rcx
008AAA3E  45 33 FF                        xor r15d, r15d
008AAA41  0F 10 45 A7                     movups xmm0, xmmword ptr [rbp - 0x59]
008AAA45  49 8D 4C 24 28                  lea rcx, [r12 + 0x28]
008AAA4A  4C 89 7D A7                     mov qword ptr [rbp - 0x59], r15
008AAA4E  0F 11 47 40                     movups xmmword ptr [rdi + 0x40], xmm0
008AAA52  0F 11 4F 50                     movups xmmword ptr [rdi + 0x50], xmm1
008AAA56  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
008AAA5A  0F 57 C0                        xorps xmm0, xmm0
008AAA5D  F3 0F 7F 45 AF                  movdqu xmmword ptr [rbp - 0x51], xmm0
008AAA62  48 39 0A                        cmp qword ptr [rdx], rcx
008AAA65  0F 85 9F FD FF FF               jne 0x1408aa80a
008AAA6B  E9 A1 FD FF FF                  jmp 0x1408aa811
008AAA70  48 8B 00                        mov rax, qword ptr [rax]
008AAA73  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
008AAA78  48 3B C2                        cmp rax, rdx
008AAA7B  0F 85 CC FE FF FF               jne 0x1408aa94d
008AAA81  E9 E0 FE FF FF                  jmp 0x1408aa966
008AAA86  BF 0D 00 00 C0                  mov edi, 0xc000000d
008AAA8B  E9 F5 FD FF FF                  jmp 0x1408aa885
008AAA90  BF 9A 00 00 C0                  mov edi, 0xc000009a
008AAA95  E9 EB FD FF FF                  jmp 0x1408aa885
008AAA9A  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
008AAA9E  E9 AA FE FF FF                  jmp 0x1408aa94d
008AAAA3  83 CB 01                        or ebx, 1
008AAAA6  E9 B1 FD FF FF                  jmp 0x1408aa85c
008AAAAB  45 33 FF                        xor r15d, r15d
008AAAAE  E9 2B FD FF FF                  jmp 0x1408aa7de
008AAAB3  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
008AAAB8  48 8D 4D C7                     lea rcx, [rbp - 0x39]
008AAABC  E8 B3 F3 FF FF                  call 0x1408a9e74
008AAAC1  E9 D3 FD FF FF                  jmp 0x1408aa899
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfSnOpenVolumesForPrefetch(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m118;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int16 v_stack_mC6;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p8;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (248);
    v_r15 = 0;
    v_stack_mF0 = v_stack_mF8;
    v_stack_m74 = 0;
    v_stack_m5C = 0;
    v_stack_mF8 = v_stack_mF8;
    v_stack_mD0 = 0;
    v_stack_p20 = 0;
    v_stack_p8 = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_p18 = 0;
    v_stack_mE8 = 0;
    v_stack_m98 = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_r13;
    v_stack_mB8 = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_r13;
    v_stack_mD8 = 0;
    result = PfSnLogOpenVolumesForPrefetch(*(unsigned __int64 *)(a1), 1, a3, a4);
    if (*(unsigned __int64 *)(a1) == 0) goto loc_008AAA86;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 112)))) >= 0x4000ULL) goto loc_008AAA86;
    a2 = (unsigned int)((1) * ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 112)))));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x76506343ULL), a4);
    *(unsigned __int64 *)(a1 + 16) = result;
    if (result == 0) goto loc_008AAA90;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 112)) <= 0) goto loc_008AA5C4;
loc_008AA581:
    a2 = 0;
    v_rdi = (v_rdi) * (0);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a1 + 16));
    result = memset(v_rdi, a2, a2 + 112, a4);
    *(unsigned __int64 *)(v_rdi + 8) = v_rdi;
    *(unsigned __int64 *)(v_rdi) = v_rdi;
    v_rsi = (unsigned int)((0) + 1);
    *(unsigned __int64 *)(v_rdi + 32) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 48) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 64) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 80) = v_xmm0;
    if (((unsigned int)(v_rsi)) < (*(unsigned int *)(*(unsigned __int64 *)(a1) + 112))) goto loc_008AA581;
loc_008AA5C4:
    v_stack_m78 = 48;
    a4 = 0;
    v_stack_m70 = 0;
    v_stack_m60 = 512;
    v_stack_m68 = 0;
    v_stack_m118 = 0;
    v_stack_m58 = v_xmm0;
    result = NtCreateEvent(v_stack_mD8, (unsigned int)(0x1F0003ULL), v_stack_m78, a4);
    if (sign_flag) goto loc_008AA880;
    a3 = 0;
    a2 = 0;
    result = IoGetDeviceInterfaces(v_rip - 9016455, a2, a3, v_stack_mE8);
    if (sign_flag) goto loc_008AA885;
    v_stack_mE0 = 0;
loc_008AA633:
    if ((*(unsigned __int16 *)(v_stack_mE8)) == 0) goto loc_008AA75A;
    v_r15 = (v_r15) | (-1);
    result = 0;
loc_008AA643:
    v_r15 = (v_r15) + 1;
    if ((*(unsigned __int16 *)(v_stack_mE8 + v_r15 * 2)) != 0) goto loc_008AA643;
    v_r13 = (v_r15 + 1) + (v_r15 + 1);
    if (0 <= v_r13) goto loc_008AA688;
loc_008AA65B:
    result = PfSnIsVolumeMounted(v_stack_mE8, v_stack_p8, v_stack_p18, v_stack_mE8);
    v_rdi = 0;
    a1 = (unsigned int)(v_stack_p8);
    if (sign_flag) { a1 = 0; }
    v_stack_p8 = (unsigned int)(a1);
    if ((unsigned int)(a1) != 0) goto loc_008AA696;
loc_008AA67C:
    v_rsi = (v_stack_mE8) + (v_r13);
    v_r15 = 0;
    goto loc_008AA633;
loc_008AA688:
    v_stack_mE0 = (unsigned int)(v_r15 * 2 + 2);
    goto loc_008AA65B;
loc_008AA696:
    if (v_stack_p18 != ((unsigned int)((unsigned int)(v_stack_mE0)))) goto loc_008AA67C;
    v_stack_m118 = v_stack_p20;
    result = PfSnQueryVolumeInfo(*(unsigned __int64 *)(a1 + 8), v_rsi, v_stack_m98, v_stack_mD0);
    if (sign_flag) goto loc_008AA67C;
    result = ExAllocatePool2(256, 72, (unsigned int)(0x76506343ULL), v_stack_mD0);
    if (result == 0) goto loc_008AA943;
    a2 = 0;
    result = memset(result, a2, a2 + 72, v_stack_mD0);
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned int *)(result + 60) = (unsigned int)((unsigned int)(v_stack_p20));
    result = 0;
    *(unsigned __int64 *)(result + 64) = v_stack_mD0;
    *(unsigned __int64 *)(result + 32) = v_xmm1;
    *(unsigned __int64 *)(result + 48) = v_rsi;
    *(unsigned int *)(result + 56) = 0;
    v_stack_m98 = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = 0;
    if ((*(unsigned __int64 *)(v_stack_mF0)) != v_stack_mF8) goto loc_008AA80A;
    *(unsigned __int64 *)(result + 8) = v_stack_mF0;
    *(unsigned __int64 *)(result) = v_stack_mF8;
    *(unsigned __int64 *)(v_stack_mF0) = 0;
    v_stack_mF0 = 0;
    goto loc_008AA67C;
loc_008AA75A:
    v_stack_p8 = result + 2;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result + 2)), (unsigned int)(0x76506343ULL), v_stack_mD0);
    if (result == 0) goto loc_008AA943;
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 108))) + (*(unsigned __int64 *)(a1));
    v_stack_p18 = a2;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 112)) <= 0) goto loc_008AA86D;
loc_008AA797:
    v_rdi = (result) * (0);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a1 + 16));
    a1 = (0 + 0 * 2) << (5);
    a1 = (a1) + (a2);
    result = ((unsigned int)(*(unsigned int *)(a1))) + (a2);
    *(unsigned __int64 *)(v_rdi + 16) = result;
    *(unsigned int *)(v_rdi + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    *(unsigned int *)(v_rdi + 104) = 0;
    result = ((unsigned int)(*(unsigned int *)(a1 + 28))) + (a2);
    *(unsigned __int64 *)(v_rdi + 96) = result;
    if (v_stack_mF8 != v_stack_mF8) goto loc_008AAA9A;
loc_008AA7DE:
    v_stack_mB8 = 0;
    v_stack_mA0 = v_stack_mF8;
    v_stack_mB0 = v_xmm0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24 + 8))) == (a1 + 24)) goto loc_008AA930;
loc_008AA80A:
loc_008AA811:
    *(unsigned __int64 *)(v_rdi) = 3;
    *(unsigned __int64 *)(v_rdi + 8) = v_stack_mF8;
    *(unsigned __int64 *)(v_stack_mF8) = v_rdi;
    *(unsigned __int64 *)(3 + 8) = v_rdi;
    result = PfSnVolumeCheckSeekPenalty(v_rdi + 32, v_stack_mD8, (unsigned int)(0x76506343ULL), v_stack_mD0);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 108))))) ^ ((unsigned int)(result)));
    a2 = (unsigned int)((a2) & (1));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 108)))));
    *(unsigned int *)(v_rdi + 108) = (unsigned int)(a2);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_008AAAA3;
    if (((0) & (3)) != 0) goto loc_008AA85C;
    result = PfSnVolumeCheckIsSdBus(v_rdi + 32, v_stack_mD8, (unsigned int)(0x76506343ULL), v_stack_mD0);
    v_rbx = 0;
    if ((unsigned int)(result) == 0) {
        v_rbx = (unsigned int)((0) | (2));
    }
    v_r13 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r13)) < (*(unsigned int *)(*(unsigned __int64 *)(a1) + 112))) goto loc_008AA797;
loc_008AA86D:
    *(unsigned int *)(v_stack_p10) = (unsigned int)(v_rbx);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x76506343ULL), v_stack_mD0);
loc_008AA880:
loc_008AA885:
    if (((v_stack_m80) & (v_r13)) != 0) goto loc_008AAAB3;
loc_008AA899:
    if (v_stack_mF8 == v_stack_mF8) goto loc_008AA8F2;
    if ((*(unsigned __int64 *)(v_stack_mF8 + 8)) != v_stack_mF8) goto loc_008AA80A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF8) + 8)) != v_stack_mF8) goto loc_008AA80A;
    v_stack_mF8 = *(unsigned __int64 *)(v_stack_mF8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF8) + 8) = v_stack_mF8;
    result = *(unsigned __int64 *)(v_stack_mF8);
    if (((*(unsigned __int64 *)(v_stack_mF8 + 40)) & (v_r13)) != 0) {
        a2 = *(unsigned __int64 *)(a1 + 8);
        a1 = v_stack_mF8 + 16;
        result = PfpOpenHandleClose(a1, a2, (unsigned int)(0x76506343ULL), v_stack_mD0);
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mF8, a2, (unsigned int)(0x76506343ULL), v_stack_mD0);
    goto loc_008AA899;
loc_008AA8F2:
    if (v_stack_mE8 != 0) {
        a2 = 0;
        a1 = v_stack_mE8;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x76506343ULL), v_stack_mD0);
    }
    if (v_stack_mD8 != 0) {
        result = NtClose(v_stack_mD8, a2, (unsigned int)(0x76506343ULL), v_stack_mD0);
    }
    a2 = 0;
    result = PfSnLogOpenVolumesForPrefetch(*(unsigned __int64 *)(a1), a2, (unsigned int)(0x76506343ULL), v_stack_mD0);
    v_rsp = (v_rsp) + (248);
    return 0;
loc_008AA930:
    *(unsigned __int64 *)(0) = 0;
    *(unsigned __int64 *)(0 + 8) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1)) = 0;
    *(unsigned __int64 *)(0 + 8) = 0;
    goto loc_008AA85C;
loc_008AA943:
    goto loc_008AA880;
loc_008AA94D:
    if (((unsigned int)(0x76506343ULL)) != (*(unsigned __int64 *)(0 + 64))) goto loc_008AAA70;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 60))))) goto loc_008AAA70;
loc_008AA966:
    if (0 == v_stack_p40) goto loc_008AAAAB;
    result = RtlStringCbPrintfW(v_stack_mE8, v_stack_p8, v_rip + 2452401, *(unsigned __int64 *)(0 + 48));
    a2 = 0;
    v_stack_mC8 = v_xmm0;
loc_008AA9A4:
    if ((*(unsigned __int16 *)(v_stack_mE8)) == 0) goto loc_008AA9B4;
    result = (v_stack_mE8) + (a2 + 2);
    a1 = ((unsigned int)((unsigned int)((unsigned int)(0x7FFFULL)))) - (1);
    if (condition_is_not_equal) goto loc_008AA9A4;
    goto loc_008AA9CD;
loc_008AA9B4:
    v_stack_mC0 = v_stack_mE8;
    result = ((unsigned int)(0x7FFFULL)) - (a1);
    result = (unsigned __int16)((result) + ((unsigned __int16)(result)));
    v_stack_mC8 = (unsigned __int16)(result);
    result = (unsigned __int16)((result) + ((unsigned __int16)(a2 + 2)));
    v_stack_mC6 = (unsigned __int16)(result);
loc_008AA9CD:
    v_r15 = (0) + (16);
    v_stack_p38 = v_r15;
    a4 = 0;
    v_stack_p30 = 128;
    v_stack_p28 = 33;
    v_stack_p20 = 0x120089ULL;
    result = PfpOpenHandleCreate(v_stack_mB8, *(unsigned __int64 *)(a1 + 8), v_stack_mC8, a4);
    if (sign_flag) goto loc_008AAAAB;
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 32) = v_xmm0;
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 48) = v_xmm1;
    v_stack_mA0 = v_stack_mB8;
    *(unsigned __int64 *)(v_r15) = v_xmm0;
    *(unsigned __int64 *)(v_r15 + 16) = v_xmm0;
    v_r15 = 0;
    v_stack_mB8 = 0;
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 64) = v_xmm0;
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 80) = v_xmm1;
    v_stack_mB0 = v_xmm0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40 + 8))) != (a1 + 40)) goto loc_008AA80A;
    goto loc_008AA811;
loc_008AAA70:
    if ((*(unsigned __int64 *)(result)) != v_stack_p40) goto loc_008AA94D;
    goto loc_008AA966;
loc_008AAA86:
    goto loc_008AA885;
loc_008AAA90:
    goto loc_008AA885;
loc_008AAA9A:
    goto loc_008AA94D;
loc_008AAAA3:
    v_rbx = (unsigned int)((v_stack_mF8) | (1));
    goto loc_008AA85C;
loc_008AAAAB:
    v_r15 = 0;
    goto loc_008AA7DE;
loc_008AAAB3:
    result = PfpOpenHandleClose(v_stack_m98, *(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1 + 40 + 8), a4);
    goto loc_008AA899;
}
```

## 5. (Beta) C Style

```c
int64_t PfSnOpenVolumesForPrefetch(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m118;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint16_t v_stack_mC6;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p8;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (248);
    local_r15 = 0;
    v_stack_mF0 = v_stack_mF8;
    v_stack_m74 = 0;
    v_stack_m5C = 0;
    v_stack_mF8 = v_stack_mF8;
    v_stack_mD0 = 0;
    v_stack_p20 = 0;
    v_stack_p8 = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_p18 = 0;
    v_stack_mE8 = 0;
    v_stack_m98 = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = local_r13;
    v_stack_mB8 = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = local_r13;
    v_stack_mD8 = 0;
    result = PfSnLogOpenVolumesForPrefetch(*(uint64_t *)(arg1), 1, Arg3, Arg4);
    if (*(uint64_t *)(arg1) == 0) goto loc_008AAA86;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x70)))) >= 0x4000ULL) goto loc_008AAA86;
    Arg2 = (uint32_t)((1) * ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x70)))));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x76506343ULL), Arg4);
    *(uint64_t *)(arg1 + 0x10) = result;
    if (result == 0) goto loc_008AAA90;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x70)) <= 0) goto loc_008AA5C4;
loc_008AA581:
    Arg2 = 0;
    local_rdi = (local_rdi) * (0);
    local_rdi = (local_rdi) + (*(uint64_t *)(arg1 + 0x10));
    result = memset(local_rdi, Arg2, Arg2 + 112, Arg4);
    *(uint64_t *)(local_rdi + 0x8) = local_rdi;
    *(uint64_t *)(local_rdi) = local_rdi;
    local_rsi = (uint32_t)((0) + 1);
    *(uint64_t *)(local_rdi + 0x20) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x30) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x40) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x50) = v_xmm0;
    if (((uint32_t)(local_rsi)) < (*(uint32_t *)(*(uint64_t *)(arg1) + 0x70))) goto loc_008AA581;
loc_008AA5C4:
    v_stack_m78 = 48;
    Arg4 = 0;
    v_stack_m70 = 0;
    v_stack_m60 = 512;
    v_stack_m68 = 0;
    v_stack_m118 = 0;
    v_stack_m58 = v_xmm0;
    result = NtCreateEvent(v_stack_mD8, (uint32_t)(0x1F0003ULL), v_stack_m78, Arg4);
    if (sign_flag) goto loc_008AA880;
    Arg3 = 0;
    Arg2 = 0;
    result = IoGetDeviceInterfaces(v_rip - 9016455, Arg2, Arg3, v_stack_mE8);
    if (sign_flag) goto loc_008AA885;
    v_stack_mE0 = 0;
loc_008AA633:
    if ((*(uint16_t *)(v_stack_mE8)) == 0) goto loc_008AA75A;
    local_r15 = (local_r15) | (-1);
    result = 0;
loc_008AA643:
    local_r15 = (local_r15) + 1;
    if ((*(uint16_t *)(v_stack_mE8 + local_r15 * 2)) != 0) goto loc_008AA643;
    local_r13 = (local_r15 + 1) + (local_r15 + 1);
    if (0 <= local_r13) goto loc_008AA688;
loc_008AA65B:
    result = PfSnIsVolumeMounted(v_stack_mE8, v_stack_p8, v_stack_p18, v_stack_mE8);
    local_rdi = 0;
    Arg1 = (uint32_t)(v_stack_p8);
    if (sign_flag) { Arg1 = 0; }
    v_stack_p8 = (uint32_t)(Arg1);
    if ((uint32_t)(Arg1) != 0) goto loc_008AA696;
loc_008AA67C:
    local_rsi = (v_stack_mE8) + (local_r13);
    local_r15 = 0;
    goto loc_008AA633;
loc_008AA688:
    v_stack_mE0 = (uint32_t)(local_r15 * 2 + 2);
    goto loc_008AA65B;
loc_008AA696:
    if (v_stack_p18 != ((uint32_t)((uint32_t)(v_stack_mE0)))) goto loc_008AA67C;
    v_stack_m118 = v_stack_p20;
    result = PfSnQueryVolumeInfo(*(uint64_t *)(arg1 + 0x8), local_rsi, v_stack_m98, v_stack_mD0);
    if (sign_flag) goto loc_008AA67C;
    result = ExAllocatePool2(256, 72, (uint32_t)(0x76506343ULL), v_stack_mD0);
    if (result == 0) goto loc_008AA943;
    Arg2 = 0;
    result = memset(result, Arg2, Arg2 + 72, v_stack_mD0);
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint32_t *)(result + 0x3C) = (uint32_t)((uint32_t)(v_stack_p20));
    result = 0;
    *(uint64_t *)(result + 0x40) = v_stack_mD0;
    *(uint64_t *)(result + 0x20) = v_xmm1;
    *(uint64_t *)(result + 0x30) = local_rsi;
    *(uint32_t *)(result + 0x38) = 0;
    v_stack_m98 = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = 0;
    if ((*(uint64_t *)(v_stack_mF0)) != v_stack_mF8) goto loc_008AA80A;
    *(uint64_t *)(result + 0x8) = v_stack_mF0;
    *(uint64_t *)(result) = v_stack_mF8;
    *(uint64_t *)(v_stack_mF0) = 0;
    v_stack_mF0 = 0;
    goto loc_008AA67C;
loc_008AA75A:
    v_stack_p8 = result + 2;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result + 2)), (uint32_t)(0x76506343ULL), v_stack_mD0);
    if (result == 0) goto loc_008AA943;
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x6C))) + (*(uint64_t *)(arg1));
    v_stack_p18 = Arg2;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x70)) <= 0) goto loc_008AA86D;
loc_008AA797:
    local_rdi = (result) * (0);
    local_rdi = (local_rdi) + (*(uint64_t *)(arg1 + 0x10));
    Arg1 = (0 + 0 * 2) << (5);
    Arg1 = (Arg1) + (Arg2);
    result = ((uint32_t)(*(uint32_t *)(arg1))) + (Arg2);
    *(uint64_t *)(local_rdi + 0x10) = result;
    *(uint32_t *)(local_rdi + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    *(uint32_t *)(local_rdi + 0x68) = 0;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x1C))) + (Arg2);
    *(uint64_t *)(local_rdi + 0x60) = result;
    if (v_stack_mF8 != v_stack_mF8) goto loc_008AAA9A;
loc_008AA7DE:
    v_stack_mB8 = 0;
    v_stack_mA0 = v_stack_mF8;
    v_stack_mB0 = v_xmm0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18 + 0x8))) == (Arg1 + 24)) goto loc_008AA930;
loc_008AA80A:
loc_008AA811:
    *(uint64_t *)(local_rdi) = 3;
    *(uint64_t *)(local_rdi + 0x8) = v_stack_mF8;
    *(uint64_t *)(v_stack_mF8) = local_rdi;
    *(uint64_t *)(3 + 0x8) = local_rdi;
    result = PfSnVolumeCheckSeekPenalty(local_rdi + 32, v_stack_mD8, (uint32_t)(0x76506343ULL), v_stack_mD0);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x6C))))) ^ ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) & (1));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x6C)))));
    *(uint32_t *)(local_rdi + 0x6C) = (uint32_t)(Arg2);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_008AAAA3;
    if (((0) & (3)) != 0) goto loc_008AA85C;
    result = PfSnVolumeCheckIsSdBus(local_rdi + 32, v_stack_mD8, (uint32_t)(0x76506343ULL), v_stack_mD0);
    local_rbx = 0;
    if ((uint32_t)(result) == 0) {
        local_rbx = (uint32_t)((0) | (2));
    }
    local_r13 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r13)) < (*(uint32_t *)(*(uint64_t *)(arg1) + 0x70))) goto loc_008AA797;
loc_008AA86D:
    *(uint32_t *)(v_stack_p10) = (uint32_t)(local_rbx);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x76506343ULL), v_stack_mD0);
loc_008AA880:
loc_008AA885:
    if (((v_stack_m80) & (local_r13)) != 0) goto loc_008AAAB3;
loc_008AA899:
    if (v_stack_mF8 == v_stack_mF8) goto loc_008AA8F2;
    if ((*(uint64_t *)(v_stack_mF8 + 0x8)) != v_stack_mF8) goto loc_008AA80A;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mF8) + 0x8)) != v_stack_mF8) goto loc_008AA80A;
    v_stack_mF8 = *(uint64_t *)(v_stack_mF8);
    *(uint64_t *)(*(uint64_t *)(v_stack_mF8) + 0x8) = v_stack_mF8;
    result = *(uint64_t *)(v_stack_mF8);
    if (((*(uint64_t *)(v_stack_mF8 + 0x28)) & (local_r13)) != 0) {
        Arg2 = *(uint64_t *)(arg1 + 0x8);
        Arg1 = v_stack_mF8 + 16;
        result = PfpOpenHandleClose(Arg1, Arg2, (uint32_t)(0x76506343ULL), v_stack_mD0);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mF8, Arg2, (uint32_t)(0x76506343ULL), v_stack_mD0);
    goto loc_008AA899;
loc_008AA8F2:
    if (v_stack_mE8 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mE8;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x76506343ULL), v_stack_mD0);
    }
    if (v_stack_mD8 != 0) {
        result = NtClose(v_stack_mD8, Arg2, (uint32_t)(0x76506343ULL), v_stack_mD0);
    }
    Arg2 = 0;
    result = PfSnLogOpenVolumesForPrefetch(*(uint64_t *)(arg1), Arg2, (uint32_t)(0x76506343ULL), v_stack_mD0);
    local_rsp = (local_rsp) + (248);
    return 0;
loc_008AA930:
    *(uint64_t *)(0) = 0;
    *(uint64_t *)(0 + 0x8) = *(uint64_t *)(arg1);
    *(uint64_t *)(*(uint64_t *)(arg1)) = 0;
    *(uint64_t *)(0 + 0x8) = 0;
    goto loc_008AA85C;
loc_008AA943:
    goto loc_008AA880;
loc_008AA94D:
    if (((uint32_t)(0x76506343ULL)) != (*(uint64_t *)(0 + 0x40))) goto loc_008AAA70;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x3C))))) goto loc_008AAA70;
loc_008AA966:
    if (0 == v_stack_p40) goto loc_008AAAAB;
    result = RtlStringCbPrintfW(v_stack_mE8, v_stack_p8, v_rip + 2452401, *(uint64_t *)(0 + 0x30));
    Arg2 = 0;
    v_stack_mC8 = v_xmm0;
loc_008AA9A4:
    if ((*(uint16_t *)(v_stack_mE8)) == 0) goto loc_008AA9B4;
    result = (v_stack_mE8) + (Arg2 + 2);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(0x7FFFULL)))) - (1);
    if (condition_is_not_equal) goto loc_008AA9A4;
    goto loc_008AA9CD;
loc_008AA9B4:
    v_stack_mC0 = v_stack_mE8;
    result = ((uint32_t)(0x7FFFULL)) - (Arg1);
    result = (uint16_t)((result) + ((uint16_t)(result)));
    v_stack_mC8 = (uint16_t)(result);
    result = (uint16_t)((result) + ((uint16_t)(Arg2 + 2)));
    v_stack_mC6 = (uint16_t)(result);
loc_008AA9CD:
    local_r15 = (0) + (16);
    v_stack_p38 = local_r15;
    Arg4 = 0;
    v_stack_p30 = 128;
    v_stack_p28 = 33;
    v_stack_p20 = 0x120089ULL;
    result = PfpOpenHandleCreate(v_stack_mB8, *(uint64_t *)(arg1 + 0x8), v_stack_mC8, Arg4);
    if (sign_flag) goto loc_008AAAAB;
    *(uint64_t *)((uint32_t)(0xC000009AULL) + 0x20) = v_xmm0;
    *(uint64_t *)((uint32_t)(0xC000009AULL) + 0x30) = v_xmm1;
    v_stack_mA0 = v_stack_mB8;
    *(uint64_t *)(local_r15) = v_xmm0;
    *(uint64_t *)(local_r15 + 0x10) = v_xmm0;
    local_r15 = 0;
    v_stack_mB8 = 0;
    *(uint64_t *)((uint32_t)(0xC000009AULL) + 0x40) = v_xmm0;
    *(uint64_t *)((uint32_t)(0xC000009AULL) + 0x50) = v_xmm1;
    v_stack_mB0 = v_xmm0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x28 + 0x8))) != (Arg1 + 40)) goto loc_008AA80A;
    goto loc_008AA811;
loc_008AAA70:
    if ((*(uint64_t *)(result)) != v_stack_p40) goto loc_008AA94D;
    goto loc_008AA966;
loc_008AAA86:
    goto loc_008AA885;
loc_008AAA90:
    goto loc_008AA885;
loc_008AAA9A:
    goto loc_008AA94D;
loc_008AAAA3:
    local_rbx = (uint32_t)((v_stack_mF8) | (1));
    goto loc_008AA85C;
loc_008AAAAB:
    local_r15 = 0;
    goto loc_008AA7DE;
loc_008AAAB3:
    result = PfpOpenHandleClose(v_stack_m98, *(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1 + 0x28 + 0x8), Arg4);
    goto loc_008AA899;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008AA4AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
