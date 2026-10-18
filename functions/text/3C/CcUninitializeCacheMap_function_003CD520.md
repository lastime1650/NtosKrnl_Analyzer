# CcUninitializeCacheMap

- RVA: `0x003CD520`–`0x003CD9CF` (길이 `1,199` bytes)
- VA: `0x00000001403CD520`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008FA08`
- 디코드: `287`개 명령, `1,199/1,199` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003CD57F` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CD5A4` → [CcGetPrivateVolumeCacheMap](../38/CcGetPrivateVolumeCacheMap_function_0038B930.md) (function, `0x0038B930`)
- `0x003CD5B2` → [CcReferencePartitionAndPrivateVolumeCacheMap](../38/CcReferencePartitionAndPrivateVolumeCacheMap_function_0038B9E0.md) (function, `0x0038B9E0`)
- `0x003CD5C2` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CD6B2` → [CcDeleteSharedCacheMap](../38/CcDeleteSharedCacheMap_function_0038A804.md) (function, `0x0038A804`)
- `0x003CD6C1` → [CcFreePrivateCacheMapIgnoreNull](../38/CcFreePrivateCacheMapIgnoreNull_function_0038AC64.md) (function, `0x0038AC64`)
- `0x003CD6E8` → [CcDereferencePartitionAndPrivateVolumeCacheMap](../38/CcDereferencePartitionAndPrivateVolumeCacheMap_function_0038B94C.md) (function, `0x0038B94C`)
- `0x003CD724` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003CD743` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD770` → [CcInsertIntoDirtySharedCacheMapList](CcInsertIntoDirtySharedCacheMapList_function_003CD9D8.md) (function, `0x003CD9D8`)
- `0x003CD7B4` → [CcNotifyWriteBehindVolume](CcNotifyWriteBehindVolume_function_003CC134.md) (function, `0x003CC134`)
- `0x003CD7CE` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD7D7` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD814` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD827` → [CcPurgeCacheSection](../38/CcPurgeCacheSection_function_0038B130.md) (function, `0x0038B130`)
- `0x003CD846` → [CcScheduleLazyWriteScan](CcScheduleLazyWriteScan_function_003CBD20.md) (function, `0x003CBD20`)
- `0x003CD882` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD88B` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD898` → [CcNotifyWriteBehindInternal](CcNotifyWriteBehindInternal_function_003CC224.md) (function, `0x003CC224`)
- `0x003CD8CE` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003CD8EC` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003CD921` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x003CD990` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x003CD9A0` → [CcAdjustWriteBehindThreadPoolIfNeeded](../38/CcAdjustWriteBehindThreadPoolIfNeeded_function_00386D94.md) (function, `0x00386D94`)
- `0x003CD9B2` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x003CD9C4` → [IoDiskIoAttributionDereference](../34/IoDiskIoAttributionDereference_function_00349978.md) (function, `0x00349978`)

### Direct callers
- [sub_006E537E](../6E/Unknown_function_006E537E.md) at `0x006E538F`

