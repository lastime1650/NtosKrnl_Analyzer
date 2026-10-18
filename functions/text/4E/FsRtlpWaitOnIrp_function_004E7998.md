# FsRtlpWaitOnIrp

- RVA: `0x004E7998`–`0x004E7F8A` (길이 `1,522` bytes)
- VA: `0x00000001404E7998`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5EB0`
- 디코드: `329`개 명령, `1,522/1,522` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x004E7A9E` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E7AD0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004E7B76` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004E7BAD` → [Feature_3609177402__private_IsEnabledDeviceUsageNoInline](../58/Feature_3609177402__private_IsEnabledDeviceUsageNoInline_function_00581D30.md) (function, `0x00581D30`)
- `0x004E7BC4` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x004E7BD2` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x004E7C09` → [FsRtlpCancelWaitingIrp](FsRtlpCancelWaitingIrp_function_004E4698.md) (function, `0x004E4698`)
- `0x004E7C24` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x004E7C85` → [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x004E7CAA` → [FsRtlCancellableWaitForSingleObject](../../page/A1/FsRtlCancellableWaitForSingleObject_function_00A1D890.md) (function, `0x00A1D890`)
- `0x004E7D0E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004E7D3F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004E7D72` → [IoCancelIrp](../27/IoCancelIrp_function_002720E0.md) (function, `0x002720E0`)
- `0x004E7D80` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x004E7D9B` → [FsRtlpRemoveAndCompleteWaitingIrp](../42/FsRtlpRemoveAndCompleteWaitingIrp_function_00425FC0.md) (function, `0x00425FC0`)
- `0x004E7DA7` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x004E7DC4` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x004E7EB9` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E7EC5` → [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x004E7F5F` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E7F71` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [FsRtlpOplockBreakToII](../4B/FsRtlpOplockBreakToII_function_004BB824.md) at `0x004BBA70`
- [FsRtlpOplockBreakByCacheFlags](FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E6D9E`
- [FsRtlpOplockBreakToNone](../4F/FsRtlpOplockBreakToNone_function_004F8354.md) at `0x004F8605`
- [FsRtlpOplockBreakNotify](../../page/71/FsRtlpOplockBreakNotify_function_00714E10.md) at `0x00714F2F`

### Static image references
- `0x004E79AD` → RVA `0x00E0A740` (`.data`; read)
- `0x004E7A1D` → RVA `0x00E06C50` (`.data`; read)
- `0x004E7A90` → RVA `0x00044A8D` (`.rdata`; read)
- `0x004E7B37` → RVA `0x00715960` (`FsRtlpOplockWaitCompleteRoutine`; read)
- `0x004E7C13` → RVA `0x00582B10` (`FsRtlpWaitingIrpCancelRoutine`; read)
- `0x004E7EAB` → RVA `0x000443F2` (`.rdata`; read)
- `0x004E7F51` → RVA `0x00044451` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x004E7AD0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004E7CAA` → [FsRtlCancellableWaitForSingleObject](../../page/A1/FsRtlCancellableWaitForSingleObject_function_00A1D890.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004E7998  4C 8B DC                        mov r11, rsp
004E799B  53                              push rbx
004E799C  56                              push rsi
004E799D  57                              push rdi
004E799E  41 54                           push r12
004E79A0  41 55                           push r13
004E79A2  41 56                           push r14
004E79A4  41 57                           push r15
004E79A6  48 81 EC E0 01 00 00            sub rsp, 0x1e0
004E79AD  48 8B 05 8C 2D 92 00            mov rax, qword ptr [rip + 0x922d8c]
004E79B4  48 33 C4                        xor rax, rsp
004E79B7  48 89 84 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rax
004E79BF  4D 8B F9                        mov r15, r9
004E79C2  4C 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r8
004E79CA  48 8B FA                        mov rdi, rdx
004E79CD  4C 8B F1                        mov r14, rcx
004E79D0  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
004E79D5  4C 8B A4 24 40 02 00 00         mov r12, qword ptr [rsp + 0x240]
004E79DD  48 8B 84 24 48 02 00 00         mov rax, qword ptr [rsp + 0x248]
004E79E5  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
004E79EA  48 8B 84 24 60 02 00 00         mov rax, qword ptr [rsp + 0x260]
004E79F2  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
004E79FA  48 8B 84 24 68 02 00 00         mov rax, qword ptr [rsp + 0x268]
004E7A02  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004E7A07  48 8B 9C 24 70 02 00 00         mov rbx, qword ptr [rsp + 0x270]
004E7A0F  C7 44 24 34 9A 00 00 C0         mov dword ptr [rsp + 0x34], 0xc000009a
004E7A17  33 C9                           xor ecx, ecx
004E7A19  88 4C 24 33                     mov byte ptr [rsp + 0x33], cl
004E7A1D  83 3D 2C F2 91 00 05            cmp dword ptr [rip + 0x91f22c], 5
004E7A24  76 7F                           jbe 0x1404e7aa5
004E7A26  49 89 93 90 FE FF FF            mov qword ptr [r11 - 0x170], rdx
004E7A2D  49 8D 83 90 FE FF FF            lea rax, [r11 - 0x170]
004E7A34  49 89 43 88                     mov qword ptr [r11 - 0x78], rax
004E7A38  49 C7 43 90 08 00 00 00         mov qword ptr [r11 - 0x70], 8
004E7A40  4D 89 B3 98 FE FF FF            mov qword ptr [r11 - 0x168], r14
004E7A47  49 8D 83 98 FE FF FF            lea rax, [r11 - 0x168]
004E7A4E  49 89 43 98                     mov qword ptr [r11 - 0x68], rax
004E7A52  49 C7 43 A0 08 00 00 00         mov qword ptr [r11 - 0x60], 8
004E7A5A  41 8B 86 90 00 00 00            mov eax, dword ptr [r14 + 0x90]
004E7A61  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
004E7A65  48 8D 44 24 50                  lea rax, [rsp + 0x50]
004E7A6A  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
004E7A6E  49 C7 43 B0 04 00 00 00         mov qword ptr [r11 - 0x50], 4
004E7A76  49 8D 83 68 FF FF FF            lea rax, [r11 - 0x98]
004E7A7D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E7A82  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
004E7A8A  45 33 C9                        xor r9d, r9d
004E7A8D  45 33 C0                        xor r8d, r8d
004E7A90  48 8D 15 F6 CF B5 FF            lea rdx, [rip - 0x4a300a]
004E7A97  48 8D 0D B2 F1 91 00            lea rcx, [rip + 0x91f1b2]
004E7A9E  E8 3D E6 F3 FF                  call 0x1404260e0
004E7AA3  33 C9                           xor ecx, ecx
004E7AA5  41 B5 01                        mov r13b, 1
004E7AA8  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
004E7AAD  48 8D 44 24 33                  lea rax, [rsp + 0x33]
004E7AB2  48 85 DB                        test rbx, rbx
004E7AB5  48 0F 45 C3                     cmovne rax, rbx
004E7AB9  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004E7ABE  88 08                           mov byte ptr [rax], cl
004E7AC0  BA 40 00 00 00                  mov edx, 0x40
004E7AC5  B9 20 01 00 00                  mov ecx, 0x120
004E7ACA  41 B8 46 53 72 6F               mov r8d, 0x6f725346
004E7AD0  E8 1B A6 69 00                  call 0x140b820f0
004E7AD5  48 8B F0                        mov rsi, rax
004E7AD8  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
004E7AE0  33 D2                           xor edx, edx
004E7AE2  48 85 FF                        test rdi, rdi
004E7AE5  74 2F                           je 0x1404e7b16
004E7AE7  48 8B 8F B8 00 00 00            mov rcx, qword ptr [rdi + 0xb8]
004E7AEE  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
004E7AF2  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
004E7AF5  89 46 30                        mov dword ptr [rsi + 0x30], eax
004E7AF8  80 39 0D                        cmp byte ptr [rcx], 0xd
004E7AFB  75 0C                           jne 0x1404e7b09
004E7AFD  81 79 18 14 00 09 00            cmp dword ptr [rcx + 0x18], 0x90014
004E7B04  41 8A C5                        mov al, r13b
004E7B07  74 02                           je 0x1404e7b0b
004E7B09  8A C2                           mov al, dl
004E7B0B  88 46 35                        mov byte ptr [rsi + 0x35], al
004E7B0E  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
004E7B12  48 89 46 38                     mov qword ptr [rsi + 0x38], rax
004E7B16  8A 84 24 50 02 00 00            mov al, byte ptr [rsp + 0x250]
004E7B1D  88 46 34                        mov byte ptr [rsi + 0x34], al
004E7B20  4D 85 FF                        test r15, r15
004E7B23  74 12                           je 0x1404e7b37
004E7B25  4C 89 7E 18                     mov qword ptr [rsi + 0x18], r15
004E7B29  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
004E7B31  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
004E7B35  EB 31                           jmp 0x1404e7b68
004E7B37  48 8D 05 22 DE 22 00            lea rax, [rip + 0x22de22]
004E7B3E  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
004E7B42  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
004E7B47  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
004E7B4B  66 89 10                        mov word ptr [rax], dx
004E7B4E  C6 40 02 06                     mov byte ptr [rax + 2], 6
004E7B52  89 50 04                        mov dword ptr [rax + 4], edx
004E7B55  48 8D 48 08                     lea rcx, [rax + 8]
004E7B59  48 89 49 08                     mov qword ptr [rcx + 8], rcx
004E7B5D  48 89 09                        mov qword ptr [rcx], rcx
004E7B60  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
004E7B68  4D 85 E4                        test r12, r12
004E7B6B  74 10                           je 0x1404e7b7d
004E7B6D  48 8B D7                        mov rdx, rdi
004E7B70  48 8B C8                        mov rcx, rax
004E7B73  49 8B C4                        mov rax, r12
004E7B76  E8 55 2F 1D 00                  call 0x1406baad0
004E7B7B  33 D2                           xor edx, edx
004E7B7D  4D 8D 66 58                     lea r12, [r14 + 0x58]
004E7B81  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
004E7B86  4C 39 20                        cmp qword ptr [rax], r12
004E7B89  74 07                           je 0x1404e7b92
004E7B8B  B9 03 00 00 00                  mov ecx, 3
004E7B90  CD 29                           int 0x29
004E7B92  4C 89 26                        mov qword ptr [rsi], r12
004E7B95  48 89 46 08                     mov qword ptr [rsi + 8], rax
004E7B99  48 89 30                        mov qword ptr [rax], rsi
004E7B9C  49 89 74 24 08                  mov qword ptr [r12 + 8], rsi
004E7BA1  48 85 FF                        test rdi, rdi
004E7BA4  0F 84 8E 00 00 00               je 0x1404e7c38
004E7BAA  89 57 30                        mov dword ptr [rdi + 0x30], edx
004E7BAD  E8 7E A1 09 00                  call 0x140581d30
004E7BB2  BE 07 00 00 00                  mov esi, 7
004E7BB7  8B CE                           mov ecx, esi
004E7BB9  85 C0                           test eax, eax
004E7BBB  74 15                           je 0x1404e7bd2
004E7BBD  49 8B 9E A0 00 00 00            mov rbx, qword ptr [r14 + 0xa0]
004E7BC4  E8 B7 C1 D8 FF                  call 0x140273d80
004E7BC9  88 47 45                        mov byte ptr [rdi + 0x45], al
004E7BCC  48 89 5F 38                     mov qword ptr [rdi + 0x38], rbx
004E7BD0  EB 0C                           jmp 0x1404e7bde
004E7BD2  E8 A9 C1 D8 FF                  call 0x140273d80
004E7BD7  88 47 45                        mov byte ptr [rdi + 0x45], al
004E7BDA  4C 89 77 38                     mov qword ptr [rdi + 0x38], r14
004E7BDE  80 7F 44 00                     cmp byte ptr [rdi + 0x44], 0
004E7BE2  74 2F                           je 0x1404e7c13
004E7BE4  4D 85 FF                        test r15, r15
004E7BE7  74 12                           je 0x1404e7bfb
004E7BE9  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
004E7BF0  80 48 03 01                     or byte ptr [rax + 3], 1
004E7BF4  BB 03 01 00 00                  mov ebx, 0x103
004E7BF9  EB 05                           jmp 0x1404e7c00
004E7BFB  BB 20 01 00 C0                  mov ebx, 0xc0000120
004E7C00  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
004E7C04  B2 01                           mov dl, 1
004E7C06  48 8B CF                        mov rcx, rdi
004E7C09  E8 8A CA FF FF                  call 0x1404e4698
004E7C0E  E9 E4 01 00 00                  jmp 0x1404e7df7
004E7C13  48 8D 05 F6 AE 09 00            lea rax, [rip + 0x9aef6]
004E7C1A  48 87 47 68                     xchg qword ptr [rdi + 0x68], rax
004E7C1E  8A 57 45                        mov dl, byte ptr [rdi + 0x45]
004E7C21  48 8B CE                        mov rcx, rsi
004E7C24  E8 17 A9 D8 FF                  call 0x140272540
004E7C29  48 8B B4 24 B8 00 00 00         mov rsi, qword ptr [rsp + 0xb8]
004E7C31  44 8A 6C 24 30                  mov r13b, byte ptr [rsp + 0x30]
004E7C36  33 D2                           xor edx, edx
004E7C38  4D 85 FF                        test r15, r15
004E7C3B  0F 85 9D 01 00 00               jne 0x1404e7dde
004E7C41  48 39 94 24 58 02 00 00         cmp qword ptr [rsp + 0x258], rdx
004E7C49  74 0A                           je 0x1404e7c55
004E7C4B  48 39 54 24 58                  cmp qword ptr [rsp + 0x58], rdx
004E7C50  41 B7 01                        mov r15b, 1
004E7C53  75 03                           jne 0x1404e7c58
004E7C55  44 8A FA                        mov r15b, dl
004E7C58  44 8A EA                        mov r13b, dl
004E7C5B  33 C0                           xor eax, eax
004E7C5D  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
004E7C64  0F 57 C0                        xorps xmm0, xmm0
004E7C67  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
004E7C6F  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
004E7C77  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
004E7C7E  49 8B 8E 98 00 00 00            mov rcx, qword ptr [r14 + 0x98]
004E7C85  E8 16 87 D6 FF                  call 0x1402503a0
004E7C8A  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
004E7C8F  41 8A C7                        mov al, r15b
004E7C92  F6 D8                           neg al
004E7C94  48 1B D2                        sbb rdx, rdx
004E7C97  48 8D 84 24 58 02 00 00         lea rax, [rsp + 0x258]
004E7C9F  48 23 D0                        and rdx, rax
004E7CA2  4C 8B C7                        mov r8, rdi
004E7CA5  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
004E7CAA  E8 E1 5B 53 00                  call 0x140a1d890
004E7CAF  8B D8                           mov ebx, eax
004E7CB1  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
004E7CB5  33 D2                           xor edx, edx
004E7CB7  45 84 FF                        test r15b, r15b
004E7CBA  74 5F                           je 0x1404e7d1b
004E7CBC  B9 02 01 00 00                  mov ecx, 0x102
004E7CC1  3B C1                           cmp eax, ecx
004E7CC3  75 56                           jne 0x1404e7d1b
004E7CC5  44 8A FA                        mov r15b, dl
004E7CC8  0F 57 C0                        xorps xmm0, xmm0
004E7CCB  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
004E7CD3  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
004E7CDB  89 94 24 80 00 00 00            mov dword ptr [rsp + 0x80], edx
004E7CE2  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
004E7CEA  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
004E7CF2  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
004E7CFA  89 8C 24 98 00 00 00            mov dword ptr [rsp + 0x98], ecx
004E7D01  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
004E7D09  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
004E7D0E  E8 BD 2D 1D 00                  call 0x1406baad0
004E7D13  41 B5 01                        mov r13b, 1
004E7D16  E9 74 FF FF FF                  jmp 0x1404e7c8f
004E7D1B  45 84 ED                        test r13b, r13b
004E7D1E  74 24                           je 0x1404e7d44
004E7D20  C7 84 24 80 00 00 00 01 00 00 00  mov dword ptr [rsp + 0x80], 1
004E7D2B  89 9C 24 98 00 00 00            mov dword ptr [rsp + 0x98], ebx
004E7D32  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
004E7D3A  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
004E7D3F  E8 8C 2D 1D 00                  call 0x1406baad0
004E7D44  81 FB 4B 00 00 C0               cmp ebx, 0xc000004b
004E7D4A  74 1E                           je 0x1404e7d6a
004E7D4C  81 FB 20 01 00 C0               cmp ebx, 0xc0000120
004E7D52  74 16                           je 0x1404e7d6a
004E7D54  48 85 FF                        test rdi, rdi
004E7D57  74 07                           je 0x1404e7d60
004E7D59  8B 5F 30                        mov ebx, dword ptr [rdi + 0x30]
004E7D5C  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
004E7D60  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004E7D65  C6 00 01                        mov byte ptr [rax], 1
004E7D68  EB 68                           jmp 0x1404e7dd2
004E7D6A  48 85 FF                        test rdi, rdi
004E7D6D  74 0A                           je 0x1404e7d79
004E7D6F  48 8B CF                        mov rcx, rdi
004E7D72  E8 69 A3 D8 FF                  call 0x1402720e0
004E7D77  EB 38                           jmp 0x1404e7db1
004E7D79  49 8B 8E 98 00 00 00            mov rcx, qword ptr [r14 + 0x98]
004E7D80  E8 1B 68 D2 FF                  call 0x14020e5a0
004E7D85  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
004E7D8A  49 8B 04 24                     mov rax, qword ptr [r12]
004E7D8E  49 3B C4                        cmp rax, r12
004E7D91  74 0D                           je 0x1404e7da0
004E7D93  48 3B F0                        cmp rsi, rax
004E7D96  75 41                           jne 0x1404e7dd9
004E7D98  48 8B C8                        mov rcx, rax
004E7D9B  E8 20 E2 F3 FF                  call 0x140425fc0
004E7DA0  49 8B 8E 98 00 00 00            mov rcx, qword ptr [r14 + 0x98]
004E7DA7  E8 14 9C D6 FF                  call 0x1402519c0
004E7DAC  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
004E7DB1  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
004E7DB7  45 33 C9                        xor r9d, r9d
004E7DBA  45 33 C0                        xor r8d, r8d
004E7DBD  33 D2                           xor edx, edx
004E7DBF  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
004E7DC4  E8 E7 68 D2 FF                  call 0x14020e6b0
004E7DC9  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004E7DCE  33 D2                           xor edx, edx
004E7DD0  88 10                           mov byte ptr [rax], dl
004E7DD2  44 8A 6C 24 30                  mov r13b, byte ptr [rsp + 0x30]
004E7DD7  EB 23                           jmp 0x1404e7dfc
004E7DD9  48 8B 00                        mov rax, qword ptr [rax]
004E7DDC  EB B0                           jmp 0x1404e7d8e
004E7DDE  48 85 FF                        test rdi, rdi
004E7DE1  74 0B                           je 0x1404e7dee
004E7DE3  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
004E7DEA  80 48 03 01                     or byte ptr [rax + 3], 1
004E7DEE  BB 03 01 00 00                  mov ebx, 0x103
004E7DF3  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
004E7DF7  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004E7DFC  45 84 ED                        test r13b, r13b
004E7DFF  0F 84 CA 00 00 00               je 0x1404e7ecf
004E7E05  83 3D 44 EE 91 00 05            cmp dword ptr [rip + 0x91ee44], 5
004E7E0C  0F 86 AC 00 00 00               jbe 0x1404e7ebe
004E7E12  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
004E7E16  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
004E7E1B  48 89 8C 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rcx
004E7E23  48 C7 84 24 F8 00 00 00 04 00 00 00  mov qword ptr [rsp + 0xf8], 4
004E7E2F  8A 00                           mov al, byte ptr [rax]
004E7E31  88 44 24 31                     mov byte ptr [rsp + 0x31], al
004E7E35  48 8D 44 24 31                  lea rax, [rsp + 0x31]
004E7E3A  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
004E7E42  48 C7 84 24 08 01 00 00 01 00 00 00  mov qword ptr [rsp + 0x108], 1
004E7E4E  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
004E7E53  48 8D 44 24 68                  lea rax, [rsp + 0x68]
004E7E58  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
004E7E60  48 C7 84 24 18 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x118], 8
004E7E6C  41 8B 86 90 00 00 00            mov eax, dword ptr [r14 + 0x90]
004E7E73  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
004E7E77  48 8D 44 24 3C                  lea rax, [rsp + 0x3c]
004E7E7C  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
004E7E84  48 C7 84 24 28 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x128], 4
004E7E90  48 8D 84 24 D0 00 00 00         lea rax, [rsp + 0xd0]
004E7E98  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E7E9D  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E7EA5  45 33 C9                        xor r9d, r9d
004E7EA8  45 33 C0                        xor r8d, r8d
004E7EAB  48 8D 15 40 C5 B5 FF            lea rdx, [rip - 0x4a3ac0]
004E7EB2  48 8D 0D 97 ED 91 00            lea rcx, [rip + 0x91ed97]
004E7EB9  E8 22 E2 F3 FF                  call 0x1404260e0
004E7EBE  49 8B 8E 98 00 00 00            mov rcx, qword ptr [r14 + 0x98]
004E7EC5  E8 D6 84 D6 FF                  call 0x1402503a0
004E7ECA  E9 95 00 00 00                  jmp 0x1404e7f64
004E7ECF  83 3D 7A ED 91 00 05            cmp dword ptr [rip + 0x91ed7a], 5
004E7ED6  0F 86 88 00 00 00               jbe 0x1404e7f64
004E7EDC  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
004E7EE0  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
004E7EE5  48 89 8C 24 50 01 00 00         mov qword ptr [rsp + 0x150], rcx
004E7EED  48 C7 84 24 58 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x158], 4
004E7EF9  8A 00                           mov al, byte ptr [rax]
004E7EFB  88 44 24 32                     mov byte ptr [rsp + 0x32], al
004E7EFF  48 8D 44 24 32                  lea rax, [rsp + 0x32]
004E7F04  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
004E7F0C  48 C7 84 24 68 01 00 00 01 00 00 00  mov qword ptr [rsp + 0x168], 1
004E7F18  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
004E7F1D  48 8D 44 24 78                  lea rax, [rsp + 0x78]
004E7F22  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
004E7F2A  48 C7 84 24 78 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x178], 8
004E7F36  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
004E7F3E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E7F43  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
004E7F4B  45 33 C9                        xor r9d, r9d
004E7F4E  45 33 C0                        xor r8d, r8d
004E7F51  48 8D 15 F9 C4 B5 FF            lea rdx, [rip - 0x4a3b07]
004E7F58  48 8D 0D F1 EC 91 00            lea rcx, [rip + 0x91ecf1]
004E7F5F  E8 7C E1 F3 FF                  call 0x1404260e0
004E7F64  8B C3                           mov eax, ebx
004E7F66  48 8B 8C 24 D0 01 00 00         mov rcx, qword ptr [rsp + 0x1d0]
004E7F6E  48 33 CC                        xor rcx, rsp
004E7F71  E8 CA 46 1C 00                  call 0x1406ac640
004E7F76  48 81 C4 E0 01 00 00            add rsp, 0x1e0
004E7F7D  41 5F                           pop r15
004E7F7F  41 5E                           pop r14
004E7F81  41 5D                           pop r13
004E7F83  41 5C                           pop r12
004E7F85  5F                              pop rdi
004E7F86  5E                              pop rsi
004E7F87  5B                              pop rbx
004E7F88  C3                              ret
004E7F89  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpWaitOnIrp(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned __int8 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m194;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned int v_stack_m1D8;
    unsigned int v_stack_m1DC;
    unsigned int v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned __int8 v_stack_m1E5;
    unsigned __int8 v_stack_m1E6;
    unsigned __int8 v_stack_m1E7;
    unsigned __int8 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned int v_stack_m1F8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (480);
    result = (*(unsigned __int64 *)(v_rip + 9579916)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m178 = a3;
    v_stack_m1A8 = a1;
    v_stack_m1B8 = a6;
    v_stack_m158 = a9;
    v_stack_m1C0 = a10;
    v_stack_m1E4 = 0xC000009AULL;
    a1 = 0;
    v_stack_m1E5 = 0;
    result = a10;
    if ((*(unsigned int *)(v_rip + 9564716)) >= = 5) {
        *(unsigned __int64 *)(v_rsp - 368) = a2;
        result = v_rsp - 368;
        *(unsigned __int64 *)(v_rsp - 120) = result;
        *(unsigned __int64 *)(v_rsp - 112) = 8;
        *(unsigned __int64 *)(v_rsp - 360) = 0;
        result = v_rsp - 360;
        *(unsigned __int64 *)(v_rsp - 104) = result;
        *(unsigned __int64 *)(v_rsp - 96) = 8;
        result = *(unsigned int *)(a1 + 144);
        v_stack_m1C8 = (unsigned int)(result);
        result = v_stack_m1C8;
        *(unsigned __int64 *)(v_rsp - 88) = result;
        *(unsigned __int64 *)(v_rsp - 80) = 4;
        result = v_rsp - 152;
        v_stack_m1F0 = result;
        v_stack_m1F8 = 5;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4861962;
        a1 = v_rip + 9564594;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
        a1 = 0;
    }
    v_stack_m1E8 = 1;
    result = v_stack_m1E5;
    if (a11 != 0) { result = a11; }
    v_stack_m1D0 = result;
    *(unsigned __int8 *)(result) = 0;
    result = ExAllocatePool2(288, 64, (unsigned int)(0x6F725346ULL), a4);
    v_stack_m160 = result;
    a2 = 0;
    if (0 == 0) goto loc_004E7B16;
    *(unsigned __int64 *)(result + 16) = 0;
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 56)));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184))) != 13) goto loc_004E7B09;
    result = 1;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 24)) != 0x90014ULL) {
        result = 0;
    }
    *(unsigned __int8 *)(result + 53) = (unsigned __int8)(result);
    *(unsigned __int64 *)(result + 56) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48);
