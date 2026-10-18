# DifMmFreeContiguousMemoryWrapper

- RVA: `0x006351F0`–`0x00635340` (길이 `336` bytes)
- VA: `0x00000001406351F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00635218` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00635240` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063526E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00635295` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006352AE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006352B6` → [MmFreeContiguousMemory](../3F/MmFreeContiguousMemory_function_003F6F60.md) (function, `0x003F6F60`)
- `0x006352DF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00635306` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063531F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00635252` → RVA `0x00F048B8` (`.data`; read)
- `0x0063525B` → RVA `0x00F04980` (`.data`; read)
- `0x00635267` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006351F0  48 8B C4                        mov rax, rsp
006351F3  48 89 58 08                     mov qword ptr [rax + 8], rbx
006351F7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
006351FB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006351FF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00635203  41 56                           push r14
00635205  48 83 EC 30                     sub rsp, 0x30
00635209  48 8B E9                        mov rbp, rcx
0063520C  0F 57 C0                        xorps xmm0, xmm0
0063520F  B9 E2 00 00 00                  mov ecx, 0xe2
00635214  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00635218  E8 17 08 E6 FF                  call 0x140495a34
0063521D  48 8B F8                        mov rdi, rax
00635220  48 85 C0                        test rax, rax
00635223  0F 84 8A 00 00 00               je 0x1406352b3
00635229  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063522C  A8 18                           test al, 0x18
0063522E  74 0C                           je 0x14063523c
00635230  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00635235  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063523A  EB 0E                           jmp 0x14063524a
0063523C  A8 04                           test al, 4
0063523E  74 0A                           je 0x14063524a
00635240  E8 C3 E9 E9 FF                  call 0x1404d3c08
00635245  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063524A  40 32 F6                        xor sil, sil
0063524D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00635252  40 38 35 5F F6 8C 00            cmp byte ptr [rip + 0x8cf65f], sil
00635259  75 0C                           jne 0x140635267
0063525B  F7 05 1B F7 8C 00 00 08 00 00   test dword ptr [rip + 0x8cf71b], 0x800
00635265  74 13                           je 0x14063527a
00635267  48 8D 0D 12 EC 8C 00            lea rcx, [rip + 0x8cec12]
0063526E  E8 AD 13 BE FF                  call 0x140216620
00635273  40 8A F0                        mov sil, al
00635276  84 C0                           test al, al
00635278  74 39                           je 0x1406352b3
0063527A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0063527E  49 8B 1E                        mov rbx, qword ptr [r14]
00635281  EB 1A                           jmp 0x14063529d
00635283  48 8D 43 F0                     lea rax, [rbx - 0x10]
00635287  48 85 C0                        test rax, rax
0063528A  74 0E                           je 0x14063529a
0063528C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00635290  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00635295  E8 36 58 08 00                  call 0x1406baad0
0063529A  48 8B 1B                        mov rbx, qword ptr [rbx]
0063529D  49 3B DE                        cmp rbx, r14
006352A0  75 E1                           jne 0x140635283
006352A2  40 84 F6                        test sil, sil
006352A5  74 0C                           je 0x1406352b3
006352A7  48 8D 0D D2 EB 8C 00            lea rcx, [rip + 0x8cebd2]
006352AE  E8 CD 4B D1 FF                  call 0x140349e80
006352B3  48 8B CD                        mov rcx, rbp
006352B6  E8 A5 1C DC FF                  call 0x1403f6f60
006352BB  48 85 FF                        test rdi, rdi
006352BE  74 64                           je 0x140635324
006352C0  40 32 F6                        xor sil, sil
006352C3  40 38 35 EE F5 8C 00            cmp byte ptr [rip + 0x8cf5ee], sil
006352CA  75 0C                           jne 0x1406352d8
006352CC  F7 05 AA F6 8C 00 00 08 00 00   test dword ptr [rip + 0x8cf6aa], 0x800
006352D6  74 13                           je 0x1406352eb
006352D8  48 8D 0D A1 EB 8C 00            lea rcx, [rip + 0x8ceba1]
006352DF  E8 3C 13 BE FF                  call 0x140216620
006352E4  40 8A F0                        mov sil, al
006352E7  84 C0                           test al, al
006352E9  74 39                           je 0x140635324
006352EB  48 83 C7 30                     add rdi, 0x30
006352EF  48 8B 1F                        mov rbx, qword ptr [rdi]
006352F2  EB 1A                           jmp 0x14063530e
006352F4  48 8D 43 F0                     lea rax, [rbx - 0x10]
006352F8  48 85 C0                        test rax, rax
006352FB  74 0E                           je 0x14063530b
006352FD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00635301  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00635306  E8 C5 57 08 00                  call 0x1406baad0
0063530B  48 8B 1B                        mov rbx, qword ptr [rbx]
0063530E  48 3B DF                        cmp rbx, rdi
00635311  75 E1                           jne 0x1406352f4
00635313  40 84 F6                        test sil, sil
00635316  74 0C                           je 0x140635324
00635318  48 8D 0D 61 EB 8C 00            lea rcx, [rip + 0x8ceb61]
0063531F  E8 5C 4B D1 FF                  call 0x140349e80
00635324  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00635329  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0063532E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00635333  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00635338  48 83 C4 30                     add rsp, 0x30
0063533C  41 5E                           pop r14
0063533E  C3                              ret
0063533F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmFreeContiguousMemoryWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(226, a2, a3, a4);
    if (result == 0) goto loc_006352B3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063523C;
    v_stack_m18 = v_stack_p0;
    goto loc_0063524A;
loc_0063523C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9238111)) != 0) goto loc_00635267;
    if (((*(unsigned int *)(v_rip + 9238299)) & (0x800ULL)) == 0) goto loc_0063527A;
