# DifExTryToAcquireFastMutexWrapper

- RVA: `0x00623250`–`0x006233AF` (길이 `351` bytes)
- VA: `0x0000000140623250`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062327F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006232A7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006232D5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006232FC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00623315` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062331D` → [ExTryToAcquireFastMutex](../44/ExTryToAcquireFastMutex_function_0044C2E0.md) (function, `0x0044C2E0`)
- `0x0062334A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00623371` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062338A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006232B9` → RVA `0x00F048B8` (`.data`; read)
- `0x006232C2` → RVA `0x00F04980` (`.data`; read)
- `0x006232CE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00623250  4C 8B DC                        mov r11, rsp
00623253  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00623257  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062325B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062325F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00623263  41 56                           push r14
00623265  48 83 EC 40                     sub rsp, 0x40
00623269  33 C0                           xor eax, eax
0062326B  0F 57 C0                        xorps xmm0, xmm0
0062326E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00623273  48 8B E9                        mov rbp, rcx
00623276  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062327A  B9 7F 01 00 00                  mov ecx, 0x17f
0062327F  E8 B0 27 E7 FF                  call 0x140495a34
00623284  48 8B F0                        mov rsi, rax
00623287  48 85 C0                        test rax, rax
0062328A  0F 84 8A 00 00 00               je 0x14062331a
00623290  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00623293  A8 18                           test al, 0x18
00623295  74 0C                           je 0x1406232a3
00623297  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062329C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006232A1  EB 0E                           jmp 0x1406232b1
006232A3  A8 04                           test al, 4
006232A5  74 0A                           je 0x1406232b1
006232A7  E8 5C 09 EB FF                  call 0x1404d3c08
006232AC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006232B1  40 32 FF                        xor dil, dil
006232B4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006232B9  40 38 3D F8 15 8E 00            cmp byte ptr [rip + 0x8e15f8], dil
006232C0  75 0C                           jne 0x1406232ce
006232C2  F7 05 B4 16 8E 00 00 08 00 00   test dword ptr [rip + 0x8e16b4], 0x800
006232CC  74 13                           je 0x1406232e1
006232CE  48 8D 0D AB 0B 8E 00            lea rcx, [rip + 0x8e0bab]
006232D5  E8 46 33 BF FF                  call 0x140216620
006232DA  40 8A F8                        mov dil, al
006232DD  84 C0                           test al, al
006232DF  74 39                           je 0x14062331a
006232E1  4C 8D 76 20                     lea r14, [rsi + 0x20]
006232E5  49 8B 1E                        mov rbx, qword ptr [r14]
006232E8  EB 1A                           jmp 0x140623304
006232EA  48 8D 43 F0                     lea rax, [rbx - 0x10]
006232EE  48 85 C0                        test rax, rax
006232F1  74 0E                           je 0x140623301
006232F3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006232F7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006232FC  E8 CF 77 09 00                  call 0x1406baad0
00623301  48 8B 1B                        mov rbx, qword ptr [rbx]
00623304  49 3B DE                        cmp rbx, r14
00623307  75 E1                           jne 0x1406232ea
00623309  40 84 FF                        test dil, dil
0062330C  74 0C                           je 0x14062331a
0062330E  48 8D 0D 6B 0B 8E 00            lea rcx, [rip + 0x8e0b6b]
00623315  E8 66 6B D2 FF                  call 0x140349e80
0062331A  48 8B CD                        mov rcx, rbp
0062331D  E8 BE 8F E2 FF                  call 0x14044c2e0
00623322  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00623326  48 85 F6                        test rsi, rsi
00623329  74 64                           je 0x14062338f
0062332B  40 32 FF                        xor dil, dil
0062332E  40 38 3D 83 15 8E 00            cmp byte ptr [rip + 0x8e1583], dil
00623335  75 0C                           jne 0x140623343
00623337  F7 05 3F 16 8E 00 00 08 00 00   test dword ptr [rip + 0x8e163f], 0x800
00623341  74 13                           je 0x140623356
00623343  48 8D 0D 36 0B 8E 00            lea rcx, [rip + 0x8e0b36]
0062334A  E8 D1 32 BF FF                  call 0x140216620
0062334F  40 8A F8                        mov dil, al
00623352  84 C0                           test al, al
00623354  74 39                           je 0x14062338f
00623356  48 83 C6 30                     add rsi, 0x30
0062335A  48 8B 1E                        mov rbx, qword ptr [rsi]
0062335D  EB 1A                           jmp 0x140623379
0062335F  48 8D 43 F0                     lea rax, [rbx - 0x10]
00623363  48 85 C0                        test rax, rax
00623366  74 0E                           je 0x140623376
00623368  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062336C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00623371  E8 5A 77 09 00                  call 0x1406baad0
00623376  48 8B 1B                        mov rbx, qword ptr [rbx]
00623379  48 3B DE                        cmp rbx, rsi
0062337C  75 E1                           jne 0x14062335f
0062337E  40 84 FF                        test dil, dil
00623381  74 0C                           je 0x14062338f
00623383  48 8D 0D F6 0A 8E 00            lea rcx, [rip + 0x8e0af6]
0062338A  E8 F1 6A D2 FF                  call 0x140349e80
0062338F  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00623393  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00623398  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062339D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006233A2  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
006233A7  48 83 C4 40                     add rsp, 0x40
006233AB  41 5E                           pop r14
006233AD  C3                              ret
006233AE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExTryToAcquireFastMutexWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(383, a2, a3, a4);
    if (result == 0) goto loc_0062331A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006232A3;
    v_stack_m28 = v_stack_p0;
    goto loc_006232B1;