loc_004E7B16:
    *(unsigned __int8 *)(result + 52) = a7;
    if (0 == 0) goto loc_004E7B37;
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 32) = v_stack_m178;
    goto loc_004E7B68;
loc_004E7B37:
    *(unsigned __int64 *)(result + 24) = v_rip + 2285090;
    *(unsigned __int64 *)(result + 32) = v_stack_m1B8;
    *(unsigned __int16 *)(v_stack_m1B8) = 0;
    *(unsigned __int8 *)(v_stack_m1B8 + 2) = 6;
    *(unsigned int *)(v_stack_m1B8 + 4) = 0;
    *(unsigned __int64 *)(v_stack_m1B8 + 8 + 8) = v_stack_m1B8 + 8;
    *(unsigned __int64 *)(v_stack_m1B8 + 8) = v_stack_m1B8 + 8;
loc_004E7B68:
    result = v_stack_m178;
    if (a5 != 0) {
        a2 = 0;
        a1 = v_stack_m178;
        result = a5;
        result = guard_dispatch_icall(a1, a2, (unsigned int)(0x6F725346ULL), a4);
        a2 = 0;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88 + 8))) != (a1 + 88)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(result) = a1 + 88;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a1 + 88 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88 + 8)) = result;
    *(unsigned __int64 *)(a1 + 88 + 8) = result;
    if (0 == 0) goto loc_004E7C38;
    *(unsigned int *)(a2 + 48) = 0;
    result = Feature_3609177402__private_IsEnabledDeviceUsageNoInline(a1, a2, (unsigned int)(0x6F725346ULL), a4);
    if ((unsigned int)(result) == 0) goto loc_004E7BD2;
    result = KeAcquireQueuedSpinLock(7, a2, (unsigned int)(0x6F725346ULL), a4);
    *(unsigned __int8 *)(a2 + 69) = (unsigned __int8)(result);
    *(unsigned __int64 *)(a2 + 56) = *(unsigned __int64 *)(a1 + 160);
    goto loc_004E7BDE;