### Static image references
- `0x003CD565` → RVA `0x00E11CC0` (`.data`; read)
- `0x003CD775` → RVA `0x00E65B88` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x003CD5EE` → [sub_006E8840](../6E/Unknown_function_006E8840.md) (`tail-transfer`)
  - `0x003CD80A` → [sub_006E8840 + 0xB7](../6E/Unknown_function_006E8840.md) (`tail-transfer`)
  - `0x003CD912` → [sub_006E8840 + 0x8C](../6E/Unknown_function_006E8840.md) (`tail-transfer`)
  - `0x003CD9BE` → [sub_006E8840 + 0xD5](../6E/Unknown_function_006E8840.md) (`tail-transfer`)
  - `0x003CD9CA` → [sub_006E8840 + 0xD5](../6E/Unknown_function_006E8840.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003CD520  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003CD525  55                              push rbp
003CD526  56                              push rsi
003CD527  57                              push rdi
003CD528  41 54                           push r12
003CD52A  41 55                           push r13
003CD52C  41 56                           push r14
003CD52E  41 57                           push r15
003CD530  48 8B EC                        mov rbp, rsp
003CD533  48 81 EC 80 00 00 00            sub rsp, 0x80
003CD53A  33 C0                           xor eax, eax
003CD53C  4C 8B E1                        mov r12, rcx
003CD53F  33 C9                           xor ecx, ecx
003CD541  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
003CD545  0F 57 C0                        xorps xmm0, xmm0
003CD548  88 4D 40                        mov byte ptr [rbp + 0x40], cl
003CD54B  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
003CD54F  8B F9                           mov edi, ecx
003CD551  88 4D 58                        mov byte ptr [rbp + 0x58], cl
003CD554  44 8B E9                        mov r13d, ecx
003CD557  4C 8B F2                        mov r14, rdx
003CD55A  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
003CD55E  0F 57 C9                        xorps xmm1, xmm1
003CD561  48 89 45 F8                     mov qword ptr [rbp - 8], rax
003CD565  48 8D 0D 54 47 A4 00            lea rcx, [rip + 0xa44754]
003CD56C  49 8B F0                        mov rsi, r8
003CD56F  48 8D 55 B8                     lea rdx, [rbp - 0x48]
003CD573  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
003CD577  0F 11 4D D0                     movups xmmword ptr [rbp - 0x30], xmm1
003CD57B  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
003CD57F  E8 1C 82 EA FF                  call 0x1402757a0
003CD584  49 8B 44 24 28                  mov rax, qword ptr [r12 + 0x28]
003CD589  45 33 DB                        xor r11d, r11d
003CD58C  4D 8B 7C 24 30                  mov r15, qword ptr [r12 + 0x30]
003CD591  48 8B 58 08                     mov rbx, qword ptr [rax + 8]
003CD595  48 85 DB                        test rbx, rbx
003CD598  74 30                           je 0x1403cd5ca
003CD59A  48 8B BB 18 02 00 00            mov rdi, qword ptr [rbx + 0x218]
003CD5A1  48 8B CB                        mov rcx, rbx
003CD5A4  E8 87 E3 FB FF                  call 0x14038b930
003CD5A9  48 8B D0                        mov rdx, rax
003CD5AC  48 8B CF                        mov rcx, rdi
003CD5AF  4C 8B E8                        mov r13, rax
003CD5B2  E8 29 E4 FB FF                  call 0x14038b9e0
003CD5B7  48 8D 8F 00 03 00 00            lea rcx, [rdi + 0x300]
003CD5BE  48 8D 55 D0                     lea rdx, [rbp - 0x30]
003CD5C2  E8 D9 81 EA FF                  call 0x1402757a0
003CD5C7  45 33 DB                        xor r11d, r11d
003CD5CA  BA 01 00 00 00                  mov edx, 1
003CD5CF  4D 85 FF                        test r15, r15
003CD5D2  74 66                           je 0x1403cd63a
003CD5D4  4D 39 67 08                     cmp qword ptr [r15 + 8], r12
003CD5D8  0F 85 F6 02 00 00               jne 0x1403cd8d4
003CD5DE  48 85 FF                        test rdi, rdi
003CD5E1  0F 84 CF 02 00 00               je 0x1403cd8b6
003CD5E7  49 8B 47 70                     mov rax, qword ptr [r15 + 0x70]
003CD5EB  48 85 C0                        test rax, rax
003CD5EE  0F 85 4C B2 31 00               jne 0x1406e8840
003CD5F4  8B 43 04                        mov eax, dword ptr [rbx + 4]
003CD5F7  FF C8                           dec eax
003CD5F9  89 43 04                        mov dword ptr [rbx + 4], eax
003CD5FC  49 8D 47 60                     lea rax, [r15 + 0x60]
003CD600  48 8B 10                        mov rdx, qword ptr [rax]
003CD603  48 39 42 08                     cmp qword ptr [rdx + 8], rax
003CD607  75 09                           jne 0x1403cd612
003CD609  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
003CD60D  48 39 01                        cmp qword ptr [rcx], rax
003CD610  74 07                           je 0x1403cd619
003CD612  B9 03 00 00 00                  mov ecx, 3
003CD617  CD 29                           int 0x29
003CD619  48 8D 83 80 01 00 00            lea rax, [rbx + 0x180]
003CD620  48 89 11                        mov qword ptr [rcx], rdx
003CD623  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
003CD627  4C 3B F8                        cmp r15, rax
003CD62A  0F 84 FA 00 00 00               je 0x1403cd72a
003CD630  4D 89 5C 24 30                  mov qword ptr [r12 + 0x30], r11
003CD635  BA 01 00 00 00                  mov edx, 1
003CD63A  48 85 DB                        test rbx, rbx
003CD63D  0F 84 F3 00 00 00               je 0x1403cd736
003CD643  4D 85 F6                        test r14, r14
003CD646  0F 85 04 02 00 00               jne 0x1403cd850
003CD64C  44 39 5B 04                     cmp dword ptr [rbx + 4], r11d
003CD650  0F 85 1F 02 00 00               jne 0x1403cd875
003CD656  48 8D 83 E8 00 00 00            lea rax, [rbx + 0xe8]
003CD65D  48 39 00                        cmp qword ptr [rax], rax
003CD660  0F 85 A6 00 00 00               jne 0x1403cd70c
003CD666  41 BE 01 00 00 00               mov r14d, 1
003CD66C  48 85 F6                        test rsi, rsi
003CD66F  0F 85 B6 02 00 00               jne 0x1403cd92b
003CD675  8B 83 98 00 00 00               mov eax, dword ptr [rbx + 0x98]
003CD67B  A8 04                           test al, 4
003CD67D  0F 84 DD 00 00 00               je 0x1403cd760
003CD683  A8 20                           test al, 0x20
003CD685  0F 85 EA 00 00 00               jne 0x1403cd775
003CD68B  44 39 5B 70                     cmp dword ptr [rbx + 0x70], r11d
003CD68F  0F 85 D8 00 00 00               jne 0x1403cd76d
003CD695  0F BA E0 0A                     bt eax, 0xa
003CD699  0F 82 B6 02 00 00               jb 0x1403cd955
003CD69F  45 33 C9                        xor r9d, r9d
003CD6A2  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
003CD6A7  4C 8D 45 D0                     lea r8, [rbp - 0x30]
003CD6AB  48 8B CB                        mov rcx, rbx
003CD6AE  48 8D 55 B8                     lea rdx, [rbp - 0x48]
003CD6B2  E8 4D D1 FB FF                  call 0x14038a804
003CD6B7  41 8A F6                        mov sil, r14b
003CD6BA  C6 45 58 00                     mov byte ptr [rbp + 0x58], 0
003CD6BE  49 8B CF                        mov rcx, r15
003CD6C1  E8 9E D5 FB FF                  call 0x14038ac64
003CD6C6  80 7D 58 00                     cmp byte ptr [rbp + 0x58], 0
003CD6CA  0F 85 CA 02 00 00               jne 0x1403cd99a
003CD6D0  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
003CD6D4  48 85 DB                        test rbx, rbx
003CD6D7  0F 85 CD 02 00 00               jne 0x1403cd9aa
003CD6DD  48 85 FF                        test rdi, rdi
003CD6E0  74 0B                           je 0x1403cd6ed
003CD6E2  49 8B D5                        mov rdx, r13
003CD6E5  48 8B CF                        mov rcx, rdi
003CD6E8  E8 5F E2 FB FF                  call 0x14038b94c
003CD6ED  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
003CD6F5  40 8A C6                        mov al, sil
003CD6F8  48 81 C4 80 00 00 00            add rsp, 0x80
003CD6FF  41 5F                           pop r15
003CD701  41 5E                           pop r14
003CD703  41 5D                           pop r13
003CD705  41 5C                           pop r12
003CD707  5F                              pop rdi
003CD708  5E                              pop rsi
003CD709  5D                              pop rbp
003CD70A  C3                              ret
003CD70B  CC                              int3
003CD70C  45 33 C9                        xor r9d, r9d
003CD70F  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
003CD714  BA 40 0C 00 00                  mov edx, 0xc40
003CD719  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
003CD720  41 8D 49 34                     lea ecx, [r9 + 0x34]
003CD724  E8 37 FF 12 00                  call 0x1404fd660
003CD729  CC                              int3
003CD72A  66 45 89 1F                     mov word ptr [r15], r11w
003CD72E  4D 8B FB                        mov r15, r11
003CD731  E9 FA FE FF FF                  jmp 0x1403cd630
003CD736  4D 85 F6                        test r14, r14
003CD739  0F 85 B1 00 00 00               jne 0x1403cd7f0
003CD73F  48 8D 4D B8                     lea rcx, [rbp - 0x48]
003CD743  E8 98 55 F7 FF                  call 0x140342ce0
003CD748  48 85 F6                        test rsi, rsi
003CD74B  0F 85 36 02 00 00               jne 0x1403cd987
003CD751  41 BE 01 00 00 00               mov r14d, 1
003CD757  40 8A 75 40                     mov sil, byte ptr [rbp + 0x40]
003CD75B  E9 5E FF FF FF                  jmp 0x1403cd6be
003CD760  48 85 F6                        test rsi, rsi
003CD763  0F 85 1A FF FF FF               jne 0x1403cd683
003CD769  A8 20                           test al, 0x20
003CD76B  75 08                           jne 0x1403cd775
003CD76D  48 8B CB                        mov rcx, rbx
003CD770  E8 63 02 00 00                  call 0x1403cd9d8
003CD775  8A 0D 0D 84 A9 00               mov cl, byte ptr [rip + 0xa9840d]
003CD77B  84 C9                           test cl, cl
003CD77D  74 62                           je 0x1403cd7e1
003CD77F  48 8B 83 58 02 00 00            mov rax, qword ptr [rbx + 0x258]
003CD786  48 05 DA 03 00 00               add rax, 0x3da
003CD78C  44 88 30                        mov byte ptr [rax], r14b
003CD78F  44 38 9F 0E 05 00 00            cmp byte ptr [rdi + 0x50e], r11b
003CD796  0F 84 95 00 00 00               je 0x1403cd831
003CD79C  0F BA AB 98 00 00 00 10         bts dword ptr [rbx + 0x98], 0x10
003CD7A4  BA 08 00 00 00                  mov edx, 8
003CD7A9  84 C9                           test cl, cl
003CD7AB  0F 84 E4 00 00 00               je 0x1403cd895
003CD7B1  49 8B CD                        mov rcx, r13
003CD7B4  E8 7B E9 FF FF                  call 0x1403cc134
003CD7B9  41 80 BD 94 04 00 00 00         cmp byte ptr [r13 + 0x494], 0
003CD7C1  75 07                           jne 0x1403cd7ca
003CD7C3  45 88 B5 D9 03 00 00            mov byte ptr [r13 + 0x3d9], r14b
003CD7CA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
003CD7CE  E8 0D 55 F7 FF                  call 0x140342ce0
003CD7D3  48 8D 4D B8                     lea rcx, [rbp - 0x48]
003CD7D7  E8 04 55 F7 FF                  call 0x140342ce0
003CD7DC  E9 76 FF FF FF                  jmp 0x1403cd757
003CD7E1  48 8B 83 18 02 00 00            mov rax, qword ptr [rbx + 0x218]
003CD7E8  48 05 1A 04 00 00               add rax, 0x41a
003CD7EE  EB 9C                           jmp 0x1403cd78c
003CD7F0  4D 39 1E                        cmp qword ptr [r14], r11
003CD7F3  0F 85 46 FF FF FF               jne 0x1403cd73f
003CD7F9  49 8B 44 24 28                  mov rax, qword ptr [r12 + 0x28]
003CD7FE  4C 39 18                        cmp qword ptr [rax], r11
003CD801  0F 84 38 FF FF FF               je 0x1403cd73f
003CD807  48 85 FF                        test rdi, rdi
003CD80A  0F 85 E7 B0 31 00               jne 0x1406e88f7
003CD810  48 8D 4D B8                     lea rcx, [rbp - 0x48]
003CD814  E8 C7 54 F7 FF                  call 0x140342ce0
003CD819  49 8B 4C 24 28                  mov rcx, qword ptr [r12 + 0x28]
003CD81E  45 33 C9                        xor r9d, r9d
003CD821  45 33 C0                        xor r8d, r8d
003CD824  49 8B D6                        mov rdx, r14
003CD827  E8 04 D9 FB FF                  call 0x14038b130
003CD82C  E9 17 FF FF FF                  jmp 0x1403cd748
003CD831  48 85 F6                        test rsi, rsi
003CD834  0F 85 34 01 00 00               jne 0x1403cd96e
003CD83A  45 33 C9                        xor r9d, r9d
003CD83D  45 33 C0                        xor r8d, r8d
003CD840  49 8B D5                        mov rdx, r13
003CD843  48 8B CF                        mov rcx, rdi
003CD846  E8 D5 E4 FF FF                  call 0x1403cbd20
003CD84B  E9 7A FF FF FF                  jmp 0x1403cd7ca
003CD850  49 8B 0E                        mov rcx, qword ptr [r14]
003CD853  48 85 C9                        test rcx, rcx
003CD856  0F 84 96 00 00 00               je 0x1403cd8f2
003CD85C  48 8D 83 E8 00 00 00            lea rax, [rbx + 0xe8]
003CD863  48 39 00                        cmp qword ptr [rax], rax
003CD866  0F 85 E0 FD FF FF               jne 0x1403cd64c
003CD86C  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
003CD870  E9 D7 FD FF FF                  jmp 0x1403cd64c
003CD875  48 85 F6                        test rsi, rsi
003CD878  0F 85 8A 00 00 00               jne 0x1403cd908
003CD87E  48 8D 4D D0                     lea rcx, [rbp - 0x30]
003CD882  E8 59 54 F7 FF                  call 0x140342ce0
003CD887  48 8D 4D B8                     lea rcx, [rbp - 0x48]
003CD88B  E8 50 54 F7 FF                  call 0x140342ce0
003CD890  E9 BC FE FF FF                  jmp 0x1403cd751
003CD895  48 8B CF                        mov rcx, rdi
003CD898  E8 87 E9 FF FF                  call 0x1403cc224
003CD89D  80 BF 0C 05 00 00 00            cmp byte ptr [rdi + 0x50c], 0
003CD8A4  0F 85 20 FF FF FF               jne 0x1403cd7ca
003CD8AA  44 88 B7 19 04 00 00            mov byte ptr [rdi + 0x419], r14b
003CD8B1  E9 14 FF FF FF                  jmp 0x1403cd7ca
003CD8B6  45 33 C9                        xor r9d, r9d
003CD8B9  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
003CD8BE  BA A3 0B 00 00                  mov edx, 0xba3
003CD8C3  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
003CD8CA  41 8D 49 34                     lea ecx, [r9 + 0x34]
003CD8CE  E8 8D FD 12 00                  call 0x1404fd660
003CD8D3  CC                              int3
003CD8D4  45 33 C9                        xor r9d, r9d
003CD8D7  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
003CD8DC  BA 9D 0B 00 00                  mov edx, 0xb9d
003CD8E1  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
003CD8E8  41 8D 49 34                     lea ecx, [r9 + 0x34]
003CD8EC  E8 6F FD 12 00                  call 0x1404fd660
003CD8F1  CC                              int3
003CD8F2  4C 39 5B 08                     cmp qword ptr [rbx + 8], r11
003CD8F6  0F 84 60 FF FF FF               je 0x1403cd85c
003CD8FC  83 8B 98 00 00 00 10            or dword ptr [rbx + 0x98], 0x10
003CD903  E9 44 FD FF FF                  jmp 0x1403cd64c
003CD908  48 8D 83 E8 00 00 00            lea rax, [rbx + 0xe8]
003CD90F  48 39 00                        cmp qword ptr [rax], rax
003CD912  0F 84 B4 AF 31 00               je 0x1406e88cc
003CD918  48 8D 4E 08                     lea rcx, [rsi + 8]
003CD91C  45 33 C0                        xor r8d, r8d
003CD91F  33 D2                           xor edx, edx
003CD921  E8 EA 19 F7 FF                  call 0x14033f310
003CD926  E9 53 FF FF FF                  jmp 0x1403cd87e
003CD92B  48 8B 83 18 01 00 00            mov rax, qword ptr [rbx + 0x118]
003CD932  48 89 06                        mov qword ptr [rsi], rax
003CD935  48 89 B3 18 01 00 00            mov qword ptr [rbx + 0x118], rsi
003CD93C  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
003CD941  F6 40 34 10                     test byte ptr [rax + 0x34], 0x10
003CD945  0F B6 45 58                     movzx eax, byte ptr [rbp + 0x58]
003CD949  41 0F 45 C6                     cmovne eax, r14d
003CD94D  88 45 58                        mov byte ptr [rbp + 0x58], al
003CD950  E9 20 FD FF FF                  jmp 0x1403cd675
003CD955  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003CD95F  48 39 43 28                     cmp qword ptr [rbx + 0x28], rax
003CD963  0F 85 04 FE FF FF               jne 0x1403cd76d
003CD969  E9 31 FD FF FF                  jmp 0x1403cd69f
003CD96E  8B 83 98 00 00 00               mov eax, dword ptr [rbx + 0x98]
003CD974  A8 20                           test al, 0x20
003CD976  0F 85 BE FE FF FF               jne 0x1403cd83a
003CD97C  45 8A CE                        mov r9b, r14b
003CD97F  45 8A C6                        mov r8b, r14b
003CD982  E9 B9 FE FF FF                  jmp 0x1403cd840
003CD987  48 8D 4E 08                     lea rcx, [rsi + 8]
003CD98B  45 33 C0                        xor r8d, r8d
003CD98E  33 D2                           xor edx, edx
003CD990  E8 7B 19 F7 FF                  call 0x14033f310
003CD995  E9 B7 FD FF FF                  jmp 0x1403cd751
003CD99A  41 8A D6                        mov dl, r14b
003CD99D  48 8B CF                        mov rcx, rdi
003CD9A0  E8 EF 93 FB FF                  call 0x140386d94
003CD9A5  E9 26 FD FF FF                  jmp 0x1403cd6d0
003CD9AA  BA 44 66 6C 74                  mov edx, 0x746c6644
003CD9AF  49 8B CC                        mov rcx, r12
003CD9B2  E8 29 9F F2 FF                  call 0x1402f78e0
003CD9B7  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
003CD9BB  48 85 C9                        test rcx, rcx
003CD9BE  0F 84 51 AF 31 00               je 0x1406e8915
003CD9C4  E8 AF BF F7 FF                  call 0x140349978
003CD9C9  90                              nop
003CD9CA  E9 46 AF 31 00                  jmp 0x1406e8915
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcUninitializeCacheMap(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (128);
    result = 0;
    a1 = 0;
    v_stack_m70 = 0;
    v_stack_p8 = 0;
    v_stack_m88 = 0;
    v_stack_p20 = 0;
    v_stack_m58 = 0;
    v_stack_m40 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m68 = v_xmm1;
    v_stack_m50 = v_xmm0;
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10766164, v_stack_m80, a3, a4);
    v_r11 = 0;
    result = *(unsigned __int64 *)(a1 + 40);
    v_rdi = 0;
    v_r13 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) != 0) {
        v_rdi = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 536);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8);
        result = CcGetPrivateVolumeCacheMap(a1, v_stack_m80, a3, a4);
        a2 = result;
        a1 = v_rdi;
        v_r13 = result;
        result = CcReferencePartitionAndPrivateVolumeCacheMap(a1, a2, a3, a4);
        a1 = v_rdi + 768;
        a2 = v_stack_m68;
        result = KeAcquireInStackQueuedSpinLock(a1, a2, a3, a4);
        v_r11 = 0;
    }
    if (*(unsigned __int64 *)(a1 + 48) == 0) goto loc_003CD63A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 8)) != a1) goto loc_003CD8D4;
    if (v_rdi == 0) goto loc_003CD8B6;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 4))) - 1);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 4) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 96) + 8)) != (*(unsigned __int64 *)(a1 + 48) + 96)) goto loc_003CD612;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 96 + 8))) != (*(unsigned __int64 *)(a1 + 48) + 96)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 96);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 96) + 8) = a1;
    if ((*(unsigned __int64 *)(a1 + 48)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 384)) goto loc_003CD72A;
loc_003CD630:
    *(unsigned __int64 *)(a1 + 48) = 0;
loc_003CD63A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) == 0) goto loc_003CD736;
    if (a2 != 0) goto loc_003CD850;
loc_003CD64C:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 4)) != 0) goto loc_003CD875;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 232)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 232)) goto loc_003CD70C;
    if (a3 != 0) goto loc_003CD92B;
loc_003CD675:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 152)))) & (4)) == 0) goto loc_003CD760;
loc_003CD683:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 152)))) & (32)) != 0) goto loc_003CD775;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 112)) != 0) goto loc_003CD76D;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 112)) < 0) goto loc_003CD955;
loc_003CD69F:
    a4 = 0;
    v_stack_m98 = 0;
    result = CcDeleteSharedCacheMap(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8), v_stack_m80, v_stack_m68, a4);
    v_stack_p20 = 0;
loc_003CD6BE:
    result = CcFreePrivateCacheMapIgnoreNull(*(unsigned __int64 *)(a1 + 48), v_stack_m80, v_stack_m68, a4);
    if (v_stack_p20 != 0) goto loc_003CD99A;
loc_003CD6D0:
    if (v_stack_m88 != 0) goto loc_003CD9AA;
    if (v_rdi != 0) {
        a2 = v_r13;
        a1 = v_rdi;
        result = CcDereferencePartitionAndPrivateVolumeCacheMap(a1, a2, v_stack_m68, a4);
    }
    v_rsp = (v_rsp) + (128);
    return 1;
loc_003CD70C:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0xC40ULL), 0xFFFFFFFFC0000420ULL, a4);
loc_003CD72A:
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 48)) = 0;
    goto loc_003CD630;
loc_003CD736:
    if (1 != 0) goto loc_003CD7F0;
loc_003CD73F:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, (unsigned int)(0xC40ULL), 0xFFFFFFFFC0000420ULL, a4);
loc_003CD748:
    if (1 != 0) goto loc_003CD987;
loc_003CD751:
loc_003CD757:
    goto loc_003CD6BE;
loc_003CD760:
    if (v_stack_p8 != 0) goto loc_003CD683;
    if ((((unsigned __int8)(result)) & (32)) == 0) {
        a1 = v_stack_p10;
        result = CcInsertIntoDirtySharedCacheMapList(a1, (unsigned int)(0xC40ULL), 0xFFFFFFFFC0000420ULL, a4);
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11109389)) == 0) goto loc_003CD7E1;
    result = (*(unsigned __int64 *)(v_stack_p10 + 600)) + (986);
loc_003CD78C:
    *(unsigned __int8 *)(result) = 1;
    if ((*(unsigned __int8 *)(v_rdi + 1294)) == 0) goto loc_003CD831;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11109389)) == 0) goto loc_003CD895;
    result = CcNotifyWriteBehindVolume(v_r13, 8, 0xFFFFFFFFC0000420ULL, a4);
    if ((*(unsigned __int8 *)(v_r13 + 1172)) == 0) {
        *(unsigned __int8 *)(v_r13 + 985) = 1;
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_m68, 8, 0xFFFFFFFFC0000420ULL, a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, 8, 0xFFFFFFFFC0000420ULL, a4);
    goto loc_003CD757;
loc_003CD7E1:
    result = (*(unsigned __int64 *)(v_stack_p10 + 536)) + (0x41AULL);
    goto loc_003CD78C;
loc_003CD7F0:
    if ((*(unsigned __int64 *)(1)) != 0) goto loc_003CD73F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40))) == 0) goto loc_003CD73F;
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, 8, 0xFFFFFFFFC0000420ULL, a4);
    a4 = 0;
    a3 = 0;
    result = CcPurgeCacheSection(*(unsigned __int64 *)(a1 + 40), 1, a3, a4);
    goto loc_003CD748;
loc_003CD831:
    if (v_stack_p8 != 0) goto loc_003CD96E;
loc_003CD83A:
    a4 = 0;
    a3 = 0;
loc_003CD840:
    result = CcScheduleLazyWriteScan(v_rdi, v_r13, a3, a4);
    goto loc_003CD7CA;
loc_003CD850:
    if (*(unsigned __int64 *)(1) == 0) goto loc_003CD8F2;
loc_003CD85C:
    if ((*(unsigned __int64 *)(v_stack_p10 + 232)) != (v_stack_p10 + 232)) goto loc_003CD64C;
    *(unsigned __int64 *)(v_stack_p10 + 8) = *(unsigned __int64 *)(1);
    goto loc_003CD64C;
loc_003CD875:
    if (v_stack_p8 != 0) goto loc_003CD908;
loc_003CD87E:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m68, v_r13, a3, a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, v_r13, a3, a4);
    goto loc_003CD751;
loc_003CD895:
    result = CcNotifyWriteBehindInternal(v_rdi, v_r13, a3, a4);
    if ((*(unsigned __int8 *)(v_rdi + 1292)) != 0) goto loc_003CD7CA;
    *(unsigned __int8 *)(v_rdi + 1049) = 1;
    goto loc_003CD7CA;
loc_003CD8B6:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0xBA3ULL), 0xFFFFFFFFC0000420ULL, a4);
loc_003CD8D4:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0xB9DULL), 0xFFFFFFFFC0000420ULL, a4);
loc_003CD8F2:
    if ((*(unsigned __int64 *)(v_stack_p10 + 8)) == 0) goto loc_003CD85C;
    goto loc_003CD64C;
loc_003CD908:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_stack_p8 + 8, a2, a3, a4);
    goto loc_003CD87E;
loc_003CD92B:
    *(unsigned __int64 *)(v_stack_p8) = *(unsigned __int64 *)(v_stack_p10 + 280);
    *(unsigned __int64 *)(v_stack_p10 + 280) = v_stack_p8;
    result = v_stack_p20;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 52)) & (16)) != 0) { result = 1; }
    v_stack_p20 = (unsigned __int8)(result);
    goto loc_003CD675;
loc_003CD955:
    if ((*(unsigned __int64 *)(v_stack_p10 + 40)) != result) goto loc_003CD76D;
    goto loc_003CD69F;
loc_003CD96E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 152)))) & (32)) != 0) goto loc_003CD83A;
    goto loc_003CD840;
loc_003CD987:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_stack_p8 + 8, a2, a3, 1);
    goto loc_003CD751;
loc_003CD99A:
    result = CcAdjustWriteBehindThreadPoolIfNeeded(v_rdi, 1, a3, 1);
    goto loc_003CD6D0;
loc_003CD9AA:
    result = ObfDereferenceObjectWithTag(a1, (unsigned int)(0x746C6644ULL), a3, 1);
    result = IoDiskIoAttributionDereference(*(unsigned __int64 *)(v_stack_p10 + 24), (unsigned int)(0x746C6644ULL), a3, 1);
}
```

