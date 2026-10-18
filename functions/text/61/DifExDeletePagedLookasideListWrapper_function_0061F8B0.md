# DifExDeletePagedLookasideListWrapper

- RVA: `0x0061F8B0`–`0x0061FA00` (길이 `336` bytes)
- VA: `0x000000014061F8B0`
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
- `0x0061F8D8` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061F900` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061F92E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061F955` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061F96E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061F976` → [ExDeletePagedLookasideList](../48/ExDeletePagedLookasideList_function_00481D20.md) (function, `0x00481D20`)
- `0x0061F99F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061F9C6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061F9DF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061F912` → RVA `0x00F048B8` (`.data`; read)
- `0x0061F91B` → RVA `0x00F04980` (`.data`; read)
- `0x0061F927` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061F8B0  48 8B C4                        mov rax, rsp
0061F8B3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0061F8B7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0061F8BB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0061F8BF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0061F8C3  41 56                           push r14
0061F8C5  48 83 EC 30                     sub rsp, 0x30
0061F8C9  48 8B E9                        mov rbp, rcx
0061F8CC  0F 57 C0                        xorps xmm0, xmm0
0061F8CF  B9 98 01 00 00                  mov ecx, 0x198
0061F8D4  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
0061F8D8  E8 57 61 E7 FF                  call 0x140495a34
0061F8DD  48 8B F8                        mov rdi, rax
0061F8E0  48 85 C0                        test rax, rax
0061F8E3  0F 84 8A 00 00 00               je 0x14061f973
0061F8E9  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061F8EC  A8 18                           test al, 0x18
0061F8EE  74 0C                           je 0x14061f8fc
0061F8F0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0061F8F5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0061F8FA  EB 0E                           jmp 0x14061f90a
0061F8FC  A8 04                           test al, 4
0061F8FE  74 0A                           je 0x14061f90a
0061F900  E8 03 43 EB FF                  call 0x1404d3c08
0061F905  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061F90A  40 32 F6                        xor sil, sil
0061F90D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0061F912  40 38 35 9F 4F 8E 00            cmp byte ptr [rip + 0x8e4f9f], sil
0061F919  75 0C                           jne 0x14061f927
0061F91B  F7 05 5B 50 8E 00 00 08 00 00   test dword ptr [rip + 0x8e505b], 0x800
0061F925  74 13                           je 0x14061f93a
0061F927  48 8D 0D 52 45 8E 00            lea rcx, [rip + 0x8e4552]
0061F92E  E8 ED 6C BF FF                  call 0x140216620
0061F933  40 8A F0                        mov sil, al
0061F936  84 C0                           test al, al
0061F938  74 39                           je 0x14061f973
0061F93A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0061F93E  49 8B 1E                        mov rbx, qword ptr [r14]
0061F941  EB 1A                           jmp 0x14061f95d
0061F943  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061F947  48 85 C0                        test rax, rax
0061F94A  74 0E                           je 0x14061f95a
0061F94C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061F950  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061F955  E8 76 B1 09 00                  call 0x1406baad0
0061F95A  48 8B 1B                        mov rbx, qword ptr [rbx]
0061F95D  49 3B DE                        cmp rbx, r14
0061F960  75 E1                           jne 0x14061f943
0061F962  40 84 F6                        test sil, sil
0061F965  74 0C                           je 0x14061f973
0061F967  48 8D 0D 12 45 8E 00            lea rcx, [rip + 0x8e4512]
0061F96E  E8 0D A5 D2 FF                  call 0x140349e80
0061F973  48 8B CD                        mov rcx, rbp
0061F976  E8 A5 23 E6 FF                  call 0x140481d20
0061F97B  48 85 FF                        test rdi, rdi
0061F97E  74 64                           je 0x14061f9e4
0061F980  40 32 F6                        xor sil, sil
0061F983  40 38 35 2E 4F 8E 00            cmp byte ptr [rip + 0x8e4f2e], sil
0061F98A  75 0C                           jne 0x14061f998
0061F98C  F7 05 EA 4F 8E 00 00 08 00 00   test dword ptr [rip + 0x8e4fea], 0x800
0061F996  74 13                           je 0x14061f9ab
0061F998  48 8D 0D E1 44 8E 00            lea rcx, [rip + 0x8e44e1]
0061F99F  E8 7C 6C BF FF                  call 0x140216620
0061F9A4  40 8A F0                        mov sil, al
0061F9A7  84 C0                           test al, al
0061F9A9  74 39                           je 0x14061f9e4
0061F9AB  48 83 C7 30                     add rdi, 0x30
0061F9AF  48 8B 1F                        mov rbx, qword ptr [rdi]
0061F9B2  EB 1A                           jmp 0x14061f9ce
0061F9B4  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061F9B8  48 85 C0                        test rax, rax
0061F9BB  74 0E                           je 0x14061f9cb
0061F9BD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061F9C1  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061F9C6  E8 05 B1 09 00                  call 0x1406baad0
0061F9CB  48 8B 1B                        mov rbx, qword ptr [rbx]
0061F9CE  48 3B DF                        cmp rbx, rdi
0061F9D1  75 E1                           jne 0x14061f9b4
0061F9D3  40 84 F6                        test sil, sil
0061F9D6  74 0C                           je 0x14061f9e4
0061F9D8  48 8D 0D A1 44 8E 00            lea rcx, [rip + 0x8e44a1]
0061F9DF  E8 9C A4 D2 FF                  call 0x140349e80
0061F9E4  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0061F9E9  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0061F9EE  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0061F9F3  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0061F9F8  48 83 C4 30                     add rsp, 0x30
0061F9FC  41 5E                           pop r14
0061F9FE  C3                              ret
0061F9FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExDeletePagedLookasideListWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(408, a2, a3, a4);
    if (result == 0) goto loc_0061F973;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061F8FC;
    v_stack_m18 = v_stack_p0;
    goto loc_0061F90A;
loc_0061F8FC:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9326495)) != 0) goto loc_0061F927;
    if (((*(unsigned int *)(v_rip + 9326683)) & (0x800ULL)) == 0) goto loc_0061F93A;
loc_0061F927:
    result = ExAcquireRundownProtection(v_rip + 9323858, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061F973;
loc_0061F93A:
    goto loc_0061F95D;
loc_0061F943:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061F95D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061F943;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9323794;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExDeletePagedLookasideList(a1, a2, a3, a4);
    if (result == 0) goto loc_0061F9E4;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9326382)) != 0) goto loc_0061F998;
    if (((*(unsigned int *)(v_rip + 9326570)) & (0x800ULL)) == 0) goto loc_0061F9AB;
loc_0061F998:
    result = ExAcquireRundownProtection(v_rip + 9323745, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061F9E4;
loc_0061F9AB:
    v_rdi = (result) + (48);
    goto loc_0061F9CE;
loc_0061F9B4:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061F9CE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_0061F9B4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9323681;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExDeletePagedLookasideListWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(408, a2, a3, a4);
    if (result == 0) goto loc_0061F973;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061F8FC;
    v_stack_m18 = v_stack_p0;
    goto loc_0061F90A;
loc_0061F8FC:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E4F9F)) != 0) goto loc_0061F927;
    if (((*(uint32_t *)(v_rip + 0x8E505B)) & (0x800ULL)) == 0) goto loc_0061F93A;
loc_0061F927:
    result = ExAcquireRundownProtection(v_rip + 9323858, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061F973;
loc_0061F93A:
    goto loc_0061F95D;
loc_0061F943:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061F95D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061F943;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9323794;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExDeletePagedLookasideList(Arg1, a2, a3, a4);
    if (result == 0) goto loc_0061F9E4;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E4F2E)) != 0) goto loc_0061F998;
    if (((*(uint32_t *)(v_rip + 0x8E4FEA)) & (0x800ULL)) == 0) goto loc_0061F9AB;
loc_0061F998:
    result = ExAcquireRundownProtection(v_rip + 9323745, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061F9E4;
loc_0061F9AB:
    local_rdi = (result) + (48);
    goto loc_0061F9CE;
loc_0061F9B4:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061F9CE:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_0061F9B4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9323681;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061F8B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061F8B0[BB_0061F8B0]
  bb_0061F8E9[BB_0061F8E9]
  bb_0061F8F0[BB_0061F8F0]
  bb_0061F8FC[BB_0061F8FC]
  bb_0061F900[BB_0061F900]
  bb_0061F90A[BB_0061F90A]
  bb_0061F91B[BB_0061F91B]
  bb_0061F927[BB_0061F927]
  bb_0061F93A[BB_0061F93A]
  bb_0061F943[BB_0061F943]
  bb_0061F94C[BB_0061F94C]
  bb_0061F95A[BB_0061F95A]
  bb_0061F95D[BB_0061F95D]
  bb_0061F962[BB_0061F962]
  bb_0061F967[BB_0061F967]
  bb_0061F973[BB_0061F973]
  bb_0061F980[BB_0061F980]
  bb_0061F98C[BB_0061F98C]
  bb_0061F998[BB_0061F998]
  bb_0061F9AB[BB_0061F9AB]
  bb_0061F9B4[BB_0061F9B4]
  bb_0061F9BD[BB_0061F9BD]
  bb_0061F9CB[BB_0061F9CB]
  bb_0061F9CE[BB_0061F9CE]
  bb_0061F9D3[BB_0061F9D3]
  bb_0061F9D8[BB_0061F9D8]
  bb_0061F9E4[BB_0061F9E4]
  bb_0061F9FF[BB_0061F9FF]
  bb_0061F8B0 -->|branch| bb_0061F973
  bb_0061F8B0 -->|fallthrough| bb_0061F8E9
  bb_0061F8E9 -->|branch| bb_0061F8FC
  bb_0061F8E9 -->|fallthrough| bb_0061F8F0
  bb_0061F8F0 -->|branch| bb_0061F90A
  bb_0061F8FC -->|branch| bb_0061F90A
  bb_0061F8FC -->|fallthrough| bb_0061F900
  bb_0061F900 -->|flow| bb_0061F90A
  bb_0061F90A -->|branch| bb_0061F927
  bb_0061F90A -->|fallthrough| bb_0061F91B
  bb_0061F91B -->|branch| bb_0061F93A
  bb_0061F91B -->|fallthrough| bb_0061F927
  bb_0061F927 -->|branch| bb_0061F973
  bb_0061F927 -->|fallthrough| bb_0061F93A
  bb_0061F93A -->|branch| bb_0061F95D
  bb_0061F943 -->|branch| bb_0061F95A
  bb_0061F943 -->|fallthrough| bb_0061F94C
  bb_0061F94C -->|flow| bb_0061F95A
  bb_0061F95A -->|flow| bb_0061F95D
  bb_0061F95D -->|branch| bb_0061F943
  bb_0061F95D -->|fallthrough| bb_0061F962
  bb_0061F962 -->|branch| bb_0061F973
  bb_0061F962 -->|fallthrough| bb_0061F967
  bb_0061F967 -->|flow| bb_0061F973
  bb_0061F973 -->|branch| bb_0061F9E4
  bb_0061F973 -->|fallthrough| bb_0061F980
  bb_0061F980 -->|branch| bb_0061F998
  bb_0061F980 -->|fallthrough| bb_0061F98C
  bb_0061F98C -->|branch| bb_0061F9AB
  bb_0061F98C -->|fallthrough| bb_0061F998
  bb_0061F998 -->|branch| bb_0061F9E4
  bb_0061F998 -->|fallthrough| bb_0061F9AB
  bb_0061F9AB -->|branch| bb_0061F9CE
  bb_0061F9B4 -->|branch| bb_0061F9CB
  bb_0061F9B4 -->|fallthrough| bb_0061F9BD
  bb_0061F9BD -->|flow| bb_0061F9CB
  bb_0061F9CB -->|flow| bb_0061F9CE
  bb_0061F9CE -->|branch| bb_0061F9B4
  bb_0061F9CE -->|fallthrough| bb_0061F9D3
  bb_0061F9D3 -->|branch| bb_0061F9E4
  bb_0061F9D3 -->|fallthrough| bb_0061F9D8
  bb_0061F9D8 -->|flow| bb_0061F9E4
```