loc_004E7BD2:
    result = KeAcquireQueuedSpinLock(7, a2, (unsigned int)(0x6F725346ULL), a4);
    *(unsigned __int8 *)(a2 + 69) = (unsigned __int8)(result);
    *(unsigned __int64 *)(a2 + 56) = a1;
loc_004E7BDE:
    if ((*(unsigned __int8 *)(a2 + 68)) == 0) goto loc_004E7C13;
    if (0 == 0) goto loc_004E7BFB;
    goto loc_004E7C00;
loc_004E7BFB:
loc_004E7C00:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC0000120ULL));
    result = FsRtlpCancelWaitingIrp(0, 1, (unsigned int)(0x6F725346ULL), a4);
    goto loc_004E7DF7;
loc_004E7C13:
    result = KeReleaseQueuedSpinLock(7, *(unsigned __int8 *)(a2 + 69), (unsigned int)(0x6F725346ULL), a4);
    a2 = 0;
loc_004E7C38:
    if (0 != 0) goto loc_004E7DDE;
    if (a8 == 0) goto loc_004E7C55;
    v_r15 = 1;
    if (v_stack_m1C0 == 0) {
        v_r15 = 0;
    }
    result = 0;
    v_stack_m194 = 0;
    v_stack_m198 = v_xmm0;
    v_stack_m188 = 0;
    v_stack_m180 = 0;
    result = ExReleaseFastMutexUnsafe(*(unsigned __int64 *)(a1 + 152), a2, (unsigned int)(0x6F725346ULL), a4);
    v_stack_m1E8 = 0;