## 5. (Beta) C Style

```c
int64_t CcUninitializeCacheMap(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (128);
    result = 0;
    Arg1 = 0;
    v_stack_m70 = 0;
    v_stack_p8 = 0;
    v_stack_m88 = 0;
    v_stack_p20 = 0;
    v_stack_m58 = 0;
    v_stack_m40 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m68 = v_xmm1;
    v_stack_m50 = v_xmm0;
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10766164, v_stack_m80, Arg3, Arg4);
    local_r11 = 0;
    result = *(uint64_t *)(arg1 + 0x28);
    local_rdi = 0;
    local_r13 = 0;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) != 0) {
        local_rdi = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x218);
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8);
        result = CcGetPrivateVolumeCacheMap(Arg1, v_stack_m80, Arg3, Arg4);
        Arg2 = result;
        Arg1 = local_rdi;
        local_r13 = result;
        result = CcReferencePartitionAndPrivateVolumeCacheMap(Arg1, Arg2, Arg3, Arg4);
        Arg1 = local_rdi + 768;
        Arg2 = v_stack_m68;
        result = KeAcquireInStackQueuedSpinLock(Arg1, Arg2, Arg3, Arg4);
        local_r11 = 0;
    }
    if (*(uint64_t *)(arg1 + 0x30) == 0) goto loc_003CD63A;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x8)) != Arg1) goto loc_003CD8D4;
    if (local_rdi == 0) goto loc_003CD8B6;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x4))) - 1);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x4) = (uint32_t)(result);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x60) + 0x8)) != (*(uint64_t *)(arg1 + 0x30) + 96)) goto loc_003CD612;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x60 + 0x8))) != (*(uint64_t *)(arg1 + 0x30) + 96)) {
        Arg1 = 3;
    }
    *(uint64_t *)(arg1) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x60);
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x60) + 0x8) = Arg1;
    if ((*(uint64_t *)(arg1 + 0x30)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 384)) goto loc_003CD72A;
loc_003CD630:
    *(uint64_t *)(arg1 + 0x30) = 0;
loc_003CD63A:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) == 0) goto loc_003CD736;
    if (Arg2 != 0) goto loc_003CD850;
loc_003CD64C:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x4)) != 0) goto loc_003CD875;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0xE8)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 232)) goto loc_003CD70C;
    if (Arg3 != 0) goto loc_003CD92B;
loc_003CD675:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x98)))) & (4)) == 0) goto loc_003CD760;
loc_003CD683:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x98)))) & (32)) != 0) goto loc_003CD775;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x70)) != 0) goto loc_003CD76D;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x70)) < 0) goto loc_003CD955;
loc_003CD69F:
    Arg4 = 0;
    v_stack_m98 = 0;
    result = CcDeleteSharedCacheMap(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8), v_stack_m80, v_stack_m68, Arg4);
    v_stack_p20 = 0;
loc_003CD6BE:
    result = CcFreePrivateCacheMapIgnoreNull(*(uint64_t *)(arg1 + 0x30), v_stack_m80, v_stack_m68, Arg4);
    if (v_stack_p20 != 0) goto loc_003CD99A;
loc_003CD6D0:
    if (v_stack_m88 != 0) goto loc_003CD9AA;
    if (local_rdi != 0) {
        Arg2 = local_r13;
        Arg1 = local_rdi;
        result = CcDereferencePartitionAndPrivateVolumeCacheMap(Arg1, Arg2, v_stack_m68, Arg4);
    }
    local_rsp = (local_rsp) + (128);
    return 1;
loc_003CD70C:
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 52, (uint32_t)(0xC40ULL), 0xFFFFFFFFC0000420ULL, Arg4);
loc_003CD72A:
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x30)) = 0;
    goto loc_003CD630;
loc_003CD736:
    if (1 != 0) goto loc_003CD7F0;
loc_003CD73F:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, (uint32_t)(0xC40ULL), 0xFFFFFFFFC0000420ULL, Arg4);
loc_003CD748:
    if (1 != 0) goto loc_003CD987;
loc_003CD751:
loc_003CD757:
    goto loc_003CD6BE;
loc_003CD760:
    if (v_stack_p8 != 0) goto loc_003CD683;
    if ((((uint8_t)(result)) & (32)) == 0) {
        Arg1 = v_stack_p10;
        result = CcInsertIntoDirtySharedCacheMapList(Arg1, (uint32_t)(0xC40ULL), 0xFFFFFFFFC0000420ULL, Arg4);
    }
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xA9840D)) == 0) goto loc_003CD7E1;
    result = (*(uint64_t *)(v_stack_p10 + 0x258)) + (986);
loc_003CD78C:
    *(uint8_t *)(result) = 1;
    if ((*(uint8_t *)(local_rdi + 0x50E)) == 0) goto loc_003CD831;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xA9840D)) == 0) goto loc_003CD895;
    result = CcNotifyWriteBehindVolume(local_r13, 8, 0xFFFFFFFFC0000420ULL, Arg4);
    if ((*(uint8_t *)(local_r13 + 0x494)) == 0) {
        *(uint8_t *)(local_r13 + 0x3D9) = 1;
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_m68, 8, 0xFFFFFFFFC0000420ULL, Arg4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, 8, 0xFFFFFFFFC0000420ULL, Arg4);
    goto loc_003CD757;
loc_003CD7E1:
    result = (*(uint64_t *)(v_stack_p10 + 0x218)) + (0x41AULL);
    goto loc_003CD78C;
loc_003CD7F0:
    if ((*(uint64_t *)(1)) != 0) goto loc_003CD73F;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x28))) == 0) goto loc_003CD73F;
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, 8, 0xFFFFFFFFC0000420ULL, Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = CcPurgeCacheSection(*(uint64_t *)(arg1 + 0x28), 1, Arg3, Arg4);
    goto loc_003CD748;
loc_003CD831:
    if (v_stack_p8 != 0) goto loc_003CD96E;
loc_003CD83A:
    Arg4 = 0;
    Arg3 = 0;
loc_003CD840:
    result = CcScheduleLazyWriteScan(local_rdi, local_r13, Arg3, Arg4);
    goto loc_003CD7CA;
loc_003CD850:
    if (*(uint64_t *)(1) == 0) goto loc_003CD8F2;
loc_003CD85C:
    if ((*(uint64_t *)(v_stack_p10 + 0xE8)) != (v_stack_p10 + 232)) goto loc_003CD64C;
    *(uint64_t *)(v_stack_p10 + 0x8) = *(uint64_t *)(1);
    goto loc_003CD64C;
loc_003CD875:
    if (v_stack_p8 != 0) goto loc_003CD908;
loc_003CD87E:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m68, local_r13, Arg3, Arg4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, local_r13, Arg3, Arg4);
    goto loc_003CD751;
loc_003CD895:
    result = CcNotifyWriteBehindInternal(local_rdi, local_r13, Arg3, Arg4);
    if ((*(uint8_t *)(local_rdi + 0x50C)) != 0) goto loc_003CD7CA;
    *(uint8_t *)(local_rdi + 0x419) = 1;
    goto loc_003CD7CA;
loc_003CD8B6:
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 52, (uint32_t)(0xBA3ULL), 0xFFFFFFFFC0000420ULL, Arg4);
loc_003CD8D4:
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 52, (uint32_t)(0xB9DULL), 0xFFFFFFFFC0000420ULL, Arg4);
loc_003CD8F2:
    if ((*(uint64_t *)(v_stack_p10 + 0x8)) == 0) goto loc_003CD85C;
    goto loc_003CD64C;
loc_003CD908:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_stack_p8 + 8, Arg2, Arg3, Arg4);
    goto loc_003CD87E;
loc_003CD92B:
    *(uint64_t *)(v_stack_p8) = *(uint64_t *)(v_stack_p10 + 0x118);
    *(uint64_t *)(v_stack_p10 + 0x118) = v_stack_p8;
    result = v_stack_p20;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34)) & (16)) != 0) { result = 1; }
    v_stack_p20 = (uint8_t)(result);
    goto loc_003CD675;
loc_003CD955:
    if ((*(uint64_t *)(v_stack_p10 + 0x28)) != result) goto loc_003CD76D;
    goto loc_003CD69F;
loc_003CD96E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x98)))) & (32)) != 0) goto loc_003CD83A;
    goto loc_003CD840;
loc_003CD987:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_stack_p8 + 8, Arg2, Arg3, 1);
    goto loc_003CD751;
loc_003CD99A:
    result = CcAdjustWriteBehindThreadPoolIfNeeded(local_rdi, 1, Arg3, 1);
    goto loc_003CD6D0;
loc_003CD9AA:
    result = ObfDereferenceObjectWithTag(Arg1, (uint32_t)(0x746C6644ULL), Arg3, 1);
    result = IoDiskIoAttributionDereference(*(uint64_t *)(v_stack_p10 + 0x18), (uint32_t)(0x746C6644ULL), Arg3, 1);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003CD520&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