loc_006232A3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9311736)) != 0) goto loc_006232CE;
    if (((*(unsigned int *)(v_rip + 9311924)) & (0x800ULL)) == 0) goto loc_006232E1;
loc_006232CE:
    result = ExAcquireRundownProtection(v_rip + 9309099, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062331A;
loc_006232E1:
    goto loc_00623304;
loc_006232EA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00623304:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006232EA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9309035;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExTryToAcquireFastMutex(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_0062338F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9311619)) != 0) goto loc_00623343;
    if (((*(unsigned int *)(v_rip + 9311807)) & (0x800ULL)) == 0) goto loc_00623356;
loc_00623343:
    result = ExAcquireRundownProtection(v_rip + 9308982, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062338F;
loc_00623356:
    v_rsi = (result) + (48);
    goto loc_00623379;
loc_0062335F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00623379:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062335F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9308918;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExTryToAcquireFastMutexWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(383, a2, a3, a4);
    if (result == 0) goto loc_0062331A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006232A3;
    v_stack_m28 = v_stack_p0;
    goto loc_006232B1;
loc_006232A3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E15F8)) != 0) goto loc_006232CE;
    if (((*(uint32_t *)(v_rip + 0x8E16B4)) & (0x800ULL)) == 0) goto loc_006232E1;
loc_006232CE:
    result = ExAcquireRundownProtection(v_rip + 9309099, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062331A;
loc_006232E1:
    goto loc_00623304;
loc_006232EA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00623304:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006232EA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9309035;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExTryToAcquireFastMutex(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_0062338F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E1583)) != 0) goto loc_00623343;
    if (((*(uint32_t *)(v_rip + 0x8E163F)) & (0x800ULL)) == 0) goto loc_00623356;
loc_00623343:
    result = ExAcquireRundownProtection(v_rip + 9308982, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062338F;
loc_00623356:
    local_rsi = (result) + (48);
    goto loc_00623379;
loc_0062335F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00623379:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062335F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9308918;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00623250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00623250[BB_00623250]
  bb_00623290[BB_00623290]
  bb_00623297[BB_00623297]
  bb_006232A3[BB_006232A3]
  bb_006232A7[BB_006232A7]
  bb_006232B1[BB_006232B1]
  bb_006232C2[BB_006232C2]
  bb_006232CE[BB_006232CE]
  bb_006232E1[BB_006232E1]
  bb_006232EA[BB_006232EA]
  bb_006232F3[BB_006232F3]
  bb_00623301[BB_00623301]
  bb_00623304[BB_00623304]
  bb_00623309[BB_00623309]
  bb_0062330E[BB_0062330E]
  bb_0062331A[BB_0062331A]
  bb_0062332B[BB_0062332B]
  bb_00623337[BB_00623337]
  bb_00623343[BB_00623343]
  bb_00623356[BB_00623356]
  bb_0062335F[BB_0062335F]
  bb_00623368[BB_00623368]
  bb_00623376[BB_00623376]
  bb_00623379[BB_00623379]
  bb_0062337E[BB_0062337E]
  bb_00623383[BB_00623383]
  bb_0062338F[BB_0062338F]
  bb_006233AE[BB_006233AE]
  bb_00623250 -->|branch| bb_0062331A
  bb_00623250 -->|fallthrough| bb_00623290
  bb_00623290 -->|branch| bb_006232A3
  bb_00623290 -->|fallthrough| bb_00623297
  bb_00623297 -->|branch| bb_006232B1
  bb_006232A3 -->|branch| bb_006232B1
  bb_006232A3 -->|fallthrough| bb_006232A7
  bb_006232A7 -->|flow| bb_006232B1
  bb_006232B1 -->|branch| bb_006232CE
  bb_006232B1 -->|fallthrough| bb_006232C2
  bb_006232C2 -->|branch| bb_006232E1
  bb_006232C2 -->|fallthrough| bb_006232CE
  bb_006232CE -->|branch| bb_0062331A
  bb_006232CE -->|fallthrough| bb_006232E1
  bb_006232E1 -->|branch| bb_00623304
  bb_006232EA -->|branch| bb_00623301
  bb_006232EA -->|fallthrough| bb_006232F3
  bb_006232F3 -->|flow| bb_00623301
  bb_00623301 -->|flow| bb_00623304
  bb_00623304 -->|branch| bb_006232EA
  bb_00623304 -->|fallthrough| bb_00623309
  bb_00623309 -->|branch| bb_0062331A
  bb_00623309 -->|fallthrough| bb_0062330E
  bb_0062330E -->|flow| bb_0062331A
  bb_0062331A -->|branch| bb_0062338F
  bb_0062331A -->|fallthrough| bb_0062332B
  bb_0062332B -->|branch| bb_00623343
  bb_0062332B -->|fallthrough| bb_00623337
  bb_00623337 -->|branch| bb_00623356
  bb_00623337 -->|fallthrough| bb_00623343
  bb_00623343 -->|branch| bb_0062338F
  bb_00623343 -->|fallthrough| bb_00623356
  bb_00623356 -->|branch| bb_00623379
  bb_0062335F -->|branch| bb_00623376
  bb_0062335F -->|fallthrough| bb_00623368
  bb_00623368 -->|flow| bb_00623376
  bb_00623376 -->|flow| bb_00623379
  bb_00623379 -->|branch| bb_0062335F
  bb_00623379 -->|fallthrough| bb_0062337E
  bb_0062337E -->|branch| bb_0062338F
  bb_0062337E -->|fallthrough| bb_00623383
  bb_00623383 -->|flow| bb_0062338F
```