loc_004E7C8F:
    result = (unsigned __int8)(-((unsigned __int8)(v_r15)));
    a2 = (a2) & (a8);
    result = FsRtlCancellableWaitForSingleObject(v_stack_m1B8, a2, a2, a4);
    v_stack_m1E4 = (unsigned int)(result);
    a2 = 0;
    if ((unsigned __int8)(v_r15) == 0) goto loc_004E7D1B;
    if (((unsigned int)(result)) != 258) goto loc_004E7D1B;
    v_stack_m198 = v_xmm0;
    v_stack_m188 = v_xmm0;
    v_stack_m198 = 0;
    v_stack_m190 = v_stack_m158;
    v_stack_m188 = 0;
    v_stack_m180 = 258;
    result = guard_dispatch_icall(v_stack_m198, a2, a2, a4);
    goto loc_004E7C8F;
loc_004E7D1B:
    if (1 != 0) {
        v_stack_m198 = 1;
        v_stack_m180 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = v_stack_m198;
        result = v_stack_m1C0;
        result = guard_dispatch_icall(a1, a2, a2, a4);
    }
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC000004BULL) goto loc_004E7D6A;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000120ULL) goto loc_004E7D6A;
    v_rbx = (unsigned int)((unsigned int)(result));
    if (0 != 0) {
        v_rbx = *(unsigned int *)(a2 + 48);
        v_stack_m1E4 = (unsigned int)(v_rbx);
    }
    *(unsigned __int8 *)(v_stack_m1D0) = 1;
    goto loc_004E7DD2;
