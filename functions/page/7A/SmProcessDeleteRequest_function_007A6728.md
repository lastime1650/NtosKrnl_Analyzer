# SmProcessDeleteRequest

- RVA: `0x007A6728`–`0x007A679F` (길이 `119` bytes)
- VA: `0x00000001407A6728`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D1CD4`
- 디코드: `34`개 명령, `119/119` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007A6742` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x007A677F` → [SmpGetProcessPartition](../../text/4A/SmpGetProcessPartition_function_004A3CCC.md) (function, `0x004A3CCC`)
- `0x007A678B` → [SmKmStoreDelete](../A6/SmKmStoreDelete_function_00A6D7D0.md) (function, `0x00A6D7D0`)

### Direct callers
- [sub_00B419D6](../B4/Unknown_function_00B419D6.md) at `0x00B41A10`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007A677F` → [SmpGetProcessPartition](../../text/4A/SmpGetProcessPartition_function_004A3CCC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007A6728  48 83 EC 28                     sub rsp, 0x28
007A672C  83 FA 08                        cmp edx, 8
007A672F  74 07                           je 0x1407a6738
007A6731  B8 06 02 00 C0                  mov eax, 0xc0000206
007A6736  EB 61                           jmp 0x1407a6799
007A6738  45 84 C0                        test r8b, r8b
007A673B  74 1F                           je 0x1407a675c
007A673D  F6 C1 03                        test cl, 3
007A6740  74 06                           je 0x1407a6748
007A6742  E8 89 38 0F 00                  call 0x140899fd0
007A6747  CC                              int3
007A6748  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
007A6752  48 3B C8                        cmp rcx, rax
007A6755  48 0F 42 C1                     cmovb rax, rcx
007A6759  90                              nop
007A675A  8A 00                           mov al, byte ptr [rax]
007A675C  48 8B 01                        mov rax, qword ptr [rcx]
007A675F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007A6764  3C 01                           cmp al, 1
007A6766  75 2A                           jne 0x1407a6792
007A6768  A9 00 FF FF FF                  test eax, 0xffffff00
007A676D  75 23                           jne 0x1407a6792
007A676F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007A6778  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
007A677F  E8 48 D5 CF FF                  call 0x1404a3ccc
007A6784  8B 54 24 4C                     mov edx, dword ptr [rsp + 0x4c]
007A6788  48 8B C8                        mov rcx, rax
007A678B  E8 40 70 2C 00                  call 0x140a6d7d0
007A6790  EB 07                           jmp 0x1407a6799
007A6792  B8 0D 00 00 C0                  mov eax, 0xc000000d
007A6797  EB 00                           jmp 0x1407a6799
007A6799  48 83 C4 28                     add rsp, 0x28
007A679D  C3                              ret
007A679E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SmProcessDeleteRequest(__int64 a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p24;

    v_rsp = (v_rsp) - (40);
    if (a2 == 8) goto loc_007A6738;
    goto loc_007A6799;
loc_007A6738:
    if (a3 == 0) goto loc_007A675C;
    result = (unsigned int)(0xC0000206ULL);
    if ((((unsigned __int8)(a1)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
    }
    if (a1 < result) { result = a1; }
loc_007A675C:
    v_stack_p20 = *(unsigned __int64 *)(a1);
    if (((unsigned __int8)(*(unsigned __int64 *)(a1))) != 1) goto loc_007A6792;
    if ((((unsigned int)(*(unsigned __int64 *)(a1))) & (0xFFFFFF00ULL)) != 0) goto loc_007A6792;
    result = SmpGetProcessPartition(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, a3, a4);
    result = SmKmStoreDelete(result, (unsigned int)(v_stack_p24), a3, a4);
    goto loc_007A6799;
loc_007A6792:
    goto loc_007A6799;
loc_007A6799:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t SmProcessDeleteRequest(int64_t Arg1, int32_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;
    uint32_t v_stack_p24;

    local_rsp = (local_rsp) - (40);
    if (Arg2 == 8) goto loc_007A6738;
    goto loc_007A6799;
loc_007A6738:
    if (Arg3 == 0) goto loc_007A675C;
    result = (uint32_t)(0xC0000206ULL);
    if ((((uint8_t)(Arg1)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, a4);
    }
    if (Arg1 < result) { result = Arg1; }
loc_007A675C:
    v_stack_p20 = *(uint64_t *)(Arg1);
    if (((uint8_t)(*(uint64_t *)(Arg1))) != 1) goto loc_007A6792;
    if ((((uint32_t)(*(uint64_t *)(Arg1))) & (0xFFFFFF00ULL)) != 0) goto loc_007A6792;
    result = SmpGetProcessPartition(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, Arg3, a4);
    result = SmKmStoreDelete(result, (uint32_t)(v_stack_p24), Arg3, a4);
    goto loc_007A6799;
loc_007A6792:
    goto loc_007A6799;
loc_007A6799:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC000000DULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007A6728&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007A6728[BB_007A6728]
  bb_007A6731[BB_007A6731]
  bb_007A6738[BB_007A6738]
  bb_007A673D[BB_007A673D]
  bb_007A6742[BB_007A6742]
  bb_007A6748[BB_007A6748]
  bb_007A675C[BB_007A675C]
  bb_007A6768[BB_007A6768]
  bb_007A676F[BB_007A676F]
  bb_007A6792[BB_007A6792]
  bb_007A6799[BB_007A6799]
  bb_007A679E[BB_007A679E]
  bb_007A6728 -->|branch| bb_007A6738
  bb_007A6728 -->|fallthrough| bb_007A6731
  bb_007A6731 -->|branch| bb_007A6799
  bb_007A6738 -->|branch| bb_007A675C
  bb_007A6738 -->|fallthrough| bb_007A673D
  bb_007A673D -->|branch| bb_007A6748
  bb_007A673D -->|fallthrough| bb_007A6742
  bb_007A6742 -->|flow| bb_007A6748
  bb_007A6748 -->|flow| bb_007A675C
  bb_007A675C -->|branch| bb_007A6792
  bb_007A675C -->|fallthrough| bb_007A6768
  bb_007A6768 -->|branch| bb_007A6792
  bb_007A6768 -->|fallthrough| bb_007A676F
  bb_007A676F -->|branch| bb_007A6799
  bb_007A6792 -->|branch| bb_007A6799
```