loc_00635267:
    result = ExAcquireRundownProtection(v_rip + 9235474, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006352B3;
loc_0063527A:
    goto loc_0063529D;
loc_00635283:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063529D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00635283;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9235410;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmFreeContiguousMemory(a1, a2, a3, a4);
    if (result == 0) goto loc_00635324;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9237998)) != 0) goto loc_006352D8;
    if (((*(unsigned int *)(v_rip + 9238186)) & (0x800ULL)) == 0) goto loc_006352EB;
loc_006352D8:
    result = ExAcquireRundownProtection(v_rip + 9235361, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00635324;
loc_006352EB:
    v_rdi = (result) + (48);
    goto loc_0063530E;
loc_006352F4:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063530E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_006352F4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9235297;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmFreeContiguousMemoryWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(226, a2, a3, a4);
    if (result == 0) goto loc_006352B3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063523C;
    v_stack_m18 = v_stack_p0;
    goto loc_0063524A;
loc_0063523C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8CF65F)) != 0) goto loc_00635267;
    if (((*(uint32_t *)(v_rip + 0x8CF71B)) & (0x800ULL)) == 0) goto loc_0063527A;
loc_00635267:
    result = ExAcquireRundownProtection(v_rip + 9235474, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006352B3;
loc_0063527A:
    goto loc_0063529D;
loc_00635283:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063529D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00635283;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9235410;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = MmFreeContiguousMemory(Arg1, a2, a3, a4);
    if (result == 0) goto loc_00635324;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CF5EE)) != 0) goto loc_006352D8;
    if (((*(uint32_t *)(v_rip + 0x8CF6AA)) & (0x800ULL)) == 0) goto loc_006352EB;
loc_006352D8:
    result = ExAcquireRundownProtection(v_rip + 9235361, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00635324;
loc_006352EB:
    local_rdi = (result) + (48);
    goto loc_0063530E;
loc_006352F4:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063530E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_006352F4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9235297;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006351F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006351F0[BB_006351F0]
  bb_00635229[BB_00635229]
  bb_00635230[BB_00635230]
  bb_0063523C[BB_0063523C]
  bb_00635240[BB_00635240]
  bb_0063524A[BB_0063524A]
  bb_0063525B[BB_0063525B]
  bb_00635267[BB_00635267]
  bb_0063527A[BB_0063527A]
  bb_00635283[BB_00635283]
  bb_0063528C[BB_0063528C]
  bb_0063529A[BB_0063529A]
  bb_0063529D[BB_0063529D]
  bb_006352A2[BB_006352A2]
  bb_006352A7[BB_006352A7]
  bb_006352B3[BB_006352B3]
  bb_006352C0[BB_006352C0]
  bb_006352CC[BB_006352CC]
  bb_006352D8[BB_006352D8]
  bb_006352EB[BB_006352EB]
  bb_006352F4[BB_006352F4]
  bb_006352FD[BB_006352FD]
  bb_0063530B[BB_0063530B]
  bb_0063530E[BB_0063530E]
  bb_00635313[BB_00635313]
  bb_00635318[BB_00635318]
  bb_00635324[BB_00635324]
  bb_0063533F[BB_0063533F]
  bb_006351F0 -->|branch| bb_006352B3
  bb_006351F0 -->|fallthrough| bb_00635229
  bb_00635229 -->|branch| bb_0063523C
  bb_00635229 -->|fallthrough| bb_00635230
  bb_00635230 -->|branch| bb_0063524A
  bb_0063523C -->|branch| bb_0063524A
  bb_0063523C -->|fallthrough| bb_00635240
  bb_00635240 -->|flow| bb_0063524A
  bb_0063524A -->|branch| bb_00635267
  bb_0063524A -->|fallthrough| bb_0063525B
  bb_0063525B -->|branch| bb_0063527A
  bb_0063525B -->|fallthrough| bb_00635267
  bb_00635267 -->|branch| bb_006352B3
  bb_00635267 -->|fallthrough| bb_0063527A
  bb_0063527A -->|branch| bb_0063529D
  bb_00635283 -->|branch| bb_0063529A
  bb_00635283 -->|fallthrough| bb_0063528C
  bb_0063528C -->|flow| bb_0063529A
  bb_0063529A -->|flow| bb_0063529D
  bb_0063529D -->|branch| bb_00635283
  bb_0063529D -->|fallthrough| bb_006352A2
  bb_006352A2 -->|branch| bb_006352B3
  bb_006352A2 -->|fallthrough| bb_006352A7
  bb_006352A7 -->|flow| bb_006352B3
  bb_006352B3 -->|branch| bb_00635324
  bb_006352B3 -->|fallthrough| bb_006352C0
  bb_006352C0 -->|branch| bb_006352D8
  bb_006352C0 -->|fallthrough| bb_006352CC
  bb_006352CC -->|branch| bb_006352EB
  bb_006352CC -->|fallthrough| bb_006352D8
  bb_006352D8 -->|branch| bb_00635324
  bb_006352D8 -->|fallthrough| bb_006352EB
  bb_006352EB -->|branch| bb_0063530E
  bb_006352F4 -->|branch| bb_0063530B
  bb_006352F4 -->|fallthrough| bb_006352FD
  bb_006352FD -->|flow| bb_0063530B
  bb_0063530B -->|flow| bb_0063530E
  bb_0063530E -->|branch| bb_006352F4
  bb_0063530E -->|fallthrough| bb_00635313
  bb_00635313 -->|branch| bb_00635324
  bb_00635313 -->|fallthrough| bb_00635318
  bb_00635318 -->|flow| bb_00635324
```