loc_004E7D6A:
    if (0 == 0) goto loc_004E7D79;
    result = IoCancelIrp(0, a2, a2, a4);
    goto loc_004E7DB1;
loc_004E7D79:
    result = ExAcquireFastMutex(*(unsigned __int64 *)(a1 + 152), a2, a2, a4);
    v_stack_m1E8 = 1;
loc_004E7D8E:
    if ((*(unsigned __int64 *)(a1 + 88)) == (a1 + 88)) goto loc_004E7DA0;
    if (v_stack_m160 != (*(unsigned __int64 *)(a1 + 88))) goto loc_004E7DD9;
    result = FsRtlpRemoveAndCompleteWaitingIrp(*(unsigned __int64 *)(a1 + 88), a2, a2, a4);
loc_004E7DA0:
    result = ExReleaseFastMutex(*(unsigned __int64 *)(a1 + 152), a2, a2, a4);
    v_stack_m1E8 = 0;
loc_004E7DB1:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_stack_m1B8, a2, a3, a4);
    a2 = 0;
    *(unsigned __int8 *)(v_stack_m1D0) = 0;
loc_004E7DD2:
    goto loc_004E7DFC;
loc_004E7DD9:
    goto loc_004E7D8E;
loc_004E7DDE:
    result = *(unsigned __int64 *)(v_stack_m1D0);
    if (0 != 0) {
        result = *(unsigned __int64 *)(a2 + 184);
    }
    v_stack_m1E4 = 259;
loc_004E7DF7:
loc_004E7DFC:
    if ((unsigned __int8)(v_stack_m1E8) == 0) goto loc_004E7ECF;
    result = v_stack_m1D0;
    if ((*(unsigned int *)(v_rip + 9563716)) >= = 5) {
        v_stack_m1E0 = 259;
        a1 = v_stack_m1E0;
        v_stack_m128 = a1;
        v_stack_m120 = 4;
        result = *(unsigned __int8 *)(v_stack_m1D0);
        v_stack_m1E7 = (unsigned __int8)(result);
        result = v_stack_m1E7;
        v_stack_m118 = result;
        v_stack_m110 = 1;
        v_stack_m1B0 = a1;
        result = v_stack_m1B0;
        v_stack_m108 = result;
        v_stack_m100 = 8;
        result = *(unsigned int *)(a1 + 144);
        v_stack_m1DC = (unsigned int)(result);
        result = v_stack_m1DC;
        v_stack_mF8 = result;
        v_stack_mF0 = 4;
        result = v_stack_m148;
        v_stack_m1F0 = result;
        v_stack_m1F8 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4864704;
        a1 = v_rip + 9563543;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    result = ExReleaseFastMutexUnsafe(*(unsigned __int64 *)(a1 + 152), a2, a3, a4);
    goto loc_004E7F64;
loc_004E7ECF:
    if ((*(unsigned int *)(v_rip + 9563514)) >= = 5) {
        v_stack_m1D8 = 259;
        a1 = v_stack_m1D8;
        v_stack_mC8 = a1;
        v_stack_mC0 = 4;
        result = *(unsigned __int8 *)(result);
        v_stack_m1E6 = (unsigned __int8)(result);
        result = v_stack_m1E6;
        v_stack_mB8 = result;
        v_stack_mB0 = 1;
        v_stack_m1A0 = a1;
        result = v_stack_m1A0;
        v_stack_mA8 = result;
        v_stack_mA0 = 8;
        result = v_stack_mE8;
        v_stack_m1F0 = result;
        v_stack_m1F8 = 5;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4864775;
        a1 = v_rip + 9563377;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (480);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlpWaitOnIrp(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint8_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m178;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m194;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint32_t v_stack_m1D8;
    uint32_t v_stack_m1DC;
    uint32_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint8_t v_stack_m1E5;
    uint8_t v_stack_m1E6;
    uint8_t v_stack_m1E7;
    uint8_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint32_t v_stack_m1F8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (480);
    result = (*(uint64_t *)(v_rip + 0x922D8C)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m178 = Arg3;
    v_stack_m1A8 = Arg1;
    v_stack_m1B8 = Arg6;
    v_stack_m158 = Arg9;
    v_stack_m1C0 = Arg10;
    v_stack_m1E4 = 0xC000009AULL;
    Arg1 = 0;
    v_stack_m1E5 = 0;
    result = Arg10;
    if ((*(uint32_t *)(v_rip + 0x91F22C)) >= = 5) {
        *(uint64_t *)(local_rsp - 0x170) = Arg2;
        result = local_rsp - 368;
        *(uint64_t *)(local_rsp - 0x78) = result;
        *(uint64_t *)(local_rsp - 0x70) = 8;
        *(uint64_t *)(local_rsp - 0x168) = 0;
        result = local_rsp - 360;
        *(uint64_t *)(local_rsp - 0x68) = result;
        *(uint64_t *)(local_rsp - 0x60) = 8;
        result = *(uint32_t *)(arg1 + 0x90);
        v_stack_m1C8 = (uint32_t)(result);
        result = v_stack_m1C8;
        *(uint64_t *)(local_rsp - 0x58) = result;
        *(uint64_t *)(local_rsp - 0x50) = 4;
        result = local_rsp - 152;
        v_stack_m1F0 = result;
        v_stack_m1F8 = 5;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4861962;
        Arg1 = v_rip + 9564594;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
        Arg1 = 0;
    }
    v_stack_m1E8 = 1;
    result = v_stack_m1E5;
    if (Arg11 != 0) { result = Arg11; }
    v_stack_m1D0 = result;
    *(uint8_t *)(result) = 0;
    result = ExAllocatePool2(288, 64, (uint32_t)(0x6F725346ULL), Arg4);
    v_stack_m160 = result;
    Arg2 = 0;
    if (0 == 0) goto loc_004E7B16;
    *(uint64_t *)(result + 0x10) = 0;
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x38)));
    if ((*(uint8_t *)(*(uint64_t *)(Arg2 + 0xB8))) != 13) goto loc_004E7B09;
    result = 1;
    if ((*(uint32_t *)(*(uint64_t *)(Arg2 + 0xB8) + 0x18)) != 0x90014ULL) {
        result = 0;
    }
    *(uint8_t *)(result + 0x35) = (uint8_t)(result);
    *(uint64_t *)(result + 0x38) = *(uint64_t *)(*(uint64_t *)(Arg2 + 0xB8) + 0x30);
loc_004E7B16:
    *(uint8_t *)(result + 0x34) = Arg7;
    if (0 == 0) goto loc_004E7B37;
    *(uint64_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x20) = v_stack_m178;
    goto loc_004E7B68;
loc_004E7B37:
    *(uint64_t *)(result + 0x18) = v_rip + 2285090;
    *(uint64_t *)(result + 0x20) = v_stack_m1B8;
    *(uint16_t *)(v_stack_m1B8) = 0;
    *(uint8_t *)(v_stack_m1B8 + 0x2) = 6;
    *(uint32_t *)(v_stack_m1B8 + 0x4) = 0;
    *(uint64_t *)(v_stack_m1B8 + 0x8 + 0x8) = v_stack_m1B8 + 8;
    *(uint64_t *)(v_stack_m1B8 + 0x8) = v_stack_m1B8 + 8;
loc_004E7B68:
    result = v_stack_m178;
    if (Arg5 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m178;
        result = Arg5;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)(0x6F725346ULL), Arg4);
        Arg2 = 0;
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x58 + 0x8))) != (Arg1 + 88)) {
        Arg1 = 3;
    }
    *(void **)(result) = Arg1 + 88;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg1 + 0x58 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x58 + 0x8)) = result;
    *(uint64_t *)(arg1 + 0x58 + 0x8) = result;
    if (0 == 0) goto loc_004E7C38;
    *(uint32_t *)(Arg2 + 0x30) = 0;
    result = Feature_3609177402__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, (uint32_t)(0x6F725346ULL), Arg4);
    if ((uint32_t)(result) == 0) goto loc_004E7BD2;
    result = KeAcquireQueuedSpinLock(7, Arg2, (uint32_t)(0x6F725346ULL), Arg4);
    *(uint8_t *)(Arg2 + 0x45) = (uint8_t)(result);
    *(uint64_t *)(Arg2 + 0x38) = *(uint64_t *)(arg1 + 0xA0);
    goto loc_004E7BDE;
loc_004E7BD2:
    result = KeAcquireQueuedSpinLock(7, Arg2, (uint32_t)(0x6F725346ULL), Arg4);
    *(uint8_t *)(Arg2 + 0x45) = (uint8_t)(result);
    *(void **)(Arg2 + 0x38) = Arg1;
loc_004E7BDE:
    if ((*(uint8_t *)(Arg2 + 0x44)) == 0) goto loc_004E7C13;
    if (0 == 0) goto loc_004E7BFB;
    goto loc_004E7C00;
loc_004E7BFB:
loc_004E7C00:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC0000120ULL));
    result = FsRtlpCancelWaitingIrp(0, 1, (uint32_t)(0x6F725346ULL), Arg4);
    goto loc_004E7DF7;
loc_004E7C13:
    result = KeReleaseQueuedSpinLock(7, *(uint8_t *)(Arg2 + 0x45), (uint32_t)(0x6F725346ULL), Arg4);
    Arg2 = 0;
loc_004E7C38:
    if (0 != 0) goto loc_004E7DDE;
    if (Arg8 == 0) goto loc_004E7C55;
    local_r15 = 1;
    if (v_stack_m1C0 == 0) {
        local_r15 = 0;
    }
    result = 0;
    v_stack_m194 = 0;
    v_stack_m198 = v_xmm0;
    v_stack_m188 = 0;
    v_stack_m180 = 0;
    result = ExReleaseFastMutexUnsafe(*(uint64_t *)(arg1 + 0x98), Arg2, (uint32_t)(0x6F725346ULL), Arg4);
    v_stack_m1E8 = 0;
loc_004E7C8F:
    result = (uint8_t)(-((uint8_t)(local_r15)));
    Arg2 = (Arg2) & (Arg8);
    result = FsRtlCancellableWaitForSingleObject(v_stack_m1B8, Arg2, Arg2, Arg4);
    v_stack_m1E4 = (uint32_t)(result);
    Arg2 = 0;
    if ((uint8_t)(local_r15) == 0) goto loc_004E7D1B;
    if (((uint32_t)(result)) != 258) goto loc_004E7D1B;
    v_stack_m198 = v_xmm0;
    v_stack_m188 = v_xmm0;
    v_stack_m198 = 0;
    v_stack_m190 = v_stack_m158;
    v_stack_m188 = 0;
    v_stack_m180 = 258;
    result = guard_dispatch_icall(v_stack_m198, Arg2, Arg2, Arg4);
    goto loc_004E7C8F;
loc_004E7D1B:
    if (1 != 0) {
        v_stack_m198 = 1;
        v_stack_m180 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = v_stack_m198;
        result = v_stack_m1C0;
        result = guard_dispatch_icall(Arg1, Arg2, Arg2, Arg4);
    }
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC000004BULL) goto loc_004E7D6A;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000120ULL) goto loc_004E7D6A;
    local_rbx = (uint32_t)((uint32_t)(result));
    if (0 != 0) {
        local_rbx = *(uint32_t *)(Arg2 + 0x30);
        v_stack_m1E4 = (uint32_t)(local_rbx);
    }
    *(uint8_t *)(v_stack_m1D0) = 1;
    goto loc_004E7DD2;
loc_004E7D6A:
    if (0 == 0) goto loc_004E7D79;
    result = IoCancelIrp(0, Arg2, Arg2, Arg4);
    goto loc_004E7DB1;
loc_004E7D79:
    result = ExAcquireFastMutex(*(uint64_t *)(arg1 + 0x98), Arg2, Arg2, Arg4);
    v_stack_m1E8 = 1;
loc_004E7D8E:
    if ((*(uint64_t *)(arg1 + 0x58)) == (Arg1 + 88)) goto loc_004E7DA0;
    if (v_stack_m160 != (*(uint64_t *)(arg1 + 0x58))) goto loc_004E7DD9;
    result = FsRtlpRemoveAndCompleteWaitingIrp(*(uint64_t *)(arg1 + 0x58), Arg2, Arg2, Arg4);
loc_004E7DA0:
    result = ExReleaseFastMutex(*(uint64_t *)(arg1 + 0x98), Arg2, Arg2, Arg4);
    v_stack_m1E8 = 0;
loc_004E7DB1:
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_stack_m1B8, Arg2, Arg3, Arg4);
    Arg2 = 0;
    *(uint8_t *)(v_stack_m1D0) = 0;
loc_004E7DD2:
    goto loc_004E7DFC;
loc_004E7DD9:
    goto loc_004E7D8E;
loc_004E7DDE:
    result = *(uint64_t *)(v_stack_m1D0);
    if (0 != 0) {
        result = *(uint64_t *)(Arg2 + 0xB8);
    }
    v_stack_m1E4 = 259;
loc_004E7DF7:
loc_004E7DFC:
    if ((uint8_t)(v_stack_m1E8) == 0) goto loc_004E7ECF;
    result = v_stack_m1D0;
    if ((*(uint32_t *)(v_rip + 0x91EE44)) >= = 5) {
        v_stack_m1E0 = 259;
        Arg1 = v_stack_m1E0;
        v_stack_m128 = Arg1;
        v_stack_m120 = 4;
        result = *(uint8_t *)(v_stack_m1D0);
        v_stack_m1E7 = (uint8_t)(result);
        result = v_stack_m1E7;
        v_stack_m118 = result;
        v_stack_m110 = 1;
        v_stack_m1B0 = Arg1;
        result = v_stack_m1B0;
        v_stack_m108 = result;
        v_stack_m100 = 8;
        result = *(uint32_t *)(arg1 + 0x90);
        v_stack_m1DC = (uint32_t)(result);
        result = v_stack_m1DC;
        v_stack_mF8 = result;
        v_stack_mF0 = 4;
        result = v_stack_m148;
        v_stack_m1F0 = result;
        v_stack_m1F8 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4864704;
        Arg1 = v_rip + 9563543;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExReleaseFastMutexUnsafe(*(uint64_t *)(arg1 + 0x98), Arg2, Arg3, Arg4);
    goto loc_004E7F64;
loc_004E7ECF:
    if ((*(uint32_t *)(v_rip + 0x91ED7A)) >= = 5) {
        v_stack_m1D8 = 259;
        Arg1 = v_stack_m1D8;
        v_stack_mC8 = Arg1;
        v_stack_mC0 = 4;
        result = *(uint8_t *)(result);
        v_stack_m1E6 = (uint8_t)(result);
        result = v_stack_m1E6;
        v_stack_mB8 = result;
        v_stack_mB0 = 1;
        v_stack_m1A0 = Arg1;
        result = v_stack_m1A0;
        v_stack_mA8 = result;
        v_stack_mA0 = 8;
        result = v_stack_mE8;
        v_stack_m1F0 = result;
        v_stack_m1F8 = 5;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4864775;
        Arg1 = v_rip + 9563377;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (480);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x90` | `32` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004E7998&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
